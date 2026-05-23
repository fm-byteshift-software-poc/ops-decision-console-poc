from datetime import datetime
from typing import Optional

from src.repositories.message_repository import MessageRepository
from src.services.message_classifier import MessageClassifier
from src.models.message import Message
from src.schemas.message import MessageIngest, MessageReview, MessageResponse, MessageListResponse


class MessageService:
    def __init__(self):
        self.repository = MessageRepository()
        self.classifier = MessageClassifier()

    def ingest_message(self, payload: MessageIngest) -> MessageResponse:
        # 1. Persist initial message with pending status
        message = Message(
            source_channel=payload.source_channel,
            sender=payload.sender,
            body=payload.body,
            status="pending",
            received_at=datetime.utcnow()
        )

        # 2. Synchronous LLM classification
        classification = self.classifier.classify(payload.body)

        # 3. Apply classification results
        message.extracted_intent = classification.get("extracted_intent")
        message.proposed_action = classification.get("proposed_action")
        message.confidence = classification.get("confidence")

        # 4. Routing logic based on confidence
        if message.confidence == "low":
            message.status = "escalated"
            message.escalation_reason = "Low confidence — routed for human review"
            message.proposed_action = None
        else:
            message.status = "actioned"

        # 5. Persist final state and return
        saved = self.repository.create(message)
        return MessageResponse.model_validate(saved.model_dump())

    def list_messages(self, status: Optional[str] = None) -> MessageListResponse:
        items = self.repository.get_all(status=status)
        return MessageListResponse(
            total=len(items),
            items=[MessageResponse.model_validate(msg.model_dump()) for msg in items]
        )

    def get_message(self, message_id: int) -> Optional[MessageResponse]:
        msg = self.repository.get_by_id(message_id)
        return MessageResponse.model_validate(msg.model_dump()) if msg else None

    def review_message(self, message_id: int, payload: MessageReview) -> Optional[MessageResponse]:
        updated = self.repository.update_review(
            message_id=message_id,
            status=payload.status,
            reviewed_by=payload.reviewed_by
        )
        return MessageResponse.model_validate(updated.model_dump()) if updated else None