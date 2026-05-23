import api from "@/lib/api";
import type { Message, IngestPayload, ReviewPayload } from "@/types/message";

export const messageService = {
  async getAll(status?: string): Promise<{ total: number; items: Message[] }> {
    const response = await api.get("/messages", { params: { status } });
    return response.data;
  },

  async getOne(id: number): Promise<Message> {
    const response = await api.get(`/messages/${id}`);
    return response.data;
  },

  async ingest(payload: IngestPayload): Promise<Message> {
    const response = await api.post("/messages/ingest", payload);
    return response.data;
  },

  async review(id: number, payload: ReviewPayload): Promise<Message> {
    const response = await api.patch(`/messages/${id}/review`, payload);
    return response.data;
  },
};
