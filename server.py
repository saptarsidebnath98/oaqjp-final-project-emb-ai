"""
Emotion Detector Flask app to analyze text and detect emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Flask instance
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """
    Handle emotion detection request and return formatted response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotions and their scores from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    # Result in dictionary format
    result_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    # Output response
    output_response = (
        f"the system response is 'anger': {result_dict['anger']}, "
        f"'disgust': {result_dict['disgust']}, 'fear': {result_dict['fear']}, "
        f"'joy': {result_dict['joy']} and 'sadness': {result_dict['sadness']}. "
        f"The dominant emotion is {result_dict['dominant_emotion']}."
    )

    return output_response

@app.route("/")
def render_index_page():
    """
    Render the index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
