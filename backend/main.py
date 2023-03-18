"""The main program is used to organize routes.

The routes defined in asynchronous manner and using
FastAPI to load it.
"""
from dotenv import load_dotenv
from fastapi import FastAPI, Body
from src.core.hit import Summarizer
import logging
import os

logging.basicConfig(level=logging.INFO)
load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    """Produces welcome message, as the dummy endpoint.

    Returns:
        A dict that consists of welcome message: 'Welcome
        to TLDR application!'.

    """
    return {
        "message": "Welcome to TLDR application!"
        + str(os.environ.get("OPENAI_API_KEY"))
        + "...."
    }


@app.post("/summarize")
async def get_summarization(
    long_text: str = Body(default="This is just a default.", embed=True)
):
    """Fetches the summary of a long text using OpenAI API.

    Retrieves the summary response using OpenAI API and
    returns only the text and the purpose of this API.

    Args:
        long_text: Text to summarize.

    Returns:
        A dict that shows the summary and the purpose of
        this API. For example:

        {
            'method': 'summarize',
            'result': 'This is the summary of the long text'
        }
    """
    if os.environ.get("OPENAI_API_KEY") != None:
        summarizer = Summarizer()
        response_from_openai = summarizer.summarize(long_text=long_text)
        results = {
            "method": summarizer.purpose,
            "result": response_from_openai["choices"][0]["text"],
        }
    else:
        results = {
            "method": "summarize_default",
            "result": "response_default",
        }

    return results
