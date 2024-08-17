from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from ollama import Client
from converter import converter


documents= converter("AA.Docx")

text_splitter = CharacterTextSplitter(chunk_size = 500,chunk_overlap=0 )
docs= text_splitter.split_documents(documents)






# client = Client(host='http://172.25.1.139:11434')
# response = client.chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'هل تعرف العربية',
#   },
# ])
# print(response)



# x= (embeddings.get_query_embedding("ho"))

