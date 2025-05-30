# SentiMeter - Sentiment Analysis Web App

**SentiMeter** is a powerful web-based sentiment analysis tool that helps you understand the emotional tone behind text content. Built with Flask and leveraging NLTK's VADER analyzer, it provides instant sentiment classification (positive, negative, or neutral) for both individual text inputs and bulk CSV file analysis.

<p align="center">
  <img src="./Screenshot%202025-05-30%20191335.png" alt="SentiMeter UI Screenshot" width="80%" />
  <br>
  <em>SentiMeter's clean, dark-themed interface with sentiment visualization</em>
</p>

## 🌐 Live Demo

Experience SentiMeter right now:  
🚀 **[Live Demo on Railway](https://web-production-62e27.up.railway.app/)**

---

## ✨ Key Features

### 📝 Flexible Input Options
- **Single Text Analysis**: Quick sentiment check for any text snippet
- **Bulk CSV Processing**: Analyze thousands of entries at once (requires 'content' column)
- **Real-time Results**: Instant feedback with detailed sentiment breakdown

### 📊 Comprehensive Sentiment Analysis
- Powered by NLTK's **VADER** (Valence Aware Dictionary and sEntiment Reasoner)
- Provides four sentiment metrics:
  - Positive score
  - Negative score
  - Neutral score
  - Compound score (normalized weighted composite)

### 🎨 User-Friendly Interface
- 🌙 Dark mode for comfortable extended use
- 📱 Fully responsive design (works on all devices)
- 🎯 Color-coded results for quick interpretation
- 📊 Visual progress bar showing sentiment strength

### 🔄 Practical Functionality
- 📥 Download analyzed results as CSV
- 🔄 One-click refresh for new analyses
- ⚡ Fast processing even for large datasets

---

## 🛠️ Technical Implementation

### 🧠 Sentiment Analysis Engine
- Uses **VADER** from NLTK library
- Rule-based model specifically attuned to social media/textual sentiments
- Scores text based on:
  - **Positive** (pos): 0.0 to 1.0
  - **Negative** (neg): 0.0 to 1.0
  - **Neutral** (neu): 0.0 to 1.0
  - **Compound**: Normalized score between -1 (most negative) and +1 (most positive)

### 📊 Classification Logic
- **Positive**: compound score ≥ 0.05
- **Negative**: compound score ≤ -0.05
- **Neutral**: -0.05 < compound score < 0.05

### 🗂️ Project Structure
SentiMeter/
├── app.py # Flask application entry point
├── templates/
│ └── index.html # Main UI template with Bootstrap 5
├── utils/
│ └── sentiment_utils.py # Core sentiment analysis functions
├── static/ # Static assets (CSS/JS)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/SentiMeter.git
cd SentiMeter
Install dependencies:

bash
pip install -r requirements.txt
Download NLTK data (first-time setup):

python
import nltk
nltk.download('vader_lexicon')
Run the application:

bash
python app.py
Access the app at: http://127.0.0.1:5000

📄 CSV File Format
For bulk analysis, prepare a CSV file with at least one column named content. Example:

csv
id,content,source
1,"I love this product! It's amazing.","Twitter"
2,"The service was terrible and slow.","Feedback form"
3,"It's okay, nothing special.","Survey"
The app will process all rows and return the original data augmented with sentiment scores.
