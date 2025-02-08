from elasticsearch7 import Elasticsearch
from config import ES_HOST, INDEX_NAME

class ElasticService:
    def __init__(self):
        self.es = Elasticsearch(ES_HOST)
        if not self.es.ping():
            raise ConnectionError("Could not connect to Elasticsearch!")

    def keyword_search(self, query):
        """Search for documents using keyword matching"""
        query_body = {"query": {"match": {"title": query}}}
        return self.es.search(index=INDEX_NAME, body=query_body)

    def semantic_search(self, query_vector):
        """Search for documents using semantic similarity"""
        query_body = {
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
                        "params": {"query_vector": query_vector},
                    },
                }
            }
        }
        return self.es.search(index=INDEX_NAME, body=query_body)

    def create_index(self, mapping):
        """Create index if it does not exist"""
        if not self.es.indices.exists(index=INDEX_NAME):
            self.es.indices.create(index=INDEX_NAME, body=mapping)
