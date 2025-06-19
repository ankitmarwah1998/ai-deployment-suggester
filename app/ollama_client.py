def get_suggestion(logs, test_results, app_type, cost, traffic, zero_downtime):
    prompt = f"""
You are a CI/CD DevOps expert.

Suggest the best deployment strategy based on:

- App Type: {app_type}
- Cost Sensitivity: {cost}
- Traffic Pattern: {traffic}
- Zero Downtime Required: {zero_downtime}
- Logs: {logs}
- Test Results: {test_results}

Explain your suggestion in 3-5 bullet points.
"""
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

