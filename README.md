# Background Remover

A Flask web application that removes backgrounds from images using AI.

## Requirements

- Python 3.8 - 3.13 (Python 3.14 is too new and may have compatibility issues)
- pip package manager

## Installation

### Option 1: Using Python 3.11 or 3.12 (Recommended)

If you have Python 3.14, you'll need to use Python 3.11 or 3.12 instead:

1. Install Python 3.11 or 3.12 from [python.org](https://www.python.org/downloads/)
2. Open a terminal in this project directory
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Option 2: Install Build Tools (For Python 3.14)

If you want to use Python 3.14, you'll need to install Visual Studio Build Tools:

1. Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)
2. During installation, select "C++ build tools"
3. Then install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### Method 1: Using the batch file (Windows)
Double-click `start.bat` or run:
```
start.bat
```

### Method 2: Using Python directly
```
python app.py
```

The application will:
- Start a Flask web server on `http://127.0.0.1:5000`
- Automatically open your web browser
- Allow you to upload images and remove their backgrounds

## Usage

1. Open the web application in your browser (usually opens automatically)
2. Click "Choose File" and select an image
3. Click "Remove Background"
4. Download the result image with transparent background

## Dependencies

- Flask - Web framework
- rembg - Background removal AI model
- Pillow (PIL) - Image processing

