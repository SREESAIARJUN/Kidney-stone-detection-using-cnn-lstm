# Kidney Stone Detection using CNN+LSTM

This repository contains a Streamlit web application for detecting kidney stones using a trained CNN+LSTM model.

## Repository Structure

```
kidney-stone-detection/
├── app.py
├── kidney_stone_detector_final.keras
├── requirements.txt
├── README.md
├── images/
│   ├── example1.jpg
│   └── example2.jpg
└── .gitignore
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/kidney-stone-detection.git
   cd kidney-stone-detection
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the model file:**

   If the `kidney_stone_detector_final.keras` file is not included (due to size limitations), download it from [link to your model file] and place it in the repository root.

### Running the Application

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## Usage

- Upload a CT scan image of a kidney (JPEG, JPG, or PNG format).
- The application will display the image and predict whether a kidney stone is detected.

## License

This project is licensed under the MIT License.

---

## .gitignore File

Create a `.gitignore` file to exclude unnecessary files:

```plaintext
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Virtual environment
venv/

# Model files (if necessary)
*.keras
*.h5

# Streamlit cache
.streamlit/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/
```

