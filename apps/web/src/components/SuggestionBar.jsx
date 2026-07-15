function SuggestionBar({ suggestions, onSelect }) {
  return (
    <div
      style={{
        display: "flex",
        gap: 10,
        marginTop: 20,
        flexWrap: "wrap",
      }}
    >
      {suggestions.map((word) => (
        <button
          key={word}
          onClick={() => onSelect(word)}
        >
          {word}
        </button>
      ))}
    </div>
  );
}

export default SuggestionBar;