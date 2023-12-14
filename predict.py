import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Retrieve data from SQLite database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT age, cholesterol, systolic_pressure, diastolic_pressure FROM health_table_tbl")
data = cursor.fetchall()
connection.close()

# Organize data into features and labels for systolic pressure
features_systolic = [(age, cholesterol) for age, cholesterol, _, _ in data]
labels_systolic = [systolic for _, _, systolic, _ in data]

# Organize data into features and labels for diastolic pressure
features_diastolic = [(age, cholesterol) for age, cholesterol, _, _ in data]
labels_diastolic = [diastolic for _, _, _, diastolic in data]

# Split data into training and testing sets for systolic pressure
X_train_systolic, X_test_systolic, y_train_systolic, y_test_systolic = train_test_split(
    features_systolic, labels_systolic, test_size=0.2, random_state=42
)

# Split data into training and testing sets for diastolic pressure
X_train_diastolic, X_test_diastolic, y_train_diastolic, y_test_diastolic = train_test_split(
    features_diastolic, labels_diastolic, test_size=0.2, random_state=42
)

# Feature Scaling for systolic pressure
scaler_systolic = StandardScaler()
X_train_scaled_systolic = scaler_systolic.fit_transform(X_train_systolic)
X_test_scaled_systolic = scaler_systolic.transform(X_test_systolic)

# Feature Scaling for diastolic pressure
scaler_diastolic = StandardScaler()
X_train_scaled_diastolic = scaler_diastolic.fit_transform(X_train_diastolic)
X_test_scaled_diastolic = scaler_diastolic.transform(X_test_diastolic)

# Model Selection and Training for systolic pressure (Linear Regression example)
model_systolic = LinearRegression()
model_systolic.fit(X_train_scaled_systolic, y_train_systolic)

# Model Selection and Training for diastolic pressure (Linear Regression example)
model_diastolic = LinearRegression()
model_diastolic.fit(X_train_scaled_diastolic, y_train_diastolic)

# Model Evaluation for systolic pressure
y_pred_systolic = model_systolic.predict(X_test_scaled_systolic)
mse_systolic = mean_squared_error(y_test_systolic, y_pred_systolic)
print("Mean Squared Error for Systolic Pressure:", mse_systolic)

# Model Evaluation for diastolic pressure
y_pred_diastolic = model_diastolic.predict(X_test_scaled_diastolic)
mse_diastolic = mean_squared_error(y_test_diastolic, y_pred_diastolic)
print("Mean Squared Error for Diastolic Pressure:", mse_diastolic)

# Prediction for new data
# Assuming you have new data
new_age = 40
new_cholesterol = 200

# Creating a new data point with the provided values
new_data_point = [(new_age, new_cholesterol)]

# Scaling the new data point using the previously fitted scaler for systolic pressure
new_data_point_scaled_systolic = scaler_systolic.transform(new_data_point)

# Scaling the new data point using the previously fitted scaler for diastolic pressure
new_data_point_scaled_diastolic = scaler_diastolic.transform(new_data_point)

# Making predictions using the trained models
predicted_systolic_pressure = model_systolic.predict(new_data_point_scaled_systolic)
predicted_diastolic_pressure = model_diastolic.predict(new_data_point_scaled_diastolic)

# Printing the predicted systolic and diastolic pressures
print("Predicted Systolic Pressure:", predicted_systolic_pressure)
print("Predicted Diastolic Pressure:", predicted_diastolic_pressure)
