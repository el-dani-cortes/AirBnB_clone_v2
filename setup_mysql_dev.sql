-- Prepares a MySQL server with specific parameters
-- Creates db hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user 'hbnb_dev' if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user 'hbnb_dev'
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
