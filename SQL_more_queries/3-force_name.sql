-- Creates the table force_name -- Script to create the table `force_name` if it doesn't already exist.
-- The table has two columns:
--   - `id` (integer)
--   - `name` (string up to 256 characters), which must not be NULL.
CREATE TABLE IF NOT EXISTS force_name (
id INT,
name VARCHAR(256) NOT NULL
);
