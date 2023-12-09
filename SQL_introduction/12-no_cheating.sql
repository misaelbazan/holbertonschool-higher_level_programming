-- updates score of Bob to 10 in the table 'second_table'
-- is not allowed to use to use Bob's id value, only the name field
UPDATE second_table
SET score = CASE
	WHEN score > 10 THEN 10
	ELSE score
	END;

SELECT score, name FROM second_table
ORDER BY score DESC;
