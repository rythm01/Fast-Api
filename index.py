from fastapi import FastAPI
from routes.index import user
from config.db import init_db
app = FastAPI()

init_db()

app.include_router(user)