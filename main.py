from fastapi import FastAPI, Depends
from model.base import Category
from sql_app.database import db,db_state_default
app = FastAPI()

def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()

@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/categories')
def get_categories():
    # get from database
    return list(Category.select().dicts())