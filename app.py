from flask import Flask, render_template, request, send_file
import pandas as pd
import os

# Import sentiment functions
from utils.sentiment_utils import analyze_sentiment, preprocess_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_results = None
    overall_sentiment = None
    analyzed_csv_available = False
    error = None

    # File path for storing analyzed results
    csv_path = os.path.join(os.getcwd(), "analyzed_results.csv")

    if request.method == "GET":
        if os.path.exists(csv_path):
            os.remove(csv_path)
        return render_template("index.html")

    # Handle text input
    text_input = request.form.get("text_input")
    file = request.files.get("file_input")

    if text_input:
        try:
            processed = preprocess_text(text_input)
            sentiment_results, overall_sentiment = analyze_sentiment([processed])
            sentiment_results = [{"text": text_input, **res} for res in sentiment_results]
        except Exception as e:
            error = f"Error analyzing text: {e}"

    # Handle CSV input
    elif file and file.filename.endswith(".csv"):
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.strip().str.lower()  # Normalize columns

            if "content" not in df.columns:
                error = "CSV must contain a 'content' column."
            else:
                processed = df["content"].apply(preprocess_text)
                sentiment_results, overall_sentiment = analyze_sentiment(processed)
                df["processed"] = processed
                df["compound"] = [res["compound"] for res in sentiment_results]
                df["label"] = [res["label"] for res in sentiment_results]
                df.to_csv(csv_path, index=False)

                sentiment_results = [
                    {"text": row["content"], "compound": row["compound"], "label": row["label"]}
                    for _, row in df.iterrows()
                ]
                analyzed_csv_available = True
        except Exception as e:
            error = f"Error processing CSV file: {e}"

    else:
        error = "Please enter text or upload a valid .csv file."

    return render_template(
        "index.html",
        sentiment_results=sentiment_results,
        overall_sentiment=overall_sentiment,
        analyzed_csv_available=analyzed_csv_available,
        error=error
    )

@app.route("/download")
def download():
    csv_path = os.path.join(os.getcwd(), "analyzed_results.csv")
    if os.path.exists(csv_path):
        return send_file(csv_path, as_attachment=True)
    return "No file available for download", 404

if __name__ == "__main__":
    app.run(debug=True)
