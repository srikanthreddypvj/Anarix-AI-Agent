
# Anarix AI Agent for E-commerce Data Question Answering

## 🔍 Project Overview

This project goal was to develop an AI-powered agent capable of answering questions based on e-commerce datasets. The agent receives natural language questions through an API, translates them into SQL queries, and returns accurate, human-readable responses.

## 📊 Datasets Used

* Product-Level Ad Sales and Metrics
* Product-Level Total Sales and Metrics
* Product-Level Eligibility Table
## 🧠 Project Objective

* Build an AI Agent that:

  * Accepts questions via API.
  * Converts them to SQL queries using a local LLM.
  * Retrieves and formats results from a SQL database.
* (Bonus Features)

  * Visualize query results using charts.
  * Provide streamed, real-time-like response outputs.

## ⚙️ Tech Stack

* **SQL (SQLite/MySQL)** — for data storage and querying.
* **Python** — for backend and integration.
* **FastAPI** — to build RESTful endpoints.
* **LangChain** / **LLM (Local/Lightweight)** — for query understanding and SQL translation.
* **Matplotlib / Plotly** *(optional)* — for generating graphs.

## 🚧 Limitations

Due to **hardware constraints** (limited RAM, storage, and processing power on my personal laptop), I was unable to fully utilize more powerful LLMs or implement complex features like:

* High-accuracy models (e.g., GPT-4, Mistral-7B) for SQL translation.
* Advanced chart rendering and real-time streaming.
* Thorough testing and fine-tuning of edge case queries.

Despite this, I’ve tried to design the architecture in a modular, extensible way so that it can be easily upgraded on better machines.

## ✅ Example Questions Supported

* What is my total sales?
* Calculate the RoAS (Return on Ad Spend).
* Which product had the highest CPC (Cost Per Click)?

## 🧪 Demo

(https://drive.google.com/file/d/1OAvWG9piewzahxjv3f8sG9fHYjkNpeAe/view?usp=sharing)


## 📌 Future Improvements

* Integrate larger or cloud-based models for better natural language understanding.
* Add full visual support using dashboards.
* Optimize for performance and accuracy under real workloads.

## 📬 Contact

For questions or collaborations:

* [PVJ Srikanth Reddy](mailto:srikanthreddypvj@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/panduga-venkata-jaya-srikanth-reddy/)

---

Let me know if you’d like me to include the folder structure or codebase explanation as well.
