import MessageCard from "@/components/MessageCard";
import type { Message } from "@/types/message";

interface Props {
  messages: Message[];
  loading: boolean;
  onReview: (message: Message) => void;
}

export default function MessageList({ messages, loading, onReview }: Props) {
  if (loading) {
    return (
      <div className="flex justify-center py-12">
        <span className="loading loading-spinner loading-lg text-primary"></span>
      </div>
    );
  }

  if (messages.length === 0) {
    return (
      <div className="text-center py-12 text-base-content/50">
        No messages found.
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {messages.map((msg) => (
        <MessageCard key={msg.id} message={msg} onReview={onReview} />
      ))}
    </div>
  );
}