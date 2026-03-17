import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def simple_fallback_analysis(article_text: str) -> dict:
    text = article_text.lower()

    positive_words = [
        "profit", "growth", "gain", "rise", "strong", "surge",
        "improved", "positive", "record", "higher", "bullish",
        "beat", "expansion", "up"
    ]
    negative_words = [
        "loss", "drop", "fall", "decline", "weak", "down",
        "crash", "risk", "negative", "lower", "bearish",
        "miss", "cut", "slowdown"
    ]

    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

    if positive_score > negative_score:
        sentiment = "Positive"
    elif negative_score > positive_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    known_companies = [
        "Reliance Industries", "TCS", "Infosys", "Wipro", "HDFC Bank",
        "ICICI Bank", "SBI", "Tata Motors", "Adani Enterprises",
        "ONGC", "Bharti Airtel", "Axis Bank", "ITC", "HCLTech",
        "Larsen & Toubro", "Maruti Suzuki", "Sun Pharma", "Tata Steel"
    ]

    companies = [c for c in known_companies if c.lower() in text]

    if not companies:
        # Very simple backup extraction for capitalized company-like phrases
        matches = re.findall(r"\b([A-Z][a-zA-Z&.\-]+(?:\s+[A-Z][a-zA-Z&.\-]+){0,3})\b", article_text)
        cleaned = []
        skip = {"Title", "Summary", "Market", "Stock", "Investors", "Article"}
        for m in matches:
            if m not in skip and m not in cleaned:
                cleaned.append(m)
        companies = cleaned[:5]

    short_summary = article_text.strip()
    if len(short_summary) > 350:
        short_summary = short_summary[:350] + "..."

    return {
        "summary": short_summary if short_summary else "No article text provided.",
        "sentiment": sentiment,
        "confidence": 60,
        "companies": companies,
        "market_impact": "Fallback local analysis used because Groq API was unavailable or rate-limited.",
        "key_points": [
            f"Detected sentiment: {sentiment}",
            "Used keyword-based fallback analysis",
            "Companies extracted using simple matching"
        ]
    }


def analyze_news(article_text: str) -> dict:
    if not client:
        return simple_fallback_analysis(article_text)

    prompt = f"""
You are a financial news analysis assistant.

Analyze the following stock market news article and return ONLY valid JSON.

Required JSON format:
{{
  "summary": "3-5 line summary",
  "sentiment": "Positive or Negative or Neutral",
  "confidence": 0,
  "companies": ["Company 1", "Company 2"],
  "market_impact": "Short explanation of likely stock market impact",
  "key_points": ["point 1", "point 2", "point 3"]
}}

Rules:
- Confidence must be an integer from 0 to 100.
- If no company is clearly mentioned, return an empty list.
- Do not include markdown.
- Do not include code fences.
- Do not include any extra text before or after JSON.

Article:
\"\"\"
{article_text}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": "You analyze financial news and return strict JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw_text = response.choices[0].message.content.strip()
        result = json.loads(raw_text)
        return result

    except Exception as e:
        fallback = simple_fallback_analysis(article_text)
        fallback["market_impact"] = f"Fallback local analysis used because Groq API failed: {str(e)}"
        return fallback