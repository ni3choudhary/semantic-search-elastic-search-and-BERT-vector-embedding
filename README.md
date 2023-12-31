## Semantic Search on Bert Vector Embeddings Using Elasticsearch

- The Jupyter Notebook (`index_data.ipynb`) is designed to perform various operations related to data processing, to generate embeddings for the product description and then indexes the data into Elastic Search.

- The Python script (`index_mapping.py`) contains index mapping definition for ElasticSearch.

- The Python script (`app.py`) is a Flask application that enables users to input a query, performs a k-NN search on the ElasticSearch index and view the relevant results.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.x Installed.
- Required Python packages listed in requirements.txt (install using pip install -r requirements.txt)

## Getting Started

To create a project from scratch use following steps -

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/your-username/semantic-search-elastic-search-and-BERT-vector-embedding.git
    cd semantic-search-elastic-search-and-BERT-vector-embedding
    ```

2. Create Python Virtual Environment using below command (The recommended python version is 3.11.0).
    ```bash
    python -m venv venv
                OR
    conda activate -p venv python==3.11
    ```

3. Activate Virtual Environment

    ```bash
    .venv/bin/activate 
            OR
    .\venv\Scripts\activate
            OR
    source ./venv/Scripts/activate
    ```

- if you have used conda to create the virtual environment, use the following command to activate the virtual environment.

    ```bash
    conda activate venv
    ```

4. Install dependencies using below command
    ```bash
    pip install -r requirements.txt
    ```

5. Install Elasticsearch with .zip on windows 

    Elasticsearch can be installed on Windows using the Windows .zip archive.

    (i) Download the .zip archive for Elasticsearch 8.11.3 from:
    ```bash
    https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.11.3-windows-x86_64.zip
    ```

    Unzip it with your favorite unzip tool. This will create a folder called elasticsearch-8.11.3, which we will refer to as %ES_HOME%. In a terminal window, cd to the %ES_HOME% directory, for instance:
    ```bash
    cd C:\elasticsearch-8.11.3
    ```

    (2) Run Elasticsearch from the command line

    Run the following command to start Elasticsearch from the command line
    ```bash
    .\bin\elasticsearch.bat
    ```

    When starting Elasticsearch for the first time, security features are enabled and configured by default. 
    
    The following security configuration occurs automatically:

    - Authentication and authorization are enabled, and a password is generated for the elastic built-in superuser.
    - Certificates and keys for TLS are generated for the transport and HTTP layer, and TLS is enabled and configured with these keys and certificates.
    - An enrollment token is generated for Kibana, which is valid for 30 minutes.

    The password for the elastic user and the enrollment token are output to your terminal.
    
    To check the elasticsearch server, copy the password for the elastic user and open the URL `https://localhost:9200` in your browser. Type your user as `elastic` and password `YOUR_PASSWORDS_FROM_TERMINAL`. Save the passwords somewhere else for your future use.

6. Set up environment variables in a `.env` file.

    - `ELASTIC_USERNAME` = "elastic"
    - `ELASTIC_PASSWORD` = YOUR_PASSWORD_FROM_TERMINAL
    - `ELASTIC_CERT_FILE_LOCATION` = "D:/ElasticSearch/elasticsearch-8.11.3/config/certs/http_ca.crt" # made changes in file location as per your installation
    - `HUGGING_FACE_MODEL` ="all-mpnet-base-v2"
    - `ES_INDEX`= "myntra_products"
    - `FLASK_APP_HOST`= "0.0.0.0"
    - `FLASK_APP_PORT`= "5000"

7. If you want to convert text data to vector embeddings using a BERT model, and perform k-nearest neighbors (k-NN) search on the indexed data in ElasticSearch. Go inside the **semantic-search-elastic-search-and-BERT-vector-embedding** directory and run the Notebook.

    This Python notebook performs the following tasks:

        i.   Establish a connection to ElasticSearch using the provided credentials and server details.
        ii.  Read data from the CSV file (myntra_products_catalog.csv), Remove rows with null values and Sample 1000 records from the dataset.
        iii. Use the Hugging Face BERT model to convert the "Description" field to vector embeddings and Add a new column, "Description_Embeddings" to the DataFrame.
        iv.  Create a new index in ElasticSearch with the specified mapping.
        v.   Ingest the sampled and transformed data into the ElasticSearch index.
        vi.  Define a search query with an input keyword and its corresponding BERT embeddings.
        vii. Perform k-NN search on the ElasticSearch index and retrieve relevant information.

    `Note`:
    - Ensure that ElasticSearch is running and accessible.
    - The notebook assumes the existence of an ElasticSearch index mapping file (index_mapping.py).


8. If you want to use the flask APP, Go inside the **semantic-search-elastic-search-and-BERT-vector-embedding** directory and run `app.py` on terminal to start local server.
    ```bash
    python app.py
    ```

    The app should now be running at `http://localhost:5000`
