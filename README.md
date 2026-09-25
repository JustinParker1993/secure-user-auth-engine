# Secure RESTful Authentication Engine 
![Python](https://shields.io)

![FastAPI](https://shields.io)

![Pydantic](https://shields.io)

![PostgreSQL](https://shields.io)

![Pytest](https://shields.io)

![Git](https://shields.io)

![Bcrypt](https://shields.io)

 

I created a backend service designed to securely manage user registration and authentication lifecycles using a relational database (PostgreSQL) infrastructure. 
 

 ## Objective

 The primary purpose of this project was strict data validation. I wanted to design and deploy a secure backend authentication service that bridges the gap between web routing protocols and persistent relational database store. 



## Technical Stack 

| Technology | Logo / Badge | Component Layer | Project Implementation Role | 

| :--- | :--- | :--- | :--- | 

| **Python 3** | ![Python](https://shields.io) | Core Language | Powers the underlying Object-Oriented application logic, module dependencies, and functional scripting. | 

| **FastAPI** | ![FastAPI](https://shields.io) | Web API Framework | Orchestrates the high-performance asynchronous web routing endpoints (`/register` and `/login`) and manages JSON HTTP requests. | 

| **Pydantic** | ![Pydantic](https://shields.io) | Schema Validation | Enforces strict backend data schemas and typing validation on incoming payloads before they hit the database. | 

| **PostgreSQL** | ![PostgreSQL](https://shields.io) | Relational Database | Manages secure user record tables, unique constraints, and handles persistent database state storage. | 

| **bcrypt** | ![bcrypt](https://shields.io) | Cryptography & Identity | Manages industry-standard adaptive hashing and automatic salting protocols to prevent credential exposure. | 

| **pytest** | ![Pytest](https://shields.io) | Test Automation | Drives the comprehensive integration testing pipeline to ensure component reliability and validate endpoint functionality. | 

| **Git** | ![Git](https://shields.io) | Version Control | Manages local workspace repositories, branching, configuration exclusion tracking, and deployment synchronization. |
 

## Architecture & Security Implementations 

 

* **Adaptive Cryptographic Hashing (bcrypt):** Upgraded security mechanics from standard legacy hashes (`hashlib`) to use `bcrypt`. This automatically handles unique cryptographic salts and utilizes a configurable work factor to fully protect database storage records against brute-force and rainbow-table compromises. 

* **SQL Injection Mitigation:** Implements parameterized query execution schemas via the `psycopg2` driver. User inputs are isolated as parameter tuples, preventing malicious data blocks from breaking query logic. 

* **Request Schema Validation:** Leverages Pydantic `BaseModel` parsing to validate all incoming JSON data payloads at the API entry point, enforcing data integrity before hits interact with the database layer. 

* **Decoupled Configuration (DevSecOps):** Rejects hardcoded application secrets. System credentials are loaded dynamically into application memory using localized, git-ignored environment parameters (`.env`). 

* **Automated Regression Suite:** Built full-lifecycle integration testing using a `pytest` execution suite and FastAPI `TestClient` to validate HTTP responses, registration uniqueness, and validation code status flows. 

 

## Local Installation  

 

1. Clone this repository to your local workspace directory. 

2. Initialize and activate a Python virtual environment: 

   ```bash 

   python -m venv venv 

   .\venv\Scripts\Activate.ps1 

   ``` 

3. Install required application dependencies: 

   ```bash 

   pip install fastapi pydantic pytest bcrypt httpx psycopg2-binary python-dotenv 

   ``` 

4. Create a localized `.env` file in the root directory and map your database secrets: 

   ```text 

   DB_PASSWORD=your_local_postgresql_password 

   ``` 

5. Execute the automated test validation suite: 

   ```bash 

   pytest 

   ``` 

 
## Evidence of Execution

This system features complete test coverage using automated integration validations. Below is the direct terminal verification log showing the FastAPI client and PostgreSQL database engine successfully processing requests end-to-end:

```text

============================= test session starts =============================

platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0

rootdir: C:\Users\Justin\OneDrive\Desktop\Projects\secure-user-auth-engine

plugins: anyio-4.15.1

collected 1 item

test_main.py .                                                           [100%]

======================== 1 passed, 2 warnings in 2.13s ========================

```



 


 

 