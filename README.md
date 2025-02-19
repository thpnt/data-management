# Scheduled ETL Pipeline with BigQuery, FastAPI, Docker, Cloud Run, and Cloud Scheduler

## 🚀 Project Overview

This project implements a **scheduled ETL pipeline** that:

1. **Retrieves data** from **Google BigQuery**.
2. **Processes and cleans the data** using Python scripts.
3. **Creates a new "preprocessed" table** in BigQuery with the cleaned data.

The pipeline is fully automated and deployed to **Google Cloud Platform (GCP)**.

---

## 🛠️ Key Components

### 🔄 ETL Process
- Data is fetched from **BigQuery**, cleaned, and saved into a **preprocessed** table.
- The Python-based ETL logic handles data transformation, currency conversion, and preprocessing.

### 🌐 FastAPI
- The ETL function is **exposed as an API** using **FastAPI**.
- You can trigger the ETL process by making an HTTP **GET** request to the Cloud Run service endpoint.

### 🐳 Docker & Google Cloud Run
- The API is containerized with **Docker** and deployed to **Google Cloud Run** for serverless execution.
- Cloud Run ensures scalability and secure access to the ETL service.

### 🕒 Google Cloud Scheduler
- **Cloud Scheduler** triggers the **FastAPI endpoint** on a scheduled basis.
- The pipeline runs automatically without manual intervention.

---

## ✅ Pipeline Status

✅ The pipeline **works perfectly**.  
✅ You can **test it manually** by triggering the Google Cloud Scheduler job.  
✅ After running, the **"preprocessed" table in BigQuery** shows an updated **refresh date**.

---

## 📊 Power BI Report

A **Power BI report** has been developed based on the cleaned BigQuery table.  

🔗 **[Click here to view the Power BI report]((https://edheccom-my.sharepoint.com/:u:/g/personal/paco_gorieu--petit-pas_edhec_com/Ef2-JRkuruJDn8iBDu9IuJABK4A-awyJ9pIIFetXS-87uQ?e=yk3ZuU))**

---

## 🚀 How to Test the Pipeline

### 🔔 Trigger the ETL Manually
1. Navigate to **Google Cloud Console** → **Cloud Scheduler**.
2. Find the ETL scheduler job and click **Run Now**.
3. Verify the **BigQuery preprocessed table** to see the updated **refresh date**.

---
