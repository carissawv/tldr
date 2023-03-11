import logging
import openai
import os

logging.basicConfig(level=logging.INFO)


class OpenAIBridge:
    """Base class of OpenAI connector."""

    def __init__(self):
        """Initializes the instance with the purpose.

        Initializes the instance with `OPENAI_API_KEY` key
        from the `.env` and set purpose of the class.

        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.purpose: str = "base class"


class Summarizer(OpenAIBridge):
    """The OpenAI connector that is used to summarize."""

    def __init__(self):
        """Initiates the summarizer class with overriding
        `OpenAIBridge` class as the base.
        """
        super().__init__()
        self.purpose = "summarize"

    def summarize(self, long_text: str) -> str:
        """Summarizes the long text with using OpenAI API

        Args:
            long_text: Text to summarize.

        Returns:
            Original response from OpenAI, that includes
            choices, created, id, model, object, and usage.
        """
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
