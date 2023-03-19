# TLDR

This repository contains code to implement TLDR application using OpenAI API.

## Requirements

- Python 3.10 and `pip` installed

## Getting started

### Backend

1. Create the virtual environment using `venv` with name `env`

```powershell
> python -m venv env
```

2. Activate the environment using `venv`

```powershell
> env/Scripts/activate
```

3. Install the packages from the `requirements.txt`

```powershell
> pip install -r requirements.txt
```

4. Copy the environment example and fill the OpenAI API Key

```powershell
> cp .env.example .env
```

5. Move to the backend folder and start the backend service

```powershell
> cd backend
> uvicorn main:app --reload
```

## Basics

### Backend

The backend consists of (_currently_) 2 APIs

- GET `/` : returns welcome message (_dummy API_)
- POST `/summarize`
  - Request Body Example
    ```json
    {
      "long_text": "A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei."
    }
    ```
  - Response Body
    ```json
    {
      "method": "summarize",
      "result": "Neutron stars are the smallest and densest stellar objects, formed from the supernova explosion of a massive star with a mass of 10-25 solar masses. They have a radius of about 10 km and a mass of 1.4 solar masses."
    }
    ```

## Others

### Python Documentation guide

Use [this Google styleguide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

### Python Debugging

For the Python, use `icecream` module instead of debug using
`logging` and `print`. Example usage:

```python
from icecream import ic

def foo(i):
    return i + 333

ic(foo(123))
```

Prints

```bash
ic| foo(123): 456
```
