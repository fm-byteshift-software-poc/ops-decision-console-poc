import { useState, useEffect } from "react";
import type { Message } from "@/types/message";
import { messageService } from "@/services/message";
import IngestForm from "@/components/IngestForm";
import StatusFilterBar from "@/components/StatusFilterBar";
import MessageList from "@/components/MessageList";

export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [filter, setFilter] = useState<string>("all");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchMessages();
  }, [filter]);

  const fetchMessages = async () => {
    setLoading(true);
    setError(null);
    try {
      const statusParam = filter === "all" ? undefined : filter;
      const response = await messageService.getAll(statusParam);
      setMessages(response.items);
    } catch (err: any) {
      setError(err.message || "Failed to load messages");
    } finally {
      setLoading(false);
    }
  };

  const handleIngest = (newMessage: Message) => {
    setMessages((prev) => [newMessage, ...prev]);
  };

  const handleReview = (updatedMessage: Message) => {
    setMessages((prev) =>
      prev.map((msg) => (msg.id === updatedMessage.id ? updatedMessage : msg))
    );
  };

  return (
    <div className="min-h-screen bg-base-100 flex flex-col items-center py-8">
      <div className="w-full max-w-[960px] px-4 space-y-6">
        
        {/* Header */}
        <header className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-primary tracking-tight">Ops Decision Console</h1>
          <p className="text-base-content/60 mt-2">Message classification and routing PoC</p>
        </header>

        {/* Ingest Form */}
        <IngestForm onIngest={handleIngest} />

        {/* Filters */}
        <StatusFilterBar currentFilter={filter} onFilterChange={setFilter} />

        {/* Error Message */}
        {error && (
          <div className="alert alert-error text-sm shadow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>{error}</span>
          </div>
        )}

        {/* Message List */}
        <MessageList 
          messages={messages} 
          loading={loading} 
          onReview={handleReview} 
        />
      </div>
    </div>
  );
}