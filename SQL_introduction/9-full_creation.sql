-- create a table named 'second_table' with three rows inside it
CREATE TABLE if not exists second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- adding some content inside the rows
INSERT INTO second_table (id, name, score) VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
