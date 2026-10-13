function SuggestionBar({
  suggestions,
  selectedIndex,
  onSelect,
}) {
  if (!suggestions.length) {
    return null;
  }

  return (
    <div className="suggestion-area">
      <div className="suggestion-label">
        Suggestions
      </div>

      <div
        className="suggestion-bar"
        role="listbox"
        aria-label="Yorùbá word suggestions"
      >
        {suggestions.map((item, index) => (
          <button
            key={`${item.word}-${index}`}
            type="button"
            role="option"
            aria-selected={index === selectedIndex}
            className={`suggestion-button ${
              index === selectedIndex ? "selected" : ""
            }`}
            onMouseDown={(event) => event.preventDefault()}
            onClick={() => onSelect(item.word)}
          >
            <span>{item.word}</span>

            {index === selectedIndex && (
              <kbd>↵</kbd>
            )}
          </button>
        ))}
      </div>
    </div>
  );
}

export default SuggestionBar;
