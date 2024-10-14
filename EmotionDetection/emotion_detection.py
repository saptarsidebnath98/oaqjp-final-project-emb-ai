import requests, json  # Import the requests library to handle HTTP requests
import numpy as np # Import Numpy

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyse)

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service

    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    #extract the scores from the response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # calculate maximum value and find dominant emotion
    scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    emotions = ['anger','disgust','fear','joy','sadness']

    #getting max value index
    max_index = np.argmax(scores)

    #result dictionary output format
    resultDict = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': emotions[max_index]
    }

    return resultDict  # Return the response from the API