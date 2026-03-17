import html
import streamlit as st
import pandas as pd
import plotly.express as px

from analyzer import analyze_news
from news_fetcher import fetch_news, fetch_news_from_all_sources, RSS_SOURCES
from pdf_utils import create_pdf_report

st.set_page_config(page_title="Online News", page_icon="🌐", layout="wide")

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 166, 158, 0.45), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(125, 211, 252, 0.35), transparent 25%),
        linear-gradient(135deg, #fff8f2 0%, #f5fbff 45%, #eef8ff 100%);
}
#MainMenu, footer {
    visibility: hidden;
}.block-container {max-width:1400px; padding-top:1.2rem; padding-bottom:2rem;}
.title {font-size:2.4rem; font-weight:900; color:#0f172a; margin-bottom:1rem;}
.card {
    background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(255,255,255,0.68));
    border: 1px solid rgba(255,255,255,0.82);
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 14px 34px rgba(70, 80, 100, 0.08);
    margin-bottom: 18px;
}
.news-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.90), rgba(255,245,230,0.82));
    border-left: 8px solid #ff9f1c;
    border-radius: 26px;
    padding: 22px;
    box-shadow: 0 12px 28px rgba(70, 80, 100, 0.08);
    margin-bottom: 18px;
}
.news-head {font-size:1.2rem; font-weight:900; color:#0f172a; margin-bottom:8px;}
.meta {color:#334155; line-height:1.8; font-size:1rem;}
.sub {font-size:1.15rem; font-weight:800; color:#6d28d9; margin-bottom:8px;}
.stButton > button, .stDownloadButton > button {
    border:none; border-radius:16px; font-weight:800; padding:0.82rem 1.55rem; color:white;
}
.stButton > button {background: linear-gradient(90deg, #ff6f91, #ff9fb2, #7fd8ff);}
.stDownloadButton > button {background: linear-gradient(90deg, #36cfc9, #5b86e5);}
[data-testid="stWidgetLabel"] * {color:#1e1b4b !important; font-weight:800 !important;}
.stTextInput > div > div > input, .stSelectbox div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.94) !important; color:#111827 !important; border-radius:16px !important;
}
.stRadio div[role="radiogroup"] label, .stRadio div[role="radiogroup"] label p {
    color:#111827 !important; font-weight:700 !important;
}
.badge-positive,.badge-negative,.badge-neutral{display:inline-block;padding:9px 16px;border-radius:999px;font-weight:800;font-size:1rem;}
.badge-positive{background:linear-gradient(90deg,#ffe7c7,#ffd6a5);color:#9a3412;}
.badge-negative{background:linear-gradient(90deg,#fee2e2,#fecaca);color:#991b1b;}
.badge-neutral{background:linear-gradient(90deg,#ede9fe,#ddd6fe);color:#5b21b6;}
.conf-wrap{width:100%;height:14px;background:#e5e7eb;border-radius:999px;overflow:hidden;margin-top:10px;margin-bottom:8px;}
.conf-bar{height:100%;background:linear-gradient(90deg,#ff7eb3,#7fd8ff);border-radius:999px;}
a {color:#2563eb !important; font-weight:700; text-decoration:none;}
a:hover {text-decoration:underline;}
</style>
""", unsafe_allow_html=True)


def esc(text):
    return html.escape(str(text)) if text is not None else ""


def badge(sentiment):
    s = str(sentiment).lower()
    if s == "positive":
        return '<span class="badge-positive">Positive</span>'
    if s == "negative":
        return '<span class="badge-negative">Negative</span>'
    return '<span class="badge-neutral">Neutral</span>'


def detect_basic_sentiment(text):
    text = text.lower()
    positive_words = ["profit", "growth", "rise", "gain", "strong", "higher", "up", "surge", "beat", "buy"]
    negative_words = ["loss", "fall", "drop", "decline", "weak", "lower", "down", "miss", "risk", "reduce"]
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)
    if pos > neg:
        return "Positive"
    if neg > pos:
        return "Negative"
    return "Neutral"


def render_card(title, body_html):
    st.markdown(
        f"""
        <div class="card">
            <div class="sub">{title}</div>
            <div class="meta">{body_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_analysis(result, chart_key):
    summary = esc(result.get("summary", "No summary available."))
    sentiment = result.get("sentiment", "Neutral")
    confidence = result.get("confidence", 0)
    market_impact = esc(result.get("market_impact", "No impact available."))
    companies = result.get("companies", [])
    key_points = result.get("key_points", [])

    try:
        confidence = int(confidence)
    except Exception:
        confidence = 0
    confidence = max(0, min(confidence, 100))

    companies_html = "<br>".join([f"• {esc(c)}" for c in companies]) if companies else "No specific companies detected."
    keypoints_html = "<br>".join([f"• {esc(k)}" for k in key_points]) if key_points else "No key points available."

    st.markdown("## Detailed AI Analysis")
    c1, c2 = st.columns(2)

    with c1:
        render_card("Summary", summary)
        render_card(
            "Sentiment",
            f"""
            {badge(sentiment)}
            <br><br>
            <b>Confidence Score:</b> {confidence}%
            <div class="conf-wrap"><div class="conf-bar" style="width:{confidence}%"></div></div>
            """
        )

    with c2:
        render_card("Companies Mentioned", companies_html)
        render_card("Market Impact", market_impact)
        render_card("Key Points", keypoints_html)

    chart_data = pd.DataFrame({"Sentiment": [str(sentiment)], "Count": [1]})
    fig = px.bar(
        chart_data,
        x="Sentiment",
        y="Count",
        text="Count",
        color="Sentiment",
        color_discrete_map={
            "Positive": "#f97316",
            "Negative": "#ef4444",
            "Neutral": "#8b5cf6",
            "Unknown": "#64748b"
        },
        title="Sentiment Overview"
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#111827", size=16),
        title_font=dict(size=24, color="#111827"),
        showlegend=False,
        margin=dict(l=60, r=40, t=70, b=60),
        xaxis=dict(title="Sentiment", title_font=dict(color="#111827", size=18), tickfont=dict(color="#111827", size=15)),
        yaxis=dict(title="Article Count", title_font=dict(color="#111827", size=18), tickfont=dict(color="#111827", size=15))
    )
    fig.update_xaxes(showgrid=False, color="#111827")
    fig.update_yaxes(showgrid=True, gridcolor="#d1d5db", color="#111827")
    fig.update_traces(textposition="outside", textfont=dict(color="#111827", size=16))

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, key=chart_key)
    st.markdown('</div>', unsafe_allow_html=True)


def show_news_cards(articles):
    st.markdown("## Fetched News Overview")
    for i, article in enumerate(articles, start=1):
        title = esc(article.get("title", "No Title"))
        summary = esc(article.get("summary", "No summary available."))
        source = esc(article.get("source", "Unknown Source"))
        link = article.get("link", "")
        sentiment = detect_basic_sentiment(f"{title} {summary}")

        st.markdown(
            f"""
            <div class="news-card">
                <div class="news-head">News {i}</div>
                <div class="meta">
                    <b>Source:</b> {source}<br>
                    <b>Title:</b> {title}<br>
                    <b>Quick Sentiment:</b> {sentiment}<br>
                    <b>Short Summary:</b> {summary[:320]}{'...' if len(summary) > 320 else ''}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if link:
            st.markdown(f"[🔗 Read Full News]({link})")


st.markdown('<div class="title">🌐 Online News Fetch</div>', unsafe_allow_html=True)

fetch_mode = st.radio(
    "Choose Fetch Mode",
    ["Single Source", "All Sources"],
    horizontal=True,
    key="fetch_mode"
)

company_search = st.text_input(
    "Search by Company or Keyword (Optional)",
    key="company_search_input",
    placeholder="Example: Reliance, Infosys, Tesla, Bank, Oil"
)

if fetch_mode == "Single Source":
    selected_source = st.selectbox(
        "Select News Source",
        list(RSS_SOURCES.keys()),
        key="online_source_select"
    )

    news_limit = st.slider(
        "Number of Articles",
        1,
        20,
        5,
        key="online_news_limit_single"
    )

    if st.button("🌐 Fetch Latest News", key="fetch_single_source_btn"):
        with st.spinner("Fetching latest news..."):
            articles = fetch_news(RSS_SOURCES[selected_source], limit=news_limit)

            if company_search.strip():
                keyword = company_search.lower().strip()
                articles = [
                    a for a in articles
                    if keyword in a.get("title", "").lower() or keyword in a.get("summary", "").lower()
                ]

            st.session_state["online_articles"] = articles

else:
    all_limit = st.slider(
        "Articles Per Source",
        1,
        5,
        2,
        key="online_news_limit_all"
    )

    if st.button("🚀 Fetch News From All Sources", key="fetch_all_sources_btn"):
        with st.spinner("Fetching news from all sources..."):
            articles = fetch_news_from_all_sources(limit_per_source=all_limit)

            if company_search.strip():
                keyword = company_search.lower().strip()
                articles = [
                    a for a in articles
                    if keyword in a.get("title", "").lower() or keyword in a.get("summary", "").lower()
                ]

            st.session_state["online_articles"] = articles

if "online_articles" in st.session_state:
    articles = st.session_state["online_articles"]

    if articles:
        show_news_cards(articles)

        st.markdown("## Select One Article for Full AI Analysis")

        article_labels = [
            f"{idx + 1}. {article.get('title', 'No Title')}"
            for idx, article in enumerate(articles)
        ]

        selected_label = st.selectbox(
            "Choose the article you want to analyze in detail",
            article_labels,
            key="online_article_select"
        )

        selected_index = article_labels.index(selected_label)
        selected_article = articles[selected_index]

        selected_title = esc(selected_article.get("title", "No Title"))
        selected_source = esc(selected_article.get("source", "Unknown Source"))
        selected_summary = esc(selected_article.get("summary", "No summary available."))
        selected_link = selected_article.get("link", "")

        st.markdown(
            f"""
            <div class="card">
                <div class="sub">Selected Article Details</div>
                <div class="meta">
                    <b>Source:</b> {selected_source}<br>
                    <b>Title:</b> {selected_title}<br>
                    <b>Summary:</b> {selected_summary}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if selected_link:
            st.markdown(f"[🔗 Open Full News Link]({selected_link})")

        if st.button("🧠 Analyze Selected Online News", key="analyze_online_news_btn"):
            article_text = f"{selected_article.get('title', '')}\n\n{selected_article.get('summary', '')}"

            with st.spinner("Analyzing selected article..."):
                result = analyze_news(article_text)

            st.session_state["online_result"] = result
            st.session_state["online_text"] = article_text
            st.session_state["online_title"] = selected_article.get("title", "Online News")
    else:
        st.warning("No articles were found for this source or keyword.")

if "online_result" in st.session_state:
    show_analysis(st.session_state["online_result"], "online_chart")

    pdf_path = create_pdf_report(
        st.session_state["online_title"],
        st.session_state["online_text"],
        st.session_state["online_result"],
        output_path="online_news_report.pdf"
    )

    with open(pdf_path, "rb") as file:
        st.download_button(
            label="⬇ Download PDF Report",
            data=file,
            file_name="online_news_report.pdf",
            mime="application/pdf",
            key="download_online_pdf"
        )