from flask import Flask, render_template, request
import os
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

from dotenv import load_dotenv
load_dotenv()

ELASTIC_USERNAME = os.environ.get("ELASTIC_USERNAME")
ELASTIC_PASSWORD = os.environ.get("ELASTIC_PASSWORD")

ELASTIC_CERT_FILE_LOCATION = os.environ.get("ELASTIC_CERT_FILE_LOCATION")

HUGGING_FACE_MODEL = os.environ.get("HUGGING_FACE_MODEL")
ES_INDEX = os.environ.get("ES_INDEX")

FLASK_APP_HOST = os.environ.get('FLASK_APP_HOST')
FLASK_APP_PORT = int(os.environ.get('FLASK_APP_PORT'))

app = Flask(__name__)

# Elasticsearch connection
try:
    es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=(ELASTIC_USERNAME,ELASTIC_PASSWORD),
    ca_certs=ELASTIC_CERT_FILE_LOCATION
    )

    if not es.ping():
        raise ConnectionError("Unable to connect to Elasticsearch")
except ConnectionError as e:
    print("Connection Error:", e)


def search(input_keyword):
    model = SentenceTransformer(HUGGING_FACE_MODEL)
    input_embeddings = model.encode(input_keyword)

    query = {
        "field": "Description_Embeddings",
        "query_vector": input_embeddings,
        "k": 3,
        "num_candidates": 500
    }
    res = es.knn_search(index=ES_INDEX,
                        knn=query,
                        source=["ProductName", "Description"]
                        )
    results = res["hits"]["hits"]

    return results


@app.route('/', methods=['GET', 'POST'])
def home():
    error_message = None
    return render_template('index.html', error_message=error_message)

@app.route('/search_query', methods=["POST"])
def knn_search_fn():
    error_message = None
    if request.method == 'POST':
        search_query = request.form['search_query']
        if search_query:
            try:
                results = search(search_query)
                return render_template('results.html', search_results=results, search_query=search_query)
            except ConnectionError as e:
                error_message = "Error connecting to Elasticsearch. Please try again later."
                return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(host=FLASK_APP_HOST, port=FLASK_APP_PORT)
