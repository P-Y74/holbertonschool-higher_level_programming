-- Create the table 'unique_id' if it doesn't exist
-- The table contains:
--   - id: an integer with a default value of 1, must be unique
--   - name: a VARCHAR field with a max length of 256
-- The 'id' column has a UNIQUE constraint to prevent duplicate values

CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1,
name VARCHAR(256),
UNIQUE (id)
);
