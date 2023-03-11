"""The main program is used to organize routes.

The routes defined in asynchronous manner and using
FastAPI to load it.
"""
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from src.core.hit import Summarizer
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to TLDR application!"}


@app.post("/summarize")
async def get_summarization(
    long_text: str = Body(default="This is just a default.", embed=True)
):
    summarizer = Summarizer()
    response_from_openai = summarizer.summarize(long_text=long_text)
    results = {
        "method": summarizer.purpose,
        "result": response_from_openai["choices"][0]["text"],
    }
    return results
