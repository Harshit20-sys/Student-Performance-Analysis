SELECT *
FROM student_performance
LIMIT 10;


SELECT COUNT(*) AS total_students
FROM student_performance;


SELECT COUNT(*)
FROM information_schema.columns
WHERE table_name='student_performance';


SELECT column_name
FROM information_schema.columns
WHERE table_name='student_performance';


SELECT
COUNT(*) FILTER (WHERE gender IS NULL) AS gender_null,
COUNT(*) FILTER (WHERE race_ethnicity IS NULL) AS race_null,
COUNT(*) FILTER (WHERE parental_education IS NULL) AS parental_null,
COUNT(*) FILTER (WHERE lunch IS NULL) AS lunch_null,
COUNT(*) FILTER (WHERE test_preparation_course IS NULL) AS prep_null,
COUNT(*) FILTER (WHERE math_score IS NULL) AS math_null,
COUNT(*) FILTER (WHERE reading_score IS NULL) AS reading_null,
COUNT(*) FILTER (WHERE writing_score IS NULL) AS writing_null
FROM student_performance;



SELECT
column_name,
data_type
FROM information_schema.columns
WHERE table_name='student_performance';



SELECT DISTINCT gender
FROM student_performance;



SELECT DISTINCT race_ethnicity
FROM student_performance;


SELECT DISTINCT parental_education
FROM student_performance;


SELECT DISTINCT lunch
FROM student_performance;


SELECT DISTINCT test_preparation_course
FROM student_performance;


