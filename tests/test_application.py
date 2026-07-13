def test_create_application(client,user_header):
    response=client.post("/user/application/", json={
        "job_title" : "QC",
        "location" : "Brampton",
        "status" : "applies"

    },headers=user_header)
    assert response.status_code == 200
    assert response.json() == {
        "message" : "application created successfully."
    }

def test_useronly_application(client, user_header):
    response = client.get("/user/list/applications",headers=user_header)
    assert response.status_code == 200

def test_user_update(client,user_header,user_create_application):
    response = client.put("/user/application/update/1",json={
        "job_title":"Qc1",
        "status" : "Got interview",
        "location" : "Brampton"
        },headers=user_header)
    assert response.status_code == 200
    assert response.json() == {
        "message" : "Update Successfully."
    }

def test_useronly_delete(client,user_create_application,user_header):
    response = client.delete("/user/application/delete/1",headers=user_header)
    assert response.status_code == 200

