import mlflow.pyfunc

def load_purchase_model():
    return mlflow.pyfunc.load_model(
        "models:/ecommerce_purchase_model/Production"
    )

def load_fraud_model():
    return mlflow.pyfunc.load_model(
        "models:/ecommerce_fraud_model/Production"
    )