from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': "FastAPI"}

@app.get("/")
def about():
    return {'message': 'Get Request in FastAPI'}