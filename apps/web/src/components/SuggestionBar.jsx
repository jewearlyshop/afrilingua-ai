function SuggestionBar({ suggestions, onSelect }) {
  if (suggestions.length === 0) {
    return null;
  }

  return (
    <div
      style={{
        display: "flex",
        gap: "10px",
        flexWrap: "wrap",
        marginTop: "20px",
      }}
    >
      {suggestions.map((word) => (
        <button
          key={word}
          onClick={() => onSelect(word)}
          style={{
            padding: "10px 16px",
            borderRadius: "20px",
            border: "1px solid #ccc",
            cursor: "pointer",
            fontSize: "16px",
            backgroundColor: "#f5f5f5",
          }}
        >
          {word}
        </button>
      ))}
    </div>
  );
}

export default SuggestionBar;