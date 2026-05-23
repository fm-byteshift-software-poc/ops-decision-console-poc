import { useState } from "react";
import { messageService } from "@/services/message";
import type { Message, IngestPayload } from "@/types/message";

interface Props {
  onIngest: (message: Message) => void;
}

export default function IngestForm({ onIngest }: Props) {
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState<IngestPayload>({
    source_channel: "email",
    sender: "",
    body: "",
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.body || !formData.sender) return;

    setIsLoading(true);
    try {
      const result = await messageService.ingest(formData);
      onIngest(result);
      setFormData({ ...formData, body: "", sender: "" });
    } catch (err) {
      console.error("Failed to ingest:", err);
      alert("Failed to ingest message");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="card bg-base-200 shadow-xl mb-6">
      <div className="card-body">
        <h2 className="card-title text-lg">Ingest Message</h2>
        
        <div className="form-control w-full">
          <label className="label">
            <span className="label-text">Source Channel</span>
          </label>
          <select
            className="select select-bordered w-full"
            value={formData.source_channel}
            onChange={(e) => setFormData({ ...formData, source_channel: e.target.value as "whatsapp" | "email" })}
          >
            <option value="email">Email</option>
            <option value="whatsapp">WhatsApp</option>
          </select>
        </div>

        <div className="form-control w-full">
          <label className="label">
            <span className="label-text">Sender</span>
          </label>
          <input
            type="text"
            placeholder="User Name or Email"
            className="input input-bordered w-full"
            value={formData.sender}
            onChange={(e) => setFormData({ ...formData, sender: e.target.value })}
            required
          />
        </div>

        <div className="form-control w-full">
          <label className="label">
            <span className="label-text">Message Body</span>
          </label>
          <textarea
            className="textarea textarea-bordered h-24"
            placeholder="Type the message content here..."
            value={formData.body}
            onChange={(e) => setFormData({ ...formData, body: e.target.value })}
            required
          ></textarea>
        </div>

        <div className="card-actions justify-end mt-4">
          <button type="submit" className="btn btn-primary" disabled={isLoading}>
            {isLoading ? "Processing..." : "Ingest & Classify"}
          </button>
        </div>
      </div>
    </form>
  );
}