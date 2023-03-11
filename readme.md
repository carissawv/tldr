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

## Others

### Documentation guide

Use [this Google styleguide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).
