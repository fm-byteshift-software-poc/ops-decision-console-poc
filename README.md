# Ops Decision Console PoC

Backend for a message classification PoC that demonstrates confidence-based routing. Low-confidence decisions are visibly escalated for human review, never silently automated.

## Stack

- Python 3.11
- FastAPI 0.111
- SQLModel 0.0.18 with SQLite in-memory
- hf-inference-gateway for LLM integration
- Pydantic v2 for validation

## Quick start

1. Create virtual environment and install dependencies

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables

```
cp .env.example .env
# Edit .env with your HF_API_TOKEN
```

3. Start the server

```
uvicorn src.main:app --reload
```

4. Open Swagger UI at http://localhost:8000/docs

## API endpoints

- POST /api/messages/ingest - Ingest and classify a message
- GET /api/messages - List messages with optional status filter
- GET /api/messages/{id} - Get a single message
- PATCH /api/messages/{id}/review - Manually review an escalated message
- GET /api/health - Health check

## Test scenarios

See the OpenAPI specification at /docs for request/response schemas. Key flows:

- Ingest a clear message → confidence high → status actioned
- Ingest an ambiguous message → confidence low → status escalated with proposed_action null
- Review an escalated message via PATCH to update status and reviewer

---

## 👤 Maintained By

This project is developed and maintained by **FM ByteShift Software**

**Fernando Magalhães**  
CEO – FM ByteShift Software  
📞 (21) 97250-1546  
✉️ [contact@fmbyteshiftsoftware.com](mailto:contact@fmbyteshiftsoftware.com)  
🌐 [fmbyteshiftsoftware.com](https://fmbyteshiftsoftware.com)  
🏢 CNPJ: 62.145.022/0001-05 (Brazil)
