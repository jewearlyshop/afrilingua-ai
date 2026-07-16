from backend.database import SessionLocal
from backend.models.history import History

db = SessionLocal()

rows = db.query(History).all()

for row in rows:
    print(
        row.previous,
        "->",
        row.selected,
        "(",
        row.count,
        ")"
    )

db.close()