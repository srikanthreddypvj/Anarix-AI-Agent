import subprocess

def generate_sql(question):
    prompt = f"""
You are an expert SQL assistant.

Given this schema, convert the user's question to a valid SQL query.

SCHEMA:
TABLE: total_sales
- date
- item_id
- total_sales
- total_units_ordered

TABLE: ad_sales
- date
- item_id
- ad_sales
- impressions
- ad_spend
- clicks
- units_sold

TABLE: eligibility
- eligibility_datetime_utc
- item_id
- eligibility
- message

❌ DO NOT use: ad_speeds, ad_saless, spend_table, sales_table, etc.
✅ Use EXACT table and column names shown above.

Return SQL only, no explanations.

User question: {question}
SQL:
"""

    try:
        result = subprocess.run(
            ["C:\\Users\\gangi\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "tinyllama"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode().strip()

        if "```sql" in output:
            output = output.split("```sql")[-1]
        if "```" in output:
            output = output.split("```")[0]

        return output.strip()

    except Exception as e:
        return f"[LLM ERROR] Ollama (TinyLLaMA) failed:\n{e}"
