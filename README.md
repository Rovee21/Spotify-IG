# Resonate: Discover New Music

## Overview
An app created with the purpose of helping people find new music while in the process connecting with new friends. You will log in with spotify, and a feed page will pop up with music recently listened by a friend. You can switch to the "For You" tab and it will give you recomendations based on the music genre you have been listening to.


## Tech Stack
- Frontend: React(Next.js), TailwindCSS
- Backend: FastAPI, RestAPI
- Database: MySQL
- ML: Scikit-learn, Jupyter Notebook, Power BI, Pandas

## App Flow

### 1. Welcome Screen

- **Purpose**: Be a nice landing page that a user who stumbles accoss my product can understand whats going on and take the next steps
- **Elements**:
    - Resonate Logo top left
    - Hero section with a gradient background
    - An Intro that explains whats possible with the app
    - A preview of what is contained in the app
    - Login and Signup options on the top right with Spotify OAuth

### 2. Feed Page

- **Purpose**: Where all of the functionality of the app happens: activity feed and for you tab
- **Elements**:
    - Spotify profile pic top left
    - Search user on the top
    - Activity tab that is a limitless feed that shows songs recently listen to by friends
    - For you tab that gives you a music archetype badge, displays a chart of what genres you have been listening to, and song recomendations.

### 3. Profile Page

- **Purpose**: Shows you followers and following
- **Elements**:
    - Spotify profile pic top
    - Name right below that
    - Followers and Following right in the middle


## Running the app
- To run the server in a new terminal, use this command: ngrok http 8000
- To run the backend with this command: ./venv/bin/uvicorn main:app --reload 
- To run the frontend, use this command: npm run dev


