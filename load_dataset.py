import argparse
import json
import re
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parent
SUBSETS = ("single_video", "cross_temporal", "cross_spatial", "cross_spatiotemporal",
           "person_recognition", "behavior_analysis", "summarization_and_reasoning")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_videos(root=DEFAULT_ROOT):
    videos = read_json(Path(root) / "videos.json")
    ids = [v["id"] for v in videos]
    names = [v["source_filename"].casefold() for v in videos]
    if len(ids) != len(set(ids)) or len(names) != len(set(names)):
        raise ValueError("Video IDs and source filenames must be unique.")
    return {v["id"]: v for v in videos}


def load_video_pools(root=DEFAULT_ROOT):
    root = Path(root)
    pools = read_json(root / "question_videos.json")
    question_ids = {q["id"] for q in read_json(root / "questions.json")}
    filenames = {v["source_filename"] for v in load_videos(root).values()}
    if set(pools) != question_ids:
        raise ValueError("Candidate pools must cover exactly the published question IDs.")
    for question_id, candidates in pools.items():
        if not isinstance(candidates, list) or not candidates:
            raise ValueError(f"Missing candidate pool: {question_id}")
        if len(candidates) != len(set(candidates)) or not set(candidates).issubset(filenames):
            raise ValueError(f"Invalid candidate pool: {question_id}")
    return pools


def get_candidate_videos(question_id, root=DEFAULT_ROOT):
    pools = load_video_pools(root)
    if question_id not in pools:
        raise ValueError(f"Unknown question ID: {question_id}")
    by_filename = {v["source_filename"]: v for v in load_videos(root).values()}
    result = []
    for filename in pools[question_id]:
        video = by_filename[filename]
        candidate = {"source_filename": filename}
        if "synthetic_context" in video:
            candidate["context"] = video["synthetic_context"]
        result.append(candidate)
    return result


def load_questions(subset=None, root=DEFAULT_ROOT):
    root = Path(root)
    questions = read_json(root / "questions.json")
    subsets = read_json(root / "subsets.json")
    pools = load_video_pools(root)
    ids = [q["id"] for q in questions]
    if len(ids) != len(set(ids)):
        raise ValueError("Question IDs must be unique.")
    selected = set(ids)
    if subset is not None:
        if subset not in SUBSETS:
            raise ValueError(f"Unknown subset: {subset}")
        group = "by_task_type" if subset in subsets["by_task_type"] else "office_by_spatiotemporal_configuration"
        selected = set(subsets[group][subset])
        if not selected.issubset(ids):
            raise ValueError("Subset references unknown question IDs.")
    for q in questions:
        if set(q) != {"id", "question", "options", "answer"}:
            raise ValueError(f"Unexpected question fields: {q['id']}")
        if q["answer"] not in q["options"]:
            raise ValueError(f"Invalid gold answer: {q['id']}")
        text = q["question"] + " " + " ".join(q["options"].values())
        references = re.findall(r"v_[A-Za-z0-9_-]+\.mp4", text)
        for filename in references:
            if filename not in pools[q["id"]]:
                raise ValueError(f"Video is outside the question candidate pool: {filename}")
    return [q for q in questions if q["id"] in selected]


def main():
    parser = argparse.ArgumentParser(description="Select complete question records from the VideoForest dataset.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--subset", choices=SUBSETS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    records = load_questions(subset=args.subset, root=args.root)
    content = json.dumps(records, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(content)
        print(f"Exported {len(records)} questions to {args.output}")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
