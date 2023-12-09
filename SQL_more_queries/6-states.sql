-- create a database hbtn_0d_usa and a table 'states' inside it
-- table 'states' description:
--	id INT AUTO_INCREMENT PRIMARY KEY
--	name VARCHAR(256) NOT NULL
-- if the database laready exists the script should not fail
-- if the table already exists the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
