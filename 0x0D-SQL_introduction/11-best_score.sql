--This is a DML query to display results sorted by score >= 10
--using ORDER BY: to display score first then name.order by score
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
