from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Flask instance
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract all the emotions and their scores from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    #result in dict format
    resultDict = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }

    #output response
    outputResponse = f"the system response is 'anger': {resultDict['anger']}, 'disgust': {resultDict['disgust']}, 'fear': {resultDict['fear']}, 'joy': {resultDict['joy']} and 'sadness': {resultDict['sadness']}. The dominant emotion is {resultDict['dominant_emotion']}."

    return outputResponse

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)



