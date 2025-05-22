import re
from bs4 import BeautifulSoup
import contractions
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = BeautifulSoup(text, "html.parser").get_text()
    text = contractions.fix(text)
    return text

def analyze_sentiment(texts):
    results = []
    for t in texts:
        scores = sid.polarity_scores(t)
        label = 'Positive' if scores['compound'] >= 0.05 else 'Negative' if scores['compound'] <= -0.05 else 'Neutral'
        results.append({'compound': scores['compound'], 'label': label})

    avg = sum([r['compound'] for r in results]) / len(results)
    overall = 'Positive' if avg >= 0.05 else 'Negative' if avg <= -0.05 else 'Neutral'
    return results, overall
