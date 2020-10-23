# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


import boto3
import json
from botocore.config import Config

comprehend = boto3.client(service_name='comprehend')
text = "It is raining today in Seattle"
# text = input("Please enter the text that should be parsed for sentiment analysis :")

print('#=== Calling DetectSentiment ===#')
response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
print(response)
print('#=== End of DetectSentiment ===#')
print("The sentence you provided has a sentiment of:", response['Sentiment'])