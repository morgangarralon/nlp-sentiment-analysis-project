from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import re, joblib

class DataTraining:
    def __init__(self, type = None):
        self.type = type
        self.dataset = None

    def loadFromUrl(self, url, separator):
        self.dataset = pd.read_csv(url, sep=separator)
        self.dataset.columns = ["label", "data"]

    def addExtraFeatures(self):
        # Number of Exclamation
        self.dataset['ratio_exclamation'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'!', x)) / len(x)))
        # Number of ?
        self.dataset['ratio_questionmark'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'\?', x)) / len(x)))
        # Number of #
        self.dataset['ratio_hashtag'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'#', x)) / len(x)))
        # Number of @
        self.dataset['ratio_mention'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'@', x)) / len(x)))
        # Number of Quotes
        self.dataset['ratio_quotes'] = self.dataset['data'].apply(lambda x: (len(re.findall(r"'", x)) / len(x)))

    def cleanData(self):
        #Removing stop words
        stop_words = set(stopwords.words('english'))
        self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: ' '.join([w for w in x.split() if not w in stop_words]))
        # Removing URLs
        self.dataset['clean_data'] = self.dataset['clean_data'].apply(lambda x: re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', '', x))
        # Removing HTML tags
        self.dataset['clean_data'] = self.dataset['clean_data'].apply(lambda x: re.sub(r'&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', '', x))
        # Removing tags (@user)
        self.dataset['clean_data'] = self.dataset['clean_data'].apply(lambda x: re.sub(r'@[\w]*', '', x))
        # Removing single character
        # self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'\w | \w(?!\w+)', '', x))))
        # Removing special characters, numbers, punctuations
        self.dataset['clean_data'] = self.dataset['clean_data'].apply(lambda x: re.sub(r'[^a-zA-Z# ]', '', x))

    def tokenizeData(self):
        tokenized_data = self.dataset["clean_data"].apply(lambda x: word_tokenize(x))
        stemmer = PorterStemmer()
        tokenized_data = tokenized_data.apply(lambda x: [stemmer.stem(i) for i in x])
        tokenized_data = tokenized_data.apply(lambda x: ' '.join(x))
        self.dataset["tokenized_data"] = tokenized_data

    def countvectorizeData(self):
        count_vectorizer = CountVectorizer()
        count_vectorised_tweet = count_vectorizer.fit_transform(self.dataset['tokenized_data'])
        self.dataset_to_modelchooser = pd.concat([
            self.dataset['ratio_exclamation'],
            self.dataset['ratio_questionmark'],
            self.dataset['ratio_hashtag'],
            self.dataset['ratio_mention'],
            self.dataset['ratio_quotes'], pd.DataFrame(count_vectorised_tweet.toarray())
            ], axis = 1)
        self.count_vectorizer = count_vectorizer

    def saveBestCountvectorizer(self, filename):
        joblib.dump(self.count_vectorizer, filename + '.cv')

    def getComputedDataset(self):
        return self.dataset_to_modelchooser

    def getLabelDataset(self):
        return self.dataset['label']