USE dnd_database;

INSERT IGNORE INTO characters (name, class, level, description) VALUES
('Aelar Stormwind', 'Wizard', 12, 'Elven archmage of the northern towers'),
('Brakus Ironfist', 'Fighter', 10, 'Dwarven arena champion'),
('Lyra Moonwhisper', 'Rogue', 8, 'Silent thief from the shadow guild'),
('Thalion Brightleaf', 'Druid', 11, 'Protector of the ancient forest'),
('Seraphina Dawn', 'Cleric', 9, 'Healer of the sun temple'),
('Darius Blackthorn', 'Warlock', 13, 'Pact-bound seeker of forbidden knowledge'),
('Kael Windrider', 'Ranger', 7, 'Hunter of the eastern wilds'),
('Mira Frostveil', 'Sorcerer', 10, 'Wielder of ice-born magic'),
('Gorim Stonebeard', 'Paladin', 14, 'Holy knight of the mountain order'),
('Elyndra Nightbreeze', 'Bard', 6, 'Traveler who sings forgotten songs');

INSERT IGNORE INTO stats (character_id, strength, dexterity, constitution, intelligence, wisdom, charisma) VALUES
(1, 8, 14, 12, 20, 15, 13),
(2, 18, 12, 16, 10, 11, 9),
(3, 10, 20, 12, 13, 14, 11),
(4, 12, 13, 15, 14, 20, 10),
(5, 11, 10, 14, 13, 18, 16),
(6, 9, 14, 13, 18, 12, 17),
(7, 14, 18, 13, 11, 15, 10),
(8, 10, 16, 14, 17, 12, 13),
(9, 20, 11, 18, 12, 14, 15),
(10, 8, 17, 11, 15, 13, 19);

INSERT IGNORE INTO spells (name, description, level, damage) VALUES
('Fireball', 'Explosive burst of fire', 3, '8d6 fire'),
('Magic Missile', 'Guaranteed arcane bolts', 1, '3d4+3 force'),
('Heal', 'Restores health to allies', 2, NULL),
('Lightning Bolt', 'High-voltage strike', 3, '8d6 lightning'),
('Invisibility', 'Makes caster unseen', 2, NULL),
('Frost Nova', 'Freezing area blast', 3, '6d6 cold'),
('Summon Wolf', 'Calls a spirit wolf', 2, NULL),
('Charm Person', 'Influences humanoid minds', 1, NULL),
('Meteor Strike', 'Massive celestial impact', 5, '12d10 fire/bludgeoning'),
('Arcane Shield', 'Protective magical barrier', 2, NULL);

INSERT IGNORE INTO items (name, description, effects) VALUES
('Sword of Dawn', 'Holy blade of light', '+5 vs undead'),
('Healing Potion', 'Restores health', 'Heals 50 HP'),
('Ring of Agility', 'Enhances reflexes', '+2 dexterity'),
('Cloak of Shadows', 'Blends with darkness', 'Stealth boost'),
('Amulet of Wisdom', 'Enhances insight', '+3 wisdom'),
('Boots of Speed', 'Increases movement', '+10 movement'),
('Fire Scroll', 'One-time fire spell', 'Casts Fireball'),
('Ice Dagger', 'Frozen blade', 'Slows enemies'),
('Shield of Valor', 'Knightly protection', '+4 defense'),
('Bag of Holding', 'Extra-dimensional storage', 'Infinite item capacity');

INSERT IGNORE INTO npcs (name, description) VALUES
('Elder Rowan', 'Village leader and sage'),
('Captain Valen', 'Town guard commander'),
('Mirael the Merchant', 'Travelling trader of rare goods'),
('Orin Blacksmith', 'Master weapon crafter'),
('Selene the Seer', 'Oracle of forgotten futures'),
('Grimwald', 'Tavern keeper with secrets'),
('Lady Arwyn', 'Noble of the eastern court'),
('Thessia', 'Healer of the mountain shrine'),
('Borik Stonehand', 'Dwarven engineer'),
('Nyx Whisper', 'Shadowy informant');

INSERT IGNORE INTO spells_learned (character_id, spell_id) VALUES
(1, 1),
(1, 10),
(2, 9),
(3, 5),
(4, 7),
(5, 3),
(6, 4),
(7, 6),
(8, 2),
(9, 8);

INSERT IGNORE INTO inventory (character_id, item_id, quantity) VALUES
(1, 7, 2),
(2, 1, 1),
(3, 4, 1),
(4, 9, 1),
(5, 2, 5),
(6, 5, 1),
(7, 6, 2),
(8, 8, 3),
(9, 3, 1),
(10, 10, 1);

INSERT IGNORE INTO quests (npc_id, objective, details, start_date, completion_date, rewards) VALUES
(1, 'Recover ancient tome', 'Find lost arcane book in ruins', '2026-01-10', NULL, '500 gold + spell scroll'),
(2, 'Clear goblin camp', 'Eliminate goblin threat near town', '2026-02-01', '2026-02-05', '300 gold'),
(3, 'Escort caravan', 'Protect merchants on trade route', '2026-02-10', '2026-02-12', '200 gold + item'),
(4, 'Forge legendary sword', 'Gather rare ores for weapon', '2026-03-01', NULL, 'Unique weapon'),
(5, 'Investigate visions', 'Solve mystery of prophetic dreams', '2026-03-10', NULL, 'Magical insight'),
(6, 'Tavern disappearance', 'Find missing travelers', '2026-03-15', '2026-03-18', '150 gold'),
(7, 'Court intrigue', 'Uncover noble conspiracy', '2026-04-01', NULL, 'Political favor'),
(8, 'Sacred healing ritual', 'Gather herbs for temple ritual', '2026-04-05', '2026-04-06', 'Blessing'),
(9, 'Repair golem core', 'Fix ancient dwarven construct', '2026-04-10', NULL, 'Mechanical companion'),
(10, 'Deliver secret message', 'Covert delivery across kingdom', '2026-04-12', '2026-04-13', 'Encrypted reward chest');

INSERT IGNORE INTO skills (character_id, name, effects) VALUES
(1, 'Perception', 'Spotting hidden enemies, hearing conversations, or finding hidden doors'),
(2, 'Stealth', 'Hiding from enemies, moving silently, or sneaking past guards'),
(3, 'Athletics', 'Boost climbing, jumping, and grappling success'),
(4, 'Persuasion', 'Negotiating, charming, or convincing NPCs to help'),
(5, 'Arcana', 'Identifying spells, magical items, or arcane lore'),
(6, 'Insight', 'Detect lies and hidden motives'),
(7, 'Investigation', 'Searching for clues, deducing locations, or analyzing evidence'),
(8, 'Acrobatics', 'Maintaining balance, escaping restraints, or performing flips.'),
(9, 'Intimidation', 'Using threats to coerce NPCs.'),
(10, 'Survival', 'Tracking enemies, foraging for food, or avoiding natural hazards');