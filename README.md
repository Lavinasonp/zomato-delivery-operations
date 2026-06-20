<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Zomato_Logo.svg" alt="Zomato Logo" width="300"/>
</div>

<br/>

# Zomato Delivery Operations Analytics

## Overview
Analyze delivery operations performance and identify key factors affecting delivery efficiency and customer service performance in the food delivery ecosystem.

## Dataset Used
The dataset used in this project is sourced from Kaggle:
**[Zomato Delivery Operations Analytics Dataset](https://www.kaggle.com/datasets/saurabhbadole/zomato-delivery-operations-analytics-dataset/data)**

### Dataset Details
* **Records**: 45,584
* **Features**: 20
* **Data Points**: Delivery partner age and ratings, order types, delivery duration, multiple deliveries, weather conditions, traffic density, city categories, vehicle types, and geographic coordinates.

## Tools & Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-E23744?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Interactive Dashboard
We built a premium, interactive Streamlit dashboard tailored with Zomato's branding. It allows business stakeholders to filter data globally by City, Weather, Traffic, and Vehicle Type.

### Key Performance Indicators (KPIs)
* Total Orders
* Average Delivery Time
* Average Driver Rating
* Fast Delivery Percentage

### Dashboard Pages
1. **Executive Overview**: Visualizes delivery speed distribution, and the impact of traffic and weather conditions on delivery times.
2. **Operations Analysis**: Compares vehicle type efficiency, hourly order volumes, and the impact of batching multiple deliveries.
3. **Driver Performance**: Explores the correlation between a driver's age, customer ratings, and their delivery speed.
4. **Key Business Insights**: Provides actionable, India-specific recommendations from a Senior Data Analyst perspective.

## Key Business Questions Addressed
1. What factors increase delivery time?
2. How much does traffic affect delivery performance?
3. How does weather influence operations?
4. Which vehicle type performs best?
5. Do highly rated drivers deliver faster?
6. Which city type experiences the most delays?

## Data Preparation Highlights
* Handled missing values across eight columns.
* Standardized datetime fields and inconsistent city naming conventions.
* **Feature Engineering**: Calculated the Haversine geographic distance between restaurant and delivery coordinates to provide deeper insights into delivery delays.

## How to Run the Dashboard Locally
Ensure you have the virtual environment activated and dependencies installed:

```bash
pip install -r requirements.txt
streamlit run app.py
```
