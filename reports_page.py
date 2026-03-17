import streamlit as st

st.markdown("""
<style>
.title {
    font-size: 2.6rem;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 1rem;
}

.info-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.90), rgba(240,249,255,0.82));
    border: 1px solid rgba(255,255,255,0.85);
    border-radius: 24px;
    padding: 18px 22px;
    color: #1e293b;
    font-weight: 600;
    box-shadow: 0 10px 24px rgba(70, 80, 100, 0.06);
    margin-bottom: 20px;
}

.card {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.76));
    border: 1px solid rgba(255,255,255,0.88);
    border-radius: 28px;
    padding: 26px;
    box-shadow: 0 14px 34px rgba(70, 80, 100, 0.08);
    margin-bottom: 24px;
}

.sub {
    font-size: 1.25rem;
    font-weight: 900;
    color: #6d28d9;
    margin-bottom: 16px;
}

.report-label {
    color: #0f172a;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 4px;
    font-size: 1rem;
}

.report-value {
    color: #334155;
    line-height: 1.8;
    font-size: 1rem;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Reports</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
This page shows your latest manual analysis and latest online news analysis from the current session.
</div>
""", unsafe_allow_html=True)

if "manual_result" in st.session_state:
    manual_result = st.session_state["manual_result"]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sub">Latest Manual Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Title</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{st.session_state.get("manual_title", "Manual News")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Summary</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{manual_result.get("summary", "No summary available.")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Sentiment</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{manual_result.get("sentiment", "Unknown")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Market Impact</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{manual_result.get("market_impact", "No market impact available.")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No manual analysis available yet.")

if "online_result" in st.session_state:
    online_result = st.session_state["online_result"]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sub">Latest Online News Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Title</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{st.session_state.get("online_title", "Online News")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Summary</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{online_result.get("summary", "No summary available.")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Sentiment</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{online_result.get("sentiment", "Unknown")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="report-label">Market Impact</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="report-value">{online_result.get("market_impact", "No market impact available.")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No online analysis available yet.")