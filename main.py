from langchain.prompts import ChatPromptTemplate
from langchain_elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from ollama import Client
from langchain_ollama import OllamaLLM
from elasticsearch import Elasticsearch
from langchain_ollama import ChatOllama
from llama_index.embeddings.ollama import OllamaEmbedding

ELASTIC_PASSWORD = "DNQ4lbVjujOprjJHyT4l"
fingerprint="f60cf2ff92778d5982fbfafbdf3f2d51c5d1cb03b8aeb1faffd98826219246b8"

template="""
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use five sentences minimum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

loader=TextLoader(r"C:\Users\DELL 5583\Desktop\rag test\elasticsearch test\text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size = 500,chunk_overlap=0 )
docs= text_splitter.split_documents(documents)
# client = Client(host='http://172.25.1.141:11434')

ollama_embedding = OllamaEmbedding(
    model_name="llama3",
    base_url="http://172.25.1.141:11434",
)


pass_embedding = ollama_embedding.get_text_embedding_batch(
    ["This is a passage!", "This is another passage"], show_progress=True
)
print(pass_embedding)

query_embedding = ollama_embedding.get_query_embedding("Where is blue?")
print(query_embedding)



# llm = Ollama(model="llama3", base_url="http://172.25.1.141:11434")
# embeddings=OllamaEmbeddings(model=llm)
# embeddings.embed_query(model = "hello")
# res=client.embeddings(model = 'llama3', prompt ='why is sky blue')
# vector_db = Elasticsearch(
#     "https://localhost:9200",
#     basic_auth=("elastic", ELASTIC_PASSWORD),
#     ssl_assert_fingerprint=fingerprint
# )

# vector_db = ElasticsearchStore.from_documents(
#     docs,
#     embedding=embeddings
# )


