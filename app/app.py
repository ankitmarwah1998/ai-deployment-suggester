from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

def get_suggestion(logs, test_results, app_type, cost, traffic, zero_downtime, commit_message="", files_changed=""):
    prompt = f"""
You are a highly experienced DevOps CI/CD expert.

Given the following context, recommend the most suitable deployment strategy.

🔹 App Type: {app_type}
🔹 Cost Sensitivity: {cost}
🔹 Traffic Pattern: {traffic}
🔹 Zero Downtime Required: {zero_downtime}
🔹 Commit Message: {commit_message}
🔹 Files Changed: {files_changed}
🔹 Logs / Patch Summary:
{logs}

✅ Test Results:
{test_results}

Please provide your recommendation in the following format:
1. **Deployment Strategy** (e.g., Rolling, Blue-Green, Canary)
2. **Reasoning** in 3–5 bullet points
3. **Risk Level** (Low, Medium, High)
4. Optional: Anything else CI/CD engineers should know
"""

    response = ollama.chat(model="gemma:2b", messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json

    suggestion = get_suggestion(
        logs=data.get("logs", ""),
        test_results=data.get("test_results", {}),
        app_type=data.get("app_type", "web"),
        cost=data.get("cost_sensitivity", "medium"),
        traffic=data.get("traffic_pattern", "low"),
        zero_downtime=data.get("zero_downtime_required", False),
        commit_message=data.get("commit_message", ""),
        files_changed=data.get("files_changed", "")
    )

    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
