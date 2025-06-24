-- Create the 'cities' table in the 'hbtn_0d_usa' database
-- The table includes:
-- - id: INT, auto-incremented, primary key
-- - state_id: INT, non-null, foreign key referencing states.id
-- - name: VARCHAR(256), non-null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
