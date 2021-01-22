__author__ = 'xead'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")

@app.route("/", methods=["POST", "GET"])
def index_page(text="", prediction_message="", color="black"):
    if request.method == "POST":
        text = request.form["text"]
        print(text)
        prediction_message = classifier.get_prediction_message(text)
        print(prediction_message)
        if prediction_message == "Positive":
            color = "green"
        if prediction_message == "Negative":
            color = "red"

    return render_template('index.html', text=text, prediction_message=prediction_message, color=color)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
