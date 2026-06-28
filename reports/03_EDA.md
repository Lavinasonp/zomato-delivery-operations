# EDA Section 1: Delivery Performance Analysis
## Key Findings
1. The average delivery time is 26.3 minutes, indicating efficient overall delivery operations.
2. The median delivery time is 26 minutes, which is very close to the average, suggesting the delivery time distribution is reasonably balanced without extreme skewness.
3. 75% of all deliveries are completed within 32 minutes, demonstrating strong operational consistency.
4. More than half of all deliveries (approximately 51%) fall into the Medium delivery category (21–35 minutes).
5. Fast deliveries account for approximately 31% of total orders, indicating a significant portion of deliveries are completed within 20 minutes.
6. Only about 18% of deliveries are classified as Slow, suggesting relatively good service performance across the network.
7. Delivery times range from 10 to 54 minutes, showing substantial variation likely influenced by traffic conditions, weather, city type, and delivery distance.

# EDA Section 2: Traffic Impact Analysis
## Key Findings
1. Traffic density has a significant impact on delivery performance.

2. Deliveries in Low traffic conditions are completed in approximately 21.5 minutes on average.

3. Deliveries in Jam conditions require approximately 31.2 minutes on average.

4. Delivery time increases by nearly 10 minutes when moving from Low traffic to Jam traffic conditions.

5. High and Medium traffic conditions show similar delivery performance, with average delivery times around 27 minutes.

6. Traffic congestion appears to be one of the strongest operational factors affecting delivery efficiency.

## Business Recommendations
* Increase delivery partner allocation during high congestion periods.
* Introduce dynamic delivery time estimates based on traffic density.
* Optimize routing strategies for heavily congested areas.
* Consider surge incentives for delivery personnel during traffic peak hours.

# EDA Section 3: Weather Impact Analysis
## Key Findings
1. Weather conditions significantly influence delivery performance.

2. Sunny weather produces the fastest deliveries, with an average delivery time of approximately 21.9 minutes.

3. Cloudy and Fog conditions are associated with the longest delivery times, averaging approximately 29 minutes.

4. Deliveries under Cloudy conditions take around 7 minutes longer than deliveries under Sunny conditions.

5. Windy, Stormy, and Sandstorm conditions show moderate delivery delays, with average delivery times between 25 and 26 minutes.

6. Adverse weather conditions can increase delivery times by more than 30% compared to favorable weather conditions.

## Business Recommendations
* Include weather-based delivery estimates in customer-facing applications.
* Increase delivery resource allocation during adverse weather conditions.
* Consider weather-aware route optimization strategies.
* Monitor delivery partner safety and efficiency during poor weather conditions.

# EDA Section 4: City Analysis
## Key Findings
1. Urban areas exhibit the fastest delivery performance with an average delivery time of approximately 23 minutes.

2. Metropolitan areas require approximately 27 minutes on average for order fulfillment.

3. Semi-Urban areas show significantly higher delivery times, averaging nearly 50 minutes.

4. The substantial increase in delivery time in Semi-Urban areas may be influenced by longer travel distances, limited delivery infrastructure, or a smaller sample size.

5. Metropolitan deliveries take approximately 18% longer than Urban deliveries.

## Business Recommendations
* Investigate delivery coverage and route efficiency in Semi-Urban regions.
* Evaluate whether longer travel distances contribute to delays.
* Consider additional delivery resources in high-demand Metropolitan zones.
* Implement location-based delivery time predictions.

### Limitation
- Semi-Urban observations represent only 164 records (0.36% of total deliveries). Therefore, conclusions regarding Semi-Urban delivery performance should be interpreted cautiously due to the limited sample size.

# EDA Section 5: Driver Rating Analysis
## Key Findings
1. Driver ratings show a moderate negative correlation (-0.33) with delivery time.

2. Higher-rated delivery partners consistently achieve faster delivery performance.

3. Drivers rated between 4.5 and 4.9 complete deliveries in approximately 24 minutes on average.

4. Drivers rated between 3.5 and 3.9 require approximately 37 minutes on average.

5. High-performing drivers complete deliveries nearly 13 minutes faster than lower-rated drivers.

6. The analysis suggests that delivery partner performance has a measurable impact on operational efficiency.

## Business Recommendations
* Prioritize retention of highly rated delivery partners.
* Develop training programs for lower-performing delivery personnel.
* Monitor delivery partner performance using rating and delivery-time KPIs.
* Consider incentive programs for consistently high-performing drivers.

## Limitation
- Very low rating groups contain relatively few observations and should be interpreted cautiously.

# EDA Section 6: Driver Age Analysis
## Key Findings
1. Driver age shows a moderate positive correlation (0.293) with delivery time.

2. Delivery partners aged between 20 and 29 complete deliveries in approximately 23 minutes on average.

3. Delivery partners aged between 30 and 39 require approximately 29–30 minutes on average.

4. Delivery time tends to increase as driver age increases.

5. Driver age appears to influence delivery efficiency, although the relationship is weaker than the impact of driver ratings.

## Business Recommendations
* Consider age-balanced delivery assignments.
* Focus on performance-based metrics rather than age alone.
* Use driver ratings and operational KPIs together when evaluating delivery performance.

## Limitation
* Age groups with very small sample sizes (e.g., 15 and 50 years) should be interpreted cautiously.

# EDA Section 7: Vehicle Type Analysis
## Key Findings
1. Electric scooters recorded the fastest average delivery time at approximately 24.5 minutes.

2. Traditional scooters showed nearly identical performance to electric scooters.

3. Bicycles required approximately 26.4 minutes on average.

4. Motorcycles recorded the highest average delivery time at approximately 27.6 minutes.

5. Vehicle type appears to influence delivery performance, although external factors such as route distance and traffic conditions may also contribute.

## Business Recommendations

* Continue evaluating electric scooter adoption for urban deliveries.
* Investigate delivery assignment patterns across vehicle categories.
* Consider vehicle-specific route optimization strategies.
* Analyze vehicle performance alongside distance and traffic conditions for deeper insights.

# EDA Conclusion

## Major Findings
### Traffic Impact
Traffic congestion is the strongest operational factor affecting delivery performance.
* Low Traffic: 21.46 minutes
* Jam Traffic: 31.18 minutes

### Weather Impact
Weather conditions significantly influence delivery efficiency.
* Sunny: 21.86 minutes
* Cloudy: 28.92 minutes

### City Impact
Urban areas achieve the fastest deliveries.
* Urban: 22.98 minutes
* Metropolitan: 27.14 minutes

### Driver Performance
Higher-rated delivery partners consistently complete deliveries faster.
Correlation:
* Driver Rating vs Delivery Time = -0.33

### Driver Age
Delivery time tends to increase moderately with age.
Correlation:
* Driver Age vs Delivery Time = +0.29

### Vehicle Performance
Electric scooters and scooters demonstrate the fastest delivery performance among available vehicle types.

## Business Recommendations
1. Improve routing during high traffic conditions.
2. Implement weather-aware delivery estimation.
3. Increase delivery capacity during peak congestion periods.
4. Monitor driver performance using ratings and delivery KPIs.
5. Expand efficient vehicle deployment strategies.

## Project Outcome
The analysis successfully identified the primary operational drivers affecting delivery performance and established a foundation for interactive dashboard development and decision-making support.




