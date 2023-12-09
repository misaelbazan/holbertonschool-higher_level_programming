-- create the table 'unique_id':
-- 	id INT DEFAUL '1' and must be unique
--	name VARCHAR(256) NOT NULL
-- if the table already exists the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
