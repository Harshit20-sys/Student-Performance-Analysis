# 📊 Student Performance Analysis

A complete End-to-End Data Analyst project developed using **PostgreSQL, SQL, Python, Advanced Excel, and Power BI**. This project analyzes student academic performance, identifies factors affecting scores, detects at-risk students, and presents insights through interactive dashboards.

---

# 📌 Project Objective

The objective of this project is to analyze student performance data and answer important academic questions such as:

- Does parental education affect student performance?
- Does completing a test preparation course improve scores?
- How do male and female students perform?
- Which students are academically at risk?
- How can school management use data for better academic decisions?

---

# 🛠 Tech Stack

- PostgreSQL
- Advanced SQL
- Python
- Pandas
- Matplotlib
- Advanced Excel
- Power BI
- VS Code
- pgAdmin

---

# 📂 Project Structure

```
Student Performance Analysis
│
├── 01_data
│   └── StudentsPerformance.xlsx
│
├── 02_sql
│   ├── 01_create_table.sql
│   ├── 02_data_exploration.sql
│   ├── 03_factor_analysis.sql
│   └── 04_at_risk_analysis.sql
│
├── 03_python
│   ├── 01_database_connection.py
│   └── 02_visualization.py
│
├── 04_excel
│   └── Student_Performance_Dashboard.xlsx
│
├── 05_powerbi
│   └── Student_Performance_Dashboard.pbix
│
├── 06_reports
│   └── Principal_Report.docx
│
├── 07_images
│   ├── Excel_Dashboard.png
│   ├── PowerBI_Dashboard.png
│   ├── chart1_gender_performance.png
│   ├── chart2_test_preparation.png
│   ├── chart3_parental_education_boxplot.png
│   ├── chart4_total_score_distribution.png
│   ├── chart5_math_vs_reading.png
│   └── chart6_correlation_heatmap.png
│
└── README.md
```

---

# 📁 Dataset Information

The dataset contains **1000 student records**.

Features include:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

---

# 🗄 Database Design

Database

```
student_performance_analysis
```

Table

```
student_performance
```

---

# SQL Analysis

The project includes SQL analysis for:

- Data Exploration
- Missing Value Check
- Data Type Verification
- Unique Value Analysis
- Factor Analysis
- Gender Performance
- Test Preparation Analysis
- Parental Education Analysis
- At-Risk Student Identification

---

# Python Analysis

Python was used for:

- PostgreSQL Database Connection
- Data Retrieval
- Data Processing
- Visualization
- Statistical Charts

Libraries Used

- pandas
- matplotlib
- psycopg2

---

# Visualizations

The following visualizations were created:

- Grouped Bar Chart
- Bar Chart
- Box Plot
- Histogram
- Scatter Plot
- Correlation Heatmap

---

# Advanced Excel Dashboard

The Excel dashboard includes:

- Total Students KPI
- Average Math Score
- Average Reading Score
- Average Writing Score
- Gender Performance
- Test Preparation Analysis
- Parental Education Analysis
- Interactive Slicers

### Dashboard Preview

```
![Excel Dashboard](07_images/Excel_Dashboard.png)
```

---

# Power BI Dashboard

The Power BI dashboard includes:

- KPI Cards
- Gender Performance Analysis
- Test Preparation Analysis
- Parental Education Analysis
- Gender Distribution
- Interactive Filters (Slicers)

### Dashboard Preview

```
![Power BI Dashboard](07_images/PowerBI_Dashboard.png)
```

---

# At-Risk Student Analysis

Students scoring below **50** in one or more subjects were identified as academically at risk.

This analysis helps school management:

- Identify struggling students
- Provide additional academic support
- Improve overall student performance

---

# Principal Report

A detailed Principal Report is included covering:

- Project Overview
- Dataset Summary
- Findings
- Insights
- Recommendations
- Conclusion

Location

```
06_reports/Principal_Report.docx
```

---

# Key Insights

- Students completing the test preparation course generally performed better.
- Higher parental education levels were associated with better average scores.
- Reading and writing scores showed a strong relationship.
- Gender-wise performance varied across subjects.
- At-risk students were successfully identified for academic intervention.

---

# Learning Outcomes

Through this project I gained hands-on experience in:

- PostgreSQL
- Advanced SQL
- Python
- Data Cleaning
- Data Visualization
- Statistical Analysis
- Advanced Excel
- Power BI Dashboard Development
- Business Reporting
- Data Storytelling

---

# Future Improvements

- Predict student performance using Machine Learning.
- Build an interactive web dashboard.
- Add automated reporting.
- Perform trend analysis on larger educational datasets.

---

# Author

**Harshit Singh**

Data Analyst Project

Developed using PostgreSQL, SQL, Python, Advanced Excel, and Power BI.