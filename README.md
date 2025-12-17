CS 575 Repository

Michael A. Goodrich  
Brigham Young University  

---

### Quick Start

1. Clone the repo in VS Code.
2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\\Scripts\\activate  # Windows PowerShell
```

3. Install dependencies for development (pytest, mypy):

```bash
pip install -e ".[dev]"
```

4. Install `graphviz` (needed by `pydot` for plotting):

```bash
# macOS
brew install graphviz
# Windows (PowerShell)
winget install -e --id Graphviz.Graphviz
```

5. Select the Python interpreter in VS Code: Command Palette → `Python: Select Interpreter` → pick `.venv`.

---

### Base vs ML Dependencies

- Base dependencies (NumPy, Pandas, NetworkX, Matplotlib, SciPy, pydot, ipykernel) install automatically.
- ML extras (installed later when needed): PyTorch, Torch Geometric, Gensim, and scikit-learn.

Install ML extras when we reach those topics:

```bash
pip install -e ".[ml]"
```

Note: Torch Geometric wheels depend on your installed PyTorch version. If you hit issues, install `torch` first, then `torch-geometric`. CPU-only builds are fine for this course.

---

### Running Tests

- Configure tests: Command Palette → `Python: Configure Tests` → `pytest` → choose `tests`.
- Or run from terminal:

```bash
pytest tests
```

---

### Branch Workflow

- `main`: student-facing branch. Students pull updates from here to keep their clone current.
- `instructor-branch`: staging branch for instructor tweaks before release.

**Student update pattern**

```bash
git switch main
git pull origin main
```

**Instructor release pattern**

```bash
git switch instructor-branch
# develop and commit changes
git push origin instructor-branch
git switch main
git merge instructor-branch
git push origin main
```

Keep releases small and frequent so students can pull cleanly; resolve conflicts on `instructor-branch` before merging to `main`.

---

### Project Structure

```
.
├── src/
│   └── network_utilities/
│   └── plotting_utilities/
├── tests/
├── notebooks/
│   └── sequence_of_Jupyter_notebook_tutorials.ipynb
├── data/           # large datasets (ignored)
├── pyproject.toml
├── README.md
└── .gitignore
```

- `src/plotting_utils`: reusable plotting utilities for class exercises.
- `notebooks`: Jupyter notebooks for demos and assignments.
- `tests`: pytest-based unit/integration tests.
- `data`: tracked folder with `.gitkeep`; contents are ignored by Git.

---

### Notes and Tips

- Avoid `pygraphviz` on macOS; use `pydot` with `graphviz` installed.
- If you’re using conda, deactivate it before activating `.venv`.
- To deactivate the virtual environment: `deactivate`.

See [pyproject.toml](pyproject.toml) for dependency details and extras.