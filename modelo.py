import joblib
import pandas as pd
from nltk.tokenize import RegexpTokenizer, RegexpTokenizer, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Modelo:

    def __init__(self):
        self.modelo = joblib.load("modeloprueba.pkl")
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stemmer_train = WordNetLemmatizer()
        self.nltk_stopwords = stopwords.words("spanish")

    def prediccion(self, texto):
        tokens = self.tokenizer.tokenize(texto)
        tokens = [palabra for palabra in tokens if palabra not in self.nltk_stopwords]
        tokens = [self.stemmer_train.lemmatize(palabra) for palabra in tokens]
        salida = ' '.join(tokens)
        pred = self.modelo.predict([salida])
        return int(pred[0])

