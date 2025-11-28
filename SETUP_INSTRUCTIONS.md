# Setup Instructions - Background Remover

## ⚠️ Important: Python Version Issue

You're currently using **Python 3.14.0**, which is too new for this project. The required packages (`numba`, `scikit-image`) don't support Python 3.14 yet.

## ✅ Solution: Use Python 3.11 or 3.12

### Step 1: Install Python 3.11 or 3.12

1. Download Python 3.11 or 3.12 from: https://www.python.org/downloads/
2. **Important**: During installation, check "Add Python to PATH"
3. Install it

### Step 2: Verify Installation

Open a new terminal/PowerShell and check:
```
python --version
```
Should show Python 3.11.x or 3.12.x

### Step 3: Install Dependencies

Navigate to this project folder and run:
```
pip install -r requirements.txt
```

### Step 4: Run the Application

Double-click `start.bat` or run:
```
python app.py
```

The app will open in your browser at http://127.0.0.1:5000

---

## Alternative: If You Must Use Python 3.14

You would need to:
1. Install Visual Studio Build Tools (large download, ~6GB)
2. Wait for package maintainers to add Python 3.14 support
3. This is **not recommended** - using Python 3.11/3.12 is much easier

---

## Quick Check

To see which Python versions you have installed:
```
py --list
```

Then you can use a specific version:
```
py -3.11 -m pip install -r requirements.txt
py -3.11 app.py
```


