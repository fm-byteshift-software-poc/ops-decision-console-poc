from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool

from src.config.settings import settings


def create_db_engine():
    """Create engine with StaticPool for in-memory SQLite persistence."""
    if settings.database_url == "sqlite:///:memory:":
        return create_engine(
            settings.database_url,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
            echo=settings.debug,
        )
    return create_engine(
        settings.database_url,
        echo=settings.debug,
    )


engine = create_db_engine()


def get_session():
    with Session(engine) as session:
        yield session