-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- cities description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
-- the foreign key has to be part of the cities table and the reference id of the state
-- in order to get the match with the table, or get an error if the state_id not exists in states id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);
