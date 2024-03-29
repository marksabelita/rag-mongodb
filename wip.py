#
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# import params
# from langchain_community.vectorstores import MongoDBAtlasVectorSearch
# from langchain_openai import OpenAIEmbeddings
# from langchain_openai import OpenAI
#
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# print(os.environ['OPENAI_API_KEY'])
#
#
# class ChatBot:
#     async def ask(self, question):
#         vector_search = MongoDBAtlasVectorSearch.from_connection_string(
#             params.mongodb_conn_string,
#             params.db_name + "." + params.collection_name,
#             OpenAIEmbeddings(),
#             index_name=params.index_name,
#         )
#
#         qa_retriever = vector_search.as_retriever(
#             search_type="similarity",
#             search_kwargs={"k": 25},
#         )
#
#         prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
#             {context}
#             Question: {question}
#             """
#
#         PROMPT = PromptTemplate(
#             template=prompt_template, input_variables=["context", "question"]
#         )
#
#         qa = RetrievalQA.from_chain_type(
#             llm=OpenAI(),
#             chain_type="stuff",
#             retriever=qa_retriever,
#             return_source_documents=True,
#             chain_type_kwargs={"prompt": PROMPT}
#         )
#
#         docs = qa(
#             {"query": "what is gpt 4?", "context": ""})
#
#         print(docs['source_documents'])
#         return docs['result']
