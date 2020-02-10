import pandas as pd
import re

class InputDataset:
    def __init__(self, type):
        self.type = type
        self.dataset = None

    def load_from_url(self, url, separator):
        self.dataset = pd.read_csv(url, sep=separator)
        self.dataset.columns = ["label", "data"]

    def add_extra_feature(self):
        # Number of Exclamation
        self.dataset['percentage_exclamation'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'!', x))))
        # Number of ?
        self.dataset['number_of_questionmark'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'?', x))))
        # Number of #
        self.dataset['number_of_hashtag'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'#', x))))
        # Number of @
        self.dataset['number_of_mention'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'@', x))))
        # Number of Quotes
        self.dataset['number_of_quotes'] = self.dataset['data'].apply(lambda x: (len(re.findall(r"'", x))))
        # Number if underscore
        self.dataset['number_of_underscore'] = self.dataset['data'].apply(lambda x: (len(re.findall(r'_', x))))

    def clean_data(self):
        # Removing URLs
        self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', '', x))))
        # Removing HTML tags
        self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', '', x))))
        # Removing tags (@user)
        self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'@[\w]*', '', x))))
        # Removing single character
        # self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'\w | \w(?!\w+)', '', x))))
        # Removing special characters, numbers, punctuations
        self.dataset['clean_data'] = self.dataset['data'].apply(lambda x: (len(re.sub(r'[^a-zA-Z#]', '', x))))


    def remove_pattern(self, text, list_word):
        for i in list_word:
            text = re.sub(i, '', text)
        return text