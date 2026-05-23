from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Message(SQLModel, table=True):
    __tablename__ = "messages"

    id: Optional[int] = Field(default=None, primary_key=True)
    received_at: datetime = Field(default_factory=datetime.utcnow)
    source_channel: str = Field()
    sender: str = Field()
    body: str = Field()
    extracted_intent: Optional[str] = Field(default=None)
    proposed_action: Optional[str] = Field(default=None)
    confidence: Optional[str] = Field(default=None)
    status: str = Field(default="pending")
    escalation_reason: Optional[str] = Field(default=None)
    reviewed_by: Optional[str] = Field(default=None)
    reviewed_at: Optional[datetime] = Field(default=None)