from fastapi import FastAPI
from .db.connection import Base, engine
from .routes import employee

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Employee router
app.include_router(employee.router, prefix="/employees", tags=["employees"])
