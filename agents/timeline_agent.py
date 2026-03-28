import json

def generate_timeline(news: list) -> list:
    '''
    Mock timeline generator (no API key needed).
    Returns a list of dicts: [{"event": ..., "impact": ...}, ...]
    '''
    return [
        {"event": news[0]["title"], "impact": news[0]["content"] + " This is a mock timeline entry."},
        {"event": news[1]["title"], "impact": news[1]["content"] + " Expected bullish impact."},
        {"event": "RBI Policy Update", "impact": "Stable rates support market sentiment."},
        {"event": news[3]["title"], "impact": news[3]["content"] + " Midcaps leading gains."},
        {"event": "Overall Market", "impact": "Positive session with broad participation across sectors."}
    ]
