from typing import Optional
from fastapi import HTTPException

from src.schemas.message import MessageIngest, MessageReview, MessageResponse, MessageListResponse
from src.services.message_service import MessageService


class MessageController:
    def __init__(self):
        self.service = MessageService()

    def ingest(self, payload: MessageIngest) -> MessageResponse:
        return self.service.ingest_message(payload)

    def list(self, status: Optional[str] = None) -> MessageListResponse:
        return self.service.list_messages(status)

    def get_one(self, message_id: int) -> MessageResponse:
        result = self.service.get_message(message_id)
        if not result:
            raise HTTPException(status_code=404, detail="Message not found")
        return result

    def review(self, message_id: int, payload: MessageReview) -> MessageResponse:
        result = self.service.review_message(message_id, payload)
        if not result:
            raise HTTPException(status_code=404, detail="Message not found")
        return result