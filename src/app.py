from fastapi import FastAPI
import redis

from .model import pipeline
from .logger_setup import logger

r = redis.Redis(host="redis123", port=6379)

app = FastAPI()


@app.get("/")
async def getHome():
    return {"message": "hello world!!"}

@app.post("/pred")
async def getPredictions(req_payload: dict):
    text = req_payload['text']
    res = pipeline(text)
    logger.info(f"UserPayload: {req_payload}, ModelOutput: {res}")

    return res