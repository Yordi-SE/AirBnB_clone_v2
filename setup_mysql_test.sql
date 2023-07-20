-- create database and prepares a MySQL server for the project
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
