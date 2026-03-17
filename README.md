📈 AI Stock Market News Analyzer
🚀 Overview

AI Stock Market News Analyzer is a powerful Streamlit-based intelligent financial news analysis platform designed to help users quickly understand complex stock market news articles.

Financial news is often lengthy, technical, and time-consuming to interpret. This application uses Artificial Intelligence and Natural Language Processing (NLP) techniques to automatically analyze news articles and generate meaningful insights such as:

Short summary

Sentiment analysis

Confidence score

Company detection

Market impact prediction

Key point extraction

Visual sentiment charts

Downloadable PDF reports

The system supports both:

✍ Manual News Analysis

🌐 Online Live News Fetch and Analysis

This project is ideal for:

Students doing AI / Data Science / NLP projects

Stock market beginners

Financial research demonstrations

Hackathons and internships

Portfolio projects

🎯 Project Objectives

The main goals of this project are:

Simplify stock market news understanding

Provide automated AI-based insights

Reduce time spent reading full financial articles

Help users identify market sentiment quickly

Generate structured analysis reports

Provide a modern interactive dashboard

🧠 Key Features
✍ Manual News Analysis

Users can paste any financial news article and the system will:

Generate a concise summary

Detect sentiment (Positive / Negative / Neutral)

Extract company names

Predict market impact

Provide key insights

Show sentiment confidence level

Display interactive bar charts

Allow PDF report download

This functionality is implemented in the manual analysis module
👉

🌐 Online News Fetching and Analysis

Users can fetch live financial news from multiple RSS sources.

Features include:

Fetch news from single source

Fetch news from multiple sources

Search by company name or keyword

Quick sentiment preview

Select article for detailed AI analysis

Generate downloadable reports

Implemented in:
👉
👉 News fetching logic:

📊 Visual Analytics

The system generates:

Sentiment bar charts

Confidence progress indicators

Structured cards for insights

Visualization uses:

Pandas

Plotly

📄 PDF Report Generation

Users can download structured AI analysis reports containing:

News title

Original article

AI summary

Sentiment and confidence

Companies mentioned

Market impact explanation

Key points

Implemented using FPDF library
👉

🧾 Reports Dashboard

A separate reports page displays:

Latest manual analysis

Latest online analysis

This helps users track session-level insights
👉

🎨 Modern UI and Navigation

The app uses:

Multi-page Streamlit navigation

Gradient UI themes

Interactive cards

Clean professional layout

Main application entry:
👉

Home page description and features:
👉

🧠 AI Analysis Engine

The project uses Groq LLM API (Llama-3 model) for deep financial news analysis.

If API is unavailable, the system automatically switches to:

Keyword-based sentiment detection

Simple company extraction

Fallback summary generation

AI logic implemented in:
👉

🌍 News Sources Supported

The system can fetch news from major global financial platforms such as:

Yahoo Finance

Reuters

CNBC

Economic Times

Moneycontrol

LiveMint

Business Standard

Financial Express

TechCrunch

BBC Business

NYTimes Business

CoinDesk

TradingView

🏗 Project Architecture
AI Stock News Analyzer
│
├── app.py                → Main navigation controller
├── home_page.py          → Dashboard landing page
├── manual_page.py        → Manual news analysis UI
├── online_page.py        → Live news fetch + analysis
├── reports_page.py       → Session reports viewer
├── analyzer.py           → AI + fallback analysis engine
├── news_fetcher.py       → RSS news fetching module
├── pdf_utils.py          → PDF report generator
├── requirements.txt      → Dependencies list

Dependencies file:
👉

⚙️ Installation
Step 1 — Clone Repository
git clone <your_repo_link>
cd ai-stock-news-analyzer
Step 2 — Install Dependencies
pip install -r requirements.txt
Step 3 — Setup Environment Variable

Create .env file

GROQ_API_KEY=your_api_key_here
Step 4 — Run Application
streamlit run app.py
🧪 Example Workflow

Open dashboard

Choose Manual or Online analysis

Provide news input

Click analyze

View insights

Download PDF report

💡 Use Cases

Financial NLP projects

AI portfolio demonstration

Business intelligence dashboards

Research prototype

Trading sentiment analysis tools

🔮 Future Enhancements

Possible future improvements:

Stock price prediction integration

Real-time news streaming

Multi-article sentiment aggregation

Trend dashboards

Sector-wise analysis

User login system

Database report storage

Mobile responsive UI

📜 License

This project is for educational and research purposes.

👨‍💻 Author

Developed as an AI-powered financial analytics project using:

Python

Streamlit

NLP

LLM APIs

Data Visualization