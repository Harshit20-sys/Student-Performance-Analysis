import psycopg2
import pandas as pd

# PostgreSQL Connection
connection = psycopg2.connect(
    host="localhost",
    database="student_performance_analysis",
    user="postgres",
    password="Harshit@8932",
    port="5432"
)

print("Database Connected Successfully!")

# Read Data
query = "SELECT * FROM student_performance;"

df = pd.read_sql(query, connection)

print("\nFirst 5 Records\n")
print(df.head())

print("\nDataset Shape")
print(df.shape)

connection.close()