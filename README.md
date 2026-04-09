---
title: RL Open Env Assessment
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---
# 🚀 OpenEnv RL Task Evaluation System

## 📌 Project Overview

This project implements a **real-world AI evaluation environment** using the OpenEnv framework.
It simulates practical tasks and evaluates how effectively an AI agent can solve them using structured observations, actions, and rewards.

The system integrates:

* Task simulation (real-world scenarios)
* AI-based inference (OpenAI client)
* Deterministic grading system
* Reward shaping mechanism
* Robust fallback handling for API failures

---

## 🎯 Problem Statement

Modern AI systems must be evaluated on **real-world tasks**, not toy problems.

This project solves:

* How to simulate real-world environments for AI agents
* How to evaluate responses objectively
* How to provide meaningful rewards
* How to ensure system reliability even under API failures

---

## 🧠 Architecture

```
User Task → Environment → AI Model → Action → Grader → Reward → Output
```

### Components:

* **Environment (`env/`)**

  * Handles task lifecycle (`reset`, `step`, `state`)
* **Tasks (`tasks/`)**

  * Real-world scenarios (easy → medium → hard)
* **Graders (`graders/`)**

  * Deterministic scoring (0.0 → 1.0)
* **Inference (`inference.py`)**

  * Runs AI agent and prints evaluation logs
* **Fallback System**

  * Ensures execution even when API fails

---

## 🧩 Tasks

### 🟢 Easy Task — Email Classification

* Detect spam emails based on content patterns

### 🟡 Medium Task — Data Cleaning

* Remove duplicates and sort dataset

### 🔴 Hard Task — Code Debugging

* Identify and fix logical bug in function

---

## ⚙️ How It Works

1. Environment initializes a task (`reset`)
2. AI model receives task prompt
3. AI generates an action (solution)
4. Environment evaluates using grader
5. Reward is assigned:

   * `1.0` → correct
   * `0.5` → partial
   * `-0.2` → incorrect
6. Output is printed in required format:

```
[START] → Task begins  
[STEP]  → Each action evaluated  
[END]   → Final result  
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Set environment variable

#### PowerShell:

```
$env:HF_TOKEN="your_openai_api_key"
```

### 3. Run inference

```
python inference.py
```

---

## 📊 Example Output

```
[START] task=easy env=openenv model=gpt-4o-mini
[STEP] step=1 action=spam reward=1.00 done=true error=null
[END] success=true steps=1 rewards=1.00
```

---

## 🛡️ Robustness & Reliability

* ✅ Handles API failures (fallback system)
* ✅ Prevents crashes (exception handling)
* ✅ Works with or without API quota
* ✅ Ensures consistent output format

---

## 🐳 Docker Support

### Build

```
docker build -t openenv_project .
```

### Run

```
docker run openenv_project
```

---

## 📁 Project Structure

```
openenv_project/
│
├── inference.py
├── env/
├── tasks/
├── graders/
├── openenv.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Key Highlights

* Real-world task simulation
* AI-driven evaluation pipeline
* Deterministic grading system
* Reward shaping logic
* Fault-tolerant architecture
* Hackathon-compliant output format

---

## 🏁 Conclusion

This project demonstrates a **complete AI evaluation pipeline**, combining:

* Reinforcement Learning concepts
* Real-world task modeling
* Robust system design

It is designed to be:

* Scalable
* Reliable
* Production-ready

---

## 👨‍💻 Author

Developed as part of the **OpenEnv RL Hackathon Challenge**
