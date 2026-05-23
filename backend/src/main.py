from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session

from src.config.settings import settings
from src.repositories.database import engine
from src.routes.messages import router as messages_router
from src.routes.health import router as health_router
from src.utils.seed import seed_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create all tables in the SQLite database
    SQLModel.metadata.create_all(engine)
    
    # Populate seed data on startup
    with Session(engine) as session:
        seed_data(session)
    
    yield


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url=None,
)

# Enable CORS for Vite dev server (localhost:5173) and production frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(messages_router)
app.include_router(health_router)