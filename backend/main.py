from fastapi import FastAPI
from dotenv import load_dotenv
import requests, os
from fastapi.responses import RedirectResponse, JSONResponse
from pathlib import Path

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://a36c349afd92.ngrok-free.app/callback"


SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_ME_URL = "https://api.spotify.com/v1/me"

@app.get("/login")
def login():
    scope = "user-read-email user-read-private user-read-recently-played"
    auth_url = (
        f"{SPOTIFY_AUTH_URL}?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope={scope}&show_dialog=true"
    )
    return RedirectResponse(auth_url)

@app.get("/callback")
def callback(code: str):
    # Exchange authorization code for access token
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(SPOTIFY_TOKEN_URL, data=payload)
    token_info = response.json()
    access_token = token_info.get("access_token")

    # Get user profile from Spotify
    headers = {"Authorization": f"Bearer {access_token}"}
    user_profile = requests.get(SPOTIFY_ME_URL, headers=headers).json()

    #getting image url
    image_url = ""
    if "images" in user_profile and len(user_profile["images"]) > 0:
        image_url = user_profile["images"][0]["url"]

    # Redirect back to frontend with user info in query params
    frontend_url = (
        f"http://localhost:5173/profile"
        f"?name={user_profile.get('display_name', '')}"
        f"&image={image_url}"
    )
    return RedirectResponse(frontend_url)