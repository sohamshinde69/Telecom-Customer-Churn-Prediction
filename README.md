# Telecom-Customer-Churn-Prediction
A Machine Learning project that predicts whether a telecom customer is likely to churn (leave the service) or stay, based on customer demographics, subscription details, and billing behavior.
<br>
<h2>This project includes:</h2>
Exploratory Data Analysis (EDA)
<br>
Model Training & Comparison
<br>
Hyperparameter Tuning using GridSearchCV
<br>
Streamlit Web App Deployment
<br>
<br>
<h2>Project Objective</h2>
Customer churn is a major problem in telecom companies. Acquiring new customers costs more than retaining existing ones.
<br>
The objective of this project is to help telecom companies identify customers who are likely to leave, so preventive actions can be taken early.
<h2>Project Files</h2>
Customer _churn jupyter.ipynb --> Complete notebook with EDA + ML training
<br>
streamlit_app.py --> Streamlit app for churn prediction
<br>
model.pkl --> Trained Random Forest model
<br>
encoder.pkl --> ColumnTransformer and OneHotEncoder
<br>
label_encoder.pkl --> Target label encoder
<h2>Dataset Information</h2>
<h3>Dataset used: Telco Customer Churn Dataset</h3>
Contains customer details such as:
<br>
Gender
<br>
Senior Citizen
<br>
Partner / Dependents
<br>
Tenure
<br>
Phone Service
<br>
Internet Service
<br>
Online Security
<br>
Contract Type
<br>
Payment Method
<br>
Monthly Charges
<br>
Total Charges
<br>
Churn Status
<h2>Exploratory Data Analysis (Insights)</h2>
<br>
Overall Churn Rate
<br>
26.5% customers churned
<br>
73.5% customers stayed
<br>
Roughly 1 in 4 customers leave the company
<h2>Key Business Insights</h2>
Contract Type Matters Most
<br>
Month-to-month customers had highest churn
<br>
One-year contract customers stayed more
<br>
Two-year contract customers had strongest retention (~97%)
<h4> ➡️ Long-term contracts reduce churn significantly.</h4>

<h2>Payment Method Impact</h2>
Customers using Electronic Check showed higher churn compared to automatic payment methods.
<br>
➡️Auto-payment users are more stable customers.

<h2>Internet Service Type</h2>
Fiber Optic users churned more
<br>
DSL users stayed more
<br>
No internet service users had highest retention
<br>
<h4>➡️ Premium users may expect better service/support.</h4>

<h2>Senior Citizens Churn More</h2>
Senior citizens had lower retention compared to non-senior customers.
<br>
<h4>➡️ Better support plans can help retention.</h4>
<br>
<h2>Security & Support Services Reduce Churn</h2>
Customers with:
<br>
Online Security
<br>
Tech Support
<br>
Device Protection
<br>
Online Backup
<br>
were much more likely to stay.

<h4>➡️ Value-added services improve loyalty.</h4>

<H2>Data Preprocessing</H2>

<H3>Performed the following steps:</H3>

Removed customerID
<BR>
Converted TotalCharges to numeric
<BR>
Removed null values
<BR>
Split features & target
<BR>
Label encoded target variable
<BR>
OneHotEncoded categorical columns using ColumnTransformer

<h2>Models Trained</h2>

<h3>Compared multiple models:</h3>

Decision Tree Classifier
<br>
Random Forest Classifier ✅
<br>
K-Nearest Neighbors (KNN)
<br>
Used GridSearchCV for hyperparameter tuning.

<h2>Best Model</h2>
Random Forest Classifier
<br>
Achieved approximately:
<br>
79% Accuracy
<br>
Chosen because it gave the best performance.

<h2>Streamlit App Features</h2>
<h4>Users can input:</h4>

Customer details
<br>
Billing info
<br>
Services subscribed
<br>
Then app predicts:
<br>
✅ Customer Will Stay
<br>
❌ Customer Likely To Churn
<br>
Streamlit App link : https://telecom-customer-churn-predictio.streamlit.app/
<h2>Future Improvements</h2>
So according to the comfussion matrix this model ismodel is better at predicting “No churn” as its biased 
<br>
dataset is imbalanced:
<br>
No churn: 5163
<br>
Churn: 1869
<br>
Need to fix that in my next project 
