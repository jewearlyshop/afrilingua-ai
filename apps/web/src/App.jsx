import { useEffect, useRef, useState } from "react";
import api from "./services/api";
import SearchBox from "./components/SearchBox";
import SuggestionBar from "./components/SuggestionBar";
import { applySuggestionSelection } from "./suggestionSelection";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const inputRef = useRef(null);
  const requestIdRef = useRef(0);
  const debounceRef = useRef(null);

  useEffect(() => {
    inputRef.current?.focus();

    return () => {
      if (debounceRef.current) {
        clearTimeout(debounceRef.current);
      }
    };
  }, []);

  async function fetchSuggestions(value) {
    if (!value.trim()) {
      setSuggestions([]);
      setSelectedIndex(0);
      setLoading(false);
      return;
    }

    const requestId = ++requestIdRef.current;

    setLoading(true);
    setError("");

    try {
      const response = await api.get(
        `/predict/${encodeURIComponent(value)}`
      );

      if (requestId !== requestIdRef.current) {
        return;
      }

      setSuggestions(response.data.suggestions || []);
      setSelectedIndex(0);
    } catch (err) {
      if (requestId !== requestIdRef.current) {
        return;
      }

      console.error("Prediction error:", err);
      setSuggestions([]);
      setError("Prediction service unavailable.");
    } finally {
      if (requestId === requestIdRef.current) {
        setLoading(false);
      }
    }
  }

  function handleChange(event) {
    const value = event.target.value;

    setText(value);
    setError("");

    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }

    debounceRef.current = setTimeout(() => {
      fetchSuggestions(value);
    }, 35);
  }

  async function recordSelection(word) {
    const trimmed = text.trim();

    if (!trimmed) {
      return;
    }

    const words = trimmed.split(/\s+/);

    let previous;

    if (text.endsWith(" ")) {
      previous = words[words.length - 1];
    } else if (words.length > 1) {
      previous = words[words.length - 2];
    } else {
      previous = words[0];
    }

    try {
      await api.post("/history/", {
        previous,
        selected: word,
      });
    } catch (err) {
      console.error("History error:", err);
    }
  }

  function handleSuggestionClick(word) {
    const nextState = applySuggestionSelection({
      text,
      word,
      recordSelection,
    });
    const newText = nextState.text;

    setText(newText);
    setSuggestions(nextState.suggestions);
    setSelectedIndex(nextState.selectedIndex);
    setError(nextState.error);

    requestIdRef.current += 1;

    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }

    requestAnimationFrame(() => {
      inputRef.current?.focus();

      if (inputRef.current) {
        inputRef.current.setSelectionRange(
          newText.length,
          newText.length
        );
      }
    });
  }

  function handleKeyDown(event) {
    if (!suggestions.length) {
      return;
    }

    if (event.key === "ArrowDown") {
      event.preventDefault();

      setSelectedIndex((index) => (index + 1) % suggestions.length);
      return;
    }

    if (event.key === "ArrowUp") {
      event.preventDefault();

      setSelectedIndex(
        (index) => (index - 1 + suggestions.length) % suggestions.length
      );
      return;
    }

    if (event.key === "Enter" || event.key === "Tab") {
      event.preventDefault();

      const selected = suggestions[selectedIndex];

      if (selected) {
        handleSuggestionClick(selected.word);
      }

      return;
    }

    if (event.key === "Escape") {
      event.preventDefault();
      setSuggestions([]);
      setSelectedIndex(0);
    }
  }

  function clearText() {
    requestIdRef.current += 1;

    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }

    setText("");
    setSuggestions([]);
    setSelectedIndex(0);
    setError("");

    requestAnimationFrame(() => {
      inputRef.current?.focus();
    });
  }

  function loadExample(example) {
    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }

    setText(example);
    setSuggestions([]);
    setSelectedIndex(0);
    setError("");

    debounceRef.current = setTimeout(() => {
      fetchSuggestions(example);
    }, 35);

    requestAnimationFrame(() => {
      inputRef.current?.focus();
    });
  }

  return (
    <main className="app-shell">
      <section className="keyboard-card">
        <header className="app-header">
          <div className="brand-mark">A</div>

          <div>
            <p className="eyebrow">AFRILINGUA AI</p>
            <h1>Yorùbá Predictive Keyboard</h1>
            <p className="subtitle">
              Type naturally. Get intelligent Yorùbá word and next-word
              suggestions.
            </p>
          </div>
        </header>

        <section className="keyboard-panel">
          <div className="input-header">
            <span>Yorùbá</span>

            <div className="input-status">
              {loading && <span className="status-dot">Predicting…</span>}

              {text && !loading && (
                <button
                  type="button"
                  className="clear-button"
                  onClick={clearText}
                >
                  Clear
                </button>
              )}
            </div>
          </div>

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

          {error && <p className="error-message">{error}</p>}

          {!text && (
            <div className="keyboard-hint">
              <span>Try:</span>

              <button
                type="button"
                onClick={() => loadExample("ọmọ náà fẹ́")}
              >
                ọmọ náà fẹ́
              </button>

              <button
                type="button"
                onClick={() => loadExample("mo fẹ́ lọ")}
              >
                mo fẹ́ lọ
              </button>
            </div>
          )}
        </section>

        <footer className="keyboard-footer">
          <div className="feature">
            <span className="feature-icon">Aa</span>
            <div>
              <strong>Tone aware</strong>
              <span>Yorùbá diacritics preserved</span>
            </div>
          </div>

          <div className="feature">
            <span className="feature-icon">→</span>
            <div>
              <strong>Context aware</strong>
              <span>Predicts what comes next</span>
            </div>
          </div>

          <div className="feature">
            <span className="feature-icon">AI</span>
            <div>
              <strong>Adaptive</strong>
              <span>Learns from your selections</span>
            </div>
          </div>
        </footer>
      </section>
    </main>
  );
}

export default App;
