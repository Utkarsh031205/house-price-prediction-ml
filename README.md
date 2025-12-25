# 🏠 House Price Prediction using Machine Learning (CSV-Based)

This project demonstrates a **basic end-to-end Machine Learning workflow** using **Python**.  
House prices are predicted based on house area using **Linear Regression**, with data loaded from a CSV file.

This project is suitable for **beginners, college mini-projects, labs, viva, and GitHub portfolios**.

---

## 📌 Project Overview

- **Type:** Supervised Machine Learning  
- **Algorithm:** Linear Regression  
- **Input Feature:** House Area (in square feet)  
- **Output:** House Price  
- **Dataset Format:** CSV  

---

## 🛠 Technologies & Libraries Used

- Python 3  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  

---

## 📁 Project Structure

house-price-prediction/
├── house_prices.csv
├── house_price_prediction.py
└── README.md

---

## 📄 Dataset Description

The dataset is stored in `house_prices.csv`.

### Columns

- **area** – Area of the house in square feet  
- **price** – Price of the house  

### Sample Data

area,price  
2600,550000  
3000,565000  
3200,610000  
3600,680000  
4000,725000  

---

## ⚙️ How the Project Works

1. Load the dataset from a CSV file using Pandas  
2. Separate input features (X) and target output (y)  
3. Split the dataset into training and testing sets  
4. Train a Linear Regression model  
5. Predict house prices  
6. Evaluate the model using Mean Squared Error (MSE)  
7. Visualize actual data and regression line  
8. Predict price for a new house area  

---

## ▶️ How to Run the Project

1. Install dependencies:
pip install numpy pandas matplotlib scikit-learn

2. Run the script:
python house_price_prediction.py

---

## 📊 Output

- Dataset preview printed in terminal  
- Mean Squared Error (MSE)  
- Learned slope and intercept  
- Graph showing:
  - Actual house prices  
  - Regression line  
- Predicted price for a new house area  

---

## 🧠 Machine Learning Concepts Used

- Supervised Learning  
- Linear Regression  
- Train–Test Split  
- Model Training  
- Model Evaluation  
- Overfitting prevention  
- Data Visualization  

---

## 🎓 Viva / Exam Ready Summary

This project predicts house prices using Linear Regression by training a model on CSV-based data, evaluating it on unseen test data, and visualizing the results.

---

## 🚀 Possible Enhancements

- Add more input features  
- Use Multiple Linear Regression  
- Apply Cross-Validation  
- Add R² score  
- Use a real-world dataset  

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## 👤 Author

Utkarsh Vohra  
Computer Science Student  

