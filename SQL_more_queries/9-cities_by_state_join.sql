-- Lists all cities in the database with their corresponding state names
-- Ordered by city ID in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
