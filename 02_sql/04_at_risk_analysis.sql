SELECT *
FROM student_performance
WHERE math_score < 50
   OR reading_score < 50
   OR writing_score < 50;



SELECT COUNT(*) AS total_at_risk_students
FROM student_performance
WHERE math_score < 50
   OR reading_score < 50
   OR writing_score < 50;



SELECT
    gender,
    COUNT(*) AS total_students
FROM student_performance
WHERE math_score < 50
   OR reading_score < 50
   OR writing_score < 50
GROUP BY gender;



SELECT
    parental_education,
    COUNT(*) AS total_students
FROM student_performance
WHERE math_score < 50
   OR reading_score < 50
   OR writing_score < 50
GROUP BY parental_education
ORDER BY total_students DESC;



SELECT
    test_preparation_course,
    COUNT(*) AS total_students
FROM student_performance
WHERE math_score < 50
   OR reading_score < 50
   OR writing_score < 50
GROUP BY test_preparation_course;