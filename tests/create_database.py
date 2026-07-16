from backend.database import Base, engine

import backend.models.history

Base.metadata.create_all(bind=engine)

print("Database created.")