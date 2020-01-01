CREATE DATABASE IF NOT EXISTS coffee_db;
use coffee_db;

CREATE TABLE IF NOT EXISTS coffees (
  id INT(11) AUTO_INCREMENT,
  name VARCHAR(20),
  description VARCHAR(255),
  PRIMARY KEY (id)
);

INSERT INTO coffees
  (id, name, description)
VALUES
  (0, 'Espresso', 'Espresso is brewed by using an espresso machine to force a small amount of nearly boiling water and steam.'),
  (0, 'Cappucino', 'Cappuccino, from Italian, is an Italian drink prepared with espresso and milk.'),
  (0, 'French press', 'A French press requires a coarser grind of coffee than a drip brew coffee filter, as finer grounds will seep through the press filter and into the coffee.'),
  (0, 'Mocaccino', 'Coffee mocha is based on espresso and hot milk but with added chocolate flavouring and sweetener, typically in the form of cocoa powder and sugar.')

