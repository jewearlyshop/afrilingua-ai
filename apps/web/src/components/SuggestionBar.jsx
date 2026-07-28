function SuggestionBar({
  suggestions,
  selectedIndex,
  onSelect,
}) {
  if (!suggestions.length) {
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
      {suggestions.map((item, index) => (
        <button
  key={item.word}
  onClick={() => onSelect(item.word)}
  tabIndex={-1}
  style={{
    padding: "10px 16px",
    borderRadius: "20px",
    border:
      index === selectedIndex
        ? "2px solid #2563eb"
        : "1px solid #ccc",
    cursor: "pointer",
    fontSize: "16px",
    backgroundColor:
      index === selectedIndex
        ? "#dbeafe"
        : "#f5f5f5",
    fontWeight:
      index === selectedIndex
        ? "bold"
        : "normal",
  }}
>
  {item.word}
</button>
      ))}
    </div>
  );
}

export default SuggestionBar;