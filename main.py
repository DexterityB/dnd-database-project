import mysql.connector
from mysql.connector import Error

def create_connection():
    '''Connect to Database'''
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dnd_database',
            user='root',
            password='password'
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        return False

def view_table(connection, table):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        table = cursor.fetchall()

        sec_len = 0
        for num in range(len(table)):
            first_len = sec_len
            try:
                sec_len = len(str(table[num]))
            except:
                sec_len = 0

            if first_len > sec_len:
                print("-" * first_len)
            else:
                print("-" * sec_len)

            print("|", end = " ")
            for value in table[num]:
                print(value, end = " | ")
            print("")
        print("-" * sec_len)

    except Error as e:
        print(f'❌ Error: "{e}" ❌')

    finally:
        return None

def add_character(connection, name, dnd_class, description, level):
    '''Add a character to the database'''
    try:
        cursor = connection.cursor()
        query = "INSERT INTO characters (name, class, level, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, dnd_class, level, description))
        connection.commit()
        print(f'✅ "{name}" added to database ✅')

        cursor.execute("SELECT id, name FROM characters WHERE name = %s", (name,))
        id = int(cursor.fetchall()[0])

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        id = None
        
    finally:
        return id

def add_character(id, strength, dexterity, constitution, intelligence, wisdom, charisma):
    '''Add a character's stats to the database'''
    try:
        cursor = connection.cursor()
        query = "INSERT INTO stats (id, strength, dexterity, constitution, intelligence, wisdom, charisma) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, strength, dexterity, constitution, intelligence, wisdom, charisma))
        connection.commit()
        print(f'✅ Stats added to database ✅')

        #cursor.execute("SELECT id, name FROM characters WHERE name = %s", (name,))
        #id = int(cursor.fetchall()[0])

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        
    finally:
        return None

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
                name = input("Name: ")
                dnd_class = input("Class: ")
                level = input("Level: ")
                description = input("Description: ")
                id = add_character(connection, name, dnd_class, description, level)

                auto - input("\nWould you like to input your statistics or randomize them automatically [manual/auto]: ").lower()
                if auto == "manual":
                    strength = int(input("Strength: "))
                    dexterity = int(input("Dexterity: "))
                    constitution = int(input("Constitution: "))
                    intelligence = int(input("Intelligence: "))
                    wisdom = int(input("Wisdom: "))
                    charisma = int(input("Charisma: "))
                
                add_stats(id, strength, dexterity, constitution, intelligence, wisdom, charisma)

            case "3":
                break
    
    connection.close()

if __name__ == "__main__":
    main()