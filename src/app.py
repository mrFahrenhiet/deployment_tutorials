from fastapi import FastAPI
from .model import pipeline

app = FastAPI()


@app.get("/")
async def getHome():
    return {"message": "hello world!!"}

@app.post("/pred")
async def getPredictions(req_payload: dict):
    text = req_payload['text']
    res = pipeline(text)

    return res