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

def insert_character(connection, name, dnd_class, description, level):
    '''Add a character to the database'''
    try:
        cursor = connection.cursor()
        query = "INSERT INTO characters (name, class, level, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, dnd_class, level, description))
        connection.commit()
        print(f'✅ "{name}" added to database ✅')

        cursor.execute("SELECT id, name FROM characters WHERE name = %s", (name,))
        id = cursor.fetchall()[0][0]

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        id = None
        
    finally:
        return id

def insert_stats(connection, id, strength, dexterity, constitution, intelligence, wisdom, charisma):
    '''Add a character's stats to the database'''
    try:
        cursor = connection.cursor()
        query = "INSERT INTO stats (character_id, strength, dexterity, constitution, intelligence, wisdom, charisma) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, strength, dexterity, constitution, intelligence, wisdom, charisma))
        connection.commit()
        print(f'✅ Stats added to database ✅')

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        
    finally:
        return None