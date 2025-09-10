# CRUD_FastAPI

A simple FastAPI CRUD application.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Shahram-ali-butt/CRUD_FastAPI.git
   cd CRUD_FastAPI

2. Create a virtual environment and install dependencies:
    python -m venv .venv
    source .venv/bin/activate   # on Linux/Mac
    .venv\Scripts\activate      # on Windows

    pip install -r requirements.txt

3. Run the app:
    uvicorn notes_API.main:app --reload

4. Open your browser at:
    API docs: http://127.0.0.1:8000/docs
    Health check: http://127.0.0.1:8000/api/healthchecker
