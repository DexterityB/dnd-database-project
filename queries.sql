USE dnd_database;
/*
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE inventory;
TRUNCATE TABLE spells_learned;
TRUNCATE TABLE stats;
TRUNCATE TABLE quests;
TRUNCATE TABLE spells;
TRUNCATE TABLE items;
TRUNCATE TABLE npcs;
TRUNCATE TABLE characters;

SET FOREIGN_KEY_CHECKS = 1;
*/

SELECT * FROM characters;
SELECT * FROM stats;
SELECT * FROM spells;
SELECT * FROM items;
SELECT * FROM npcs;
SELECT * FROM spells_learned;
SELECT * FROM inventory;
SELECT * FROM quests;