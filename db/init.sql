CREATE DATABASE IF NOT EXISTS coffee_db;
use coffee_db;

CREATE TABLE IF NOT EXISTS coffees (
  name VARCHAR(20),
  description VARCHAR(255)
);

INSERT INTO coffees
  (name, description)
VALUES
  ('Espresso', 'Espresso is brewed by using an espresso machine to force a small amount of nearly boiling water and steam.'),
  ('Cappucino', 'Cappuccino, from Italian, is an Italian drink prepared with espresso and milk.'),
  ('French press', 'A French press requires a coarser grind of coffee than a drip brew coffee filter, as finer grounds will seep through the press filter and into the coffee.');

