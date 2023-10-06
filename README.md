# Welcome to rocinante-vectordb
Simple repository demoing how to train OpenAI LLM using LangChain on text documents for querying.

## Getting Started

A pre-requisite for this project is to have Python 3.11 installed on your machine, and to have some basic familiarity
with the language. You can find the installation instructions for Python [here](https://www.python.org/downloads/).

1. Clone this repository.
2. Install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. Create a trial account on [Pinecone](https://pinecone.io).
4. Create a new index on Pinecone called `policy-index`. Use `euclidean` as the index type and `1536` as the dimension.
5. Copy your Pinecone API key from the Pinecone console. 
6. Create an environment variable with the key `PINECONE_API_KEY` and the value of the copied API key.
7. Copy the environment name in Pinecone and update the `pinecone.init()` line in `main.py`.
8. Create an account on [OpenAI](https://platform.openai.com/).
9. Copy your OpenAI API key from the OpenAI console.
10. Create an environment variable with the key `OPENAI_API_KEY` and the value of the copied API key.
11. Run the script.

    ```bash
    python main.py
    ```

To modify the kind of query you want to run on the document, change the `query` variable in `main.py`. This is intended 
to give a general idea on how you can simply use Pinecone and OpenAI to build a simple search engine for text documents.
