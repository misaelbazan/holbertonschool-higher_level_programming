-- create the table 'force_name'
-- description:
-- 	id INT
-- 	name VARCHAR(256) can't be NULL
-- if 'force_name' table already exists the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
)
