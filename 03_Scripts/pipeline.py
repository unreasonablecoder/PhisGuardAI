import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import joblib
import os

# 1. INGESTION (Component #1)
# Loading the file you just downloaded
raw_path = '../01_Raw_Data/phishing_raw.csv'
df = pd.read_csv(raw_path)

# 2. CLEANING & ELT (Component #3)
# Dropping the 'index' column if it exists (usually not needed for analysis)
if 'index' in df.columns:
    df = df.drop(columns=['index'])

# Renaming columns for better readability in Power BI
df.columns = [col.replace('_', ' ').title() for col in df.columns]

# 3. DATA MODELING - STAR SCHEMA (Component #4)
# We will create a Dimension table for 'Result' (Legitimate vs Phishing)
dim_result = pd.DataFrame({
    'Result_ID': [1, -1],
    'Security_Status': ['Legitimate', 'Phishing'],
    'Risk_Level': ['Low', 'High']
})

# The Fact Table contains all the technical details (measurements)
# We ensure the 'Result' column matches our Result_ID
fact_scans = df.copy()
fact_scans = fact_scans.rename(columns={'Result': 'Result_ID'})

# 4. STORAGE (Component #2)
# Saving these into our 'Processed' folder as our "Data Warehouse"
output_folder = '../02_Processed_Data/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

dim_result.to_csv(f'{output_folder}Dim_Result.csv', index=False)
fact_scans.to_csv(f'{output_folder}Fact_Scans.csv', index=False)

print("✅ Pipeline Complete: Fact and Dimension tables generated in 02_Processed_Data")


# 5. THE AI/ML COMPONENT
print("🤖 Starting Machine Learning Training...")

# Selecting features for the AI to learn from
# We exclude 'Result_ID' because that's what we want to predict
X = fact_scans.drop(columns=['Result_ID']) 
y = fact_scans['Result_ID']

# Split data: 80% for training, 20% for testing the AI
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Calculate Accuracy for your PPT
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ AI Model Trained. Accuracy: {accuracy * 100:.2f}%")


# 6. EVALUATION - Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("--- Confusion Matrix ---")
print(f"Correctly caught Phishing: {cm[0][0]}")
print(f"Correctly identified Safe: {cm[1][1]}")
print(f"Mistakes (False Alarms): {cm[0][1] + cm[1][0]}")

# 7. SAVE THE MODEL (Optional: To show the HoD you can 'Deploy' it)
joblib.dump(model, '../02_Processed_Data/phishing_model.pkl')