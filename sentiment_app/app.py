from flask import Flask, render_template, request, send_file, redirect, url_for
import pandas as pd
from utils.sentiment_utils import analyze_sentiment, preprocess_text
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        
        if os.path.exists("analyzed_results.csv"):
            os.remove("analyzed_results.csv")
        return render_template("index.html")

    sentiment_results = None
    overall_sentiment = None
    analyzed_csv_available = False
    error = None

    text_input = request.form.get("text_input")
    file = request.files.get("file_input")

    if text_input:
        processed = preprocess_text(text_input)
        sentiment_results, overall_sentiment = analyze_sentiment([processed])
        sentiment_results = [{"text": text_input, **res} for res in sentiment_results]

    elif file and file.filename.endswith(".csv"):
        df = pd.read_csv(file)
        if "content" not in df.columns:
            error = "CSV must have a 'content' column."
        else:
            processed = df["content"].apply(preprocess_text)
            sentiment_results, overall_sentiment = analyze_sentiment(processed)
            df["processed"] = processed
            df["compound"] = [res["compound"] for res in sentiment_results]
            df["label"] = [res["label"] for res in sentiment_results]
            df.to_csv("analyzed_results.csv", index=False)
            sentiment_results = [{"text": row["content"], "compound": row["compound"], "label": row["label"]}
                                 for _, row in df.iterrows()]
            analyzed_csv_available = True

    return render_template("index.html",
                           sentiment_results=sentiment_results,
                           overall_sentiment=overall_sentiment,
                           analyzed_csv_available=analyzed_csv_available,
                           error=error)

@app.route("/download")
def download():
    if os.path.exists("analyzed_results.csv"):
        return send_file("analyzed_results.csv", as_attachment=True)
    return "No file available for download", 404

if __name__ == "__main__":
    app.run(debug=True)
