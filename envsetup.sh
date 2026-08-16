#!/usr/bin/env bash

set -e

echo
echo "=============================================="
echo "  Streamlit Trading App - Environment Setup"
echo "=============================================="
echo

VENV_DIR=".venv"
REQUIREMENTS_FILE="requirements.txt"

# ------------------------------------------------
# 1. Check Python
# ------------------------------------------------

echo "[1/6] Checking Python..."

PYTHON=""

if command -v python >/dev/null 2>&1; then
    PYTHON="python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
elif command -v py >/dev/null 2>&1; then
    PYTHON="py"
elif cmd.exe /c "where py" >/dev/null 2>&1; then
    PYTHON="py"
fi

if [ -z "$PYTHON" ]; then
    echo
    echo "ERROR: Python was not found."
    echo
    echo "Please install Python 3.10+ and make sure it is"
    echo "available from Git Bash."
    echo
    echo "If Python is already installed, try:"
    echo
    echo "  cmd.exe /c \"where py\""
    echo
    exit 1
fi

echo "Python command: $PYTHON"

# ------------------------------------------------
# 2. Display Python version
# ------------------------------------------------

echo
echo "[2/6] Checking Python version..."

$PYTHON --version

# ------------------------------------------------
# 3. Check requirements.txt
# ------------------------------------------------

echo
echo "[3/6] Checking requirements.txt..."

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo
    echo "ERROR: $REQUIREMENTS_FILE was not found."
    echo
    echo "Please run this script from the project root."
    echo
    exit 1
fi

echo "Found: $REQUIREMENTS_FILE"

# ------------------------------------------------
# 4. Create virtual environment
# ------------------------------------------------

echo
echo "[4/6] Checking virtual environment..."

if [ ! -d "$VENV_DIR" ]; then

    echo "Creating virtual environment..."

    $PYTHON -m venv "$VENV_DIR"

    echo "Virtual environment created."

else

    echo "Virtual environment already exists."

fi

# ------------------------------------------------
# 5. Activate virtual environment
# ------------------------------------------------

echo
echo "[5/6] Activating virtual environment..."

if [ -f "$VENV_DIR/Scripts/activate" ]; then

    # Windows / Git Bash
    source "$VENV_DIR/Scripts/activate"

elif [ -f "$VENV_DIR/bin/activate" ]; then

    # Linux / macOS
    source "$VENV_DIR/bin/activate"

else

    echo
    echo "ERROR: Could not find virtual environment activation script."
    echo
    exit 1

fi

echo "Virtual environment activated."

# ------------------------------------------------
# 6. Install dependencies
# ------------------------------------------------

echo
echo "[6/6] Installing dependencies..."

python -m pip install --upgrade pip

python -m pip install -r "$REQUIREMENTS_FILE"

# ------------------------------------------------
# Verification
# ------------------------------------------------

echo
echo "=============================================="
echo "  Environment Setup Completed Successfully"
echo "=============================================="
echo

echo "Python:"
python --version

echo
echo "Python location:"
which python || true

echo
echo "Pip:"
python -m pip --version

echo
echo "=============================================="
echo "  Next Steps"
echo "=============================================="
echo

echo "Your virtual environment is active."

echo
echo "Run the application:"
echo
echo "  streamlit run app.py"

echo
echo "To activate it again later:"
echo
echo "  source .venv/Scripts/activate"

echo
echo "To deactivate:"
echo
echo "  deactivate"

echo