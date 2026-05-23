interface Props {
  currentFilter: string;
  onFilterChange: (filter: string) => void;
}

export default function StatusFilterBar({ currentFilter, onFilterChange }: Props) {
  const filters = [
    { label: "All", value: "all" },
    { label: "Pending", value: "pending" },
    { label: "Actioned", value: "actioned" },
    { label: "Escalated", value: "escalated" },
  ];

  return (
    <div className="flex flex-wrap gap-2 mb-6">
      {filters.map((f) => (
        <button
          key={f.value}
          className={`btn btn-sm ${
            currentFilter === f.value ? "btn-primary" : "btn-ghost"
          }`}
          onClick={() => onFilterChange(f.value)}
        >
          {f.label}
        </button>
      ))}
    </div>
  );
}