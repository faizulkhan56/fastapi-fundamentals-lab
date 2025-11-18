# FastAPI Fundamentals Lab -- Complete End‑to‑End Guide

## 📌 Introduction

This lab provides a **complete FastAPI learning project**, including: -
Deep theoretical explanation of FastAPI internals\
- Full CRUD API implementation\
- Path & Query Parameters\
- Pydantic model validation\
- Architecture diagrams\
- End‑to‑end request flow\
- Deployment (Local, Docker, Docker Compose)\
- Testing via Swagger & Postman\
- ML‑readiness discussion\
- References & best practices

This README is designed so **anyone can learn FastAPI from zero to
deployment**.

------------------------------------------------------------------------

# 🧠 1. What is FastAPI?

FastAPI is a modern, high‑performance web framework for building APIs in
Python.\
Key features include:

-   **Automatic validation** via Python type hints\
-   **Automatic documentation** (OpenAPI + Swagger UI)\
-   **Pydantic models** for request/response schemas\
-   **Async support** (built on Starlette and Uvicorn)\
-   Extremely fast --- comparable to Node.js & Go

FastAPI is widely used for: - Machine Learning model deployment\
- Backend microservices\
- Real‑time applications\
- Internal APIs & integrations

------------------------------------------------------------------------

# 🏗️ 2. Architecture Overview

    Client → Load Balancer (optional) → FastAPI (Uvicorn) → CRUD Logic → Database (In‑memory for this lab)

### 🔍 Detailed Flow

1.  **Client** sends HTTP request\
2.  **FastAPI router** matches endpoint\
3.  **Pydantic validation** checks input\
4.  **CRUD functions** handle business logic\
5.  Response goes back via **Uvicorn ASGI server**\
6.  FastAPI automatically converts everything to JSON

------------------------------------------------------------------------

# 📁 3. Project Structure

    fastapi-fundamentals-lab/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── routes.py
    │   ├── models.py
    │   ├── crud.py
    │   └── database.py
    ├── requirements.txt
    ├── docker-compose.yml
    ├── Dockerfile
    ├── README.md
    └── medium.md

This structure is **ML‑ready** and matches industry standards.

------------------------------------------------------------------------

# 🧩 4. Deep Code Explanation

## 4.1 main.py

Creates FastAPI app and includes routers.

    app = FastAPI()
    app.include_router(api_router)

## 4.2 models.py

Defines Pydantic `Item` model.

    class Item(BaseModel):
        id: int
        name: str
        description: Optional[str] = None

Pydantic automatically: - Validates JSON input - Serializes responses -
Generates OpenAPI schemas

## 4.3 database.py

Simple in‑memory list simulates a database.

## 4.4 CRUD Logic (crud.py)

Encapsulates business logic:

-   get_items()
-   get_item()
-   create_item()
-   update_item()
-   delete_item()

## 4.5 routes.py

Contains all API endpoints: - GET `/items/` - GET `/items/{id}` - POST
`/items/` - PUT `/items/{id}` - DELETE `/items/{id}` - Query param
examples (`filter/`, `search/`)

------------------------------------------------------------------------

# 🌐 5. End-to-End Request Example

### User runs:

    PUT /items/2

### Request body:

``` json
{
  "id": 2,
  "name": "Updated",
  "description": "Updated description"
}
```

### Flow:

    Browser/Postman
       ↓
    FastAPI Router (/items/{item_id})
       ↓
    Pydantic validates JSON → Item object
       ↓
    CRUD.update_item()
       ↓
    Items list updated
       ↓
    FastAPI returns response_model Item

------------------------------------------------------------------------

# 🧪 6. Testing the API

## Swagger UI (auto-generated)

Open:

    http://localhost:8000/docs

FastAPI auto-generates: - Request/response schemas\
- Try‑it‑out buttons\
- Documentation

## Postman

Examples:

### GET all items:

    GET /items/

### Create item:

    POST /items/
    Body:
    {
      "id": 4,
      "name": "Item Four",
      "description": "Great item"
    }

------------------------------------------------------------------------

# 🐳 7. Docker Deployment

## Build Image

    docker build -t fastapi-lab .

## Run Container

    docker run -p 8000:8000 fastapi-lab

## Docker Compose

    docker compose up --build

------------------------------------------------------------------------

# 🚀 8. Cloud Deployment (VM + Load Balancer)

1.  Provision VM
2.  Install Python / Docker
3.  Deploy app
4.  Expose via load balancer
5.  Verify using:

```{=html}
<!-- -->
```
    https://<LB-DNS>/items/

------------------------------------------------------------------------

# 🤖 9. ML API-Ready Architecture

To add a prediction endpoint: 1. Train ML model\
2. Load model in FastAPI\
3. Add `/predict` route\
4. Use Pydantic schema for features

Example:

``` python
@app.post("/predict/")
def predict(input: Features):
    return model.predict(...)
```

------------------------------------------------------------------------

# 📚 10. References

Official Docs: - https://fastapi.tiangolo.com/\
- https://pydantic-docs.helpmanual.io/\
- https://uvicorn.org/

------------------------------------------------------------------------

# 🏁 Conclusion

This FastAPI lab is a **complete foundation** for: - Learning API
development\
- Deploying backend services\
- Deploying ML models\
- Understanding API architecture

You can now extend this into production‑grade systems.
