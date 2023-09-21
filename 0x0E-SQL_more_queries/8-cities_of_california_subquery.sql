-- lists all the cities of California that can be found in the db hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name.
-- only one SELECT statement
-- Results must be sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
