def test_register(user_register):
    assert user_register.status_code == 200
    assert user_register.json() == {
        "message": "User created successfully."
    }

def test_login(client, user_register):
    response = client.post("/login",json={
        "name":"Vasudev",
        "password":"123456"
    })


    assert response.status_code == 200
    assert "Token" in response.json()

def test_username_error(client):
    response = client.post("/login",json={
        "name" : "lakha",
        "password" : "123456"
    })
    assert response.status_code == 404
    assert response.json() == {
        "detail" : "User not found."
    } 

def test_userpassword_error(client,user_header):
    response = client.post("/login",json={
        "name" : "Vasudev",
        "password" : "12345"
    })
    assert response.status_code == 403
    assert response.json() == {
        "detail" : "Invalid credentials."
    } 

def test_register_error(client,user_register):
    response = client.post("/register",json={
        "name":"Vasudev",
        "password" : "123456",
        "role" : "user"
    })
    assert response.status_code == 400
    assert response.json() == {
        "detail":"User already exist."
    }

    
