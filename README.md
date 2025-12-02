🏙️ Real Estate AI Insights Platform
Your Personal AI Real-Estate Analyst — Powered by Data, Analytics & LLMs
🌟 Overview

The Real Estate AI Insights Platform transforms raw real-estate Excel data into smart, human-like insights.

Users can ask questions like:
“Analyze Aundh”
“Compare Ambegaon Budruk and Aundh”
“Show price growth for Akurdi over the last 3 years”

And the system instantly responds with:

✔ Intelligent written insights (powered by LLaMA 3)
✔ Interactive trend charts
✔ Data-driven comparisons
✔ Clean, structured tables

It behaves like a professional real-estate agent, analyzing years of data and giving clear, easy explanations.

🧠 System Workflow
User Query → Backend Parser → Excel Data Extraction → 
LLM Summary Generation → Charts + Tables → Frontend Display

✔ Step 1: User enters a natural question
✔ Step 2: Backend detects which location(s) are mentioned
✔ Step 3: Pandas extracts relevant rows
✔ Step 4: AI generates insight text
✔ Step 5: Charts and tables are built
✔ Step 6: Frontend presents everything clearly


🛠️ Tech Stack
🎨 Frontend
React
Bootstrap
Axios
Chart.js

⚙️ Backend
Django
Django REST Framework
Pandas
Groq LLaMA-3 API
Python

📊 Data
Excel Dataset (realestate.xlsx)
Multiple locations
Year-wise supply, sale, and pricing data

🔍 Example Queries & Responses
🏠 “Analyze Aundh”

→ AI returns a 3–4 line real-estate summary
→ Price & demand trend charts
→ Clean table view

🆚 “Compare Ambegaon Budruk and Aundh demand trends”

→ AI explains which area has higher demand
→ Shows both locations’ charts side-by-side
→ Displays combined table

📈 “Show price growth for Akurdi over the last 3 years”

→ LLM gives growth narrative
→ Chart highlights last 3 years
→ Data table shows clear change

📂 Project Structure
RealEstateFullStack/
│
├── backend/
│   ├── backend/        # Django project
│   ├── api/            # API logic
│   ├── realestate.xlsx # Dataset
│   └── manage.py
│
└── frontend/
    ├── src/            # React components
    ├── public/
    └── package.json

🎯 Purpose of the Project

This project demonstrates:
Real-world data analysis skills
LLM integration into full-stack systems
Backend–frontend communication
Chart visualization and interactive UI design
Clean API development
Real estate domain understanding
Handling natural language queries
