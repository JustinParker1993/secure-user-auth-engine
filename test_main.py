# Integration Test Suite

import pytest 
from fastapi.testclient import TestClient 
from main import app 

 

client = TestClient(app) 

 

def test_api_auth_lifecycle(): 

    # 1. Clean registration request assertions 

    payload = {"username": "jakes_resume_dev", "password": "SecureBcryptPassword1!"} 

    response = client.post("/register", json=payload) 

    assert response.status_code == 200 

    assert response.json() == {"message": "User registered successfully!"} 

 

    # 2. Assert duplicate protection triggers bad request codes 

    dup_response = client.post("/register", json=payload) 

    assert dup_response.status_code == 400 

 

    # 3. Verify clean authentication routes pass 

    login_response = client.post("/login", json=payload) 

    assert login_response.status_code == 200 