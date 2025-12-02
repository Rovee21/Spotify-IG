
# Social Music MVP Plan

## Scope

Implement end-to-end flow with improved login experience, feed supporting comments/reactions (no ratings), enriched profiles, notebook-based recommendation pipeline, and Music Concierge chatbot. Include infra guidance where relevant.

## Steps

1. **login-ux** – Revamp `frontend/src/pages/Login.tsx` to include onboarding carousel, preview cards (sample feed/trending), social proof banner, and gradient hero design.
2. **feed-features** – Define backend/data models and frontend components for feed with infinite scroll, filters (friend/genre/time), sorting (recent/most-commented/most-shared), play previews, reactions (like/save/share), activity feed, trending & discover sections. Update FastAPI routes and add pagination APIs.
3. **profile-enhancements** – Extend `frontend/src/pages/Profile.tsx` and backend analytics endpoints to provide stats dashboard, followers/following, taste visualizations (genre breakdown, heatmap), and privacy settings management.
4. **comments-reactions** – Remove rating logic (if any placeholder exists) and implement commenting system with threads + reactions storage, including notification triggers for friend activity/replies.
5. **notebook-recs** – Create data export pipeline (CSV/Parquet) from listening history, build Jupyter notebook (e.g., `notebooks/recommendations.ipynb`) using Pandas/Scikit-learn to prototype collaborative + clustering-based recommendations, and expose results via new API endpoint.
6. **concierge-bot** – Implement Music Concierge chatbot backend endpoint integrating LLM (e.g., OpenAI) that interprets user queries, pulls feed/recommendation data, and returns conversational suggestions; add frontend chat UI component.
7. **infra-guidance** – Document containerization (Dockerfiles, docker-compose), cloud deployment steps (ECS + RDS or similar), and CI/CD pipeline configuration (GitHub Actions workflow) covering lint/test/build/deploy.

## Todos

- login-ux: Gradient hero + onboarding & preview sections
- feed-core: Infinite scroll, filters/sorting, previews, reactions
- profile-upgrades: Stats dashboard, followers graph, privacy settings
- comments-notifs: Comment threads, reactions backend, notifications
- notebook-recs: Data export + recommendation notebook + API
- concierge-bot: LLM endpoint + frontend chat UI
- infra-docs: Dockerization, cloud deploy, CI/CD guidance