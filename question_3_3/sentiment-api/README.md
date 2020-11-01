# Pre-requisites on development machine

1. Serverless framework
2. AWS account credentials
3. NPM dependencies: serverless-wsgi, serverless-python-requirements
4. Python dependencies: see requirements.txt

# Deployment

Use "sls deploy" command

# Calling API

API endpoint: https://fhv4zgrdy0.execute-api.us-east-1.amazonaws.com/dev

POST Request:
{
"text": "This product is not very good"
}

Response:
{
"ResponseMetadata": {some_metadata},
"Sentiment": "NEGATIVE",
"SentimentScore": {
"Mixed": 1.2162070106569445e-06,
"Negative": 0.9998801946640015,
"Neutral": 7.249005284393206e-05,
"Positive": 4.6150704292813316e-05
}
}
