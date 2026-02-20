# 📦 Supply Chain Demand Forecasting Project

### 📌 Project Overview

This project focuses on **Supply Chain Analytics and Demand Forecasting** using Data Analysis, SQL, Machine Learning, and Streamlit.

The objective is to predict the **future number of products sold** (demand) based on supply chain factors such as price, stock levels, lead time, manufacturing cost, and logistics data.

The project includes:

- Exploratory Data Analysis (EDA)

- SQL-based business insights

- Machine Learning model comparison

- Interactive Streamlit dashboard

### 🎯 Business Problem

In supply chain management, poor demand estimation can lead to:

- Overstocking

- Stock-outs

- Increased logistics cost

- Inefficient production planning

This project aims to:

✔ Analyze supply chain data

✔ Identify key influencing factors

✔ Build predictive models for demand forecasting

✔ Provide business insights for inventory optimization

### 📊 Dataset Description

The dataset contains supply chain information from a fashion & beauty startup.

**Key Features**:

- Product type

- Price

- Stock levels

- Lead times

- Order quantities

- Revenue generated

- Shipping costs

- Supplier details

- Manufacturing costs

- Defect rates

- Location

**Target Variable:**

**Number of products sold**

### 🛠 Project Workflow
#### 1️⃣ Data Preparation

- Loaded dataset

- Checked missing values and duplicates

- Performed basic cleaning

#### 2️⃣ Exploratory Data Analysis (EDA)

- Key visualizations:

- Revenue by product type

- Stock levels vs sales

- Shipping cost distribution

- Lead time comparison

- Manufacturing cost analysis

#### 3️⃣ SQL Analysis (DuckDB)

- Performed business-level analysis:

- Revenue by product

- Inventory risk detection

- Supplier efficiency analysis

- Logistics performance insights

#### 4️⃣ Feature Engineering

- One-hot encoding for categorical features

- Feature scaling using StandardScaler

- Train-test split (80-20)

#### 5️⃣ Machine Learning Models

Three models were compared:

| Model                     | MAE        |
| ------------------------- | ---------- |
| Baseline (Mean Predictor) | **277.45** |
| Neural Network            | 464.38     |
| Random Forest             | 358.19     |


### 📈 Model Performance Analysis

- The baseline model (predicting mean sales) achieved the lowest MAE.

- Neural Network and Random Forest did not outperform the baseline.

- This indicates that the current dataset has limited predictive signal for demand forecasting.

**Key Insight:**

The performance suggests that additional features such as:

- Seasonal trends

- Promotion intensity

- Time-based variables

may be required to improve forecasting accuracy.

### 📊 Evaluation Metrics

- Mean Squared Error (MSE)

- Mean Absolute Error (MAE)

- R² Score

- Actual vs Predicted scatter plot

### 🖥 Streamlit Dashboard

An interactive dashboard was built using Streamlit that includes:

- Key Performance Indicators (KPIs)

- Revenue & sales visualization

- Inventory analysis

- Supplier & logistics insights

- Demand prediction interface


### ▶️ How to Run the Project

#### 1️⃣ Install Dependencies

pip install -r requirements.txt

#### 2️⃣ Run Streamlit Dashboard

python -m streamlit run app.py

Open in browser:

http://localhost:8501

### 🧠 Key Learnings

- End-to-end ML workflow implementation

- Importance of baseline comparison

- Model benchmarking and performance evaluation

- Realistic understanding of predictive limitations

- Dashboard deployment using Streamlit

### 🚀 Future Improvements

- Add time-series features (Month, Seasonality)

- Hyperparameter tuning

- Try Gradient Boosting models

- Deploy publicly using Streamlit Cloud

- Integrate real-time supply chain data

### 👤 Author

**Bibek Kumar Majhi**

Data Analytics & Machine Learning Enthusiast


