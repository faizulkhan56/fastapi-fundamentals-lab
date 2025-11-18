# FastAPI Fundamentals Lab – ML API Ready CRUD Project

(Shortened README for the downloadable project. See chat for full explanation.)

## Quickstart

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or with Docker:

```bash
docker compose up --build
```

Then open:

- Swagger UI: http://localhost:8000/docs
- Root: http://localhost:8000/
