
import os
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from queue import Queue
from threading import Thread
from utils.callback_handler import CustomCallbackHandler

load_dotenv()


class ChatBot:
    def ask(self, question):
        # Creating a Streamer queue
        streamer_queue = Queue()
        databaseName = os.getenv("DB_NAME")
        collectionName = os.getenv("COLLECTION_NAME")
        databaseAndCollection = ""

        if databaseName is not None and collectionName is not None:
            databaseAndCollection = databaseName + "." + collectionName

        connString = os.getenv("MONGODB_CONN_STRING")
        indexName = os.getenv("INDEX_NAME")

        vector_search = MongoDBAtlasVectorSearch.from_connection_string(
            connString,
            databaseAndCollection,
            OpenAIEmbeddings(),
            index_name=indexName,
        )

        qa_retriever = vector_search.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 25},
        )

        prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
            {context}
            Question: {question}
            """

        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        my_handler = CustomCallbackHandler(streamer_queue)

        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo-16k",
            callbacks=[my_handler],
            streaming=True,
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=qa_retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )

        def invokeQA(query):
            qa.invoke(input=query)

        # # Creating a thread with generate function as a target
        thread = Thread(target=invokeQA, kwargs={
                        "query": question})
        thread.start()
        #
        while True:
            # Obtain the value from the streamer queue
            value = streamer_queue.get()
            # Check for the stop signal, which is None in our case
            if value is None:
                # If stop signal is found break the loop
                break
            # Else yield the value
            yield f"data: {value}\n\n"
            # statement to signal the queue that task is done
            streamer_queue.task_done()
