from fastapi import FastAPI, Body, Depends
import schemas
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.get("/")
def getItems(session : Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.post("/")
def addItem(item:schemas.Item, session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

@app.delete("/{id}")
def deleteItem(id:int, session = Depends(get_session)):
    itemObject = session.query (models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted'


fakeDatabase = {
    1: {'task' : 'Clean car'},
    2: {'task' : 'write blog'},
    3: {'task' : 'start stream'}
}
#@app.get("/")
# def getItems():
#     return fakeDatabase

# @app.get("/{id}")
# def getItem(id:int):
#     return fakeDatabase[id]

#POST, PUT, DELETE requests to modify the fakeDatabase
#POST: add data
#PUT: Update data
#DELETE: delete

#option 1:
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task": task}
#     return fakeDatabase

#option 2 (pydantic):
@app.post("/")
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":item.task}
    return fakeDatabase 

#option 3:
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":body['task']}
#     return fakeDatabase 



#updating data using put
#note here that we're using the same URL path as getItem, but this
#ouute will specifically hangle the put request.
# @app.put("/{id}")
# def updateItem(id:int, item:schemas.Item):
#     fakeDatabase[id]['task'] = item.task
#     return fakeDatabase

#delete
# @app.delete("/{id}")
# def deleteItem(id:int):
#     del fakeDatabase[id]
#     return fakeDatabase