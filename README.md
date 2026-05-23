# Ops Decision Console PoC

Full-stack PoC demonstrating confidence-based message classification and routing. Low-confidence decisions are visibly escalated for human review and never silently automated. Includes a React frontend for operational workflow validation and a FastAPI backend for LLM integration and data persistence.

## Stack

**Backend**

- Python 3.11
- FastAPI 0.111
- SQLModel 0.0.18 with SQLite in-memory
- hf-inference-gateway for LLM integration
- Pydantic v2 for validation

**Frontend**

- React 19 with TypeScript
- Vite 6
- Tailwind CSS 4 with DaisyUI 5
- Axios for API communication
- Single-page operational layout (no routing library required)

## Quick start

**Backend**

1. Create virtual environment and install dependencies

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your HF_API_TOKEN
```

3. Start the server

```bash
uvicorn src.main:app --reload
```

**Frontend**

1. Install dependencies

```bash
cd frontend
npm install
```

2. Configure environment variables

```bash
cp .env.example .env
# Edit .env with VITE_API_BASE_URL if needed (defaults to http://localhost:8000)
```

3. Start the development server

```bash
npm run dev
```

4. Open http://localhost:3000 in your browser

## API endpoints

- POST /api/messages/ingest - Ingest and classify a message
- GET /api/messages - List messages with optional status filter
- GET /api/messages/{id} - Get a single message
- PATCH /api/messages/{id}/review - Manually review an escalated message
- GET /api/health - Health check

## UI Features

- Real-time message ingestion and LLM classification
- Confidence-based status routing with visual badges
- Escalation alerts for low-confidence messages (proposed_action hidden)
- Inline manual review workflow for operators
- Status filtering (All, Pending, Actioned, Escalated)
- Responsive layout optimized for operational dashboards

## Test scenarios

See the OpenAPI specification at /docs for request/response schemas. Key flows:

- Ingest a clear message -> confidence high -> status actioned
- Ingest an ambiguous message -> confidence low -> status escalated with proposed_action null
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
