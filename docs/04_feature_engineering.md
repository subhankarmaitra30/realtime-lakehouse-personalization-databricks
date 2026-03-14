# Feature Engineering

## Behavioral and Customer Intelligence Features

---

# 1. Overview

Feature engineering plays a critical role in transforming raw event data into meaningful
signals that machine learning models can use for prediction.

In this project, the feature engineering pipeline converts raw clickstream events into 
structured behavioral, product, and customer-value features.

These features capture multiple dimensions of user behavior, including:

- interaction intensity
- purchasing patterns
- customer recency and frequency
- product demand signals

The resulting feature sets provide the foundation for training machine learning models
that predict purchase likelihood and detect suspicious activity.

---

# 2. Feature Engineering Architecture

Feature engineering is implemented within the **Silver layer of the Medallion architecture**.
Raw Events (Bronze)
↓
Clean Events (Silver)
↓
Sessionized Events
↓
Feature Engineering
↓
Feature Tables


The engineered feature tables are later combined to produce the Gold-layer machine learning dataset.

---

# 3. Sessionization

User behavior is naturally organized into browsing sessions.

A session represents a sequence of user interactions separated by inactivity periods.

This system reconstructs sessions using a **30-minute inactivity threshold**.

If the time gap between two events exceeds 30 minutes, a new session begins.
User Event Timeline
↓
Time Gap Detection
↓
Session Boundary Creation

Sessionization allows the system to capture meaningful interaction patterns such as:

- browsing intensity
- purchase behavior within sessions
- session duration

These signals are essential for modeling user intent.

---

# 4. Behavioral Features

Behavioral features summarize user interactions within each session.

These features quantify how users interact with products during their browsing activity.

Example features include:

| Feature | Description |
|-------|-------------|
| total_events | total interactions within a session |
| views | number of product views |
| add_to_cart | number of cart additions |
| purchases | number of completed purchases |
| avg_price | average price of products interacted with |

These features capture **user engagement intensity** and provide strong predictive signals 
for purchase likelihood.

---

# 5. Product Popularity Features

Ecommerce systems often rely on product demand signals to support recommendation systems.

This project computes product popularity using time-window aggregations.

Example features include:

| Feature | Description |
|-------|-------------|
| events_last_hour | number of interactions for a product within the last hour |
| events_last_day | number of interactions within the last day |

These metrics capture **short-term demand trends**, allowing the system to identify trending products.

Popularity signals are widely used in recommendation systems and merchandising analytics.

---

# 6. Customer Value Features (RFM)

Customer value is modeled using the **Recency-Frequency-Monetary (RFM) framework**, a widely
used technique in ecommerce analytics.

RFM features measure the strength of customer relationships.

| Feature | Description |
|-------|-------------|
| recency_days | number of days since last interaction |
| frequency | total number of user interactions |
| monetary_value | cumulative purchase value |

### Recency

Measures how recently a user interacted with the platform.

More recent interactions typically indicate higher engagement.

### Frequency

Measures how often a user interacts with the platform.

Frequent interactions suggest strong user interest.

### Monetary Value

Measures the economic value of the user's purchases.

Higher purchase value may indicate more valuable customers.

Together, these features capture **customer lifetime value signals**.

---

# 7. Feature Table Design

The feature engineering stage produces several Silver-layer feature tables.

| Table | Description |
|------|-------------|
| silver_user_behavior_features | session-level interaction features |
| silver_product_popularity_features | product demand signals |
| silver_user_rfm_features | customer value metrics |

These tables represent different perspectives of user behavior.

---

# 8. Feature Integration

The Gold layer combines all engineered features into a unified dataset used for machine learning.
Behavioral Features
+
Product Popularity Features
+
RFM Features
↓
Gold ML Training Dataset

This dataset contains the final feature set used by machine learning models.

---

# 9. Feature Importance

Feature importance analysis using SHAP indicates that the following features often contribute
strongly to predictions:

- purchase history
- interaction frequency
- recency of activity
- session engagement metrics

These results confirm that the engineered features effectively capture user behavior patterns.

---

# 10. Design Considerations

Several design principles guided the feature engineering process.

### Interpretability

Features were designed to remain interpretable and meaningful for business users.

### Scalability

Feature computations are implemented using distributed Spark operations.

### Reusability

Feature tables are stored independently so they can be reused by multiple analytical and 
machine learning workflows.

---

# 11. Summary

Feature engineering transforms raw clickstream events into meaningful behavioral signals.

Key feature groups include:

- session-level interaction features
- product demand signals
- customer value metrics

Together, these features enable machine learning models to understand user behavior 
and generate accurate predictions.

The feature engineering framework provides a scalable foundation for building predictive
ecommerce analytics systems.
