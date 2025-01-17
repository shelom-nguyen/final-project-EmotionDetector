"""
server.py: application
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detetector")

@app.route('/')
def render_index_page():
    """
    rendering index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def text_input():
    """
    getting text to analyse
    """
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        text_result = "Invalid text! Please try again!"
    else:
        text_result = f"For the given statement, the system response is 'anger': {result['anger']},\
                    'disgust': {result['disgust']},\
                    'fear': {result['fear']},\
                    'joy': {result['joy']}\
                     and 'sadness': {result['sadness']}.\
                     The dominant emotion is <b>{result['dominant_emotion']}</b>."
    return text_result

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
