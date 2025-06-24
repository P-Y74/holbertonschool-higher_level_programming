-- This script creates the database 'hbtn_0d_usa' if it does not already exist,
-- and defines the table 'states' inside it with two fields:
--   - 'id': an auto-incremented primary key (INT)
--   - 'name': a non-null VARCHAR(256)
-- If either the database or the table already exists, the script does not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
