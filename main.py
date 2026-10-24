import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
excel_path = base_dir / "expense_tracker.xlsx"

df = pd.read_excel(excel_path)
print(df)

required_columns = {"Amount", "Description"}
missing_columns = required_columns - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

# Convert amount to numeric for calculations
# and ensure description values are strings for categorization

df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Description"] = df["Description"].fillna("").astype(str)

# Total spending
total_expense = df["Amount"].sum()
# Average expense
average_expense = df["Amount"].mean()
# Highest expense
highest_expense = df["Amount"].max()
# Lowest expense
lowest_expense = df["Amount"].min()

print("\nExpense Summary:")
print("Total Expense:", total_expense)
print("Average Expense:", average_expense)
print("Highest Expense:", highest_expense)
print("Lowest Expense:", lowest_expense)


def categorize(description):
    description = str(description).lower()

    if "swiggy" in description or "restaurant" in description or "dinner" in description:
        return "Food"

    elif "uber" in description or "petrol" in description:
        return "Transport"

    elif "amazon" in description:
        return "Shopping"

    elif "electricity" in description:
        return "Bills"

    elif "netflix" in description or "movie" in description:
        return "Entertainment"

    elif "pharmacy" in description:
        return "Healthcare"

    elif "grocery" in description:
        return "Groceries"

    else:
        return "Other"


df["Category"] = df["Description"].str.lower().apply(categorize)
print(df)

# Spending by category
category_spending = df.groupby("Category")["Amount"].sum()

print("\nSpending by Category:")
print(category_spending.to_string())

# Highest spending category
highest_category = category_spending.idxmax()
highest_category_amount = category_spending.max()

print("\nHighest Spending Category:")
print(highest_category, "-", highest_category_amount)

# Lowest spending category
lowest_category = category_spending.idxmin()
lowest_category_amount = category_spending.min()

print("\nLowest Spending Category:")
print(lowest_category, "-", lowest_category_amount)

# Most expensive transaction
most_expensive = df.loc[df["Amount"].idxmax()]

print("\nMost Expensive Transaction:")
print(most_expensive["Description"], "-", most_expensive["Amount"])

# Spending by payment method
payment_spending = df.groupby("Payment_Method")["Amount"].sum()

print("\nSpending by Payment Method:")
print(payment_spending.to_string())

# Spending by month
df["Date"] = pd.to_datetime(df["Date"])

monthly_spending = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()

print("\nSpending by Month:")
print(monthly_spending.to_string())

# Highest spending month
highest_month = monthly_spending.idxmax()
highest_month_amount = monthly_spending.max()

print("\nHighest Spending Month:")
print(highest_month, "-", highest_month_amount)

#monthly budget calculation
monthly_budget = 15000

print("\nMonthly Budget:", monthly_budget)

for month, amount in monthly_spending.items():
    if amount > monthly_budget:
        print(month, "- Over Budget by", amount - monthly_budget)
    else:
        print(month, "- Under Budget by", monthly_budget - amount)

#average monthly spending calculation
average_monthly_spending = monthly_spending.mean()

print("\nAverage Monthly Spending:")
print(average_monthly_spending)

# Save analyzed data
df.to_excel("expense_tracker_analyzed.xlsx", index=False)

print("\nAnalyzed data saved successfully.")

# Gemini AI integration
from google import genai
from getpass import getpass

api_key = getpass("Enter your Gemini API key: ")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"""
You are an AI expense analysis assistant.

Here is my expense summary:

Total Expense: ₹{total_expense:.2f}
Average Expense: ₹{average_expense:.2f}
Highest Expense: ₹{highest_expense:.2f}
Lowest Expense: ₹{lowest_expense:.2f}

Spending by Category:
{category_spending.to_string()}

Monthly Spending:
{monthly_spending.to_string()}

Give me 3 useful observations about my spending.
"""
)

print(response.text)

user_question = input("\nAsk your expense assistant: ")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"""
You are an AI expense assistant.

Here is my expense data:

Total Expense: ₹{total_expense:.2f}
Average Expense: ₹{average_expense:.2f}
Highest Expense: ₹{highest_expense:.2f}
Lowest Expense: ₹{lowest_expense:.2f}

Spending by Category:
{category_spending.to_string()}

Monthly Spending:
{monthly_spending.to_string()}

The user's question is:
{user_question}

Answer the user's question using the expense data above.
"""
)

print("\nAI Assistant:")
print(response.text)
