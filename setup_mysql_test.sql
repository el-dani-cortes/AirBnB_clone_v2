-- Prepares a MySQL server with specific parameters for 'hbnb_test'
-- Creates db hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user 'hbnb_test' if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets password for user 'hbnb_test'
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grants privileges to 'hbnb_test' on db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privileges to 'hbnb_test' on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
