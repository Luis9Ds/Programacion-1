import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

def train_model(texts, labels):
    text_preprocessed = [preprocess_text(text) for text in texts]
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(text_preprocessed)
    model = LogisticRegression()
    model.fit(features, labels)
    return model, vectorizer

def evaluate_model(model, vectorizer, texts, labels):
    text_preprocessed = [preprocess_text(text) for text in texts]
    features = vectorizer.transform(text_preprocessed)
    predictions = model.predict(features)
    report = classification_report(labels, predictions)
    return report, predictions

# Datos de entrenamiento
textos_entrenamiento = [
    "Me encanta este producto",
    "No estoy satisfecho con la calidad",
    "Excelente servicio al cliente",
    "El producto es terrible",
    "El envío fue rápido y eficiente",
    "Buena relación calidad-precio",
    "No lo recomendaría a nadie",
    "El producto superó mis expectativas",
    "El servicio al cliente es pésimo",
    "Producto de mala calidad",
    "La atención al cliente fue excepcional",
    "Muy contento con mi compra",
    "No volvería a comprar este producto",
    "Recomendaría este producto a mis amigos",
    "La calidad del producto es impresionante",
    "El precio es demasiado alto para lo que ofrece"
]
etiquetas_entrenamiento = [
    "positivo",
    "negativo",
    "positivo",
    "negativo",
    "positivo",
    "positivo",
    "negativo",
    "positivo",
    "negativo",
    "negativo",
    "positivo",
    "positivo",
    "negativo",
    "positivo",
    "positivo",
    "negativo"
]

# Datos de prueba
textos_prueba = [
    "El producto cumplió mis expectativas",
    "No estoy contento con la compra",
    "Mala calidad y mal servicio",
    "Altamente recomendado",
    "No lo compraría nuevamente"
]
etiquetas_prueba = [
    "positivo",
    "negativo",
    "negativo",
    "positivo",
    "negativo"
]

# Entrenamiento del modelo
modelo, vectorizer = train_model(textos_entrenamiento, etiquetas_entrenamiento)

# Validación cruzada del modelo
scores = cross_val_score(modelo, vectorizer.transform(textos_entrenamiento), etiquetas_entrenamiento, cv=5)
print("Precisión promedio: {:.2f}".format(scores.mean()))

# Evaluación del modelo en los datos de prueba
reporte, predicciones = evaluate_model(modelo, vectorizer, textos_prueba, etiquetas_prueba)
print("Reporte de clasificación:")
print(reporte)

# Imprimir las predicciones
for texto, etiqueta in zip(textos_prueba, predicciones):
    print("Texto:", texto)
    print("Predicción:", etiqueta)
    print()
