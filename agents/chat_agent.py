from agents.data_agent import get_news


def chat_with_news(query: str) -> str:
    """
    Rule-based context-aware chat agent. No API key required.
    Matches keywords in the user query and returns relevant news insights.
    """
    news = get_news()
    query_lower = query.lower()

    headlines = [n["title"] for n in news]
    contents  = [n["content"] for n in news]

    # Build a combined context string for use in responses
    top_title   = news[0]["title"]
    top_content = news[0]["content"]

    if any(w in query_lower for w in ["what", "current", "latest", "news", "today"]):
        return (
            f"Current market update: {top_title}. {top_content} "
            f"Other highlights: {headlines[1]} and {headlines[2]}."
        )

    elif any(w in query_lower for w in ["why", "reason", "cause", "because"]):
        return (
            f"Key reasons behind the market move: {contents[0]} "
            f"Additionally, {contents[1]}"
        )

    elif any(w in query_lower for w in ["future", "predict", "forecast", "outlook", "next"]):
        return (
            f"Short-term outlook: Based on recent developments — {top_content} — "
            f"the trend appears bullish. Watch for {headlines[2]} as a key indicator."
        )

    elif any(w in query_lower for w in ["invest", "buy", "sell", "recommend", "should i"]):
        return (
            f"Investment note: Recent news favors sectors mentioned in '{top_title}'. "
            f"{top_content} Consider monitoring these stocks closely before making decisions."
        )

    elif any(w in query_lower for w in ["sensex", "market", "index", "nifty"]):
        return (
            f"Market status: {news[1]['title']}. {news[1]['content']} "
            f"Broader market also seeing: {headlines[3]}."
        )

    elif any(w in query_lower for w in ["rbi", "rate", "interest", "repo"]):
        rbi_news = next((n for n in news if "rbi" in n["title"].lower() or "rate" in n["title"].lower()), news[0])
        return f"RBI & Rate update: {rbi_news['title']}. {rbi_news['content']}"

    elif any(w in query_lower for w in ["it", "tech", "technology", "software"]):
        it_news = next((n for n in news if "it" in n["title"].lower() or "tech" in n["title"].lower()), news[0])
        return f"IT Sector: {it_news['title']}. {it_news['content']}"

    else:
        all_headlines = " | ".join(headlines)
        return (
            f"Here's a quick market snapshot based on your query '{query}': "
            f"Top stories today — {all_headlines}. "
            f"Key insight: {top_content}"
        )