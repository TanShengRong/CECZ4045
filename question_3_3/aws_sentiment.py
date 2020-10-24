# CZ4045 Assignment 1
# Question 3.3

import json
import requests
import pandas as pd
import os.path
import multiprocessing as mp
#import time

class SentimentAnalysis:

    url = "https://fhv4zgrdy0.execute-api.us-east-1.amazonaws.com/dev"

    def __init__(self, df: pd.DataFrame):
        self.df = df#.iloc[[0]]
        self.sentiments = None

    def query_sentiment(self):
        # do multiprocessing when calling API
        no_threads = mp.cpu_count()
        api_pool = mp.Pool(processes=no_threads)
        self.sentiments = api_pool.map(self.query_api, self.df["comment"])
        self.sentiments = pd.Series(self.sentiments)
        #self.sentiments = self.df["comment"].map(self.query_api)

    def query_api(self, comment: str):
        payload = {
            "text": comment
        }
        r = requests.post(self.url, json=payload)
        r_dict = json.loads(r.text)
        return r_dict['Sentiment']

    def _print(self):
        _df = pd.concat([self.df['stars'], self.df['comment'], self.sentiments], axis=1, keys=['Rating', 'Review', 'Sentiment'])
        print(_df)


if __name__ == "__main__":
    print("""
 ## ##   ### ##    ## ##   ##  ###  ### ##            ## ##     ## ###
##   ##   ##  ##  ##   ##  ##   ##   ##  ##           ##  ##   ##   ##
##        ##  ##  ##   ##  ##   ##   ##  ##               ##   ##
##  ###   ## ##   ##   ##  ##   ##   ##  ##              ##    ## ###
##   ##   ## ##   ##   ##  ##   ##   ## ##              ##     ##   ##
##   ##   ##  ##  ##   ##  ##   ##   ##                #   ##  ##   ##
 ## ##   #### ##   ## ##    ## ##   ####              ######    ## ##
    """)
    filepath = input("Enter name of file in current directory or its relative location: ")
    # filepath = "30_reviews.csv"
    if os.path.exists(filepath):
        print("Classifying using AWS Comprehend...")
        #start_time = time.time()
        sa = SentimentAnalysis(pd.read_csv(filepath))
        sa.query_sentiment()
        sa._print()
        #print(time.time() - start_time)
    else:
        print("Please check filename and location")