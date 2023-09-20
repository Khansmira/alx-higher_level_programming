-- DDL query that displays maximum temperature of each state, stored by state
SELECT state,MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
