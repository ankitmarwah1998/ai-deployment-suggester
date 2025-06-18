import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def get_suggestion(logs, test_results):
    with open("app/prompts/deployment_prompt.txt") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(logs=logs, test_results=test_results)

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })

    return response.json().get("response", "").strip()

