--This is a DML query to display results sorted by score >= 10
--using ORDER BY
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
