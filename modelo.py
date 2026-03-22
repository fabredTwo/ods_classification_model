print("probando pues...")
import joblib
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.data.path.append("/usr/share/nltk_data")
print("CARGANDO MODELO")
modelo_globalizado = joblib.load("/var/task/modeloprueba.pkl", mmap_mode="r")
print("MODELO cargado")
class Modelo:

    def __init__(self):
        print("INIT MODELO") 
        self.modelo = modelo_globalizado
        print("TOKENIZER")
        self.tokenizer = RegexpTokenizer(r'\w+')
        print("lematizer")
        self.stemmer_train = WordNetLemmatizer()
        print("STOPWORDS")
        self.nltk_stopwords = stopwords.words("spanish")

    def prediccion(self, texto):

        tokens = self.tokenizer.tokenize(texto)
        tokens = [p for p in tokens if p not in self.nltk_stopwords]
        tokens = [self.stemmer_train.lemmatize(p) for p in tokens]

        salida = " ".join(tokens)

        pred = self.modelo.predict([salida])

        return int(pred[0])