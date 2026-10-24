#Expense Tracker — Python, Power BI & Gemini AI

An end-to-end personal expense tracking and analysis project built using **Python, Pandas, Excel, Power BI, and Google Gemini AI.

The project takes expense data from Excel, processes and analyzes it using Python, visualizes spending patterns in Power BI, and provides an interactive AI expense assistant powered by Gemini.

#Project Overview

This project demonstrates how raw expense data can be transformed into meaningful financial insights through a complete data analytics workflow.

#Workflow

Excel Expense Data
        ↓
Python + Pandas
        ↓
Data Cleaning & Categorization
        ↓
Expense Analysis
        ↓
Analyzed Excel Dataset
        ↓
Power BI Dashboard
        ↓
Gemini AI Expense Assistant

#Technologies Used

* Python — Data processing and analysis
* Pandas — Data manipulation and analysis
* OpenPyXL — Excel file handling
* Microsoft Excel — Expense data source
* Power BI — Interactive dashboards and visualization
* Google Gemini AI — AI-powered expense analysis
* Git & GitHub — Version control and project hosting


#Features

#Expense Analysis

The Python application calculates:

* Total expenses
* Average transaction amount
* Highest expense
* Lowest expense
* Highest spending category
* Lowest spending category
* Most expensive transaction
* Spending by payment method
* Monthly spending
* Average monthly spending
* Monthly budget comparison

#Automatic Expense Categorization

Transactions are automatically categorized based on their descriptions.

Example categories:

* Food
* Transport
* Shopping
* Bills
* Entertainment
* Healthcare
* Groceries
* Other

#Budget Analysis

The project compares monthly spending against a predefined monthly budget and identifies whether each month is:

* Under budget
* Over budget

#Power BI Dashboard

The Power BI dashboard provides interactive visualizations for:

* Total expenses
* Spending by category
* Spending by payment method
* Monthly spending trends
* Highest and lowest expenses
* Detailed transaction analysis
* Category filtering
* Payment method filtering
* Monthly filtering

The dashboard contains two main pages:

1. Executive Dashboard
2. Expense Analysis

#AI Expense Assistant

The project includes an interactive Gemini-powered expense assistant.

Users can ask questions such as:

Which category should I reduce spending on?

Which month had the highest spending?

What are my biggest spending areas?

Give me practical suggestions to reduce my expenses.

The AI receives the calculated expense summary and provides observations based on the available data.

#API Key Security

The application does *not* store the Gemini API key.

When the program starts, the user is prompted to enter their own API key:

Enter your Gemini API key:

The key is entered using Python's "getpass" module, so it is not displayed while being entered.

The API key is:

* Not hardcoded in the source code
* Not saved to an ".env" file
* Not written to Excel
* Not committed to Git
* Not uploaded to GitHub
* Only held temporarily while the application is running

When the application exits, the Python process ends and the temporary key is no longer retained by the application.

**Never publish or share your Gemini API key publicly.**

#Project Structure

ExpenseTracker/
│
├── main.py
├── expense_tracker.xlsx
├── expense_tracker_analyzed.xlsx
├── Expense_Tracker_Dashboard.pbix
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── dashboard.png
    ├── expense_analysis.png
    └── ai_assistant.png


#How to Run the Project

#1. Clone the repository

git clone https://github.com/shashankks-ops/expense-tracker-python-powerbi-ai.git

Navigate into the project:

cd ExpenseTracker

#2. Install the required Python packages

pip install -r requirements.txt


#3. Run the Python application

python main.py

#4. Enter your Gemini API key

When prompted:

Enter your Gemini API key:

Enter your own Gemini API key and press Enter.

The key is used only during the current execution of the application.

#Power BI Dashboard

The project includes a Power BI dashboard built from the analyzed Excel dataset.

The dashboard allows users to explore expense patterns using interactive charts and slicers.

#Dashboard Pages

*Executive Dashboard*

* Total Expense
* Spending by Category
* Spending by Payment Method
* Monthly Spending Trend
* Category filtering

*Expense Analysis*

* Detailed transaction table
* Highest Expense
* Lowest Expense
* Category filter
* Payment Method filter
* Monthly filter

## 📸 Project Screenshots

### Executive Dashboard

![Executive Dashboard](screenshots/dashboard.png)

### Expense Analysis

![Expense Analysis](screenshots/expense_analysis.png)

### AI Expense Assistant

![AI Expense Assistant](screenshots/ai_assistant.png)

#Requirements

The project uses the following Python packages:

pandas
openpyxl
google-genai

Install them using:

pip install -r requirements.txt

#Data Processing Pipeline

The Python script performs the following steps:

1. Reads expense data from Excel.
2. Converts the date column into a proper date format.
3. Categorizes expenses based on transaction descriptions.
4. Calculates key expense metrics.
5. Groups expenses by category.
6. Groups expenses by payment method.
7. Calculates monthly spending.
8. Compares monthly spending with the budget.
9. Saves the processed dataset to "expense_tracker_analyzed.xlsx".
10. Sends summarized expense information to Gemini.
11. Allows the user to interact with the AI expense assistant.

#Learning Objectives

This project was built to practice and demonstrate:

* Python fundamentals
* Pandas data analysis
* Excel data handling
* Data cleaning and transformation
* Conditional logic
* Grouping and aggregation
* Financial data analysis
* Power BI dashboard development
* AI API integration
* Secure handling of API credentials
* Git and GitHub project management

#Future Improvements

Potential future improvements include:

* Expense prediction using machine learning
* Automatic anomaly detection
* More advanced expense categorization
* Additional Power BI KPIs
* Monthly spending alerts
* Savings recommendations
* Natural-language queries for the dashboard
* Database integration instead of Excel
* Web-based expense tracking interface

#Project

*Expense Tracker — Python + Power BI + Gemini AI*

An end-to-end data analytics project demonstrating the process of turning raw expense data into *analysis, interactive dashboards, and AI-powered insights*.
