# FastAPI server with Pydantic validation

import os
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from app import UserManager 
from dotenv import load_dotenv



# Loads the environment variables from the hidden .env file
load_dotenv()


app = FastAPI(title="Secure Authentication API") 

 

# Database Configuration 

DB_CONFIG = { 

"dbname": "test_db", 
"user": "postgres", 
"password": os.getenv("DB_PASSWORD"),
"host": "localhost",
"port": "5432" 

} 

 

# Initialize your existing database class 

db_manager = UserManager(DB_CONFIG) 

 

# Data structure schema for incoming web requests 

class UserCredentials(BaseModel): 

    username: str 

    password: str 
 

@app.post("/register") 

def register(user: UserCredentials): 

 """API Endpoint to register a new user securely.""" 

 success = db_manager.register_user(user.username, user.password) 

 if not success: 

    raise HTTPException(status_code=400, detail="Username already exists.") 

 return {"message": "User registered successfully!"} 

 

@app.post("/login") 

def login(user: UserCredentials): 

 """API Endpoint to verify user login credentials.""" 

 is_valid = db_manager.verify_user(user.username, user.password) 

 if not is_valid: 

    raise HTTPException(status_code=401, detail="Invalid username or password.") 

 return {"message": "Login successful!"} 