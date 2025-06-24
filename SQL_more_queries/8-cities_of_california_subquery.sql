-- Selects the id and name of all cities from the database hbtn_0d_usa
-- where the city is located in the state of California.
-- Uses a subquery to get the state ID from the states table (without JOIN),
-- and orders the result by city id in ascending order.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
