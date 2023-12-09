-- create a table 'id_not_null':
-- 	id INT with default value '1'
-- 	name VARCHAR(256) not NULL
-- if the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT '1',
	name VARCHAR(256) NOT NULL
);
