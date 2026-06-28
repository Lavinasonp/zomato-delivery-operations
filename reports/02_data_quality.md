# Data Quality Report

## Missing Values
| Column                  | Missing Values |
| ----------------------- | -------------: |
| Delivery_person_Age     |           1854 |
| Delivery_person_Ratings |           1908 |
| Time_Orderd             |           1731 |
| Weather_conditions      |            616 |
| Road_traffic_density    |            601 |
| multiple_deliveries     |            993 |
| Festival                |            228 |
| City                    |           1200 |

## Data Quality Issues Identified
1. Delivery_person_Ratings contains value 6.0 (>5).
2. City contains typo "Metropolitian".
3. Missing values present in 8 columns.
4. No duplicate records found.
5. Delivery_person_Ratings contains 53 records with value 6.0, exceeding the expected rating scale (1–5).

## Rating Correction
Issue:
- 53 records contained Delivery_person_Ratings = 6.0
Action:
- Since ratings are expected on a 1–5 scale, values above 5 were capped at 5.
Reason:
- Preserve valid delivery records while correcting invalid rating values.

# Data Cleaning Summary
## Cleaning Activities Performed

## Missing Value Treatment

### Numerical Columns

| Column                  | Method |
| ----------------------- | ------ |
| Delivery_person_Age     | Median |
| Delivery_person_Ratings | Median |
| multiple_deliveries     | Median |

### Categorical Columns
| Column               | Method |
| -------------------- | ------ |
| Weather_conditions   | Mode   |
| Road_traffic_density | Mode   |
| Festival             | Mode   |
| City                 | Mode   |

### Data Quality Corrections

1. Corrected city typo:
   * Metropolitian → Metropolitan

2. Corrected invalid rating values:
   * Ratings above 5 were capped at 5

### Time Data Standardization
Issue:
* Time columns contained a mixture of standard time format and Excel serial time values.

Action:
* Converted Excel serial values into HH:MM format.

### Datetime Processing

Converted:
* Order_Date

Generated:
* Order_Day
* Order_Month
* Order_Weekday

### Feature Engineering

Created:
* Order_Hour
* Missing_Order_Time
* Delivery_Speed

### Final Outcome
The dataset was transformed into an analysis-ready format suitable for exploratory analysis and Power BI dashboard development.
