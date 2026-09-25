# Secure RESTful Authentication Engine 
![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![bcrypt](https://img.shields.io/badge/bcrypt-525252?logo=letsencrypt&logoColor=white)
 

I created a backend service designed to securely manage user registration and authentication lifecycles using a relational database (PostgreSQL) infrastructure. 
 


 ## Objective
-
 The primary purpose of this project was strict data validation. I wanted to design and deploy a secure backend authentication service that bridges the gap between web routing protocols and persistent relational database store. 



## Technical Stack 


| Technology | Component Layer | Project Implementation Role |
| :--- | :--- | :--- |
| **Python 3** | Core Language | Powers the underlying object-oriented application logic, module dependencies, and functional scripting. |
| **FastAPI** | Web API Framework | Orchestrates the asynchronous web routing endpoints (`/register` and `/login`) and manages JSON HTTP requests. |
| **Pydantic** | Schema Validation | Enforces strict backend data schemas and type validation on incoming payloads before they hit the database. |
| **PostgreSQL** | Relational Database | Manages secure user record tables, unique constraints, and persistent state storage. |
| **bcrypt** | Cryptography & Identity | Handles adaptive hashing and automatic salting to prevent credential exposure. |
| **pytest** | Test Automation | Drives integration testing to validate endpoint functionality and component reliability. |
| **Git** | Version Control | Manages local repositories, branching, configuration exclusion, and deployment synchronization. |
 

## Architecture & Security Implementations 

 

* **Adaptive Cryptographic Hashing (bcrypt):** Upgraded security mechanics from standard legacy hashes (`hashlib`) to use `bcrypt`. This automatically handles unique cryptographic salts and utilizes a configurable work factor to fully protect database storage records against brute-force and rainbow-table compromises. 

* **SQL Injection Mitigation:** Implements parameterized query execution schemas via the `psycopg2` driver. User inputs are isolated as parameter tuples, preventing malicious data blocks from breaking query logic. 

* **Request Schema Validation:** Leverages Pydantic `BaseModel` parsing to validate all incoming JSON data payloads at the API entry point, enforcing data integrity before hits interact with the database layer. 

* **Decoupled Configuration (DevSecOps):** Rejects hardcoded application secrets. System credentials are loaded dynamically into application memory using localized, git-ignored environment parameters (`.env`). 

* **Automated Regression Suite:** Built full-lifecycle integration testing using a `pytest` execution suite and FastAPI `TestClient` to validate HTTP responses, registration uniqueness, and validation code status flows. 

* **Deterministic Database Lifecycle Isolation:** Employs a dedicated `pytest` database cleanup fixture using psycopg2. The fixture targets and purges ephemeral mock profiles (e.g., test users and injection payloads) before or after execution loops, ensuring a completely stateless, repeatable test cycle without modifying structural database schemas. 
 

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



 


 

 