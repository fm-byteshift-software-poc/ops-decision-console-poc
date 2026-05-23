from typing import Optional, List
from sqlmodel import Session, select, desc
from datetime import datetime

from src.models.message import Message
from src.repositories.database import engine


class MessageRepository:
    @staticmethod
    def create(message: Message) -> Message:
        with Session(engine) as session:
            session.add(message)
            session.commit()
            session.refresh(message)
            return message

    @staticmethod
    def get_by_id(message_id: int) -> Optional[Message]:
        with Session(engine) as session:
            statement = select(Message).where(Message.id == message_id)
            return session.exec(statement).one_or_none()

    @staticmethod
    def get_all(status: Optional[str] = None) -> List[Message]:
        with Session(engine) as session:
            statement = select(Message)
            if status:
                statement = statement.where(Message.status == status)
            statement = statement.order_by(desc(Message.received_at))
            return session.exec(statement).all()

    @staticmethod
    def update_review(message_id: int, status: str, reviewed_by: str) -> Optional[Message]:
        with Session(engine) as session:
            statement = select(Message).where(Message.id == message_id)
            message = session.exec(statement).one_or_none()
            if message:
                message.status = status
                message.reviewed_by = reviewed_by
                message.reviewed_at = datetime.utcnow()
                session.add(message)
                session.commit()
                session.refresh(message)
            return message