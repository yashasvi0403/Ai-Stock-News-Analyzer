import feedparser

RSS_SOURCES = {
    "Yahoo Finance": "https://finance.yahoo.com/rss/topstories",
    "MarketWatch": "http://feeds.marketwatch.com/marketwatch/topstories/",
    "Investing.com": "https://www.investing.com/rss/news.rss"
}


def fetch_news(source_url: str, limit: int = 5):
    feed = feedparser.parse(source_url)
    news_list = []

    for entry in feed.entries[:limit]:
        news_list.append({
            "title": entry.get("title", "No Title"),
            "summary": entry.get("summary", entry.get("description", "No summary available")),
            "link": entry.get("link", "")
        })

    return news_list