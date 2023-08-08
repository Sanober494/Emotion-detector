from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    if request.method == 'POST':
        statement = request.form.get('statement')
        result = emotion_detector(statement)
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
