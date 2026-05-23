import { useState } from "react";
import { messageService } from "@/services/message";
import type { Message } from "@/types/message";

interface Props {
  message: Message;
  onReview: (message: Message) => void;
}

export default function MessageCard({ message, onReview }: Props) {
  const [isReviewing, setIsReviewing] = useState(false);
  const [reviewStatus, setReviewStatus] = useState<"actioned" | "escalated">("actioned");
  const [reviewerName, setReviewerName] = useState("");

  const handleReview = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!reviewerName) return;

    try {
      const updated = await messageService.review(message.id, {
        status: reviewStatus,
        reviewed_by: reviewerName,
      });
      onReview(updated);
      setIsReviewing(false);
    } catch (err) {
      console.error("Review failed:", err);
    }
  };

  const confidenceColor =
    message.confidence === "high"
      ? "badge-success"
      : message.confidence === "medium"
      ? "badge-warning"
      : "badge-error";

  return (
    <div className="card bg-base-100 shadow-md border border-base-300">
      <div className="card-body p-4">
        {/* Header */}
        <div className="flex justify-between items-start">
          <div className="flex flex-col">
            <span className="font-bold text-lg">{message.sender}</span>
            <div className="flex gap-2 text-xs text-base-content/60">
              <span className="uppercase">{message.source_channel}</span>
              <span>•</span>
              <span>{new Date(message.received_at).toLocaleString()}</span>
            </div>
          </div>
          <div className="flex gap-2">
            <div className={`badge ${confidenceColor}`}>{message.confidence?.toUpperCase()}</div>
            <div className={`badge ${message.status === "escalated" ? "badge-error" : "badge-neutral"}`}>
              {message.status.toUpperCase()}
            </div>
          </div>
        </div>

        {/* Body */}
        <p className="mt-2 p-2 bg-base-200 rounded text-sm">{message.body}</p>

        {/* Classification Details */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2 text-sm">
          <div>
            <strong className="text-base-content/70">Intent:</strong>
            <p>{message.extracted_intent || "None"}</p>
          </div>
          {message.proposed_action && (
            <div>
              <strong className="text-base-content/70">Proposed Action:</strong>
              <p>{message.proposed_action}</p>
            </div>
          )}
        </div>

        {/* Escalation Alert & Review */}
        {message.status === "escalated" && (
          <div className="mt-4">
            <div className="alert alert-warning text-sm shadow-sm">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="stroke-current shrink-0 h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                />
              </svg>
              <span>Escalation Reason: {message.escalation_reason || "Low confidence"}</span>
            </div>

            {!isReviewing ? (
              <button className="btn btn-sm btn-outline mt-2" onClick={() => setIsReviewing(true)}>
                Review Message
              </button>
            ) : (
              <form onSubmit={handleReview} className="mt-2 flex flex-col sm:flex-row gap-2 bg-base-200 p-3 rounded">
                <select
                  className="select select-bordered select-sm"
                  value={reviewStatus}
                  onChange={(e) => setReviewStatus(e.target.value as "actioned" | "escalated")}
                >
                  <option value="actioned">Actioned</option>
                  <option value="escalated">Keep Escalated</option>
                </select>
                <input
                  type="text"
                  placeholder="Reviewer Name"
                  className="input input-bordered input-sm flex-1"
                  value={reviewerName}
                  onChange={(e) => setReviewerName(e.target.value)}
                  required
                />
                <button type="submit" className="btn btn-sm btn-primary">Save Review</button>
              </form>
            )}
          </div>
        )}
      </div>
    </div>
  );
}