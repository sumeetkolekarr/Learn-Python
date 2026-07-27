# Learn-Python

Personal Python learning repo, now split into two parts:

## `Python course resources/`
Everything from the original Python course (basics through OOP, plus two mini
projects). Kept as an archive/reference - not actively worked on anymore.

## `Python Basics - Practice/`
Active. Original, solution-free exercises covering core Python (variables,
operators, data types, conditionals, loops, lists/tuples, dicts/sets,
functions, exceptions, file handling), ending in a small capstone project.
Intended to build confidence in the basics before touching the roadmap
folders below - see that folder's own README.md for how to work through it
and get evaluated.

## Roadmap toward AI / Data Science / Visualization
New folders, each targeting a specific gap between "finished a Python course"
and "can read/write real AI/DS code":

1. **Python Fundamentals - Advanced** - generators, decorators, context
   managers, `functools`, type hints
2. **NumPy** - vectorized arrays, broadcasting, the foundation everything else
   sits on
3. **Pandas** - loading, cleaning, and transforming real datasets
4. **Visualization** - Matplotlib fundamentals + Seaborn statistical plots
5. **Math and Stats for DS** - descriptive stats, correlation, distributions,
   linear algebra basics, all in code
6. **Intro to ML** - scikit-learn's standard workflow (split -> fit ->
   predict -> evaluate) to see how everything above feeds into modeling

Each folder has a starter `index.py` with worked examples plus `TODO Qn`
practice problems to solve yourself - same style as the original course
folders.

### Setup
```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Recommended to work through these mostly in Jupyter/JupyterLab or VS Code's
notebook mode rather than plain scripts, since that's the standard DS workflow.
