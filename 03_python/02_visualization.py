import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# PostgreSQL Connection
connection = psycopg2.connect(
    host="localhost",
    database="student_performance_analysis",
    user="postgres",
    password="Harshit@8932",
    port="5432"
)

# Read Data
query = "SELECT * FROM student_performance;"
df = pd.read_sql(query, connection)

connection.close()

print(df.head())

# Create Total Score Column
df["total_score"] = (
    df["math_score"]
    + df["reading_score"]
    + df["writing_score"]
)

print(df[["math_score", "reading_score", "writing_score", "total_score"]].head())

gender_avg = df.groupby("gender")[["math_score", "reading_score", "writing_score"]].mean()

gender_avg.plot(kind="bar")

plt.title("Average Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")

plt.tight_layout()
plt.savefig("../07_images/chart1_gender_performance.png", dpi=300, bbox_inches="tight")
plt.show()


# =====================================================
# CHART 2 - Bar Chart
# Test Preparation vs Average Total Score
# =====================================================

prep_avg = df.groupby("test_preparation_course")["total_score"].mean()

prep_avg.plot(kind="bar")

plt.title("Test Preparation vs Average Total Score")
plt.xlabel("Test Preparation")
plt.ylabel("Average Total Score")
plt.tight_layout()
plt.savefig("../07_images/chart2_test_preparation.png", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# CHART 3 - Box Plot
# Parental Education vs Total Score
# =====================================================

education_groups = []

labels = []

for education in df["parental_education"].unique():

    education_groups.append(
        df[df["parental_education"] == education]["total_score"]
    )

    labels.append(education)

plt.boxplot(education_groups, tick_labels=labels)

plt.xticks(rotation=30)

plt.title("Parental Education vs Total Score")
plt.xlabel("Parental Education")
plt.ylabel("Total Score")

plt.tight_layout()
plt.savefig("../07_images/chart3_parental_education_boxplot", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# CHART 4 - Histogram
# Total Score Distribution
# =====================================================

plt.hist(df["total_score"], bins=20)

plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("../07_images/chart4_total_score_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# CHART 5 - Scatter Plot
# Math vs Reading
# =====================================================

plt.scatter(df["math_score"], df["reading_score"])

plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")

plt.tight_layout()
plt.savefig("../07_images/chart5_math_vs_reading.png", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# CHART 6 - Correlation Heatmap
# (Without Seaborn)
# =====================================================

correlation = df[
    ["math_score", "reading_score", "writing_score"]
].corr()

plt.imshow(correlation)

plt.colorbar()

plt.xticks(
    range(3),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(3),
    correlation.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("../07_images/chart6_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nAll Charts Generated Successfully!")