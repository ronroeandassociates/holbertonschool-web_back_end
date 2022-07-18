--  SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;


CREATE TABLE IF NOT EXISTS orders (
  id INTEGER NOT NULL AUTO_INCREMENT,
  item_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
);

CREATE TABLE IF NOT EXISTS items (
  id INTEGER NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  quantity INTEGER NOT NULL,
);
