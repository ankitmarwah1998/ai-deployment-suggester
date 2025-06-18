from flask import Flask, request, jsonify
from app.ollama_client import get_suggestion

app = Flask(__name__)

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    logs = data.get("logs", "")
    test_results = data.get("test_results", {})
    suggestion = get_suggestion(logs, test_results)
    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

