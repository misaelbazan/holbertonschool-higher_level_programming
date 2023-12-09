-- create a database 'hbtn_0d_2' and the user 'user_0d_2'
-- if the database 'hbtn_0d_2' already exists, the script should not fail
-- if the user 'user_0d_2' already exists, the script should not fail
-- 'user_0d_2' should  have only SELECT privilege on 'hbtn_0d_2' DB
-- 'user_0d_2' password should be set to 'user_0d_2_pwd'
CREATE DATABASE if not exists hbtn_0d_2;
CREATE USER if not exists 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
