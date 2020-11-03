# app.py

from flask import Flask, request, jsonify

import boto3
app = Flask(__name__)

@app.route("/", methods=["POST"])
def analyse_sentiment():
    comprehend = boto3.client('comprehend')
    text_analysed = request.json.get("text")
    if text_analysed is None or text_analysed=="":
        return jsonify({'error': 'No text was provided!'}), 500
    
    response = comprehend.detect_sentiment(Text=text_analysed, LanguageCode='en')
    return response