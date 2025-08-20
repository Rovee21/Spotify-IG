from fastapi import FastAPI
from dot_env import load_dotenv
import requests, os
from fastapi.responses import RedirectResponse, JSONResponse

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://localhost:8000/callback"

