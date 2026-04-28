CREATE DATABASE IF NOT EXISTS dnd_database;
USE dnd_database;

CREATE TABLE IF NOT EXISTS characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    class VARCHAR(50),
    level INT,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS stats (
    character_id INT PRIMARY KEY,
    strength INT,
    dexterity INT,
    constitution INT,
    intelligence INT,
    wisdom INT,
    charisma INT,
    description VARCHAR(255),
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS spells (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    level INT
);

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    effects VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS npcs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS spells_learned (
    id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT,
    spell_id INT,
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE,
    FOREIGN KEY (spell_id) 
        REFERENCES spells(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT,
    item_id INT,
    quantity INT,
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE,
    FOREIGN KEY (item_id) 
        REFERENCES items(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS quests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    npc_id INT,
    objective VARCHAR(255),
    details VARCHAR(255),
    start_date DATE,
    completion_date DATE,
    rewards VARCHAR(255),
    FOREIGN KEY (npc_id) 
        REFERENCES npcs(id)
        ON DELETE CASCADE
);

SELECT * FROM characters;
SELECT * FROM stats;
SELECT * FROM spells;
SELECT * FROM items;
SELECT * FROM npcs;
SELECT * FROM spells_learned;
SELECT * FROM inventory;
SELECT * FROM quests;