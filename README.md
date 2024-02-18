# Q&A with RAG and Custom Dataset using MongoDB Vecctor Database.

Overview
One of the most powerful applications enabled by LLMs is sophisticated question-answering (Q&A) chatbots. These are applications that can answer questions about specific source information. These applications use a technique known as Retrieval Augmented Generation, or RAG.

What is RAG?
RAG is a technique for augmenting LLM knowledge with additional data.

LLMs can reason about wide-ranging topics, but their knowledge is limited to the public data up to a specific point in time that they were trained on. If you want to build AI applications that can reason about private data or data introduced after a model’s cutoff date, you need to augment the knowledge of the model with the specific information it needs. The process of bringing the appropriate information and inserting it into the model prompt is known as Retrieval Augmented Generation (RAG).

LangChain has a number of components designed to help build Q&A applications, and RAG applications more generally.
Question and Answer using

## Installation

Provide `.env` configuration for your database details and open ai key

```
OPENAI_API_KEY=
MONGODB_CONN_STRING=
DB_NAME=
COLLECTION_NAME=
INDEX_NAME=
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

run project using venv

```
$ python3 -m venv venv
$ . ./venv/bin/activate
```

Install project dependencies

```bash
$ pip install -r requirements.txt
```

Run the application

```
$ uvicorn main:app --reload
```

## Deploy using Docker container

```
docker build -t fastapi_learn .
docker run -d -p 8000:80 fastapi_learn
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
