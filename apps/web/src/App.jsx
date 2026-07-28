import { useState, useRef } from "react";
import api from "./services/api";
import SearchBox from "./components/SearchBox";
import SuggestionBar from "./components/SuggestionBar";

function App() {
  const [text, setText] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef(null);
  
  async function handleChange(e) {
    const value = e.target.value;
    setText(value);

    if (!value.trim()) {
      setSuggestions([]);
      return;
    }

    try {
      const response = await api.get(
        `/predict/${encodeURIComponent(value)}`
      );

      setSuggestions(response.data.suggestions);
      setSelectedIndex(0);
    } catch (error) {
      console.error("Prediction error:", error);
      setSuggestions([]);
    }
  }

 async function handleSuggestionClick(word) {
  const endsWithSpace = text.endsWith(" ");
  let words = text.trim().split(" ");

  // Record learning
  const previous = endsWithSpace
    ? words[words.length - 1]
    : words[words.length - 1];

  try {
    await api.post("/history/", {
      previous,
      selected: word,
    });
  } catch (error) {
    console.error("History error:", error);
  }

  if (endsWithSpace) {
    // User finished a word and is choosing the NEXT word
    words.push(word);
  } else {
    // User is completing the current word
    words[words.length - 1] = word;
  }

  setText(words.join(" ") + " ");
  setSuggestions([]);
}
 function handleKeyDown(event) {
  console.log("Key pressed:", event.key);
  if (!suggestions.length) {
    return;
  }

  switch (event.key) {
  case "ArrowDown":
  event.preventDefault();

  setSelectedIndex((index) => {
    const next = (index + 1) % suggestions.length;
    return next;
  });

  requestAnimationFrame(() => {
    inputRef.current?.focus();
  });

  break;
   
  case "ArrowUp":
  event.preventDefault();

  setSelectedIndex((index) => {
    const next =
      (index - 1 + suggestions.length) % suggestions.length;
    return next;
  });
  requestAnimationFrame(() => {
    inputRef.current?.focus();
  });

  break;

  case "Enter":
  event.preventDefault();

  if (suggestions.length > 0) {
    handleSuggestionClick(
      suggestions[selectedIndex].word
    );
  }

  break;

case "Tab":
  event.preventDefault();

  if (suggestions.length > 0) {
    handleSuggestionClick(
      suggestions[selectedIndex].word
    );
  }

  break;

    case "Escape":
      setSuggestions([]);
      break;

    default:
      break;
  }
}
console.log("selectedIndex =", selectedIndex);
  return (
    <div
      style={{
        maxWidth: "700px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1>🌍 AfriLingua AI</h1>

      <p>
        Intelligent Yoruba predictive keyboard powered by AI.
      </p>

      <SearchBox
      ref={inputRef}
      value={text}
      onChange={handleChange}
      onKeyDown={handleKeyDown}
      />

      <SuggestionBar
        suggestions={suggestions}
        selectedIndex={selectedIndex}
        onSelect={handleSuggestionClick}
      />
    </div>
  );
}

export default App;