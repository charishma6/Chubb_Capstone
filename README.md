# 📈 Stock Trading & Investment Performance Analytics System

An end-to-end data analytics application designed to process, analyze, and visualize stock market and portfolio trading data using modern data engineering and BI tools.

---

## 📌 Project Overview

Individual traders and investment firms often deal with large volumes of raw stock market data spread across multiple sources. Manual analysis of this data is time-consuming, error-prone, and does not scale.

This project addresses those challenges by building a centralized analytics system that:

* Automates data ingestion and processing  
* Applies structured data cleaning and transformations  
* Computes portfolio performance and risk metrics  
* Delivers interactive dashboards for decision-making  

---

## 🎯 Project Objectives

* Build a **Bronze–Silver–Gold** data architecture  
* Automate ETL pipelines using **Apache Airflow**  
* Perform scalable analytics using **PySpark on Databricks**  
* Deliver business-ready insights using **Power BI dashboards**  
* Demonstrate real-world financial analytics use cases  

---

## 🏗️ End-to-End Architecture

### Data Flow

```
Raw Dataset (CSV)
        ↓
Bronze Layer – Raw ingestion (Databricks)
        ↓
Silver Layer – Cleaning & standardization
        ↓
Gold Layer – Analytics & KPIs
        ↓
Power BI Dashboards
        ↓
Airflow – Orchestrates the entire pipeline
```


### Workflow Orchestration

* Apache Airflow triggers Databricks jobs  
* A single Databricks job (`stock_trading_etl_job`) contains:
  * Bronze Task  
  * Silver Task  
  * Gold Task  

---

## 🛠️ Technology Stack

### Data Processing & Analytics
* Python  
* Pandas  
* PySpark  

### Big Data Platform
* Databricks  
* Delta Lake  

### Workflow Orchestration
* Apache Airflow (Docker-based)  

### Visualization
* Power BI Desktop  

### Storage & Formats
* CSV (Raw)  
* Delta Tables (Bronze, Silver, Gold)  

### Version Control
* Git & GitHub  

---

## 📂 Data Scope

The system processes the following datasets:

### 1️⃣ Stock Prices
* Date  
* Ticker  
* Open, High, Low, Close  
* Volume  

### 2️⃣ Portfolio Transactions
* Transaction ID  
* Date  
* Ticker  
* Action (BUY / SELL)  
* Quantity  
* Price  

### 3️⃣ Company Sector Mapping
* Ticker  
* Sector  

### 4️⃣ Market Benchmark Index
* Date  
* Open  
* Close  

---

## 🔄 ETL Pipeline Design

### 🥉 Bronze Layer – Raw Ingestion & Validation
**Notebook:** `bronze_ingestion.ipynb`

* Loads raw CSV files from mounted storage  
* Performs:
  * Schema inference  
  * Null checks  
  * Invalid value detection  
  * Business rule validations  
* Stores data as Delta tables  
* Generates validation logs  

---

### 🥈 Silver Layer – Data Cleaning & Standardization
**Notebook:** `silver_cleaning.ipynb`

Handles:
* Null values  
* Invalid prices, quantities, and dates  
* Action standardization (BUY/SELL)  
* Negative and zero-value filtering  

Separates:
* Valid records  
* Invalid records (for auditing)  

Produces clean, analytics-ready datasets.

---

### 🥇 Gold Layer – Business Analytics
**Notebook:** `gold_analytics.ipynb`

Creates curated tables for reporting:
* Daily stock metrics (returns, moving averages, volatility)  
* Portfolio holdings and market value  
* Portfolio trades fact table  
* Sector-level performance metrics  
* Benchmark vs portfolio comparison  
* Risk indicators (volatility, drawdowns, Sharpe-like metrics)  

---

## ⏱️ Workflow Automation with Apache Airflow

* Airflow runs inside Docker containers  
 **DAG:** `stock_trading_etl_pipeline.py`  

A single DAG orchestrates the full pipeline:
* Bronze Task → Silver Task → Gold Task


Uses `DatabricksRunNowOperator` and supports:
* Scheduled runs  
* Retries and failure handling  
* Manual triggering for demos  

---

## 📊 Power BI Dashboards

Dashboards are built **only on Gold layer tables**.

### 1️⃣ Executive Dashboard
- Total Portfolio Value  
- Active Holdings Count  
- Total Trades  
- Buy vs Sell Ratio  
- Portfolio Volatility (30D)  
- Portfolio value trend  
- Allocation by stock  

### 2️⃣ Stock Performance & Risk Analytics
- Stock price trends  
- Daily return analysis  
- Moving average crossover  
- Volatility comparison  
- Risk indicators  

### 3️⃣ Market & Sector Overview
- Sector performance over time  
- Sector ranking by returns  
- Benchmark market trend  
- Excess returns analysis  

### 4️⃣ Portfolio & Trading Analysis
- Buy vs Sell activity  
- Trading volume over time  
- Drawdowns  
- Portfolio vs benchmark comparison  

---

## 🔍 Key Insights

* Portfolio shows strong growth with high volatility  
* Trading strategy is active rather than passive  
* Concentration risk exists in top-performing stocks  
* Technology and Financial sectors dominate returns  
* Benchmark comparison reveals mixed excess performance  
* Risk indicators highlight volatile assets contributing to drawdowns  

---

## 🚀 Future Enhancements

* Real-time market data ingestion via APIs  
* Machine learning models for price prediction  
* Advanced risk metrics (Beta, VaR, Sortino)  
* Incremental & streaming pipelines  
* Automated Power BI Service refresh  
* Alerting system for abnormal market movements  

---

## 🚀 How to Run This Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/charishma6/Chubb_Capstone.git
```

### 2️⃣ Databricks

- Upload notebooks
- Create job
- Connect with Airflow

### 3️⃣ Run Airflow
```bash
cd Airflow
docker compose up
```


Access UI: 
👉 [http://localhost:8080](http://localhost:8080)

Trigger DAG: `stock_trading_etl_pipeline`

4️⃣ Power BI

* Open `Stock Trading & Investment Performance Analytics System.pbix`
* Refresh data
* Explore dashboards

## 🏁 Conclusion

This project demonstrates a production-style data analytics pipeline that transforms raw financial data into actionable insights using modern data engineering, orchestration, and visualization tools.

Thank you

### Author:
Charishma