CREATE DATABASE coffee_db;
\connect coffee_db

CREATE TABLE coffees (
  id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  name varchar(20) NOT NULL,
  description varchar(255) NOT NULL
);

INSERT INTO coffees
  (id, name, description)
VALUES
  (DEFAULT, 'Espresso', 'Espresso is brewed by using an espresso machine to force a small amount of nearly boiling water and steam.'),
  (DEFAULT, 'Cappucino', 'Cappuccino, from Italian, is an Italian drink prepared with espresso and milk.'),
  (DEFAULT, 'French press', 'A French press requires a coarser grind of coffee than a drip brew coffee filter, as finer grounds will seep through the press filter and into the coffee.'),
  (DEFAULT, 'Mocaccino', 'Coffee mocha is based on espresso and hot milk but with added chocolate flavouring and sweetener, typically in the form of cocoa powder and sugar.')

