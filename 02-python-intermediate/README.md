# Python Intermediate — Self-Study Course

A self-contained, self-paced course that builds directly on Python Fundamentals. No videos required — every lesson is a complete, standalone unit of reading material, worked examples, exercises, solutions, and a quiz, designed to be studied directly from this repository.

---

## Who This Course Is For

This course assumes you already know the fundamentals of Python (variables, data types, arithmetic, comparisons — Lessons 01–05). It moves into data structures, function design, and safe error handling — the building blocks needed before tackling object-oriented and advanced Python.

## Prerequisites

- Python 3 installed locally (`python3 --version` should return a version number)
- A text editor of your choice
- A terminal or command-line interface
- Familiarity with Python Fundamentals (Lessons 01–05)

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
└── quiz.md          Review quiz with an answer key at the end
```

## How to Study Each Lesson

1. Read `lesson.md` from top to bottom before writing any code.
2. Run `examples.py` yourself, and modify the values to see how the output changes.
3. Attempt every exercise in `exercise.md` without looking at the solution first.
4. Check your work against `solution.py`, comparing your approach, not just your output.
5. Take the quiz in `quiz.md` to confirm the lesson's concepts are solid before moving on.
6. Review [`CheatSheet-Part-02.md`](./CheatSheet-Part-02.md) once you have completed this block of lessons.

Lessons are designed to be completed in order — later lessons assume the syntax and vocabulary introduced earlier.

---

## Lesson Index

| Lesson | Topic | Core Concepts |
|---|---|---|
| [06](./Lesson-06-Sets-and-Operations) | Sets and Operations | `set()`, union, intersection, difference |
| [07](./Lesson-07-Defining-Functions) | Defining Functions | `def`, parameters, `return`, docstrings |
| [08](./Lesson-08-Arguments-and-Scope) | Arguments and Scope | Default arguments, local vs. global scope, `*args`, `**kwargs` |
| [09](./Lesson-09-Higher-Order-Functions) | Higher-Order Functions | `lambda`, `map()`, `filter()`, `sorted(key=...)` |
| [10](./Lesson-10-Try-and-Except) | Try and Except | `try`/`except`/`else`/`finally`, catching specific exceptions |

**Reference material:** [`CheatSheet-Part-02.md`](./CheatSheet-Part-02.md) — covers Lessons 06–10.

---

## Repository Conventions

- All code follows PEP 8 formatting.
- Every code example is executable as written, with no missing imports or setup steps.
- Exercises progress from easy to hard within each lesson and avoid repeating the same underlying problem with different numbers.
- Explanations prioritize understanding the *why* behind a rule over memorizing the rule itself.

## License

This course is provided for personal, self-study use.
