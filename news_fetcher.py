import feedparser
import re
from html import unescape

RSS_SOURCES = {
    "Yahoo Finance": "https://finance.yahoo.com/rss/topstories",
    "MarketWatch": "http://feeds.marketwatch.com/marketwatch/topstories/",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "Reuters Business": "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "Economic Times": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
    "Moneycontrol": "https://www.moneycontrol.com/rss/latestnews.xml",
    "LiveMint": "https://www.livemint.com/rss/markets",
    "Business Standard": "https://www.business-standard.com/rss/markets-106.rss",
    "Financial Express": "https://www.financialexpress.com/market/feed/",
    "CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "CoinTelegraph": "https://cointelegraph.com/rss",
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "BBC Business": "http://feeds.bbci.co.uk/news/business/rss.xml",
    "Guardian Business": "https://www.theguardian.com/business/rss",
    "NYTimes Business": "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
    "Benzinga": "https://www.benzinga.com/feed",
    "TradingView": "https://www.tradingview.com/news/rss/",
    "Zacks": "https://www.zacks.com/stock/news/rss.xml",
    "Finextra": "https://www.finextra.com/rss/finextra-news.xml",
}


def clean_html(text):
    if not text:
        return "No summary available"

    text = unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text if text else "No summary available"


def get_source_name_from_url(source_url):
    for source_name, url in RSS_SOURCES.items():
        if url == source_url:
            return source_name
    return source_url


def fetch_news(source_url, limit=5):
    feed = feedparser.parse(source_url)
    articles = []
    seen_links = set()

    source_name = get_source_name_from_url(source_url)

    for entry in feed.entries:
        title = entry.get("title", "No Title").strip()
        summary = entry.get("summary", entry.get("description", "No summary available"))
        link = entry.get("link", "").strip()

        summary = clean_html(summary)

        if link in seen_links:
            continue

        seen_links.add(link)

        articles.append({
            "title": title,
            "summary": summary,
            "link": link,
            "source": source_name
        })

        if len(articles) >= limit:
            break

    return articles


def fetch_news_from_all_sources(limit_per_source=3):
    all_articles = []
    seen_links = set()

    for source_name, source_url in RSS_SOURCES.items():
        try:
            feed = feedparser.parse(source_url)
            count = 0

            for entry in feed.entries:
                title = entry.get("title", "No Title").strip()
                summary = entry.get("summary", entry.get("description", "No summary available"))
                link = entry.get("link", "").strip()

                summary = clean_html(summary)

                if link in seen_links:
                    continue

                seen_links.add(link)

                all_articles.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "source": source_name
                })

                count += 1
                if count >= limit_per_source:
                    break

        except Exception:
            continue

    return all_articles