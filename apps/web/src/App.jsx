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

    if (!value) {
      setSuggestions([]);
      return;
    }

    try {
      const response = await api.get(
        `/predict/${encodeURIComponent(value)}`
      );

      setSuggestions(response.data.suggestions);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div style={{ maxWidth: 700, margin: "40px auto" }}>
      <h1>🌍 AfriLingua AI</h1>

      <SearchBox
        value={text}
        onChange={handleChange}
      />

      <SuggestionBar
        suggestions={suggestions}
        onSelect={setText}
      />
    </div>
  );
}

export default App;