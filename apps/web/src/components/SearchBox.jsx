import { forwardRef } from "react";

const SearchBox = forwardRef(function SearchBox(
  { value, onChange, onKeyDown },
  ref
) {
  return (
    <div className="search-box">
      <textarea
        ref={ref}
        value={value}
        onChange={onChange}
        onKeyDown={onKeyDown}
        placeholder="Type in Yorùbá…"
        rows={3}
        spellCheck={false}
        autoComplete="off"
        aria-label="Yorùbá predictive keyboard input"
      />
    </div>
  );
});

export default SearchBox;
