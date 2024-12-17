"""
Hosting API for Emotion Detection
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def rendex_index():
    """
    Render the index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    """
    Analyze the text and return the emotion detected
    """
    analyzed_text = request.args.get('textToAnalyze')

    response = emotion_detector(analyzed_text)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion == None:
        return "Invalid input! Try again."
    else:
        return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




