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
('Star Lord', 'https://i.pinimg.com/originals/89/3a/c1/893ac1b31a89071e67cd29d552581e72.jpg', 'Helmet', 'Human and Clestial Hybrid', 'You Said It Yourself. We are The Guardians Of The Galaxy', 'Expert Marksman'),
('Rocket', 'https://w0.peakpx.com/wallpaper/673/776/HD-wallpaper-rocket-raccoon-in-avengers-endgame-thumbnail.jpg', 'Laser Cannon', 'Raccoon', 'Aint No Thing Like Me, Except Me!', 'Engineering Genius'),
('Groot', 'https://d23.com/app/uploads/2022/08/1180w-600h_081022_Groot-Languages_00.jpg', 'Quad Blasters', 'Flora colossus', 'I am Groot!', 'Manipulates His Body'),
('Drax the Destroyer', 'https://www.superherohype.com/wp-content/uploads/sites/4/2023/01/Drax-the-Destroyer.jpg', 'Dual Knives', 'Kylosian', 'Nothing Goes Over My Head! My Reflexes Are Too Fast, I Would Catch It!', 'Expert Combatant'),
('Gamora', 'https://www.themarysue.com/wp-content/uploads/2019/10/zoe-saldana-gamora-featured.jpg?w=1200&resize=1200%2C600', 'Godslayer', 'Zehoberei', 'I am gonna die surrounded by the biggest idiots in the galaxy', 'Body Mods and Expert Swordsmen');

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);