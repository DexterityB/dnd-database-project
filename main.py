from database import create_connection, view_table, add_data, update_data, delete_data

def char_menu(connection):
    print("\n🧙 Character Menu 👑")
    print("=" * 20)

    print("1. Add Character")
    print("2. Update Character")
    print("3. Delete Character")
    select = input("Selection: ")
    
    match select:
        case '1':
            add_character(connection)

        case '2':
            return None

        case '3':
            id = int(input("Input Character ID: "))
            delete_data(connection, 'characters', id)

    return None



def spell_menu(connection):
    print("\n🪄  Spell Menu 📜")
    print("=" * 16)
    return None




def quest_menu(connection):
    print("\n🧭 Quest Menu 🗺️")
    print("=" * 16)
    return None




def add_character(connection):
    name = input("Name: ")
    dnd_class = input("Class: ")
    level = input("Level: ")
    description = input("Description: ")
    id = add_data(connection, 'characters (name, class, level, description)', (name, dnd_class, level, description), name, True)

    auto = input("\nWould you like to input your statistics or randomize them automatically [manual/auto]: ").lower()
    if auto == "manual":
        strength = int(input("Strength: "))
        dexterity = int(input("Dexterity: "))
        constitution = int(input("Constitution: "))
        intelligence = int(input("Intelligence: "))
        wisdom = int(input("Wisdom: "))
        charisma = int(input("Charisma: "))
    add_data(connection, 'stats (character_id, strength, dexterity, constitution, intelligence, wisdom, charisma)', (id, strength, dexterity, constitution, intelligence, wisdom, charisma), name + "'s stats")

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
        print("5. Exit")
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
                break
    
    connection.close()

if __name__ == "__main__":
    main()