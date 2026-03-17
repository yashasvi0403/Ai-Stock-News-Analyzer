import html
import streamlit as st
import pandas as pd
import plotly.express as px

from analyzer import analyze_news
from pdf_utils import create_pdf_report

st.set_page_config(page_title="Manual Analysis", page_icon="✍", layout="wide")

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
}
.block-container {max-width:1400px; padding-top:1.2rem; padding-bottom:2rem;}
.title {font-size:2.4rem; font-weight:900; color:#0f172a; margin-bottom:1rem;}
.card {
    background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(255,255,255,0.68));
    border: 1px solid rgba(255,255,255,0.82);
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 14px 34px rgba(70, 80, 100, 0.08);
    margin-bottom: 18px;
}
.sub {font-size:1.15rem; font-weight:800; color:#6d28d9; margin-bottom:8px;}
.stButton > button, .stDownloadButton > button {
    border:none; border-radius:16px; font-weight:800; padding:0.82rem 1.55rem; color:white;
}
.stButton > button {
    background: linear-gradient(90deg, #ff6f91, #ff9fb2, #7fd8ff);
}
.stDownloadButton > button {
    background: linear-gradient(90deg, #36cfc9, #5b86e5);
}
[data-testid="stWidgetLabel"] * {color:#1e1b4b !important; font-weight:800 !important;}
.stTextInput > div > div > input, .stTextArea textarea {
    background: rgba(255,255,255,0.94) !important; color:#111827 !important; border-radius:16px !important;
}
.badge-positive,.badge-negative,.badge-neutral{display:inline-block;padding:9px 16px;border-radius:999px;font-weight:800;font-size:1rem;}
.badge-positive{background:linear-gradient(90deg,#ffe7c7,#ffd6a5);color:#9a3412;}
.badge-negative{background:linear-gradient(90deg,#fee2e2,#fecaca);color:#991b1b;}
.badge-neutral{background:linear-gradient(90deg,#ede9fe,#ddd6fe);color:#5b21b6;}
.conf-wrap{width:100%;height:14px;background:#e5e7eb;border-radius:999px;overflow:hidden;margin-top:10px;margin-bottom:8px;}
.conf-bar{height:100%;background:linear-gradient(90deg,#ff7eb3,#7fd8ff);border-radius:999px;}
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


def render_card(title, body_html):
    st.markdown(
        f"""
        <div class="card">
            <div class="sub">{title}</div>
            <div style="color:#334155; line-height:1.8;">{body_html}</div>
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


st.markdown('<div class="title">✍ Manual News Analysis</div>', unsafe_allow_html=True)

manual_title = st.text_input("News Title", key="manual_title_input")
manual_news = st.text_area("Paste Financial News Here", height=240, key="manual_news_input")

if st.button("✨ Analyze Manual News", key="analyze_manual_btn"):
    if manual_news.strip():
        with st.spinner("Analyzing manual news..."):
            result = analyze_news(manual_news)

        st.session_state["manual_result"] = result
        st.session_state["manual_text"] = manual_news
        st.session_state["manual_title"] = manual_title.strip() if manual_title.strip() else "Manual News"
    else:
        st.warning("Please paste the news text before analyzing.")

if "manual_result" in st.session_state:
    show_analysis(st.session_state["manual_result"], "manual_chart")

    pdf_path = create_pdf_report(
        st.session_state["manual_title"],
        st.session_state["manual_text"],
        st.session_state["manual_result"],
        output_path="manual_news_report.pdf"
    )

    with open(pdf_path, "rb") as file:
        st.download_button(
            label="⬇ Download PDF Report",
            data=file,
            file_name="manual_news_report.pdf",
            mime="application/pdf",
            key="download_manual_pdf"
        )