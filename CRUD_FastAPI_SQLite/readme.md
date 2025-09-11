# CRUD_FastAPI

A simple FastAPI CRUD application with SQLite and SQLAlchemy ORM.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Shahram-ali-butt/CRUD_FastAPI_SQLite.git
   cd CRUD_FastAPI

2. Create a "notes.db" file inside notes_API folder
    ```bash
    touch /notes_API/notes.db

3. Create a virtual environment and install dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # on Linux/Mac
    .venv\Scripts\activate      # on Windows

    pip install -r requirements.txt

4. Run the app:
    ```bash
    uvicorn notes_API.main:app --reload

5. Open your browser at:
    API docs: http://127.0.0.1:8000/docs
    Health check: http://127.0.0.1:8000/api/healthchecker
