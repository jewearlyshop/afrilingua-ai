from backend.database import SessionLocal
from backend.models.history import History

db = SessionLocal()

record = History(
    previous="fẹ́",
    selected="lọ",
    count=1,
)

db.add(record)
db.commit()

print("Saved!")

db.close()