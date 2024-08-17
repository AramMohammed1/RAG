
import requests
import io

from elasticsearch import Elasticsearch
from llama_index.embeddings.ollama import OllamaEmbedding


ollama_embedding = OllamaEmbedding(
    model_name="llama3",
    base_url="http://172.25.1.141:11434",
)


es_client = Elasticsearch(
    "http://localhost:9200"
    )



x= (ollama_embedding.get_query_embedding("ho"))

header={
    "content-type":"application/json"
}
json_data={
    "data":"vvv"
}
url="http://localhost:9200/"
response=requests.put(url = url+"data-file/_doc/1?pretty", headers=header ,json=json_data)
print (response)
