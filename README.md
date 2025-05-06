# 🧮 Discrete Math – Year 1, UCU
## Regex Engine Project Report

The goal of this assignment was to build a simple regular expression (regex) engine in Python 🐍, demonstrating my understanding of **finite automata** 🤖 and **regular languages** 🔤 from our Discrete Mathematics course.

---

## 🧠 1. What I Built

I implemented a custom regex engine that supports the following features:

* ✅ Literal characters (e.g., `'a'`, `'b'`)
* 🔘 Dot `.` — matches any single character
* ⭐ Star `*` — zero or more repetitions
* ➕ Plus `+` — one or more repetitions
* 🔡 Character ranges and classes like `[abc]`, `[a-z]`, `[0-9]` (implemented as an additional task)

The engine is based on a **Finite State Machine (FSM)** model, constructed directly from the input regex pattern.

---

## 🛠️ 2. How It Works

My project is structured into two main Python modules:

* 📄 `regex.py` — core regex engine logic
* 🧪 `test_regex.py` — unit tests for validating behavior

### 🧩 Key Components (regex.py)

* `State` – Abstract base class for all state types
* Specialized subclasses: `AsciiState`, `DotState`, `StarState`, `CharactersState`, etc.
* `RegexFSM` – Main class that:
  * Parses the regex pattern ✍️
  * Builds a Non-deterministic Finite Automaton (NFA) 🔗
  * Simulates string matching via the constructed NFA 🔍

---

## 🧪 3. Testing

I wrote unit tests comparing my engine’s output with Python’s built-in `re` module to verify correctness.
This included both **positive** and **negative** test cases for various regex patterns.

🔍 This helped ensure that:
* The FSM transitions are correct
* Edge cases are handled properly
* The behavior aligns with standard regex expectations

---

## ✅ 4. Conclusion

This assignment gave me the chance to turn abstract mathematical concepts into a working program 🎯. I gained a deeper understanding of:

* How NFAs work internally 🤖
* How to implement state machines using object-oriented Python
* How regex engines process and match patterns

I'm especially proud of implementing character ranges like `[a-z]`, which were part of the additional tasks 🔡.
Overall, this was a challenging but highly rewarding project that showed how theory can be applied in practice 💡💻.

---

## 🔗 5. References & Reflections

The starter code was slightly difficult to follow due to the use of class variables instead of instance variables, which made the flow less intuitive at first.

What helped me the most was this article:
🔗 [Regex under the hood: Implementing a simple regex compiler in Go](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079)

It gave me the insight to treat each state as a matcher, and model epsilon transitions (empty moves) between states, helping me design the FSM effectively.
