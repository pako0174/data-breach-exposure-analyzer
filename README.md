<p align="center">
  <img src="[logo.png](https://github.com/pako0174/data-breach-exposure-analyzer/blob/main/7ce3e00d-1e1b-4ed1-9bdb-5890cc6b0b6d.png)" width="200"/>
</p>

# Data Breach Exposure Analyzer

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

This tool checks whether email addresses have been exposed in public data breaches using the HaveIBeenPwned API.

## 🔐 Features
- Checks one or multiple email addresses from CSV
- CLI support with detailed breach results
- Prepares for future notebook-based analysis
- Fast setup and easy-to-use design

## 🛠️ Getting Started

### 1. Clone or download the repo
```bash
git clone https://github.com/your-username/data-breach-exposure-analyzer.git
cd data-breach-exposure-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your emails
Open `data/emails.csv` and add your email addresses, one per line.

### 4. Insert your HIBP API Key
Edit `main.py` and replace:
```python
API_KEY = "your_api_key_here"
```

### 5. Run the scanner
```bash
python main.py
```

## 📄 License
This project is licensed under the MIT License.

---

*Author: Mikel Angel*
