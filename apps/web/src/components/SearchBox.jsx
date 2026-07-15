function SearchBox({ value, onChange }) {
  return (
    <input
      value={value}
      onChange={onChange}
      placeholder="Type Yoruba..."
      style={{
        width: "100%",
        padding: 16,
        fontSize: 24,
        borderRadius: 10,
      }}
    />
  );
}

export default SearchBox;