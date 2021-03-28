-- Prepares a MySQL server with specific parameters for hbnb_dev
-- Creates db hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user 'hbnb_dev' if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user 'hbnb_dev'
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants privileges to 'hbnb_dev' on db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privileges to 'hbnb_dev' on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
