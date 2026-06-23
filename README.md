# 🚚 Zomato Delivery Operations Analytics

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Zomato_Logo.svg" alt="Zomato Logo" width="300"/>
</div>

---

## 📌 Project Overview

Food delivery platforms operate in highly dynamic environments where factors such as traffic congestion, weather conditions, delivery partner performance, vehicle type, and order demand can significantly impact delivery efficiency.

This project performs an end-to-end analysis of Zomato delivery operations using Python, Power BI, and Streamlit to uncover operational bottlenecks, evaluate driver performance, and generate actionable business insights.

The solution includes:

* Data Cleaning & Preprocessing
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Interactive Power BI Dashboard
* Streamlit Web Application
* Business Recommendations

---

## 🎯 Business Problem

How can Zomato improve delivery efficiency and customer experience by understanding the impact of:

* Traffic Density
* Weather Conditions
* Vehicle Type
* Driver Ratings
* Driver Age
* Multiple Deliveries
* City Categories
* Order Demand Patterns

on delivery performance?

---

## 📊 Dataset Information

### Source

Kaggle Dataset:
Zomato Delivery Operations Analytics Dataset

### Dataset Summary

| Metric            | Value                    |
| ----------------- | ------------------------ |
| Records           | 45,584                   |
| Original Features | 20                       |
| Final Features    | 28+                      |
| Domain            | Food Delivery Operations |

### Key Variables

* Delivery Partner Age
* Delivery Partner Rating
* Vehicle Type
* Weather Conditions
* Traffic Density
* Festival Status
* City Category
* Multiple Deliveries
* Delivery Time

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-E23744?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white)

---

## 🧹 Data Cleaning & Preparation

The dataset underwent extensive preprocessing before analysis.

### Data Quality Improvements

* Handled missing values across multiple columns
* Standardized city names and categorical values
* Corrected invalid delivery partner ratings
* Standardized mixed-format time columns
* Converted date and time fields to proper formats
* Preserved missing order timestamps using dedicated flags

### Missing Value Treatment

| Column                  | Treatment |
| ----------------------- | --------- |
| Delivery_person_Age     | Median    |
| Delivery_person_Ratings | Median    |
| multiple_deliveries     | Median    |
| Weather_conditions      | Mode      |
| Road_traffic_density    | Mode      |
| Festival                | Mode      |
| City                    | Mode      |

---

## ⚙️ Feature Engineering

Created business-focused features to enhance operational analysis.

### Engineered Features

* Order_Day
* Order_Month
* Order_Weekday
* Order_Hour
* Delivery_Speed
* Missing_Order_Time

### Delivery Speed Categories

* Fast (0–20 mins)
* Medium (21–35 mins)
* Slow (36+ mins)

### Geographic Analysis

Implemented Haversine Distance calculation using restaurant and delivery coordinates to support delivery distance analysis.

---

## 📈 Exploratory Data Analysis

Key analyses performed:

* Traffic Density vs Delivery Time
* Weather Impact Analysis
* Vehicle Performance Analysis
* Driver Rating Analysis
* Driver Age Analysis
* Multiple Deliveries Impact
* City Performance Analysis
* Delivery Speed Distribution
* Peak Order Hour Analysis

---

## 🔍 Key Insights

### Traffic Impact

* Jam traffic conditions produce the longest delivery times.
* Low traffic conditions consistently achieve the fastest deliveries.

### Weather Impact

* Cloudy and foggy weather significantly increase delivery delays.
* Sunny weather results in the fastest deliveries.

### Vehicle Performance

* Electric scooters achieve the lowest average delivery time.
* Motorcycles show the highest average delivery duration.

### Driver Performance

* Higher-rated drivers consistently deliver faster.
* Driver ratings show a moderate negative correlation with delivery time.

### Operational Findings

* Multiple deliveries significantly increase delivery duration.
* Metropolitan regions account for the majority of delivery volume.
* Most deliveries fall into the Medium delivery speed category.

---

# 📊 Power BI Dashboard

A premium Zomato-themed interactive dashboard was developed using Power BI.

### Page 1: Executive Overview

Features:

* Total Orders
* Average Delivery Time
* Average Driver Rating
* Fast Delivery Percentage
* Traffic Impact Analysis
* Weather Impact Analysis
* Delivery Speed Distribution
* City Performance Summary

### Page 2: Operations Analysis

Features:

* Peak Order Hours Analysis
* Orders by Weekday
* Vehicle Performance Analysis
* Multiple Deliveries Impact
* Festival Impact Analysis
* Operational Insights

### Page 3: Driver Performance Analysis

Features:

* Driver Rating Distribution
* Driver Age Distribution
* Driver Rating vs Delivery Time
* Driver Age vs Delivery Efficiency
* Vehicle Performance Analysis
* Driver Insights

---

## 📸 Dashboard Screenshots

### Executive Overview

[Insert Screenshot]

### Operations Analysis

[Insert Screenshot]

### Driver Performance Analysis

[Insert Screenshot]

---

# 🌐 Streamlit Application

An interactive Streamlit application was built to enable dynamic exploration of delivery operations data.

### Features

* Interactive Filters
* KPI Monitoring
* Operational Analytics
* Driver Performance Analysis
* Business Insights
* Responsive User Interface

### Live Application

🔗 **https://zomatodelivery.streamlit.app/**

---

## 💡 Business Recommendations

### Traffic Optimization

Implement dynamic routing algorithms to reduce delays caused by traffic congestion.

### Driver Development

Introduce performance improvement programs for lower-rated delivery partners.

### Fleet Optimization

Expand electric scooter adoption in high-demand urban regions.

### Smart Delivery Allocation

Reduce excessive delivery batching during peak demand periods.

### Demand Forecasting

Increase delivery partner availability during peak ordering hours.

---

## 📂 Project Structure

```text
Zomato-Delivery-Operations-Analytics

├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   └── 03_Feature_Engineering.ipynb
│
├── dashboard
│   └── Zomato_Delivery_Analytics.pbix
│
├── images
│   ├── page1.png
│   ├── page2.png
│   └── page3.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

