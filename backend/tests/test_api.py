def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["mode"] == "local-demo"


def test_chat_local_fallback(client):
    response = client.post("/api/chat", json={"message": "I feel stressed about work"})
    assert response.status_code == 200
    assert response.json()["emotion"] == "stressed"
    assert response.json()["safety_escalation"] is False


def test_chat_crisis_escalation(client):
    response = client.post("/api/chat", json={"message": "I want to end my life"})
    assert response.status_code == 200
    assert response.json()["safety_escalation"] is True
    assert "14416" in response.json()["reply"]


def test_mood_lifecycle(client):
    created = client.post("/api/moods", json={"mood": "Calm", "journal": "A quiet walk helped."})
    assert created.status_code == 201
    entry_id = created.json()["id"]
    assert client.get("/api/moods").json()[0]["mood"] == "Calm"
    assert client.get("/api/moods/summary").json()["total"] >= 1
    assert client.delete(f"/api/moods/{entry_id}").status_code == 204


def test_input_validation(client):
    assert client.post("/api/chat", json={"message": ""}).status_code == 422
    assert client.post("/api/moods", json={"mood": "Unknown"}).status_code == 422
