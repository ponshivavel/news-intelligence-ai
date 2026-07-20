# AI News Brain 🧠

### 🏆 Semi-Finalist — The Economic Times GenAI Hackathon 2026
An AI-powered Financial News Intelligence System that transforms static market news into interactive, decision-driven intelligence. Built and recognized at a nation-scale innovation challenge.

---


# AI News Brain 🧠
> **AI-Powered Financial News Intelligence System**  
> Transform static market news into interactive, decision-driven intelligence.

---

## What is AI News Brain?

AI News Brain is a full-stack web application that reimagines how users consume financial news. Instead of passively scrolling through articles, users get:

- **A smart briefing** — AI-generated executive summary of the day's top stories
- **A market timeline** — chronological visualisation of events and their impact  
- **A conversational assistant** — ask any market question and get an instant answer

Built with **FastAPI** (Python backend) and **Vanilla JS** (frontend), using a **multi-agent architecture** with zero external API dependencies.

---

## Quick Start

```bash
# 1. Navigate to project folder
cd "your-project-folder"

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Start the backend
python -m uvicorn main:app --reload

# 4. Open index.html in your browser
```

Backend runs at: `http://127.0.0.1:8000`  
Interactive API docs: `http://127.0.0.1:8000/docs`

---

## Required Folder Structure

```
project/
├── main.py
├── index.html
├── app.js
└── agents/
    ├── __init__.py          ← required (creates Python package)
    ├── data_agent.py
    ├── summary_agent.py
    ├── timeline_agent.py
    └── chat_agent.py
```

> **Common error:** `ModuleNotFoundError: No module named 'agents'`  
> **Fix:** Create the `agents/` folder and move all agent files inside. Add an empty `__init__.py` file.

---

## System Architecture

```
User Browser  →  FastAPI Backend  →  Agent Layer  →  Data Source
(HTML/JS)        (main.py :8000)     (4 modules)     (Mock → Real API)
```

### API Endpoints

| Method | Endpoint  | Description                        | Response Shape              |
|--------|-----------|------------------------------------|-----------------------------|
| GET    | `/news`   | Fetch articles + AI summary        | `{ summary, articles[] }`   |
| GET    | `/timeline` | Market event timeline            | `{ timeline[] }`            |
| POST   | `/chat`   | Natural language query             | `{ response }`              |

---

## Agent Details

Each agent is an independent Python module. All four together form the intelligence pipeline.

### `data_agent.py` — News Provider
Returns a list of news articles. Currently uses mock data. Swap for any real source:

```python
# Replace mock data with a real API call, e.g. NewsAPI:
import requests
res = requests.get("https://newsapi.org/v2/top-headlines", 
                   params={"category": "business", "apiKey": "YOUR_KEY"})
return [{"title": a["title"], "content": a["description"]} for a in res.json()["articles"]]
```

### `summary_agent.py` — Briefing Generator
Combines top headlines into a 2–3 sentence executive briefing string. No AI API needed.

### `timeline_agent.py` — Event Sequencer
Maps news articles to structured timeline events with `event` and `impact` fields.

### `chat_agent.py` — Conversational NLP
Keyword-based router across 8 user intent categories:

| Keywords Detected | Response Focus |
|---|---|
| `what`, `latest`, `today`, `current` | Top headline + market snapshot |
| `why`, `reason`, `cause` | Explanatory content from news body |
| `future`, `predict`, `outlook` | Forward-looking trend analysis |
| `invest`, `buy`, `sell`, `recommend` | Investment-relevant news note |
| `sensex`, `market`, `nifty` | Index-specific update |
| `rbi`, `rate`, `repo` | RBI / interest rate news |
| `it`, `tech`, `software` | IT sector news filter |
| *(anything else)* | Full market snapshot |

---

## Frontend Features

- **Three-panel layout**: Briefing, Timeline, and AI Chat sections
- **Loading state animations**: Pulsing indicators on every async action
- **Responsive design**: Mobile, tablet, and desktop friendly
- **Enter key support**: Press Enter in chat input to send
- **Error messages**: All API failures show clear, friendly messages
- **Typography**: Playfair Display + DM Sans + DM Mono (Google Fonts)
- **Dark luxury theme**: `#0a0a0f` base, `#c8a96e` gold accent

---

## Technologies Used

| Category | Technology | Purpose |
|---|---|---|
| Backend Framework | FastAPI | REST API with auto Swagger docs |
| ASGI Server | Uvicorn | High-performance Python server |
| Frontend | HTML5 / CSS3 / Vanilla JS | UI — no framework needed |
| Typography | Google Fonts | Playfair Display + DM Sans |
| CORS | FastAPI CORSMiddleware | Frontend–backend connection |
| AI Layer | Rule-based Python NLP | Zero API key — fully local |

---

## Upgrading to Production

### Step 1: Connect Real News
Replace mock data in `data_agent.py` with a call to [NewsAPI](https://newsapi.org) (free tier available) or any RSS feed.

### Step 2: Add Real AI
Replace rule-based agents with LLM calls:
```python
# In chat_agent.py — swap the keyword logic with:
import anthropic
client = anthropic.Anthropic()  # set ANTHROPIC_API_KEY env var
message = client.messages.create(model="claude-sonnet-4-20250514", ...)
```

### Step 3: Deploy
- **Backend**: Heroku, Railway, or Render (free tier)
- **Frontend**: Vercel, Netlify, or GitHub Pages
- Update `BACKEND` URL in `app.js` to your deployed backend URL

---

## Future Roadmap

- [ ] Real news API integration (NewsAPI, Finnhub, RSS)
- [ ] LLM upgrade — swap rule-based agents with Claude / GPT
- [ ] User personalisation — watchlists, sector alerts
- [ ] Multi-language support — Hindi, Tamil, regional languages
- [ ] Mobile app — React Native / Progressive Web App
- [ ] Portfolio integration — personalised impact analysis

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'agents'` | Agent files not in `agents/` subfolder | Create `agents/` folder, move files, add `__init__.py` |
| `uvicorn: command not found` | Uvicorn not in PATH | Use `python -m uvicorn main:app --reload` |
| CORS error in browser | Frontend hitting wrong URL | Ensure backend is running on `http://127.0.0.1:8000` |
| `422 Unprocessable Entity` on `/chat` | Sending query as URL param not JSON body | Send `{ "query": "your question" }` as JSON POST body |

---

## Project Structure Summary

```
AI News Brain
├── Problem:     Fragmented, static financial news — no synthesis or action
├── Solution:    Multi-agent system with briefing + timeline + chat
├── Tech:        FastAPI + Vanilla JS, zero API key
├── AI:          Rule-based NLP (upgradeable to LLM)
└── Status:      Demo-ready prototype, production-scalable architecture
```

---

*Built for hackathon demonstration. All agents are modular and independently upgradeable.*
