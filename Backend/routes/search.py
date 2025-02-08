from flask import Blueprint, jsonify, request
from services.elastic import ElasticService
from services.embedder import EmbedderService

search_bp = Blueprint("search", __name__)
es_service = ElasticService()
embedder_service = EmbedderService()

@search_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    keyword_results = es_service.keyword_search(query)
    query_vector = embedder_service.get_vector(query)
    semantic_results = es_service.semantic_search(query_vector)

    results = []
    for hit in keyword_results["hits"]["hits"]:
        results.append({"type": "Keyword", "score": hit["_score"], "title": hit["_source"]["title"]})

    for hit in semantic_results["hits"]["hits"]:
        results.append({"type": "Semantic", "score": hit["_score"], "title": hit["_source"]["title"]})

    return jsonify(results)
