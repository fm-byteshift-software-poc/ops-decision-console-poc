from datetime import datetime, timedelta

from sqlmodel import Session

from src.models.message import Message


def seed_data(session: Session) -> None:
    """Insert 10 hardcoded messages on server startup. LLM is NOT called."""
    now = datetime.utcnow()
    
    seed_messages = [
        Message(
            received_at=now - timedelta(hours=2),
            source_channel="whatsapp",
            sender="Mariana C. (+55 21 98888-1234)",
            body="Hi, I need to reschedule my meeting scheduled for tomorrow. Would Friday work?",
            extracted_intent="Sender wants to reschedule tomorrow's meeting to Friday",
            proposed_action="Confirm Friday availability and update calendar invite",
            confidence="high",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=4),
            source_channel="email",
            sender="supplier@logexpress.com.br",
            body="Ref order 4471 — delivery delayed due to postal service strike. New estimated date: July 18.",
            extracted_intent="Supplier notifying delivery delay for order 4471 until July 18",
            proposed_action="Update order 4471 delivery date and notify internal logistics team",
            confidence="high",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=6),
            source_channel="whatsapp",
            sender="Carlos M. (+55 11 97777-5566)",
            body="Can you send me that file again?? I need it urgently.",
            extracted_intent="Sender requesting re-send of an unspecified file urgently",
            proposed_action=None,
            confidence="low",
            status="escalated",
            escalation_reason="Low confidence — routed for human review"
        ),
        Message(
            received_at=now - timedelta(hours=10),
            source_channel="email",
            sender="hr@grupoalfa.com",
            body="Dear team, we are forwarding the updated proposal as discussed in the July 10 meeting. Awaiting your feedback.",
            extracted_intent="HR team following up on updated proposal sent after July 10 meeting",
            proposed_action="Route proposal to decision-maker for review and schedule follow-up",
            confidence="medium",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=14),
            source_channel="whatsapp",
            sender="Beatriz L. (+55 31 96666-7788)",
            body="Yes, Saturday works for me.",
            extracted_intent="Sender confirming an unspecified arrangement for Saturday",
            proposed_action=None,
            confidence="low",
            status="escalated",
            escalation_reason="Low confidence — routed for human review"
        ),
        Message(
            received_at=now - timedelta(hours=18),
            source_channel="email",
            sender="support@plataformaxyz.io",
            body="Your API key will expire in 7 days. Renew at dashboard.plataformaxyz.io",
            extracted_intent="Automated notice that API key expires in 7 days",
            proposed_action="Forward to technical owner for API key renewal",
            confidence="high",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=24),
            source_channel="whatsapp",
            sender="Roberto F. (+55 85 95555-3344)",
            body="I cannot access the system since yesterday. Can someone help?",
            extracted_intent="Sender reporting system access failure since yesterday",
            proposed_action="Escalate to IT support and request access log review",
            confidence="high",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=30),
            source_channel="email",
            sender="contact@parceirobeta.com",
            body="Hello! We would like to explore a partnership. We offer logistics solutions and believe there is synergy. Can we schedule a call?",
            extracted_intent="External company proposing partnership and requesting a call",
            proposed_action="Route to business development team for qualification",
            confidence="medium",
            status="actioned"
        ),
        Message(
            received_at=now - timedelta(hours=36),
            source_channel="whatsapp",
            sender="Anonymous (+55 11 94444-9900)",
            body="Did you see that?? lol send it to me too",
            extracted_intent="Sender requesting an unknown item seen elsewhere",
            proposed_action=None,
            confidence="low",
            status="escalated",
            escalation_reason="Low confidence — routed for human review"
        ),
        Message(
            received_at=now - timedelta(hours=42),
            source_channel="email",
            sender="leadership@internaldomain.com",
            body="We need a consolidated report for the month of June by this Thursday.",
            extracted_intent="Internal leadership requesting consolidated June report by Thursday",
            proposed_action="Acknowledge request and assign report generation task",
            confidence="high",
            status="actioned"
        ),
    ]
    
    session.add_all(seed_messages)
    session.commit()