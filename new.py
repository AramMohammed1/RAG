from elasticsearch import Elasticsearch
from llama_index.embeddings.ollama import OllamaEmbedding


ELASTIC_PASSWORD = "DNQ4lbVjujOprjJHyT4l"
fingerprint="f60cf2ff92778d5982fbfafbdf3f2d51c5d1cb03b8aeb1faffd98826219246b8"

ollama_client = OllamaEmbedding(
    model_name="llama3",
    base_url="http://172.25.1.141:11434",
    ollama_additional_kwargs={"mirostat": 0}

)


es_client = Elasticsearch(
    "http://localhost:9200"
    )

movies = [
    {"title": "Inception"},
    {"title": "The Shawshank Redemption"},
    {"title": "The Godfather"},
    {"title": "Pulp Fiction"},
    {"title": "Forrest Gump"}
]
# doc = ollama_client.get_query_embedding("Where is blue?")
# es_client.index(index="movies", document=doc,timeout="30s")
print (es_client.indices.get(index="data-file").body)
# Indexing movies
# for movie in movies:
#     movie['title_embedding'] = ollama_client.get_text_embedding_batch([movie['title']])
#     es_client.index(index="movies", document=movie)