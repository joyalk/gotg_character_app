CREATE DATABASE guradians_of_the_galaxy_characters_db;

\c guradians_of_the_galaxy_characters_db

CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name TEXT,
    image_url TEXT,
    weapons TEXT,
    species TEXT,
    catchphrase TEXT,
    abilities TEXT
);
INSERT INTO characters(name, image_url, weapons, species, catchphrase, abilities)
VALUES