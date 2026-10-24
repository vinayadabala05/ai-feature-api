# AI Feature API

Clean FastAPI backend that exposes AI capabilities (Q&A, summarization, classification) as reliable REST endpoints.

Designed for easy integration with other services.

## Features
- Clean REST API design
- Pydantic validation
- Health check & proper error handling
- Ready for LLM integration
- Docker-ready structure

## Tech Stack
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs: http://localhost:8000/docs

## Endpoints
- `GET /health`
- `POST /summarize`
- `POST /classify`
- `POST /ask`

Built with production reliability and easy backend integration in mind.
