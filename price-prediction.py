import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# load dataset from CSV file

df = pd.read_csv("homeprices.csv")

print("Dataset loaded from CSV:")
print(df)



# separate features and target
X = df[['area']]  
y = df['price']

# split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# make predictions on test data
y_pred = model.predict(X_test)


# evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)



# display model parameters
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)



# visualize actual data and regression line

plt.scatter(X, y, label="Actual Prices")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price (₹ lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()


# predict price for a new house size
new_size = np.array([[1400]])
predicted_price = model.predict(new_size)

print(f"Predicted price for 1400 sqft house: ₹{predicted_price[0]:.2f} lakhs")
