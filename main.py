from fastapi import FastAPI, Depends
from model.category import Category
from schema.category import Category as CategorySchema
from sql_app.database import db,db_state_default
from typing import List

app = FastAPI()

@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()

@app.on_event('shutdown')
def startup():
    if not db.is_closed():
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/categories', response_model=List[CategorySchema])
def get_categories():
    # get from database
    return list(Category.select())