SELECT
    parental_education,
    ROUND(AVG(math_score),2) AS avg_math,
    ROUND(AVG(reading_score),2) AS avg_reading,
    ROUND(AVG(writing_score),2) AS avg_writing
FROM student_performance
GROUP BY parental_education
ORDER BY avg_math DESC;


SELECT
    test_preparation_course,
    ROUND(AVG(math_score),2) AS avg_math,
    ROUND(AVG(reading_score),2) AS avg_reading,
    ROUND(AVG(writing_score),2) AS avg_writing
FROM student_performance
GROUP BY test_preparation_course;


SELECT
    gender,
    ROUND(AVG(math_score),2) AS avg_math,
    ROUND(AVG(reading_score),2) AS avg_reading,
    ROUND(AVG(writing_score),2) AS avg_writing
FROM student_performance
GROUP BY gender;


SELECT
    MIN(math_score + reading_score + writing_score) AS minimum_score,
    MAX(math_score + reading_score + writing_score) AS maximum_score,
    ROUND(AVG(math_score + reading_score + writing_score),2) AS average_score
FROM student_performance;


