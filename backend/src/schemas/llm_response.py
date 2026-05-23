from typing import Optional, Literal
from pydantic import BaseModel, Field


class ClassificationResponse(BaseModel):
    extracted_intent: str = Field(..., description="One sentence, max 15 words, describing what the sender wants")
    proposed_action: Optional[str] = Field(None, description="One sentence, max 15 words, describing the operational response")
    confidence: Literal["high", "medium", "low"] = Field(..., description="Confidence level of the classification")