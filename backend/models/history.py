from sqlalchemy import Column, Integer, String

from backend.database import Base


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)

    previous = Column(String, index=True)

    selected = Column(String)

    count = Column(Integer, default=1)