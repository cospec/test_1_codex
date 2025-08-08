def test_crud_flow(client):
    # Create
    r = client.post("/notes", json={"title": "First", "content": "Hello"})
    assert r.status_code == 201, r.get_json()
    note = r.get_json()
    note_id = note["id"]

    # Get one
    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "First"

    # Update
    r = client.put(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    assert r.get_json()["title"] == "Updated"

    # List with search
    r = client.get("/notes?q=Upda")
    assert r.status_code == 200
    data = r.get_json()
    assert data["total"] >= 1
    assert any(item["id"] == note_id for item in data["items"])

    # Delete
    r = client.delete(f"/notes/{note_id}")
    assert r.status_code == 200
    assert r.get_json()["deleted"] == note_id

    # 404 after delete
    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 404
