from fastapi import FastAPI
from app.routes.api import router
from app.db.sql_connection import engine
from app.models.domains import articles

app = FastAPI()

app.include_router(router)

articles.Base.metadata.create_all(engine)
