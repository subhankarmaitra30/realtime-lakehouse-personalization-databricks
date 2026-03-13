# 🚀 Real-Time Ecommerce Intelligence Platform  
### Databricks Lakehouse | Streaming Analytics | ML Personalization | Fraud Detection

An end-to-end **real-time ecommerce analytics and machine learning platform** built on the **Databricks Lakehouse architecture**.  
The system ingests streaming clickstream events, processes them through a **Medallion Architecture (Bronze → Silver → Gold)**, trains ML models for **purchase prediction and fraud detection**, and serves predictions through a **live analytics dashboard**.

This project demonstrates a **complete modern data + ML platform** combining streaming pipelines, feature engineering, model lifecycle management, explainable AI, and real-time monitoring.

---

# 📊 Architecture

![Lakehouse Architecture](architecture/lakehouse_architecture.drawio.png)

The platform follows the **Databricks Lakehouse architecture**:
Streaming Event Generator
↓
Auto Loader Ingestion
↓
Bronze Layer (Raw Events)
↓
Silver Layer (Feature Engineering)
↓
Gold Layer (ML Training Dataset)
↓
MLflow Training + Model Registry
↓
Distributed Batch Inference
↓
Real-Time Intelligence Dashboard

---

# ⭐ Key Features

### 🔹 Real-Time Data Streaming
Simulated clickstream events stream into the platform using a **streaming event simulator**.

### 🔹 Delta Lake Medallion Architecture
The pipeline is structured using the **Bronze → Silver → Gold** architecture for scalable analytics.

### 🔹 Advanced Feature Engineering
Silver layer transformations include:

- Sessionization algorithm
- Behavioral features
- Product popularity windows
- RFM customer metrics

### 🔹 Machine Learning Lifecycle
Models are trained and tracked using **MLflow** with:

- Experiment tracking
- Model versioning
- Model Registry
- Production model promotion

### 🔹 Explainable AI
Model predictions are explained using **SHAP feature importance**, enabling interpretable ML.

### 🔹 Distributed Model Inference
Predictions are generated using **Spark distributed scoring with Pandas UDFs**, enabling scalable batch inference.

### 🔹 Real-Time Analytics Dashboard
A Databricks SQL dashboard provides real-time insights including:

- Streaming event throughput
- Trending products
- Fraud detection alerts
- Purchase probability predictions

---

# 🗂 Data Pipeline

The platform follows the **Medallion Architecture**.

### Bronze Layer
Raw clickstream data ingested using **Auto Loader**.

Table:

```
bronze_clickstream_events
```

Contains raw streaming events.

---

### Silver Layer
Cleaned and enriched datasets.

Tables:

```
silver_events_clean
silver_sessionized_events
silver_user_behavior_features
silver_product_popularity_features
silver_user_rfm_features
```

Transformations include:

- Data cleaning
- Timestamp normalization
- Sessionization
- Behavioral feature engineering
- Customer RFM features

---

### Gold Layer
ML-ready dataset.

Table:

```
gold_ml_training_dataset
```

This dataset powers both **purchase prediction** and **fraud detection** models.

---

# 🤖 Machine Learning Pipeline

### Model Training

Models trained using:

- Random Forest Classifier
- Scikit-learn
- MLflow experiment tracking

Models:

```
ecommerce_purchase_model
ecommerce_fraud_model
```

---

### Model Lifecycle

MLflow manages:

```
Experiment Tracking
↓
Model Registry
↓
Version Control
↓
Production Deployment
```

Models are promoted to **Production stage** in the registry.

---

### Model Explainability

Feature importance is analyzed using **SHAP**.

Example insights:

| Feature | Impact |
|------|------|
| purchases | strongest signal |
| frequency | strong predictor |
| recency_days | important behavioral signal |
| views | moderate impact |

This ensures **interpretable ML predictions**.

---

# ⚡ Distributed Batch Inference

Predictions are generated using **Spark distributed scoring**.

Pipeline:

```
Gold Dataset
↓
Load Production Model
↓
Vectorized Pandas UDF Scoring
↓
gold_predictions table
```

Table:

```
gold_predictions
```

Contains purchase and fraud predictions.

---

# 📊 Real-Time Intelligence Dashboard

Dashboard: **Ecommerce Real-Time Intelligence**

Metrics include:

### 📈 Streaming Event Throughput
Tracks incoming event rate.

### 🔥 Top Trending Products
Identifies popular products in real time.

### ⚠ Fraud Detection Alerts
Flags suspicious sessions.

### 🎯 Purchase Prediction Insights
Highlights high-conversion users.

Example dashboard:

![Dashboard](docs/dashboard.png)

---

# ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
https://github.com/subhankarmaitra30/realtime-lakehouse-personalization-databricks.git
