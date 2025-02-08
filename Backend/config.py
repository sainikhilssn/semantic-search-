import os

ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
USE_PATH = os.getenv("USE_PATH", "/models/USE4")
INDEX_NAME = "questions-index"
