function SearchBox({ value, onChange }) {
  return (
    <input
      value={value}
      onChange={onChange}
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
}

export default SearchBox;