CREATE DATABASE IF NOT EXISTS dnd_database;
USE dnd_database;

CREATE TABLE IF NOT EXISTS characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    character_class VARCHAR(50),
    level INT,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS stats (
    character_id INT PRIMARY KEY,
    strength INT CHECK (strength >= 1 AND strength <= 20),
    dexterity INT CHECK (dexterity >= 1 AND dexterity <= 20),
    constitution INT CHECK (constitution >= 1 AND constitution <= 20),
    intelligence INT CHECK (intelligence >= 1 AND intelligence <= 20),
    wisdom INT CHECK (wisdom >= 1 AND wisdom <= 20),
    charisma INT CHECK (charisma >= 1 AND charisma <= 20),
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS spells (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    level INT,
    -- Use VARCHAR instead of INT due to damage being dice based (ex. d4, 2d6) 
    damage VARCHAR(50)
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
    character_id INT NOT NULL,
    spell_id INT NOT NULL,
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE,
    FOREIGN KEY (spell_id) 
        REFERENCES spells(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS inventory (
    character_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (character_id, item_id),
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE,
    FOREIGN KEY (item_id) 
        REFERENCES items(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS quests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    npc_id INT NOT NULL,
    objective VARCHAR(255),
    details VARCHAR(255),
    start_date DATE,
    completion_date DATE,
    rewards VARCHAR(255),
    FOREIGN KEY (npc_id) 
        REFERENCES npcs(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    effects VARCHAR(255),
    FOREIGN KEY (character_id) 
        REFERENCES characters(id)
        ON DELETE CASCADE
);