import { forwardRef } from "react";

const SearchBox = forwardRef(function SearchBox(
  { value, onChange, onKeyDown },
  ref
) {
  return (
    <input
      ref={ref}
      value={value}
      onChange={onChange}
      onKeyDown={onKeyDown}
      placeholder="Type Yoruba..."
      style={{
        width: "100%",
        padding: "16px",
        fontSize: "24px",
        borderRadius: "10px",
        border: "1px solid #ccc",
        boxSizing: "border-box",
      }}
    />
  );
});

export default SearchBox;