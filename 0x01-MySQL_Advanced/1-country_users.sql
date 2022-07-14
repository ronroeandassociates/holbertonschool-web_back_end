-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country VARCHAR(255) NOT NULL DEFAULT 'US',
  PRIMARY KEY (id)
);
-- end of script
