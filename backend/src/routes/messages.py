from fastapi import APIRouter, Query
from typing import Optional

from src.controllers.message_controller import MessageController
from src.schemas.message import MessageIngest, MessageReview, MessageResponse, MessageListResponse

router = APIRouter(prefix="/api", tags=["operations"])
controller = MessageController()


@router.post("/messages/ingest", response_model=MessageResponse, status_code=200)
def ingest_message(payload: MessageIngest):
    """Ingest raw message, classify via LLM, and route based on confidence."""
    return controller.ingest(payload)


@router.get("/messages", response_model=MessageListResponse)
def list_messages(status: Optional[str] = Query(None, description="Filter by status: pending, actioned, escalated")):
    """Retrieve messages, optionally filtered by status. Ordered by received_at descending."""
    return controller.list(status=status)


@router.get("/messages/{message_id}", response_model=MessageResponse)
def get_message(message_id: int):
    """Retrieve a single message by ID."""
    return controller.get_one(message_id)


@router.patch("/messages/{message_id}/review", response_model=MessageResponse)
def review_message(message_id: int, payload: MessageReview):
    """Manually update status and mark as reviewed by an operator."""
    return controller.review(message_id, payload)