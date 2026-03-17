import streamlit as st

st.set_page_config(
    page_title="AI Stock Market News Analyzer",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 166, 158, 0.45), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(125, 211, 252, 0.35), transparent 25%),
        linear-gradient(135deg, #fff8f2 0%, #f5fbff 45%, #eef8ff 100%);
    color: #172033;
}

#MainMenu, footer {
    visibility: hidden;
}

/* TOP HEADER */
header[data-testid="stHeader"] {
    background: rgba(255,255,255,0.82) !important;
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.65);
}

/* top nav area */
[data-testid="stHeader"] [data-baseweb="tab-list"] {
    gap: 10px !important;
    padding-left: 14px;
    padding-right: 14px;
}

/* nav tabs */
[data-testid="stHeader"] [data-baseweb="tab"] {
    background: rgba(255,255,255,0.82) !important;
    color: #0f172a !important;
    border-radius: 14px !important;
    padding: 10px 18px !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    border: 1px solid rgba(148, 163, 184, 0.18) !important;
    box-shadow: 0 6px 18px rgba(70, 80, 100, 0.06);
}

/* selected tab */
[data-testid="stHeader"] [aria-selected="true"] {
    background: linear-gradient(90deg, #ffd4e5, #d8e9ff, #d9fbff) !important;
    color: #111827 !important;
    border: 1px solid rgba(255,255,255,0.9) !important;
    box-shadow: 0 8px 22px rgba(255, 105, 145, 0.12);
}

/* nav text visibility */
[data-testid="stHeader"] [data-baseweb="tab"] p,
[data-testid="stHeader"] [data-baseweb="tab"] span,
[data-testid="stHeader"] [data-baseweb="tab"] div {
    color: #0f172a !important;
    opacity: 1 !important;
    font-weight: 800 !important;
}

/* right side text */
[data-testid="stToolbar"] * {
    color: #0f172a !important;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.1rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

home = st.Page("home_page.py", title="Home", icon="🏠", default=True)
manual = st.Page("manual_page.py", title="Manual Analysis", icon="✍")
online = st.Page("online_page.py", title="Online News", icon="🌐")
reports = st.Page("reports_page.py", title="Reports", icon="📄")

pg = st.navigation(
    [home, manual, online, reports],
    position="top",
    expanded=True
)

pg.run()