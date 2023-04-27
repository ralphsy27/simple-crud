from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getItems():
    return ['item1', 'item2', 'item2']