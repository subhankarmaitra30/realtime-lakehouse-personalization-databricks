# System Architecture

## Real-Time Ecommerce Intelligence Platform  
**Databricks Lakehouse Architecture**

---

# 1. Architectural Overview

This project implements a complete **data and machine learning platform** built on the **Databricks Lakehouse architecture**.

The system ingests streaming ecommerce events, transforms them through a Medallion data architecture, trains machine learning models for behavioral prediction, and produces real-time analytical insights.

The architecture integrates **data engineering, feature engineering, machine learning operations, and visualization** within a unified pipeline.

---

# 2. High-Level System Architecture
Synthetic Event Generator
↓
Streaming Event Simulator
↓
Bronze Layer (Raw Clickstream Events)
↓
Silver Layer (Feature Engineering)
↓
Gold Layer (ML Training Dataset)
↓
Machine Learning Training Pipeline
↓
MLflow Model Registry
↓
Distributed Batch Inference
↓
Gold Predictions Table
↓
Real-Time Intelligence Dashboard

This architecture demonstrates how modern data platforms unify **streaming analytics and machine learning pipelines**.

---

# 3. Architectural Principles

The system design follows several important engineering principles.

### Separation of Concerns

Data ingestion, transformation, feature engineering, and machine learning are implemented as independent layers.

This ensures that:

- Raw data remains immutable
- Feature engineering pipelines remain reusable
- Machine learning pipelines remain modular

---

### Medallion Architecture

The platform uses the **Bronze → Silver → Gold** pattern.

| Layer | Purpose |
|------|--------|
| Bronze | Raw streaming events |
| Silver | Cleaned data and engineered features |
| Gold | Analytical datasets and ML training data |

This layered architecture improves data quality, maintainability, and reproducibility.

---

### Scalable Distributed Processing

All transformations and model inference pipelines use **Apache Spark distributed processing**, ensuring the system can scale to large datasets.

---

### Machine Learning Lifecycle Management

The ML pipeline uses **MLflow** to manage:

- experiment tracking
- model versioning
- model promotion through the Model Registry

This enables production-grade model lifecycle management.

---

# 4. Data Ingestion Architecture

The system simulates real-time ecommerce activity using a streaming event generator.

## Event Simulation

Synthetic events represent common ecommerce interactions:

- product views
- add-to-cart actions
- purchases
- session metadata

These events are written into a streaming input directory and processed by Structured Streaming.

---

## Streaming Pipeline
Event Generator
↓
Event Batch Files
↓
Streaming Simulator
↓
Structured Streaming Ingestion

The simulator introduces small delays between batches to mimic real-time traffic.

---

# 5. Bronze Layer

The Bronze layer stores **raw event data exactly as ingested**.

### Characteristics

- Immutable raw records
- No transformations applied
- Schema captured from event ingestion

### Example fields

| Field | Description |
|------|-------------|
| user_id | unique customer identifier |
| session_id | session identifier |
| product_id | product viewed or purchased |
| event_type | user action |
| price | product price |
| timestamp | event timestamp |

Bronze tables provide a **reliable system of record for event data**.

---

# 6. Silver Layer

The Silver layer performs **data cleaning and feature engineering**.

This stage converts raw event streams into structured behavioral datasets.

---

## Data Cleaning

Cleaning transformations include:

- timestamp normalization
- event standardization
- duplicate removal
- schema validation

---

## Sessionization

User sessions are reconstructed using a **30-minute inactivity rule**.
User Event Timeline
↓
Detect Inactivity Gaps
↓
Create Session Boundaries

Sessionization enables behavioral analytics such as session length and activity patterns.

---

## Feature Engineering

Several feature categories are created.

### Behavioral Features

Derived from session activity:

- total_events
- views
- add_to_cart
- purchases
- average price viewed

---

### Product Popularity Features

Popularity signals measure product demand over time windows.

Example features:

- product_views_last_hour
- product_views_last_day

These signals are commonly used in recommendation systems.

---

### RFM Features

Customer value signals are computed using the **Recency-Frequency-Monetary framework**.

| Feature | Meaning |
|-------|--------|
| Recency | days since last activity |
| Frequency | number of interactions |
| Monetary | total purchase value |

RFM features are widely used in ecommerce analytics and customer segmentation.

---

# 7. Gold Layer

The Gold layer produces **machine-learning-ready datasets**.

This layer integrates all engineered features into a unified training dataset.
Silver Feature Tables
↓
Feature Joins
↓
Gold ML Training Dataset

Example columns:

| Feature |
|-------|
| views |
| add_to_cart |
| purchases |
| avg_price |
| recency_days |
| frequency |
| monetary_value |

Label columns are also generated for training.

---

# 8. Machine Learning Pipeline

The machine learning pipeline trains two models.

### Purchase Prediction Model

Predicts the probability that a user will complete a purchase.

### Fraud Detection Model

Identifies suspicious purchasing behavior.

Both models are trained using **Random Forest classifiers**.

---

## MLflow Experiment Tracking

MLflow records:

- model parameters
- evaluation metrics
- trained model artifacts
- feature signatures

This ensures full reproducibility of experiments.

---

# 9. Model Registry

After training, models are registered in the **MLflow Model Registry**.
MLflow Experiment
↓
Registered Model
↓
Production Stage

Two models are maintained:

- ecommerce_purchase_model
- ecommerce_fraud_model

The inference pipeline always loads the **Production stage model**, ensuring consistent predictions.

---

# 10. Batch Inference Pipeline

Prediction pipelines generate model outputs using **distributed Spark scoring**.
Gold Dataset
↓
Load Production Model
↓
Vectorized Spark Inference
↓
Prediction Dataset

Predictions include:

- purchase likelihood
- fraud risk score

Results are stored in the **gold_predictions table**.

---

# 11. Explainable AI

Model predictions are interpreted using **SHAP (SHapley Additive Explanations)**.

SHAP analysis identifies which features most influence predictions.

Typical influential features include:

- purchase history
- session frequency
- recent activity

Explainability improves model transparency and trust.

---

# 12. Real-Time Analytics Dashboard

A dashboard provides operational visibility into the system.

Metrics include:

- trending products
- purchase predictions
- fraud alerts
- streaming event throughput

The dashboard refreshes periodically to reflect the latest pipeline outputs.

---

# 13. End-to-End Data Flow
Event Generator
↓
Streaming Ingestion
↓
Bronze Raw Events
↓
Silver Feature Engineering
↓
Gold ML Dataset
↓
Model Training
↓
Model Registry
↓
Distributed Batch Inference
↓
Gold Predictions
↓
Dashboard Analytics

This architecture demonstrates how modern Lakehouse platforms integrate **data engineering, machine learning, and analytics** in a unified system.

---

# 14. Scalability Considerations

Several design choices ensure scalability:

- Delta Lake storage for efficient data management
- Spark distributed processing for feature engineering
- Pandas UDF inference for scalable prediction
- MLflow for model lifecycle management

These patterns align with **production data platform architectures**.

---

# 15. Summary

The architecture demonstrates how a Lakehouse platform can support:

- real-time event processing
- scalable feature engineering
- machine learning lifecycle management
- explainable predictions
- operational analytics dashboards

Together, these components form a **complete end-to-end data and AI platform** suitable for modern ecommerce analytics systems.
