-- create a table with UNIQUE values and DEFAULT 1
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
