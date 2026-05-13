# 📈 Stock Price Prediction Web Application

 Link:https://stocks-price-prediction-project.streamlit.app/

An interactive Machine Learning based web application developed using **Python**, **Scikit-Learn**, and **Streamlit** to predict stock closing prices using historical stock market data. The application performs data preprocessing, visualization, predictive analysis, and provides users with a simple interface for forecasting stock prices.

---

# 🚀 Project Overview

The Stock Price Prediction System is designed to analyze historical stock market data and predict the closing price of stocks using Machine Learning algorithms. This project demonstrates the complete Machine Learning workflow including:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Prediction
- Model Evaluation
- Web Application Deployment

The project is converted into an interactive web application using Streamlit where users can input stock-related values and receive predicted closing prices instantly.

---

# 🎯 Objectives

- Analyze historical stock market data
- Predict stock closing prices using Machine Learning
- Build an interactive web application using Streamlit
- Visualize stock price trends
- Understand real-world Machine Learning workflow

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| Joblib | Model Saving & Loading |

---

# 📂 Project Structure

```bash
StockPrediction/
│
├── app.py                  # Streamlit Web Application
├── stock_model.pkl         # Trained Machine Learning Model
├── stock_data.csv          # Dataset
├── requirements.txt        # Required Libraries
├── README.md               # Project Documentation
```

---

# 📊 Dataset Information

The dataset contains historical stock market information including:

- Open Price
- High Price
- Low Price
- Closing Price
- Trading Volume
- Date
- Stock Name

The project uses historical market patterns to train a prediction model.

---

# ⚙️ Machine Learning Workflow

## 1️⃣ Data Collection
Historical stock market dataset is loaded using Pandas.

## 2️⃣ Data Preprocessing
- Handling missing values
- Selecting useful features
- Converting data types
- Filtering stock-specific data

## 3️⃣ Exploratory Data Analysis (EDA)
Visualizing stock closing prices and understanding market trends using graphs.

## 4️⃣ Feature Selection
Input Features:
- Open Price
- High Price
- Low Price
- Volume

Target:
- Closing Price

## 5️⃣ Model Training
A Linear Regression model is trained using Scikit-Learn.

## 6️⃣ Model Evaluation
Performance is evaluated using:
- RMSE (Root Mean Squared Error)
- R² Score

## 7️⃣ Prediction
The trained model predicts stock closing prices based on user inputs.

---

# 🌐 Streamlit Web Application Features

✅ Interactive User Interface  
✅ Real-Time Prediction  
✅ Stock Price Visualization  
✅ Dataset Preview  
✅ Simple and Clean Design  
✅ Fast Prediction System  

---

# 💻 Installation & Setup

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/stock-price-prediction.git
```

---

## Step 2: Navigate to Project Folder

```bash
cd stock-price-prediction
```

---

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📈 How the Prediction Works

The user enters:
- Open Price
- High Price
- Low Price
- Trading Volume

The Machine Learning model analyzes the input values and predicts the estimated closing stock price.

---

# 📉 Model Used

## Linear Regression

The project currently uses a Linear Regression algorithm to predict stock prices based on historical numerical patterns.

Linear Regression Formula:

```math
y = mx + b
```

Where:
- y = Predicted Output
- x = Input Features
- m = Slope
- b = Intercept

---

# 📸 Application Preview

The application includes:

- Prediction Interface
- Stock Trend Graph
- Dataset Table
- Interactive Inputs

---

# 📌 Key Features

- End-to-End Machine Learning Project
- User-Friendly Interface
- Historical Data Analysis
- Predictive Analytics
- Model Deployment using Streamlit
- Beginner-Friendly Project Structure

---

# 🚀 Future Improvements

The project can be further enhanced by adding:

- LSTM Deep Learning Model
- Real-Time Stock API Integration
- Candlestick Charts
- Multiple Stock Selection
- Buy/Sell Recommendation System
- Advanced Data Visualization
- Deployment on Cloud Platforms

---

# 📚 Learning Outcomes

Through this project, the following concepts were learned:

- Machine Learning Workflow
- Data Preprocessing
- Feature Engineering
- Regression Models
- Data Visualization
- Streamlit Deployment
- Model Serialization using Joblib

---

# ⚠️ Disclaimer

This project is developed for educational and learning purposes only. Stock market prices are influenced by multiple real-world factors such as economic conditions, global events, company performance, and market sentiment. Therefore, predictions generated by this application may not always reflect actual market behavior.

---

# 👨‍💻 Author
### Vansh Agarwal
B.Tech CSE Student | Data Science & Machine Learning Enthusiast

---

# ⭐ Conclusion

The Stock Price Prediction Web Application demonstrates the practical implementation of Machine Learning concepts in finance-related prediction systems. The project combines data analysis, predictive modeling, and web deployment into a complete end-to-end Machine Learning solution.

---
