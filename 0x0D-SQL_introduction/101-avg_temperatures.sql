--This is a DML query to display average temperature by city 
--it imports temperatures into hbtn_0c_0
SELECT city,
AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
