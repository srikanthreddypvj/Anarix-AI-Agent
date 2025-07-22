from flask import Flask, render_template, request
from query_engine import process_question, generate_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sql_query = None
    result = None
    chart_url = None

    if request.method == "POST":
        question = request.form["question"]
        output = process_question(question)
        sql_query = output.get("sql")
        result = output.get("results")
        chart_url = generate_chart(question)

    return render_template("index.html", sql_query=sql_query, result=result, chart_url=chart_url)

if __name__ == "__main__":
    app.run(debug=True)
