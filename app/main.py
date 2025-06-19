from flask import Flask, request, jsonify
from app.ollama_client import get_suggestion

app = Flask(__name__)

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    logs = data.get("logs", "")
    test_results = data.get("test_results", {})
    app_type = data.get("app_type", "web")
    cost = data.get("cost_sensitivity", "medium")
    traffic = data.get("traffic_pattern", "low")
    zero_downtime = data.get("zero_downtime_required", False)

    suggestion = get_suggestion(
        logs=logs,
        test_results=test_results,
        app_type=app_type,
        cost=cost,
        traffic=traffic,
        zero_downtime=zero_downtime
    )
    return jsonify({"suggestion": suggestion})

