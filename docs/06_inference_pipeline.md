# Inference Pipeline

## Scalable Batch Prediction with Distributed Spark Scoring

---

# 1. Overview

After training and registering machine learning models, the next stage in the system is 
**model inference**.

The inference pipeline generates predictions using the production models stored in the **MLflow Model 
Registry** and applies them to the Gold-layer dataset.

The goal of this stage is to produce scalable predictions that can support analytics, dashboards, and
recommendation workflows.

Unlike simple notebook-based inference pipelines, this project implements **distributed batch inference 
using Spark**, enabling predictions to scale across large datasets.

---

# 2. Inference Pipeline Architecture

The prediction workflow follows this architecture:
Gold ML Training Dataset
↓
Load Production Model
↓
Distributed Spark Scoring
↓
Prediction Dataset
↓
Gold Predictions Table
↓
Dashboard / Demo Layer

This architecture ensures that predictions can be computed efficiently across large volumes 
of behavioral data.

---

# 3. Model Loading

Models are loaded directly from the **MLflow Model Registry**.

This ensures that inference pipelines always use the **latest production-approved version
of the model**.

Example model references:
models:/ecommerce_purchase_model/Production
models:/ecommerce_fraud_model/Production

Using registry references eliminates the need to reference specific training run IDs.

This approach supports a production-grade ML lifecycle.

---

# 4. Prediction Strategy

Two prediction strategies are commonly used in ML pipelines:

| Strategy | Description |
|--------|-------------|
| Driver-side inference | Convert Spark data to Pandas and score locally |
| Distributed inference | Score data across Spark workers |

Driver-side inference is simple but **not scalable**.

This project uses **distributed inference using Spark Pandas UDFs**, which enables prediction workloads to scale horizontally.

---

# 5. Distributed Spark Scoring

Distributed inference is implemented using **vectorized Pandas UDF scoring**.

The workflow is as follows:
Spark DataFrame
↓
Partition Data Across Workers
↓
Vectorized Pandas UDF
↓
Model Prediction
↓
Return Predictions to Spark

Each Spark worker processes a subset of the data and generates predictions in parallel.

This approach avoids memory bottlenecks and allows the system to scale efficiently.

---

# 6. Prediction Features

The prediction pipeline uses the same feature set used during training.

Example features include:

| Feature | Description |
|------|-------------|
| total_events | number of session interactions |
| views | number of product views |
| add_to_cart | cart additions |
| purchases | purchase count |
| avg_price | average product price |
| frequency | interaction frequency |
| monetary_value | purchase value |
| recency_days | recency of activity |

Maintaining consistent features between training and inference ensures reliable predictions.

---

# 7. Prediction Outputs

The inference pipeline generates two prediction outputs.

### Purchase Prediction

This model predicts whether a user session is likely to result in a purchase.

Output column: purchase_prediction

---

### Fraud Detection Prediction

This model identifies potentially suspicious purchasing behavior.

Output column: fraud_prediction

These predictions provide signals that can support recommendation systems and risk monitoring.

---

# 8. Prediction Storage

Prediction results are written to a **Delta Lake table**.
gold_predictions


Example schema:

| Column | Description |
|------|-------------|
| user_id | customer identifier |
| session_number | session identifier |
| purchase_prediction | purchase likelihood |
| fraud_prediction | fraud risk score |

Storing predictions as Delta tables allows them to be easily queried by downstream applications.

---

# 9. Table Optimization

After writing predictions, the table is optimized using Delta Lake operations.

Example optimization tasks include:

- Delta file compaction
- improved query performance
- efficient dashboard queries

These optimizations ensure that the dashboard layer can retrieve predictions efficiently.

---

# 10. Integration with Analytics Layer

The predictions table supports several downstream analytics workflows.

Example queries include:

### High Purchase Probability Users

Identify users most likely to purchase.
SELECT *
FROM gold_predictions
ORDER BY purchase_prediction DESC
LIMIT 10

---

### Fraud Risk Monitoring

Detect potentially suspicious sessions.
SELECT *
FROM gold_predictions
WHERE fraud_prediction = 1

These insights can be visualized through dashboards.

---

# 11. Demo and Recommendation Layer

The predictions table powers the interactive demo layer.

The demo allows users to query predictions for a specific user ID and observe predicted outcomes.

Example workflow:
User Input
↓
Query Predictions Table
↓
Display Recommendation Signals

This provides a simple demonstration of how predictive analytics can support recommendation systems.

---

# 12. Scalability Considerations

Several design choices enable scalable inference:

- Spark distributed processing
- vectorized Pandas UDF scoring
- Delta Lake storage
- model registry integration

These components allow the system to scale prediction workloads as data volumes increase.

---

# 13. Summary

The inference pipeline transforms trained models into operational predictions.
Production Model
↓
Distributed Spark Inference
↓
Prediction Dataset
↓
Analytics and Dashboard

This stage bridges the gap between machine learning experimentation and operational analytics.

By implementing scalable inference pipelines, the platform demonstrates how machine learning models
can be integrated into real-world data platforms.
