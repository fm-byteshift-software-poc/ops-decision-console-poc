from typing import Dict, Any
from hf_inference_gateway import HuggingFaceGateway, GatewayConfig

from src.config.settings import settings
from src.schemas.llm_response import ClassificationResponse

# SYSTEM_PROMPT = """You are a message classification engine. Given a raw inbound message, extract:
# 1. extracted_intent: one sentence, max 15 words, describing what the sender wants.
# 2. proposed_action: one sentence, max 15 words, describing the single most appropriate operational response.
# 3. confidence: exactly one of 'high', 'medium', or 'low'.
#    - high: intent is unambiguous, action is clear.
#    - medium: intent is probable, minor assumptions made.
#    - low: intent is unclear, information is missing, or multiple interpretations are equally plausible.
# Respond ONLY with a JSON object with exactly these three keys. No explanation. No markdown. No preamble."""

SYSTEM_PROMPT = """You are a message classification engine. Given a raw inbound message, extract:
1. extracted_intent: one sentence, max 15 words, describing what the sender wants.
2. proposed_action: one sentence, max 15 words, describing the single most appropriate operational response.
3. confidence: exactly one of 'high', 'medium', or 'low'.
   - high: intent is unambiguous, ALL required context is present, action is clear and immediately executable without assumptions.
   - medium: intent is probable but requires ONE minor assumption; action is clear only if that assumption is correct.
   - low: intent is unclear, critical information is missing (who/what/when/where), multiple interpretations are equally plausible, message is extremely short (<5 words), OR message lacks actionable specificity.
CRITICAL: When in doubt, default to 'low'. It is safer to escalate uncertain cases than to automate incorrectly.
Respond ONLY with a JSON object with exactly these three keys. No explanation. No markdown. No preamble."""

class MessageClassifier:
    def __init__(self):
        config = GatewayConfig(
            api_token=settings.hf_api_token,
            model_id=settings.hf_model_id,
            base_url=settings.hf_base_url,
            timeout=30,
            max_retries=2
        )
        self.gateway = HuggingFaceGateway(config)

    def classify(self, body: str) -> Dict[str, Any]:
        try:
            result = self.gateway.execute_inference(
                message=body,
                context={},
                system_prompt=SYSTEM_PROMPT,
                response_schema=ClassificationResponse
            )
            data = result.payload
            return {
                "extracted_intent": data.get("extracted_intent"),
                "proposed_action": data.get("proposed_action"),
                "confidence": data.get("confidence")
            }
        except Exception as e:
            print(f"Classification failed: {e}")
            return {
                "extracted_intent": "Parsing error",
                "proposed_action": None,
                "confidence": "low"
            }