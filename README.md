# Business Automation Agent

A multi-agent AI system that analyzes business data files and generates professional executive reports.

## What it does

Upload any CSV or Excel file and get:
- Deep data analysis with specific numbers and trends
- Actionable recommendations and KPIs
- Professional executive report downloadable as Markdown

## Agent Pipeline

Reader Agent -> Analyst Agent -> Advisor Agent -> Writer Agent

| Agent | Role |
|-------|------|
| Reader | Reads CSV/Excel files using pandas |
| Analyst | Extracts patterns, trends, and insights |
| Advisor | Generates recommendations and KPIs |
| Writer | Produces executive report in Markdown |

## Tech Stack

- Python 3.13
- Google Gemini API (gemini-3.5-flash-lite)
- Streamlit
- Pandas + OpenPyXL
- Pydantic

## Setup

1. Clone the repo and enter folder
2. Create venv: python -m venv .venv
3. Activate: .venv\Scriptsctivate
4. Install: pip install -r requirements.txt
5. Add key: echo GEMINI_API_KEY=your_key > .env
6. Run: python -m streamlit run app.py

## Supported Files

- CSV
- Excel (.xlsx, .xls)

## API Key

Free at https://aistudio.google.com/apikey
