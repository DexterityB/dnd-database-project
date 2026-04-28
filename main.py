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

def add_character(connection, name, dnd_class, description, level):
    '''Add a character to the database'''
    try:
        cursor = connection.cursor()
        query = "INSERT INTO characters (name, class, level, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, dnd_class, level, description))
        connection.commit()
        print(f'✅ "{name}" added to database ✅')

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        
    finally:
        return None

def view_table(connection, table):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        table = cursor.fetchall()
        for row in table:
            print(row)
        #connection.commit()

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
        print("\n1. Add Character")
        print("2. View All Characters")
        print("3. Exit")
        
        select = input("Selection: ")
        
        if select == "1":
            name = input("Name: ")
            dnd_class = input("Class: ")
            level = input("Level: ")
            description = input("Description: ")
            add_character(connection, name, dnd_class, description, level)

        elif select == "2":
            view_table(connection, 'characters')

        elif select == "3":
            break
    
    connection.close()

if __name__ == "__main__":
    main()