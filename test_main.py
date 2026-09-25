# Test Suite

import pytest 

import psycopg2 

from fastapi.testclient import TestClient 

from main import app, DB_CONFIG 

 

client = TestClient(app) 

 

@pytest.fixture(autouse=True) 

def database_cleanup(): 

    """CLEANUP FIXTURE: Automatically purges test user records before each execution run.""" 

    connection = psycopg2.connect(**DB_CONFIG) 

    with connection.cursor() as cursor: 

        # Safely delete our specific test profiles to ensure a fresh, repeatable state 

        cursor.execute( 

            "DELETE FROM users WHERE username IN (%s, %s, %s);", 
            ("standard_user_2026", "schema_fail_user", "admin' --") 

        ) 

        connection.commit() 

    connection.close() 

 

def test_api_auth_lifecycle(): 

    """1. INTEGRATION TEST: Validates standard registration and login lifecycles.""" 

    payload = {"username": "standard_user_2026", "password": "SecureBcryptPassword1!"} 

    response = client.post("/register", json=payload) 

    assert response.status_code == 200 

    assert response.json() == {"message": "User registered successfully!"} 

     

    dup_response = client.post("/register", json=payload) 

    assert dup_response.status_code == 400 

    assert dup_response.json()["detail"] == "Username already exists." 

     

    login_response = client.post("/login", json=payload) 

    assert login_response.status_code == 200 

    assert login_response.json() == {"message": "Login successful!"} 

 

def test_api_invalid_login_credentials(): 

    """2. EDGE CASE TEST: Asserts authentication failure for non-existent users or bad passwords.""" 

    # Pre-register our test user for credential testing 

    payload = {"username": "standard_user_2026", "password": "SecureBcryptPassword1!"} 

    client.post("/register", json=payload) 

     

    bad_password_payload = {"username": "standard_user_2026", "password": "WrongPassword123!"} 

    response = client.post("/login", json=bad_password_payload) 

    assert response.status_code == 401 

    assert response.json()["detail"] == "Invalid username or password." 

     

    fake_user_payload = {"username": "ghost_profile_99", "password": "SomePassword1!"} 

    fake_response = client.post("/login", json=fake_user_payload) 

    assert fake_response.status_code == 401 

 

def test_api_input_schema_validation_failures(): 

    """3. INPUT SANITIZATION TEST: Asserts Pydantic blocks payloads missing parameters.""" 

    broken_payload = {"username": "schema_fail_user"} 

    response = client.post("/register", json=broken_payload) 

    assert response.status_code == 422 

 

def test_api_sql_injection_string_handling(): 

    """4. SECURITY EDGE CASE: Asserts parameterized queries safely handle attack vectors.""" 

    injection_payload = { 

        "username": "admin' --",  

        "password": "SELECT * FROM users WHERE '1'='1" 

    } 

    response = client.post("/register", json=injection_payload) 

    assert response.status_code == 200 

    assert response.json() == {"message": "User registered successfully!"} 

 




