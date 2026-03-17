import streamlit as st

st.markdown("""
<style>
/* Page-specific styling */
.home-hero {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.72));
    border: 1px solid rgba(255,255,255,0.88);
    border-radius: 36px;
    padding: 42px 44px;
    box-shadow: 0 22px 50px rgba(70, 80, 100, 0.10);
    margin-bottom: 28px;
}

.home-title {
    font-size: 3.3rem;
    font-weight: 900;
    color: #0f172a;
    line-height: 1.1;
    margin-bottom: 12px;
}

.home-subtitle {
    font-size: 1.18rem;
    color: #334155;
    line-height: 1.9;
    max-width: 1100px;
}

.section-title {
    font-size: 2rem;
    font-weight: 900;
    color: #0f172a;
    margin-top: 0.4rem;
    margin-bottom: 1rem;
}

.feature-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.90), rgba(255,255,255,0.72));
    border: 1px solid rgba(255,255,255,0.85);
    border-radius: 28px;
    padding: 26px;
    box-shadow: 0 14px 34px rgba(70, 80, 100, 0.08);
    margin-bottom: 18px;
    height: 100%;
}

.feature-title {
    font-size: 1.25rem;
    font-weight: 900;
    color: #6d28d9;
    margin-bottom: 10px;
}

.feature-text {
    color: #334155;
    line-height: 1.8;
    font-size: 1rem;
}

.small-info-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(240,249,255,0.80));
    border: 1px solid rgba(255,255,255,0.86);
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 12px 28px rgba(70, 80, 100, 0.07);
    margin-bottom: 18px;
}

.small-info-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
}

.small-info-text {
    color: #475569;
    line-height: 1.8;
    font-size: 0.98rem;
}

.highlight-card {
    background: linear-gradient(90deg, rgba(255,228,230,0.90), rgba(219,234,254,0.90), rgba(236,254,255,0.90));
    border: 1px solid rgba(255,255,255,0.88);
    border-radius: 28px;
    padding: 26px;
    box-shadow: 0 16px 34px rgba(70, 80, 100, 0.08);
    margin-top: 10px;
    margin-bottom: 22px;
}

.highlight-title {
    font-size: 1.3rem;
    font-weight: 900;
    color: #111827;
    margin-bottom: 8px;
}

.highlight-text {
    color: #334155;
    line-height: 1.8;
    font-size: 1rem;
}

.steps-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.76));
    border: 1px solid rgba(255,255,255,0.88);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 14px 34px rgba(70, 80, 100, 0.08);
    margin-top: 10px;
}

.steps-title {
    font-size: 1.25rem;
    font-weight: 900;
    color: #6d28d9;
    margin-bottom: 12px;
}

.step-line {
    color: #334155;
    font-size: 1rem;
    line-height: 2;
    margin-bottom: 2px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="home-hero">
    <div class="home-title">📈 AI Stock Market News Analyzer</div>
    <div class="home-subtitle">
        This dashboard helps you understand stock market news in a simple way.
        You can paste a news article yourself or fetch live news from the internet.
        The app then explains what the news means, whether it sounds positive or negative,
        which company names are mentioned, and what effect it may have on the market.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="highlight-card">
    <div class="highlight-title">Why this app is useful</div>
    <div class="highlight-text">
        Financial news can be long, confusing, and time-consuming to read.
        This app turns that news into clear points that are easier to understand.
        It helps you quickly see the main idea of the article instead of reading everything line by line.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">What You Can Do Here</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">✍ Analyze News Manually</div>
        <div class="feature-text">
            Paste any business or stock-related news article and get:
            <br>• a short and clear summary
            <br>• whether the news feels positive, negative, or neutral
            <br>• company names found in the article
            <br>• the likely effect on the market
            <br>• important points in simple language
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🌐 Fetch Live News Online</div>
        <div class="feature-text">
            Bring in the latest news from online sources and review it in one place.
            You can:
            <br>• view fresh financial headlines
            <br>• choose one article for deeper analysis
            <br>• search by company name or keyword
            <br>• understand news faster without opening many websites
        </div>
    </div>
    """, unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    <div class="small-info-card">
        <div class="small-info-title">🧾 Clear Summary</div>
        <div class="small-info-text">
            The app reads the article and explains the main idea in a short and simple form.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="small-info-card">
        <div class="small-info-title">😊 Easy Sentiment</div>
        <div class="small-info-text">
            It tells you whether the overall news sounds good, bad, or balanced.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="small-info-card">
        <div class="small-info-title">📄 PDF Download</div>
        <div class="small-info-text">
            After analysis, you can save the result as a report and use it later.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

st.markdown("""
<div class="steps-card">
    <div class="steps-title">Simple 4-Step Flow</div>
    <div class="step-line">1. Open the page you want: Manual Analysis or Online News.</div>
    <div class="step-line">2. Paste your own news or fetch a live article from online sources.</div>
    <div class="step-line">3. Click the analyze button to see the result in an easy format.</div>
    <div class="step-line">4. Download the result as a PDF if you want to save it.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Best For</div>', unsafe_allow_html=True)

b1, b2 = st.columns(2)

with b1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">👩‍🎓 Students and Projects</div>
        <div class="feature-text">
            This app is useful for project demonstrations, presentations, and understanding financial news in a better way.
        </div>
    </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📊 Quick News Understanding</div>
        <div class="feature-text">
            It is helpful when you want to know the meaning of a market news article quickly without spending too much time reading everything in detail.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.success("Use the top navigation to open Manual Analysis, Online News, or Reports.")