from fastapi.testclient import TestClient
from .main import app
import os

client = TestClient(app)

DUMMY_STRING = "This is just a dummy string."


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TLDR application!"}


def test_if_no_api_key_provided_should_return_no_api_key_string():
    _environ = dict(os.environ)
    try:
        os.environ.update({"OPENAI_API_KEY": ""})
        response = client.post("/summarize", json={"long_text": DUMMY_STRING})
        assert response.json()["result"] == "No API key provided. Please provide."
    finally:
        os.environ.clear()
        os.environ.update(_environ)


def test_if_no_api_key_provided_should_return_400_response():
    _environ = dict(os.environ)
    try:
        os.environ.update({"OPENAI_API_KEY": ""})
        response = client.post("/summarize", json={"long_text": DUMMY_STRING})
        assert response.status_code == 400
    finally:
        os.environ.clear()
        os.environ.update(_environ)
