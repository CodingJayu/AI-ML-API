
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk
nltk.download('stopwords')

stopwords = stopwords.words('english')
stemmer = PorterStemmer()

app = FastAPI()

class model_input(BaseModel):
    
    narrative : str
       
        
# loading the saved model
with open('prod_predictor_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('transformer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.post('/prediction')
def predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    narr = input_dictionary['narrative']

    narr = narr.replace('xx', '')
    narr = narr.replace('XX', '')
    words = narr.split()
    filtered_words = [word for word in words if word not in stopwords]
    narr=' '.join(filtered_words)
    
    # Stem the words
    wod = narr.split()
    stemmed_words = [stemmer.stem(word) for word in wod]
    narr= ' '.join(stemmed_words)
    
    # Transform the text data into a TF-IDF matrix
    narr = vectorizer.transform([narr])

    
    prediction = model.predict(narr)
    return prediction
#uvicorn Api:app
    
   
    
