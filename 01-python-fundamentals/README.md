# Python Fundamentals — Self-Study Course

A self-contained, self-paced course for learning Python from zero prior programming experience. No videos are required — every lesson is a complete, standalone unit of reading material, worked examples, exercises, solutions, and a quiz, designed to be studied directly from this repository.

---

## Who This Course Is For

This course assumes no prior programming knowledge. Concepts are introduced before syntax, every idea is explained with a real-world analogy, and every lesson builds directly on the one before it.

## Prerequisites

- Python 3 installed locally (`python3 --version` should return a version number)
- A text editor of your choice
- A terminal or command-line interface

No other software or account is required.

---

## Course Structure

The course is organized into numbered lessons. Each lesson lives in its own folder and contains exactly five files:

```text
Lesson-XX-Topic-Name/
├── lesson.md       Full lesson: concepts, diagrams, examples, common mistakes, debugging practice
├── examples.py     All lesson examples, ready to run
├── exercise.md      Ten practice exercises (easy, medium, hard) — questions only
├── solution.py      Complete, explained solutions to every exercise
└── quiz.md          Twenty-question quiz with an answer key at the end
```

Every five lessons, a consolidated `CheatSheet-Part-XX.md` file is added, summarizing the syntax and concepts from that block of lessons into a single quick-reference page.

## How to Study Each Lesson

1. Read `lesson.md` from top to bottom before writing any code.
2. Run `examples.py` yourself, and modify the values to see how the output changes.
3. Attempt every exercise in `exercise.md` without looking at the solution first.
4. Check your work against `solution.py`, comparing your approach, not just your output.
5. Take the quiz in `quiz.md` to confirm the lesson's concepts are solid before moving on.
6. Review the relevant cheat sheet once you have completed a block of five lessons.

Lessons are designed to be completed in order — later lessons assume the syntax and vocabulary introduced earlier.

---

## Lesson Index

| Lesson | Topic | Core Concepts |
|---|---|---|
| [01](./Lesson-01-Your-First-Program) | Your First Program | `print()`, comments, program execution order |
| [02](./Lesson-02-Variables-and-Data-Types) | Variables and Data Types | Variables, `int`, `float`, `str`, `bool`, `type()` |
| [03](./Lesson-03-Working-with-Numbers) | Working with Numbers | Arithmetic operators, floor division, modulo, exponents |
| [04](./Lesson-04-Type-Conversion) | Type Conversion | `int()`, `float()`, `str()`, `bool()`, conversion pitfalls |
| [05](./Lesson-05-Comparison-and-Boolean-Logic) | Comparison and Boolean Logic | `==`, `!=`, `<`, `>`, `and`, `or`, `not` |

**Reference material:** [`CheatSheet-Part-01.md`](./CheatSheet-Part-01.md) — covers Lessons 01–05.

---

## Repository Conventions

- All code follows PEP 8 formatting.
- Every code example is executable as written, with no missing imports or setup steps.
- Exercises progress from easy to hard within each lesson and avoid repeating the same underlying problem with different numbers.
- Explanations prioritize understanding the *why* behind a rule over memorizing the rule itself.

## License

This course is provided for personal, self-study use.
