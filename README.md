# CrossVideoQA: A Benchmark for Cross-Video Reasoning

**CrossVideoQA** is a comprehensive benchmark dataset designed to evaluate **cross-video reasoning** capabilities, with a special focus on **human-centric queries** spanning different spatial locations and temporal periods.
> 🌲 This benchmark is introduced in our **ACMMM 2025** paper:  
> [**VideoForest: Person-Anchored Hierarchical Reasoning for Cross-Video Question Answering**](https://openreview.net/forum?id=bUioJlKXN6)

---

## 🧠 Motivation

Cross-video understanding is essential for real-world applications such as:

- **Surveillance**: Tracking individuals across distributed camera networks (e.g., office buildings, transportation hubs).
- **Content Analysis**: Discovering related events from different perspectives to reconstruct coherent narratives.

Existing video QA datasets are limited to single-source settings. **CrossVideoQA** fills this gap by challenging models to reason across multiple videos in diverse spatial-temporal conditions.

---

## 📦 Dataset Overview

CrossVideoQA integrates two complementary datasets:

We thank the University of Edinburgh for the use of the low resolution video and ground truth data.
- **[Edinburgh Office Surveillance Dataset (EOSD)](https://homepages.inf.ed.ac.uk/rbf/OFFICEDATA/)**  
  - 20 surveillance videos  
  - 3 indoor locations across 12 dates  
  - ~450,000 frames  
  - Suitable for structured, multi-day human behavior analysis  


- **[HACS (Human Action Clips and Segments)](http://hacs.csail.mit.edu/)**  
  - 50,000 web videos  
  - 1.55 million action clips  
  - High visual and semantic diversity  

**Combined Dataset:**  
> `DCrossVideoQA = DEOSD ∪ DHACS`

###  Task Categories

CrossVideoQA questions are categorized into:Person Recognition、Behavior Analysis and Summarization & Causal Inference.

###  Reasoning Modalities

Each QA pair falls under one of four spatial-temporal reasoning configurations:

| Modality               | Description                                              |
|------------------------|----------------------------------------------------------|
| `single`              | Within a single video (same location, same day)          |
| `cross-spatial`       | Across multiple locations within the same time frame     |
| `cross-temporal`      | Same location but across different dates                 |
| `cross-spatiotemporal`| Full spatial-temporal integration                        |

This design enables systematic evaluation of models across increasing levels of complexity.

---

## 🏗️ Benchmark Construction Pipeline

We adopt a three-stage QA construction process:

1. **Expert Annotation**  
   - Human-written exemplar QA pairs for each reasoning type and modality.

2. **LLM-Augmented Generation**  
   - Automatic generation under controlled prompts to enhance diversity.

3. **Human Validation**  
   - Manual filtering and correction to ensure:
     - Answerability
     - Accuracy
     - Balanced difficulty


---

## 📥 Data Access

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

---

## 📄 Citation

If you use this benchmark, please cite:

```bibtex
@inproceedings{anonymous2025videoforest,
  title     = {VideoForest: Person-Anchored Hierarchical Reasoning for Cross-Video Question Answering},
  author    = {Yiran Meng and Junhong Ye and Wei Zhou and Guanghui Yue and Xudong Mao and Ruomei Wang and Baoquan Zhao},
  booktitle = {ACM Multimedia 2025},
  year      = {2025},
  url       = {https://openreview.net/forum?id=bUioJlKXN6}
}
