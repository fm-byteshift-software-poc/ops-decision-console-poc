from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field


class MessageIngest(BaseModel):
    source_channel: Literal["whatsapp", "email"]
    sender: str = Field(..., max_length=120)
    body: str = Field(..., min_length=1)


class MessageReview(BaseModel):
    status: Literal["actioned", "escalated"]
    reviewed_by: str = Field(..., max_length=80)


class MessageResponse(BaseModel):
    id: int
    received_at: datetime
    source_channel: str
    sender: str
    body: str
    extracted_intent: Optional[str] = None
    proposed_action: Optional[str] = None
    confidence: Optional[Literal["high", "medium", "low"]] = None
    status: str
    escalation_reason: Optional[str] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None


class MessageListResponse(BaseModel):
    total: int
    items: list[MessageResponse]