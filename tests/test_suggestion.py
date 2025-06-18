import requests

def test_suggestion():
    response = requests.post("http://localhost:5001/suggest", json={
        "logs": "Minor patch release. All tests passed.",
        "test_results": {"passed": True}
    })
    assert response.status_code == 200
    print(response.json())

