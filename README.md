<div align="center">

<img src="https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/leetcode.svg" alt="LeetCode Logo" width="60" height="60" />

# 🚀 Daily DSA Problem Solving Tracker

### <i>Mastering Data Structures & Algorithms — One problem at a time.</i>

<p align="center">
  <a href="#-about">About</a> •
  <a href="#-metrics--milestones">Metrics</a> •
  <a href="#-core-topics--patterns">Topics</a> •
  <a href="#-daily-progress-log">Progress Log</a>
</p>

[![LeetCode Stats](https://img.shields.io/badge/LeetCode-Journey-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](#)
[![Consistency Status](https://img.shields.io/badge/Consistency-Active-brightgreen?style=for-the-badge&logo=github)](#)

</div>

---

## 📖 About
This repository documents my daily journey in mastering Data Structures and Algorithms (DSA) primarily structured around LeetCode problems. The goal is purely consistent, deliberate practice focused on identifying **structural patterns** rather than just memorizing solutions. 

All solutions inside this repository will include clean code, time/space complexity analysis, and approach explanations.

## 🏆 Metrics & Milestones
To maintain consistency, I measure my weekly progress through a metric-based system derived from algorithmic difficulty.

| Difficulty | Points | Objective |
| :--- | :---: | :--- |
| **🟢 Easy Problem** | `+10 pts` | Solidifying conceptual fundamentals. |
| **🟡 Medium Problem**| `+30 pts` | Pattern recognition and efficient implementation. |
| **🔴 Hard Problem** | `+50 pts` | Optimal time/space optimization and complex architectures. |

**Consistency Milestones:**
- `Level 1`: 7 Consecutive Days (Discipline Established)
- `Level 2`: 30 Consecutive Days (Habit Formed)
- `Level 3`: 100 Consecutive Days (Advanced Proficiency)

---

## 🧠 Core Topics & Patterns
Focusing on algorithmic patterns is the most efficient way to master DSA. I've categorized my practice into these core pillars:

<details>
<summary><b>🛠️ Core Data Structures</b> (Click to expand)</summary>

- `Arrays` & `Hashing`
- `Strings`
- `Linked Lists`
- `Stacks` & `Queues`
- `Trees` & `Graphs`
- `Heaps` / `Priority Queues`
- `Tries`
</details>

<details>
<summary><b>🧩 Algorithmic Patterns</b> (Click to expand)</summary>

- 🏃‍♂️ `Two Pointers`
- 🪟 `Sliding Window`
- 🗺️ `Fast & Slow Pointers`
- 🔍 `Binary Search`
- 🌳 `Depth-First Search (DFS)` & `Breadth-First Search (BFS)`
- ⏪ `Backtracking`
- 🔢 `Dynamic Programming (1D & 2D)`
- 🏗️ `Greedy Algorithms`
</details>

---

## 📅 Daily Progress Log

| Day | Date | Problem | Difficulty | Topic / Pattern | Status | Points |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **1** | `YYYY-MM-DD` | [0001. Two Sum](./Arrays/0001-Two-Sum.py) | 🟢 | Arrays / Hash Map | ✅ | `+10 pts` |
| **2** | `YYYY-MM-DD` | [0003. Longest Substring Without Repeating Characters](./Strings/0003-Longest-Substring.py) | 🟡 | Sliding Window | ✅ | `+30 pts` |
| ... | ... | ... | ... | ... | ... | ... |

> **Note:** I will be adding new problems to this table daily to track my consistency!

---

## 📂 Repository Structure

The folder structure is kept modular and clean, grouping problems primarily by Topic or Pattern:

```text
📦 Dsa-practice
 ┣ 📂 Arrays
 ┃ ┣ 📜 0001-Two-Sum.py
 ┃ ┗ 📜 0217-Contains-Duplicate.py
 ┣ 📂 SlidingWindow
 ┃ ┗ 📜 0121-Best-Time-to-Buy-and-Sell-Stock.py
 ┣ 📂 BinarySearch
 ┃ ┗ 📜 0704-Binary-Search.py
 ┗ 📜 README.md
```

## 🚀 How to Navigate
1. Clone the repository locally if required:
   ```bash
   git clone https://github.com/Vignesh-Salian/Dsa-practice.git
   ```
2. Navigate to the specific topic/pattern category.
3. Every solution file contains the original problem statement details and the optimal approach.

---

<div align="center">
  <h3 id="daily-quote">⚡ Daily Motivation</h3>
  <blockquote id="quote-text">
    <i>"The successful warrior is the average man, with laser-like focus." — Bruce Lee</i>
  </blockquote>
  <p>Maintained with ❤️ & ☕ by <b>Vignesh Salian</b></p>
</div>

<!-- This script automatically updates the quote on GitHub using standard Markdown injection if possible, but is represented here as a placeholder for a GitHub Action or manual rotation -->
<script>
  const quotes = [
    "\"The successful warrior is the average man, with laser-like focus.\" — Bruce Lee",
    "\"First, solve the problem. Then, write the code.\" – John Johnson",
    "\"Any fool can write code that a computer can understand. Good programmers write code that humans can understand.\" – Martin Fowler",
    "\"Experience is the name everyone gives to their mistakes.\" – Oscar Wilde",
    "\"Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.\" – Dan Salomon",
    "\"It's not a bug. It's an undocumented feature!\" – Anonymous"
  ];
  try {
    const today = new Date().getDay();
    document.getElementById("quote-text").innerHTML = "<i>" + quotes[today % quotes.length] + "</i>";
  } catch (e) {}
</script>
