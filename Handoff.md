# Handoff

Pick this repo back up on any machine. Clone it, follow setup, check the
progress checklist below to see where you left off.

## Repo
```
git clone https://github.com/sumeetkolekarr/Learn-Python.git
```

## Setup on a new machine
```bash
cd Learn-Python
python -m venv venv

# activate:
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```
Python version used originally: 3.10.2 (anything 3.10+ should work fine).

Recommended editor: VS Code with the Python + Jupyter extensions installed,
so `.py` files can run notebook-style (`# %%` cells) if you want that
workflow instead of plain scripts.

## What's in this repo
- `Python course resources/` — archived material from the original Python
  course (basics through OOP + 2 mini projects). Reference only, not active.
- `Python Basics - Practice/` — active, current focus. Solution-free basics
  exercises (variables through file handling) plus a capstone mini project,
  used to rebuild confidence before moving on to the roadmap below.
- Everything else at the root — the roadmap toward AI / Data Science /
  Visualization, picked back up once the basics practice folder feels solid.
  See `README.md` for what each folder covers.

## Progress checklist
Update this section yourself as you go — check things off, add notes on what
you tried, and commit it. That way "where did I leave off" is always answered
by this file instead of your memory.

- [ ] **Python Basics - Practice** — 11 files, 01 (variables/operators)
  through 11 (contact book capstone). Work through in order, get each file
  reviewed before moving to the next.
- [ ] **Python Fundamentals - Advanced** — generators, decorators, context
  managers, functools, type hints (paused until basics practice is done)
- [ ] **NumPy** — arrays, vectorized ops, broadcasting, reshape/axis
- [ ] **Pandas** — loading, cleaning, groupby, merge
  - [ ] Downloaded a real dataset (e.g. Titanic from Kaggle) — not included
    in the repo, needs re-downloading on a new machine
- [ ] **Visualization** — Matplotlib basics
- [ ] **Visualization** — Seaborn basics (needs internet the first time, to
  fetch the built-in `tips`/`titanic` sample datasets)
- [ ] **Math and Stats for DS** — descriptive stats, correlation,
  distributions, linear algebra basics
- [ ] **Intro to ML** — scikit-learn split/fit/predict/evaluate workflow

## Notes / last session
- 2026-07-26: Repo restructured — old course work archived under
  `Python course resources/`, new roadmap folders scaffolded with starter
  `index.py` files and TODO practice problems. Nothing in the new folders
  has been solved yet.
