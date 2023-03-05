import logging
import openai
import os


class Summarizer:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def summarize(self, long_text: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{long_text}\n\nTl;dr",
            temperature=0.7,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        return response
