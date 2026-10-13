export function applySuggestionSelection({ text, word, recordSelection }) {
  recordSelection(word);

  const endsWithSpace = text.endsWith(" ");
  const words = text.trim().split(/\s+/).filter(Boolean);

  if (endsWithSpace) {
    words.push(word);
  } else if (words.length > 0) {
    words[words.length - 1] = word;
  } else {
    words.push(word);
  }

  return {
    text: `${words.join(" ")} `,
    suggestions: [],
    selectedIndex: 0,
    error: "",
  };
}