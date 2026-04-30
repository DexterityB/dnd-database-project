# D&D Database



## ERD



## Installation

1. git clone https://github.com/DexterityB/dnd-database-project.git

2. cd dnd-database-project

3. pip install mysql-connector-python

4. pip install tabulate


## Usage 
To run python menu

1. python3 main.py

To make docker container and create database

1. docker run --name dnd-database   -e MYSQL_ROOT_PASSWORD=password   -p 3306:3306   -d mysql:latest

2. docker start dnd-database

3. docker exec -it final-project-db mysql -uroot -ppassword < schema.sql

## Example Usage



## Testing

To add example data and see example queries

1. docker exec -it final-project-db mysql -uroot -ppassword < data.sql

2. docker exec -it final-project-db mysql -uroot -ppassword < queries.sql

## Table Descriptions

- Characters
    - Gives info about each player's name, class, current level, and description of their character  
- Stats
    - Defines a character’s physical and mental capabilities to determine success on dice rolls
- Spells Learned
    - Used to connect Characters and Spells tables 
- Spells
    - Magical effects that allow characters to perform supernatural feats such as dealing damage or healing wounds
- Inventory
    - Used to connect Character and Items tables 
- Items
    - Mundane or magical objects that are used to enhance abilities, provide utility, or offer protection
- Skills
    - Specific applications of the six core stats used to determine the success of uncertain actions
- Quests
    - Defined objectives or missions that drive the narrative forward
- Npcs
    - Any character in the game world controlled by the DM, providing information, plot hooks, or opposition to drive the story. 

## Features List



## Known Bugs or Limitations



## Reflection