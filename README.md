# F.R.I.E.N.D.

**AI-Based Emotional Navigation System** — a local-first companion for expressing feelings, tracking moods, and finding small, practical resets. F.R.I.E.N.D. supports reflection and first-layer guidance; it does not diagnose, treat, or replace professional care. The project aligns with UN Sustainable Development Goal 3: Good Health and Well-being.

## Why it exists

People often need a low-friction place to name what is happening before they are ready for a larger conversation. F.R.I.E.N.D. combines a calm chat interface, mood journaling, descriptive insights, and short grounding exercises. Local demo mode works without a paid AI account.

## Features

- Responsive React interface with landing, chat, check-in, insights, toolkit, and safety pages.
- FastAPI endpoints for chat, moods, summaries, deletion, and health checks.
- SQLite persistence through SQLAlchemy; chat messages are not saved.
- Modular safety screening and rule-based local emotion fallback.
- Crisis-aware response with India resources: Tele-MANAS 14416 and emergency 112.
- Guided box-breathing timer, grounding instructions, and journaling prompts.
- Pytest and Vitest coverage for core backend/frontend behavior.

## Technology and architecture

React, Vite, TypeScript, React Router, Recharts-ready visualization surface, FastAPI, Pydantic, SQLAlchemy, SQLite, and pytest. See [docs/TECHNICAL_DESIGN.md](docs/TECHNICAL_DESIGN.md) for diagrams and design decisions.

```
backend/        FastAPI app, services, database, and tests
frontend/       Vite React client and tests
data/           Fictional sample data and manual test cases
docs/           Technical design
```

## Prerequisites

Python 3.11+, Node.js 18+, and npm.

## Run locally

1. Copy `.env.example` to `.env` if you want to configure the client API URL.
2. Start the backend:

   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

   Swagger UI is available at http://localhost:8000/docs.

3. In a second terminal, start the frontend:

   ```powershell
   cd frontend
   npm install
   npm run dev
   ```

   Open the Vite URL shown in the terminal (normally http://localhost:5173).

SQLite is initialized automatically on backend startup. Set `VITE_API_BASE_URL` to change the API URL. `FRIEND_AI_PROVIDER=local` is the supported offline demo mode; no API key is required.

## Tests and checks

```powershell
cd backend
pip install -r requirements.txt
pytest

cd ..\frontend
npm install
npm test
npm run build
```

The manual cases in [data/test_cases.md](data/test_cases.md) are intentionally marked “Not run” until someone executes them interactively.

## API

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/health` | Service status |
| POST | `/api/chat` | Local safety-screened chat response |
| POST | `/api/moods` | Create a mood entry |
| GET | `/api/moods` | List recent entries |
| GET | `/api/moods/summary` | Counts and recent entries |
| DELETE | `/api/moods/{id}` | Delete one entry |

## Privacy and safety

No registration is needed. The local SQLite database contains mood entries and optional journal notes; protect the database file on any shared machine. Chat content is not persisted by this implementation. Do not enter identifying information. AI output and automated screening can be wrong. F.R.I.E.N.D. is not an emergency service. If you may be in immediate danger, contact local emergency services or a trusted person. In India, Tele-MANAS is 14416 and emergency services are 112; verify current availability for your location.

## Troubleshooting

- If the client cannot connect, confirm Uvicorn is running on port 8000 and `VITE_API_BASE_URL` matches it.
- If `npm` or `pip` is unavailable, install the prerequisites and retry.
- Delete the local `friend.db` only when you intentionally want to clear all local mood data.

## Limitations and future work

The local emotion model is keyword-based and illustrative, not a reliable sentiment assessment. The current demo has no authentication, migrations, encrypted storage, or per-user data isolation. A production deployment should add those controls, verified regional resources, observability that excludes sensitive text, and a reviewed provider adapter.

## Contributing and license

Open an issue or pull request with a focused change, tests, and documentation updates. This project is distributed under [Apache License 2.0](LICENSE) (`Apache-2.0`). Dependencies remain under their own licenses; consult their project notices before redistribution. No `NOTICE` file is needed for project-created attribution at this time.
