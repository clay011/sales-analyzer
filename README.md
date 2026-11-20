# Sales Data Analyzer

A Python script that loads sales data from a CSV file, cleans it, and creates a report with Pandas and Matplotlib.

## What it does
- Reads sales data from `sales.csv`
- Cleans the data (date conversion, removes empty rows)
- Calculates total revenue, revenue by category, revenue by month, and the top 3 products
- Saves charts to `report.png`

## Tech Stack
Python, Pandas, Matplotlib

## How to Run
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python analyze.py`