from flask import Flask, request, jsonify
import re
import string
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import joblib
import numpy as np

app = Flask(__name__)

# load the model
clf = joblib.load('models/voting_model.pkl')

def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',text)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    print(data)
    url = data['url']
    page = requests.get(url)

    if page.status_code != 200:
        return jsonify({'status_code': page.status_code})

    soup = BeautifulSoup(page.content, 'html.parser')

    # getting text from all paragraphs
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])

    # cleaning the text
    text = remove_URL(text)
    
    # classify the text
    prediction = clf.predict(np.array([text]))

    return jsonify({'classification': prediction})
