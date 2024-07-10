import joblib
# Load the trained XGBoost model
loaded_model = joblib.load('D://Final Year Project//LOS//xgb_model.joblib')

# Function for making predictions with the loaded XGBoost model
def predict_with_xgb_model(input_data):
    # Make predictions
    predictions = loaded_model.predict(input_data)
    # Round predictions to whole numbers
    rounded_predictions = [round(pred) for pred in predictions]
    return rounded_predictions