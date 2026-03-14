# Machine Learning Pipeline

## Predictive Modeling and ML Lifecycle Management

---

# 1. Overview

The machine learning pipeline transforms engineered behavioral features into predictive models that generate actionable insights.

This project implements two machine learning models:

- **Purchase Prediction Model** — estimates the likelihood that a user will complete a purchase.
- **Fraud Detection Model** — identifies potentially suspicious purchasing behavior.

The ML pipeline integrates **feature preparation, model training, experiment tracking, model registry, and explainability** using the Databricks ML ecosystem.

---

# 2. ML Pipeline Architecture

The machine learning workflow follows a structured pipeline.
Gold ML Training Dataset
↓
Feature Selection
↓
Train/Test Split
↓
Model Training
↓
MLflow Experiment Tracking
↓
Model Evaluation
↓
Model Registry
↓
Production Model

This architecture ensures reproducible experiments and production-ready model lifecycle management.

---

# 3. Training Dataset

The training dataset is produced in the **Gold layer** by combining several feature sources:

- behavioral interaction features
- product popularity signals
- RFM customer value features

Example feature columns include:

| Feature | Description |
|-------|-------------|
| total_events | number of interactions within session |
| views | product views |
| add_to_cart | cart additions |
| purchases | completed purchases |
| avg_price | average product price |
| frequency | user interaction frequency |
| recency_days | days since last interaction |
| monetary_value | cumulative purchase value |

These features collectively capture both **short-term session behavior and long-term customer value**.

---

# 4. Label Construction

Supervised machine learning requires labeled data.

Labels are derived from behavioral signals in the dataset.

### Purchase Prediction Label
label_purchase = 1 if purchases > 0
label_purchase = 0 otherwise

This label represents whether a session resulted in a purchase.

---

### Fraud Detection Label

Fraud signals are simulated using abnormal behavior thresholds.
label_fraud = 1 if purchases > threshold
label_fraud = 0 otherwise

Although synthetic, this approach allows the fraud detection pipeline to demonstrate anomaly classification workflows.

---

# 5. Model Selection

Both models are implemented using **Random Forest classifiers**.

Random Forest was chosen due to several advantages:

- robust performance with heterogeneous features
- minimal feature scaling requirements
- resistance to overfitting
- compatibility with SHAP explainability

Random Forest models also perform well with tabular behavioral datasets.

---

# 6. Training Workflow

The training pipeline follows these steps:
Load Gold Dataset
↓
Feature Selection
↓
Train/Test Split
↓
Model Training
↓
Model Evaluation

The dataset is split into training and test subsets to evaluate model performance.

Example split:
80% training
20% testing

This allows unbiased evaluation of model generalization.

---

# 7. Experiment Tracking with MLflow

MLflow is used to track all model training experiments.

Each training run records:

- model parameters
- evaluation metrics
- trained model artifacts
- feature signatures

Example metrics logged include:

| Metric | Description |
|------|-------------|
| accuracy | classification accuracy |
| fraud_accuracy | fraud detection accuracy |

Experiment tracking enables reproducibility and comparison between model runs.

---

# 8. Model Signature

The model signature defines the expected input and output schema for the trained model.

Capturing the signature ensures that inference pipelines can validate inputs before scoring.

Example input features:
total_events
views
add_to_cart
purchases
avg_price
frequency
monetary_value
recency_days

This improves reliability of production inference pipelines.

---

# 9. Model Registry

After training, models are registered in the **MLflow Model Registry**.

Two models are maintained:

| Model | Purpose |
|------|--------|
| ecommerce_purchase_model | purchase likelihood prediction |
| ecommerce_fraud_model | fraud detection |

The registry enables:

- model versioning
- stage transitions
- production deployment management

---

# 10. Model Promotion

Models are promoted to the **Production stage** after evaluation.
MLflow Experiment
↓
Model Registry
↓
Production Stage

Inference pipelines always load the **Production version** of the model, ensuring stable predictions.

Example model reference: models:/ecommerce_purchase_model/Production

This eliminates the need to reference individual run IDs.

---

# 11. Model Explainability

To improve transparency and trust, model predictions are analyzed using **SHAP (SHapley Additive Explanations)**.

SHAP provides insights into which features contribute most to model predictions.

Example influential features include:

- purchase history
- session engagement
- customer recency
- interaction frequency

Explainability is critical for:

- model validation
- business interpretability
- responsible AI practices

---

# 12. Model Lifecycle

The ML pipeline supports the following lifecycle:

This eliminates the need to reference individual run IDs.

---

# 11. Model Explainability

To improve transparency and trust, model predictions are analyzed using **SHAP (SHapley Additive Explanations)**.

SHAP provides insights into which features contribute most to model predictions.

Example influential features include:

- purchase history
- session engagement
- customer recency
- interaction frequency

Explainability is critical for:

- model validation
- business interpretability
- responsible AI practices

---

# 12. Model Lifecycle

The ML pipeline supports the following lifecycle:
Training
↓
Experiment Tracking
↓
Model Registry
↓
Production Model
↓
Batch Inference

This lifecycle reflects modern MLOps practices used in production machine learning systems.

---

# 13. Summary

The machine learning pipeline enables predictive analytics within the ecommerce intelligence platform.

Key capabilities include:

- behavioral prediction using engineered features
- experiment tracking with MLflow
- model versioning and lifecycle management
- explainable machine learning

These components transform the Lakehouse data platform into a **complete data and AI system capable
of generating predictive insights from streaming behavioral data**.
