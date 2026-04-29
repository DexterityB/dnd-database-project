from database import create_connection, view_table, insert_character, insert_stats

def add_character():
    name = input("Name: ")
    dnd_class = input("Class: ")
    level = input("Level: ")
    description = input("Description: ")
    id = insert_character(connection, name, dnd_class, description, level)

    auto = input("\nWould you like to input your statistics or randomize them automatically [manual/auto]: ").lower()
    if auto == "manual":
        strength = int(input("Strength: "))
        dexterity = int(input("Dexterity: "))
        constitution = int(input("Constitution: "))
        intelligence = int(input("Intelligence: "))
        wisdom = int(input("Wisdom: "))
        charisma = int(input("Charisma: "))
    insert_stats(connection, id, strength, dexterity, constitution, intelligence, wisdom, charisma)

def main():
    print("🗡️  D&D Database Manager 🐉")
    print("=" * 26)
    
    connection = create_connection()
    if not connection:
        return None
    
    while True:
        print("\n1. View Table")
        print("2. Add Character")
        print("3. Exit")
        
        select = input("Selection: ")
        
        match select:
            case "1":
                table = input("Table name: ").lower()
                print("")
                view_table(connection, table)

            case "2":
                add_character()

            case "3":
                break
    
    connection.close()

if __name__ == "__main__":
    main()