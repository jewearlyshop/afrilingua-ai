from sqlalchemy import desc

from backend.database import SessionLocal
from backend.models.history import History


class HistoryService:

    def record(self, previous, selected):
        db = SessionLocal()

        record = (
            db.query(History)
            .filter(
                History.previous == previous,
                History.selected == selected,
            )
            .first()
        )

        if record:
            record.count += 1
        else:
            record = History(
                previous=previous,
                selected=selected,
                count=1,
            )
            db.add(record)

        db.commit()
        db.close()

    def predict(self, previous, limit=5):
        db = SessionLocal()

        rows = (
            db.query(History)
            .filter(History.previous == previous)
            .order_by(desc(History.count))
            .limit(limit)
            .all()
        )

        db.close()

        return [row.selected for row in rows]


_history = HistoryService()


def get_history():
    return _history