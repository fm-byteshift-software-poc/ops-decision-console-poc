export interface Message {
  id: number;
  received_at: string;
  source_channel: "whatsapp" | "email";
  sender: string;
  body: string;
  extracted_intent: string | null;
  proposed_action: string | null;
  confidence: "high" | "medium" | "low" | null;
  status: "pending" | "actioned" | "escalated";
  escalation_reason: string | null;
  reviewed_by: string | null;
  reviewed_at: string | null;
}

export interface IngestPayload {
  source_channel: "whatsapp" | "email";
  sender: string;
  body: string;
}

export interface ReviewPayload {
  status: "actioned" | "escalated";
  reviewed_by: string;
}
