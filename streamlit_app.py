# This Streamlit application predicts whether a telecom customer is likely to churn
# (leave the service) or stay , based on customer details.
# The prediction is made using a trained Random Forest Classifier
# with approximately 79 % accuracy .

## Import Required Libraries

import streamlit as st # for building the web app
import pandas as pd # for data handling 
import pickle # for loading trained model files

# Load saved files

ct = pickle.load(open("encoder.pkl", "rb")) 
model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))


# App title and description
st.title("Telecom Customer Churn Prediction")
st.write("Please write the details of the customer to predict whether the customer will churn or not .")

input_data = {
    "gender" : "Female" ,
    "SeniorCitizen" : 0 ,
    "Partner" : "Yes" ,
    "Dependents" : "No" , 
    "tenure" : 1 ,
    "PhoneService" : "No" ,
    "MultipleLines" : "No phone service" ,
    "InternetService" : "DSL" ,
    "OnlineSecurity" : "No" ,
    "OnlineBackup" : "Yes" ,
    "DeviceProtection" : "No" ,
    "TechSupport" : "No" ,
    "StreamingTV" : "No" ,
    "StreamingMovies" : "No" ,
    "Contract" : "Month-to-month" ,
    "PaperlessBilling" : "Yes" ,
    "PaymentMethod" : "Electronic check" ,
    "MonthlyCharges" : 29.85 ,
    "TotalCharges" : 29.85
}

# User Input Section

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 1)
phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check",
    "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly = st.number_input("Monthly Charges", 0.0)
total = st.number_input("Total Charges", 0.0)

#was going to keep the total as the following but the total changes as the discount is applied so now enter manually 
#total = monthly * tenure
#st.write(f"Total Charges (auto-calculated): {total:.2f}")


input_data = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "MultipleLines": multiple,
    "InternetService": internet,
    "OnlineSecurity": security,
    "OnlineBackup": backup,
    "DeviceProtection": device,
    "TechSupport": tech,
    "StreamingTV": tv,
    "StreamingMovies": movies,
    "Contract": contract,
    "PaperlessBilling": paperless,
    "PaymentMethod": payment,
    "MonthlyCharges": monthly,
    "TotalCharges": total
}

# Display Prediction Result

if st.button("Predict Churn"):
    input_df = pd.DataFrame([input_data])
    input_encoded = ct.transform(input_df)
    prediction_encoded = model.predict(input_encoded)
    prediction = le.inverse_transform(prediction_encoded)

    st.subheader("Prediction Result:")
    if prediction[0] == "Yes":
        st.error("The Customer Is Likely To Churn .")
        
    else:
        st.success("The Customer Is Likely To Stay .")

# Model Information

st.info("This prediction is based on trained Random Forest Model with ~79 % accuracy .")