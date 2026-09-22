# VideoForest Dataset

197 questions: 103 Office + 94 HACS.

## Usage

Run from the dataset directory:

```python
from load_dataset import load_questions, get_candidate_videos

questions = load_questions(subset="person_recognition")
question = questions[0]
candidates = get_candidate_videos(question["id"])
```

`load_questions(subset)` returns complete question records. Choose one subset below, or call `load_questions()` for all 197 questions. `get_candidate_videos(question_id)` returns only that question's candidate videos.

## Subsets

| Subset | Questions | Source |
|---|---:|---|
| `single_video` | 26 | Office |
| `cross_temporal` | 25 | Office |
| `cross_spatial` | 26 | Office |
| `cross_spatiotemporal` | 26 | Office |
| `person_recognition` | 57 | Office |
| `behavior_analysis` | 80 | Office + HACS |
| `summarization_and_reasoning` | 60 | Office + HACS |

## Fields

| Record | Field | Meaning |
|---|---|---|
| Question | `id` | Question ID; pass it to `get_candidate_videos`. |
| Question | `question` | Question text. |
| Question | `options` | Option letters mapped to answer text or video filenames. |
| Question | `answer` | Gold option letter, used for evaluation. |
| Candidate | `source_filename` | Filename of the video to load. |
| Candidate | `context` | Office day, date label, and room; absent for HACS. |

Each Office question has nine candidates. HACS video-selection questions have three; HACS comparison questions have two. Load only the returned candidates. Numeric times are playback seconds from the start of each video.
