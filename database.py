import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

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

        headers = [val[0].upper() for val in cursor.description]
        #print(headers)
        #headers = ["Id", "Name", "Class", "Level", "Description"]
        print(tabulate(table, headers = headers, tablefmt = "grid"))



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