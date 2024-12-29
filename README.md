# py-calculate-resin-genshin

A Python utility for calculating the time required to fully regenerate resin in Genshin Impact.

## Features

- Calculate the time required to fully regenerate resin.
- Display the exact time when the resin will be fully regenerated.
- User-friendly GUI built with Tkinter.
- Displays current time in Bangkok timezone.

## Requirements

- Python 3.x
- Tkinter
- Pillow
- Pytz

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/py-calculate-resin-genshin.git
    cd py-calculate-resin-genshin
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python py-calculate-resin-genshin.py
    ```

2. Enter your current resin amount (0-200) and click "Calculate".

## Deployment

To create an executable using PyInstaller, run:
```bash
pyinstaller --onefile --windowed --add-data "assets;assets" --icon="assets/paimon.png" py-calculate-resin-genshin.py