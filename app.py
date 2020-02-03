from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
import re
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
# to be continued

def remove_pattern(input_text, pattern):
    r = re.findall(pattern, input_text)
    for i in r:
        input_text = re.sub(i, '', input_text)
    return input_text

def count_punct(input_text):
    count = sum([i for char in input_text if string.punctionation])
    return round(count/(len(input_text) - input_text.count(" ")), 3) * 100

app = Flask(__name__)

data = pd.read_csv('.data/sentiment.csv', sep = '\t')
print('salut')