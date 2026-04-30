USE dnd_database;

SELECT name, class, level
FROM characters
WHERE level > 5;

SELECT name, class, level
FROM characters
ORDER BY level DESC
LIMIT 1;

SELECT name, description, damage
FROM spells
WHERE level = 2;

SELECT name, effects
FROM items
WHERE effects LIKE '%heal%';

SELECT COUNT(*) AS total_characters
FROM characters;

SELECT character_id, strength
FROM stats
WHERE strength > 15;

SELECT c.name, c.class, s.strength, s.dexterity
FROM characters c
JOIN stats s ON c.id = s.character_id;

SELECT c.name AS character_name, i.name AS item, inv.quantity
FROM characters c
JOIN inventory inv ON c.id = inv.character_id
JOIN items i ON inv.item_id = i.id;