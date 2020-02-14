from app import app
from flask import render_template
from app.models.DataTraining import DataTraining
from app.models.ModelChooser import ModelChooser

@app.route('/train', methods=['GET'])
def train():
    data_training = DataTraining()
    data_training.loadFromUrl("https://raw.githubusercontent.com/morgangarralon/nlp-sentiment-analysis/morgan/app/static/data/training/tweets.tsv?token=ABUFSBXTLPPZBGAV7H47IBC6JVMAA", separator = "\t")
    data_training.cleanData()
    data_training.tokenizeData()
    data_training.addExtraFeatures()
    data_training.countvectorizeData()

    dataset_x = data_training.getComputedDataset()
    dataset_y = data_training.getLabelDataset()

    model_chooser = ModelChooser()
    model_chooser.findBestModel(dataset_x, dataset_y)
    model_chooser.saveBestModel(type(model_chooser.best_model).__name__)
    data_training.saveBestCountvectorizer(type(model_chooser.best_model).__name__)

    template = render_template('train.html')

    return template