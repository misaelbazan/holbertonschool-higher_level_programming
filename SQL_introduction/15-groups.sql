-- lists the number of records with the same score in 'second_table'
-- the result should display: score, the number of records for this score
-- 	with the label 'number'
-- list should be sorted by the number of records (DESC)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
