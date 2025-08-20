from fastapi import FastAPI
from dotenv import load_dotenv
import requests, os
from fastapi.responses import RedirectResponse, JSONResponse
from pathlib import Path

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://localhost:8000/callback"