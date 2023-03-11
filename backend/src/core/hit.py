import logging
import openai
import os

logging.basicConfig(level=logging.INFO)


class OpenAIBridge:
    purpose: str = None

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")


class Summarizer(OpenAIBridge):
    def __init__(self):
        super().__init__()
        self.purpose = "summarize"

    def summarize(self, long_text: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{long_text}\n\nTl;dr:\n",
            temperature=0,
            max_tokens=512,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        return response
