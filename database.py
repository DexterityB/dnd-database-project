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

def view_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("\nList of available tables: ", end = "")
        options = []
        for option in tables:
            options.append(option[0])
        print(options)

        table = input("Table name: ").lower()
        print("")

        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        table = cursor.fetchall()

        headers = [val[0].upper() for val in cursor.description]
        print(tabulate(table, headers = headers, tablefmt = "grid"))

    except Error as e:
        print(f'❌ Error: "{e}" ❌')

    finally:
        return None

def add_data(connection, table, data, added, get_id = False):
    '''Add a row of data to the database'''
    try:
        cursor = connection.cursor()
        parameters = []
        for value in data:
            parameters.append('%s')

        query = f"INSERT INTO {table} VALUES ({", ".join(parameters)})"
        cursor.execute(query, data)
        connection.commit()
        print(f'✅ {added} added to database ✅')

        if get_id:
            query = f"SELECT id, name FROM {table} WHERE name = " + "%s"
            cursor.execute(query, (data[0],))
            id = cursor.fetchall()[0][0]
        else:
            id = None

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        id = None
        
    finally:
        return id

def update_data(connection, table, rows, data, id_name, updated):
    '''Update a row of data in the database'''
    try:
        cursor = connection.cursor()
        parameters = []
        for num in range(len(rows)):
            parameters.append(rows[num] + ' = %s')

        query = f"UPDATE {table} SET {", ".join(parameters)} WHERE {id_name} = " + "%s"
        cursor.execute(query, data)
        connection.commit()
        print(f'✅ {updated} updated in database ✅')

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        
    finally:
        return None

def delete_data(connection, table, id):
    '''Delete a row of data from the database'''
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table} WHERE id = " + "%s"
        cursor.execute(query, (id,))
        connection.commit()
        print('✅ Successfly deleted data from database ✅')
    
    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        
    finally:
        return None