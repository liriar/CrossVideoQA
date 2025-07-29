# CrossVideoQA: A Benchmark for Cross-Video Reasoning

**CrossVideoQA** is a comprehensive benchmark dataset designed to evaluate **cross-video reasoning** capabilities, with a special focus on **human-centric queries** spanning different spatial locations and temporal periods.

---

## 🧠 Motivation

Cross-video understanding is essential for real-world applications such as:

- **Surveillance**: Tracking individuals across distributed camera networks (e.g., office buildings, transportation hubs).
- **Content Analysis**: Discovering related events from different perspectives to reconstruct coherent narratives.

Existing video QA datasets are limited to single-source settings. **CrossVideoQA** fills this gap by challenging models to reason across multiple videos in diverse spatial-temporal conditions.

---

## 📦 Dataset Overview

CrossVideoQA integrates two complementary datasets:

- **Edinburgh Office Surveillance Dataset (EOSD)**  
  - 18 surveillance videos  
  - 3 indoor locations across 12 dates  
  - ~450,000 frames  
  - Suitable for structured, multi-day human behavior analysis  
  - Video length: 6–21 min (avg ~14 min)

- **HACS (Human Action Clips and Segments)**  
  - 50,000 web videos  
  - 1.55 million action clips  
  - High visual and semantic diversity  
  - Clip length: 9 sec – 4 min (avg ~2 min)

**Combined Dataset:**  
> `DCrossVideoQA = DEOSD ∪ DHACS`

---

## 📊 Dataset Statistics & Structure

- **Total videos used:** 100  
- **Total QA pairs:** 197  
- **Average video duration:** ~3 min  
- **Average number of video segments per question:** 2.33  
- **Reasoning depth:** From low-level perception to high-level causal reasoning

### 🧪 Task Categories

CrossVideoQA questions are categorized into:

| Category                      | Count |
|------------------------------|-------|
| Person Recognition           | 56    |
| Behavior Analysis            | 81    |
| Summarization & Causal Inference | 60    |

### 🔍 Reasoning Modalities

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

