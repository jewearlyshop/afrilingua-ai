from backend.services.history_service import get_history

history = get_history()

history.record("fẹ́", "lọ")
history.record("fẹ́", "lọ")
history.record("fẹ́", "lọ")

print(history.predict("fẹ́"))