from datetime import datetime
from elasticsearch import Elasticsearch



ELASTIC_PASSWORD = "DNQ4lbVjujOprjJHyT4l"
fingerprint="f60cf2ff92778d5982fbfafbdf3f2d51c5d1cb03b8aeb1faffd98826219246b8"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ELASTIC_PASSWORD),
    ssl_assert_fingerprint=fingerprint
    )

doc = {
    "author": "kimchy",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now(),
}
resp = client.index(index="test-index", id=1, document=doc)
print(resp["result"])
