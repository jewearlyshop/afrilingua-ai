import { useState } from "react";
import api from "./services/api";
import SearchBox from "./components/SearchBox";
import SuggestionBar from "./components/SuggestionBar";

function App() {
  const [text, setText] = useState("");
  const [suggestions, setSuggestions] = useState([]);

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
    } catch (error) {
      console.error("Prediction error:", error);
      setSuggestions([]);
    }
  }

  function handleSuggestionClick(word) {
    const words = text.split(" ");

    // Replace only the last word being typed
    words[words.length - 1] = word;

    setText(words.join(" "));
    setSuggestions([]);
  }

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
        value={text}
        onChange={handleChange}
      />

      <SuggestionBar
        suggestions={suggestions}
        onSelect={handleSuggestionClick}
      />
    </div>
  );
}

export default App;