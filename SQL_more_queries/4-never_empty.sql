-- Script to create the table id_not_null
-- id has a default value of 1
-- name is a VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256)
);