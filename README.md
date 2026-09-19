# Project Title
Insurance Premium Lookup

## Description
User inputs their zip code and web app retrieves averages for liability, comprehensive and collision insurance in their state for years 2021-2023

## Tech Stack
- Data Ingestion: Python, pdfplumber, pandas
- Backend: FastAPI, PostgreSQL, psycopg2
- Frontend: React, Chart.js

## Project Structure
insurance-project/
├── data/              # raw PDF dataset
├── data-ingestion/    # PDF processing and DB loading
├── backend/           # FastAPI REST API
├── frontend/          # React UI
└── README.md

## Setup and Installation
### 1. Data Ingestion
cd data-ingestion
pip install -r requirements.txt
python ingest.py

### 2. Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

### 3. Frontend
cd frontend
npm install
npm start



## API Endpoints
GET /insurance?zip=95032
Returns average premiums for the last 3 years for the state matching the zip code.

## How It Works
1. User enter zip code
2. Frontend sends request to backend API 
3. Backend matches zip code to state
4. Backend queries data and returns JSON to frontend
5. Frontend processes and displays results as bar chart

## Data Source
NAIC 2022/2023 Auto Insurance Database Report
