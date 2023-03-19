"""The main program is used to organize routes.

The routes defined in asynchronous manner and using
FastAPI to load it.
"""
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Response, status
from pydantic import BaseModel, Field
from src.core.hit import Summarizer
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

app = FastAPI()


class ResponseModel(BaseModel):
    method: str = Field(title="The method called from the API.")
    result: str = Field(
        title="The result of hitting API key, but if there is no API key provided, this field may tells you if no API key is provided."
    )


@app.get("/")
async def root():
    """Produces welcome message, as the dummy endpoint.

    Returns:
        A dict that consists of welcome message: 'Welcome
        to TLDR application!'.

    """
    return {"message": "Welcome to TLDR application!"}


@app.post("/summarize", status_code=200)
async def get_summarization(
    response: Response,
    long_text: str = Body(default="This is just a default.", embed=True),
) -> ResponseModel:
    """Fetches the summary of a long text using OpenAI API.

    Retrieves the summary response using OpenAI API and
    returns only the text and the purpose of this API.

    Args:
        long_text: Text to summarize.

    Returns:
        A dict that either shows the summary (if API key
        is provided) or a text that shows that the API key
        is missing and the purpose of this API.
    """
    summarizer = Summarizer()
    response_from_openai = summarizer.summarize(long_text=long_text)

    # Init results dict
    results = {
        "method": summarizer.purpose,
    }

    if len(response_from_openai) == 0:
        # If the length of response is empty, then no API
        # key is provided. Return the 400 status code
        results["result"] = "No API key provided. Please provide."
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        results["result"] = response_from_openai["choices"][0]["text"]

    return results
