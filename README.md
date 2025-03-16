# Test case for QC position at Gameloft

## Backend Setup

### Prerequisites
- Python 3.12 or higher
- UV package manager

### Installing UV Package Manager
```bash
# For Linux and macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# More information available at: https://docs.astral.sh/uv/
```

### Using UV Package Manager
UV is a modern Python package manager. Here are common commands:

```bash
# Create a new virtual environment
uv venv [path]

# Two ways to run Python files with virtual environment:

# 1. Direct run without activating (Recommended)
uv run python_file.py

# 2. Activate virtual environment then run normally
# For Linux/macOS
source .venv/bin/activate
# For Windows
.venv\Scripts\activate
# Then run Python normally
python python_file.py

# Install packages from pyproject.toml
uv sync

# Install a specific package
uv add package_name

# Install multiple packages
uv add package1 package2

# Install package with specific version
uv add package_name==1.0.0

# Install development dependencies
uv add --dev pytest black

# Update all packages
uv pip compile --upgrade

# List installed packages
uv pip list

# Remove a package
uv remove package_name
```

⚠️ **Important Notes**:

1. Always use `uv add` instead of `uv pip install`. While `uv pip install` will install the package, it won't update your project's dependencies in pyproject.toml. Using `uv add` ensures proper dependency tracking and management.

Example:
```bash
# ❌ Don't do this - package won't be tracked in pyproject.toml
uv pip install requests

# ✅ Do this instead - properly tracks dependency
uv add requests
```

2. Running Python files:
```bash
# ✅ Recommended: Use uv run directly - no activation needed
uv run script.py

# ⚠️ Alternative: Activate venv then run normally
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python script.py
```

### Running project
1. Clone the repository:
```bash
git clone https://github.com/VoThiHoaiThanh/QC_Gameloft_Test.git
```

2. Create virtual environment and install dependencies:
```bash
uv venv --python 3.12
uv sync
```

### Run the test

```bash
uv run src/test.py
```
