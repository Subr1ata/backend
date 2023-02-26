from fastapi import FastAPI
from config.database import db
from router import api

app = FastAPI()

@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()

@app.on_event('shutdown')
def startup():
    if not db.is_closed():
        db.close()

app.include_router(api.router)