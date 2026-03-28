def get_news():
    """
    Returns news articles.
    Currently returns mock data — replace the list below with a
    real API call (e.g. NewsAPI, Finnhub, or your own scraper).

    Example with NewsAPI:
        import requests
        res = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={"category": "business", "country": "in", "apiKey": "YOUR_KEY"}
        )
        articles = res.json().get("articles", [])
        return [{"title": a["title"], "content": a["description"] or ""} for a in articles[:5]]
    """
    return [
        {
            "title": "IT stocks surge after Union Budget",
            "content": "Government announced major tax cuts and PLI scheme extensions boosting the IT sector. TCS, Infosys, Wipro all up 3-5%."
        },
        {
            "title": "Sensex rallies 500 points",
            "content": "Benchmark indices surged as FII inflows returned to Indian markets. Strong Q3 earnings season adds momentum."
        },
        {
            "title": "RBI holds repo rate steady at 6.5%",
            "content": "Reserve Bank of India maintains accommodative stance citing improving inflation trajectory and robust GDP growth."
        },
        {
            "title": "Midcap rally continues for third week",
            "content": "BSE Midcap index outperforms frontline indices driven by domestic consumption themes and infrastructure spending."
        }
    ]
