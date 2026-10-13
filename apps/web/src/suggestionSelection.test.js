import assert from "node:assert/strict";
import test from "node:test";
import { applySuggestionSelection } from "./suggestionSelection.js";

test("suggestion selection returns input updates before history learning resolves", () => {
  let recordedWord = "";

  const nextState = applySuggestionSelection({
    text: "ọmọ náà fẹ́ ",
    word: "jẹun",
    recordSelection(word) {
      recordedWord = word;

      return new Promise(() => {});
    },
  });

  assert.equal(recordedWord, "jẹun");
  assert.deepEqual(nextState, {
    text: "ọmọ náà fẹ́ jẹun ",
    suggestions: [],
    selectedIndex: 0,
    error: "",
  });
});

test("suggestion selection replaces the active word", () => {
  const nextState = applySuggestionSelection({
    text: "omo",
    word: "ọmọ",
    recordSelection() {},
  });

  assert.equal(nextState.text, "ọmọ ");
});
