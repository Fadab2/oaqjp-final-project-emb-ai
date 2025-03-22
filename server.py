"""Flask web app for detecting emotions using Watson NLP API."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
"""Route to analyze emotion from a given statement."""
@app.route("/emotionDetector")

def emotion_detector_route():
    """
    Route to analyze emotion from a given statement.
    Returns a formatted string response or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if not response or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 422

    output = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output

@app.route("/")
def index():
    """Render the homepage with input form."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
