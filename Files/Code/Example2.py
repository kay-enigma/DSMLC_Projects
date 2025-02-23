import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# File paths to the datasets
billing_path = "Files/Data/billing_cleaned.xlsx"  # Replace with the correct file path
employees_path = "Files/Data/employees_cleaned.xlsx"  # Replace with the correct file path

# Step 1: Load the datasets
billing = pd.read_excel(billing_path)
employees = pd.read_excel(employees_path)

# Step 2: Merge 'rate' column from employees into billing
billing = pd.merge(billing, employees[['employee_id', 'rate']], on='employee_id', how='left')

# Step 3: Handle missing values
billing['rate'] = billing['rate'].fillna(billing['rate'].mean())  # Replace missing rates with the mean
billing['revenue'] = billing['hours'] * billing['rate']  # Calculate revenue

# Step 4: Prepare features and target
X = billing[['rate', 'hours']]  # Features: employee rate and hours worked
y = billing['revenue']  # Target: total revenue generated by each employee

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model
print("\nRegression Evaluation:")
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R-squared (R²):", r2_score(y_test, y_pred))

# Step 9: Visualize the relationship between 'hours' and 'revenue'
plt.figure(figsize=(6, 4))
plt.scatter(X_test['hours'], y_test, color='blue', label='Actual Revenue')
plt.scatter(X_test['hours'], y_pred, color='red', label='Predicted Revenue')
plt.xlabel('Hours Worked')
plt.ylabel('Revenue')
plt.title('Actual vs Predicted Revenue')
plt.legend()
plt.show()