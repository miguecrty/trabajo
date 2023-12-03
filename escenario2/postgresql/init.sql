CREATE DATABASE sta;
\c sta;
CREATE TABLE datos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  edad INTEGER
);

