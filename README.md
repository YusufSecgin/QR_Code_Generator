
# QR Code Generator
A simple and user-friendly QR Code Generator application built with Python using Tkinter for the graphical user interface. This application allows users to generate QR codes from URLs, save them as images with transparent backgrounds, and open URLs directly in a web browser.

## Features

- Generate QR codes from valid URLs.
- Save generated QR codes as PNG or JPEG images with transparent backgrounds.
- Open the generated URLs directly in your default web browser.
- User-friendly interface with a clean design.
## Requirements

- Python 3.x
- Libraries:
  - `qrcode`
  - `Pillow`
  - `Tkinter` (usually included with Python installations)
## Installation
1. Clone the repository:

2. Create a virtual environment (optional but recommended):
   ```bash
    python3 -m venv .venv

    source .venv/bin/activate  # On macOS/Linux

    .venv\Scripts\activate     # On Windows

3. Install the required libraries:
- pip install qrcode[pil] Pillow
## Usage

1. Run the application:
   ```bash
    python main.py
2. Enter the URL you want to generate a QR code for in the text field.
3. Click the "Generate QR Code" button to create the QR code.
4. Use the "Save" button to save the QR code image to your local machine.
5. Click "Open in Browser" to navigate to the entered URL.
