# Retail-Analysis
This repository presents an end-to-end data analysis project focused on simulating real-world business intelligence workflows. Using historical sales and returns data, the analysis identifies key performance drivers across regions, categories, and customer types, offering actionable insights for business decision-making.

# Data Cleaning and Preprocessing
Reading Data: Loaded Orders and Returns sheets using pandas.read_excel().

Initial Checks: Printed head(), info(), isnull().sum() and duplicate counts to assess data quality.

Duplicate Removal: Dropped duplicate Order IDs to ensure uniqueness of transactions.

Date Conversion: Converted Order Date and Ship Date columns to datetime format.

Numeric Conversion: Ensured columns like Quantity, Discount, Profit, and Sales are properly treated as numeric.

Profit Filter: Removed records with negative profits to focus on profitable sales data.

Merging Returns Data: Merged returns info with the main dataset using Order ID and filled missing values with "No".

Outlier Removal: Applied the IQR method to filter out outliers in the Profit column.

# Objectives
# Objective 1: Trend Analysis (Monthly & Yearly Profit Trends)
Purpose: Understand seasonal fluctuations and year-over-year performance.

Method: Extracted Year and Month from Order Date, grouped by them, and plotted using seaborn.lineplot.

Insights: Helps in identifying peak profit months and annual growth trends.

# Objective 2: Regional Performance (Average Profit per Order)
Purpose: Identify high and low-performing regions.

Method: Grouped by Region and calculated mean Profit, visualized using a barplot with annotations.

Insights: Highlights which regions are underperforming or excelling, aiding strategic focus.

# Objective 3: Returns Analysis by Category
Purpose: Assess which product categories face higher return rates.

Method: Created a Returned_flag using .apply(), grouped by Category, and plotted a pie chart.

Insights: Understanding return behavior helps in refining product quality and customer satisfaction strategies.

# Objective 4: Shipping Duration Analysis
Purpose: Evaluate delivery performance.

Method: Calculated Shipping Duration in days and visualized using histplot with KDE.

Insights: Identifies delivery time trends and potential delays affecting customer experience.

# Objective 5: Customer Segment Evaluation
Purpose: Analyze contribution of different customer types (Consumer, Corporate, Home Office) in terms of:

Sales

Quantity Ordered

Profit

Method: Grouped by Segment and plotted bar charts for each metric.

Insights: Useful for targeted marketing and understanding profitability per segment.

# Heatmap: Correlation Between Variables
Purpose: Visualize relationships between numerical features (Sales, Profit, Discount, etc.).

Method: Used sns.heatmap() with annot=True for clear correlation values.

Insights: Helps identify potential multicollinearity or key variables influencing performance.

# Final Output
The cleaned and processed dataset is exported to an Excel file (output_data.xlsx) for further use.
