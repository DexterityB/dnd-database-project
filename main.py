from database import create_connection, view_table, add_data, update_data, delete_data

def char_menu(connection):
    print("\n🧙 Character Menu 👑")
    print("=" * 20)

    print("1. Add Character")
    print("2. Update Character")
    print("3. Delete Character")
    print("4. Add Skill")
    print("5. Update Skill")
    print("6. Delete Skill")
    print("7. Main Menu")
    select = input("Selection: ")
    
    match select:
        case '1':
            add_character(connection)

        case '2':
            update_character(connection)

        case '3':
            id = int(input("Input Character ID: "))
            delete_data(connection, 'characters', id)

        case '4':
            add_skill(connection)

        case '5':
            update_skill(connection)

        case '6':
            id = int(input("Input Skill ID: "))
            delete_data(connection, 'skills', id)

    return None

def spell_menu(connection):
    print("\n🪄  Spell Menu 📜")
    print("=" * 16)
    
    print("\n1. Add Spell")
    print("2. Learn Spell")
    print("2. Update Spell")
    print("4. Delete Spell")
    select = input("Selection: ")
    
    match select:
        case '1':
            add_spell(connection)

        case '2':
            learn_spell(connection)

        case '2':
            update_spell(connection)
        
        case '4':
            id = int(input("Input Spell ID: "))
            delete_data(connection, 'spells', id)

    return None

def quest_menu(connection):
    print("\n🧭 Quest Menu 🗺️")
    print("=" * 16)

    print("\n1. Add Quest")
    print("2. Update Quest")
    print("3. Delete Quest")
    select = input("Selection: ")

    match select:
        case '1':
            add_quest(connection)

        case '2':
            update_quest(connection)

        case '3':
            id = int(input("Input Character ID: "))
            delete_data(connection, 'characters', id)

    return None

def npc_menu(connection):
    print("\n👤 Npc Menu 💬")
    print("=" * 14)

    print("\n1. Add Npc")
    print("2. Update Npc")
    print("3. Delete Npc")
    select = input("Selection: ")

    match select:
        case '1':
            add_npc(connection)

        case '2':
            update_npc(connection)

        case '3':
            id = int(input("Input Npc ID: "))
            delete_data(connection, 'npcs', id)

    return None


def item_menu(connection):
    print("📦 Item Menu 🎒")
    print("=" * 15)

    print("\n1. Add Item")
    print("2. Player Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    select = input("Selection: ")

    match select:
        case '1':
            add_item(connection)

        case '2':
            inventory(connection)

        case '3':
            update_item(connection)

        case '4':
            id = int(input("Input Item ID: "))
            delete_data(connection, 'item', id)

    return None


def add_character(connection):
    name = input("Name: ")
    character_class = input("Class: ")
    level = input("Level: ")
    description = input("Description: ")
    id = add_data(connection, 'characters', '(name, character_class, level, description)', (name, character_class, level, description), name, True)

    auto = input("\nWould you like to input your statistics or randomize them automatically [manual/auto]: ").lower()
    if auto == "manual":
        strength = int(input("Strength: "))
        dexterity = int(input("Dexterity: "))
        constitution = int(input("Constitution: "))
        intelligence = int(input("Intelligence: "))
        wisdom = int(input("Wisdom: "))
        charisma = int(input("Charisma: "))
    add_data(connection, 'stats', '(character_id, strength, dexterity, constitution, intelligence, wisdom, charisma)', (id, strength, dexterity, constitution, intelligence, wisdom, charisma), name + "'s stats")

def update_character(connection):
    id = input("ID of Character: ")
    name = input("New Name: ")
    character_class = input("New Class: ")
    level = input("New Level: ")
    description = input("New Description: ")
    update_data(connection, 'characters', ('name', 'character_class', 'level', 'description'), (name, character_class, level, description, id), 'id', name)
    return None

def add_skill(connection):
    character_id = input("ID of Character with Skill: ")
    name = input("Name of Skill: ")
    effect = input("Effect: ")
    add_data(connection, 'skills', '(character_id, name, effects)', (character_id, name, effect), name)
    return None

def update_skill(connection):
    id = input("ID of Skill: ")
    character_id = input("New ID of Character with Skill: ")
    name = input("New Name of Skill: ")
    effect = input("New Effect: ")
    update_data(connection, 'skills', ('character_id', 'name', 'effects'), (character_id, name, effect, id), 'id', name)
    return None

def learn_spell(connection):
    character_id = input("Character Id: ")
    spell_id = input("Spell Id: ")
    spell_name = input("Spell Name: ")
    character_name = input("Character Name: ")
    added = spell_name + " spell to " + character_name + " character"
    add_data(connection, 'spells_learned', '(character_id, spell_id)', (character_id, spell_id), added)

def add_spell(connection):
    name = input("Name: ")
    level = input("Level: ")
    damage = input("Damage (If Applicable): ")
    description = input("Description: ")
    add_data(connection, 'spells', '(name, level, damage, description)', (name, level, damage, description), name)

def update_spell(connection):
    id = input("ID of Spell: ")
    name = input("New Name: ")
    level = input("New Level: ")
    damage = input("New Damage (If Applicable): ")
    description = input("New Description: ")
    update_data(connection, 'spells', ('name', 'level', 'damage', 'description'), (name, level, damage, description, id), 'id', name)
    return None

def add_quest(connection):
    npc_id = input("Npc Id: ")
    if npc_id == "":
        npc_id = None
    objective = input("Objective: ")
    details = input("Details: ")
    start_date = input("Start Date (YYYY-MM-DD or blank): ")
    completion_date = input("Completion Date (YYYY-MM-DD or blank): ")
    if completion_date == "":
        completion_date = None
    rewards = input("Rewards: ")
    add_data(connection, 'quests', '(npc_id, objective, details, start_date, completion_date, rewards)', (npc_id, objective, details, start_date, completion_date, rewards), objective)

def update_quest(connection):
    id = input("ID of Quest: ")
    npc_id = input("New Npc Id: ")
    if npc_id == "":
        npc_id = None
    objective = input("New Objective: ")
    details = input("New Details: ")
    start_date = input("New Start Date (YYYY-MM-DD or blank): ")
    completion_date = input("New Completion Date (YYYY-MM-DD or blank): ")
    if completion_date == "":
        completion_date = None
    update_data(connection, 'quests', ('npc_id', 'objective', 'details', 'start_date', 'completion_date', 'rewards'), (npc_id, objective, details, start_date, completion_date, rewards, id), 'id', objective)
    return None

def add_npc(connection):
    name = input("Name: ")
    description = input("Description: ")
    add_data(connection, 'npcs', '(name, description)', (name, description), name)

def update_npc(connection):
    id = input("ID of NPC: ")
    name = input("New Name: ")
    description = input("New Description: ")
    update_data(connection, 'npcs', ('name', 'description'), (name, description, id), 'id', name)
    return None

def add_item(connection):
    name = input("Name: ")
    description = input("Description: ")
    effects = input("Effects: ")
    add_data(connection, 'items', '(name, description, effects)', (name, description, effects), name)

def update_item(connection):
    id = input("ID of Item: ")
    name = input("New Name: ")
    description = input("New Description: ")
    effects = input("New Effects: ")
    update_data(connection, 'items', ('name', 'description', 'effects'), (name, description, effects, id), 'id', name)
    return None

def inventory(connection):
    character_id = input("Character Id: ")
    item_id = input("Item Id: ")
    item_name = input("Item Name: ")
    character_name = input("Character Name: ")
    added = item_name + " item to " + character_name + " character"
    add_data(connection, 'inventory', '(character_id, item_id)', (character_id, item_id), added)

def main():    
    connection = create_connection()
    if not connection:
        return None
    
    while True:
        print("\n🗡️  D&D Database Manager 🐉")
        print("=" * 26)

        print("1. View Table")
        print("2. Character Menu")
        print("3. Spell Menu")
        print("4. Quest Menu")
        print("5. Npc Menu")
        print("6. Item Menu")
        print("7. Exit")
        select = input("Selection: ")
        
        match select:
            case '1':
                view_table(connection)

            case '2':
                char_menu(connection)

            case '3':
                spell_menu(connection)

            case '4':
                quest_menu(connection)

            case '5':
                npc_menu(connection)

            case '6':
                item_menu(connection)

            case '7':
                break
    
    connection.close()

if __name__ == "__main__":
    main()