-- create a MySQL server user 'user_0d_1'
-- 'user_0d_1' should have all the privileges
-- if the user 'user_0d_1' already exists, the script should not fail
CREATE USER if not exists 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
