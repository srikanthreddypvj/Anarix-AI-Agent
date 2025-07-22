import sqlite3
from llm import generate_sql
import pandas as pd
import matplotlib.pyplot as plt
import os

def execute_query(sql):
    try:
        conn = sqlite3.connect('database/ecommerce.db')
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        return f"[DB ERROR] {e}"

VALID_TABLES = {"total_sales", "ad_sales", "eligibility"}

def is_valid_sql(sql):
    valid_tables = ["total_sales", "ad_sales", "eligibility"]
    valid_columns = [
        "date", "item_id", "total_sales", "total_units_ordered",
        "ad_sales", "impressions", "ad_spend", "clicks", "units_sold",
        "eligibility_datetime_utc", "eligibility", "message"
    ]

    # Normalize SQL
    sql_lower = sql.lower()

    for word in sql_lower.replace(",", " ").replace("(", " ").replace(")", " ").split():
        if "from" in word or "join" in word:
            continue
        for token in word.split():
            if token.startswith("ad_") or token.startswith("total_") or token.startswith("eligibility"):
                if token not in valid_tables and token not in valid_columns:
                    print(f"❌ Invalid token in SQL: {token}")
                    return False
    return True


def process_question(question):
    sql = generate_sql(question)
    print("🧠 Generated SQL:", sql)

    if sql.startswith("[LLM ERROR]") or not sql.lower().startswith("select"):
        return {"sql": sql, "results": None}

    if not is_valid_sql(sql):
        return {"sql": sql, "results": "[LLM ERROR] Invalid SQL — please rephrase."}

    result = execute_query(sql)
    return {"sql": sql, "results": result}




def generate_chart(question):
    if "chart" in question.lower() or "visual" in question.lower():
        conn = sqlite3.connect('database/ecommerce.db')
        df = pd.read_sql("SELECT item_id, SUM(total_sales) as total_sales FROM total_sales GROUP BY item_id", conn)

        os.makedirs('static/charts', exist_ok=True)
        chart_path = "static/charts/chart.png"

        df.plot(kind='bar', x='item_id', y='total_sales', color='skyblue', legend=False)
        plt.title("Total Sales by Product")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
        return "/" + chart_path
    return None
