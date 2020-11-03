#!/usr/bin/env python
# coding: utf-8

# # Pos tagger for Dataset linguistic characteristic analysis.


## Copy the POS Tagger.py file into data directory where text data files are present before executing the script.


from nltk import pos_tag,sent_tokenize,word_tokenize
import glob
import random
import matplotlib.pyplot as plt

## Read in the dataset files.
files = glob.glob('*.txt')

## Sentence segmentation for POS tagging each sentence. 
print("Sentence segmentation performing...")
sentences = []
for f in files:
    f = open(f, "r", encoding="utf-8")
    text = f.read()
    templist = sent_tokenize(text)
    for item in templist:
        sentences.append(item)
print("segementation completed successfully!!")


## select random sentences and apply POS tagging. 

for i in range(3):
    random_num = random.randint(0, len(sentences))
    print(sentences[random_num])
    print('\n')
    print(pos_tag(word_tokenize(sentences[random_num])))
    print('\n')





