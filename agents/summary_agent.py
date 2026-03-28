def summarize_news(news: list) -> str:
    """
    Generates a summary from news articles. No API key required.
    Combines titles and key content into a structured briefing.
    """
    titles   = [n["title"] for n in news]
    contents = [n["content"] for n in news]

    summary = (
        f"Today's market briefing: {titles[0]} — {contents[0]} "
        f"Meanwhile, {titles[1].lower()} with {contents[1]} "
        f"Other developments include: {titles[2]} and {titles[3]}."
    )
    return summary