import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def is_valid_table(connection, table):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    return table in [t[0] for t in cursor.fetchall()]


def get_valid_columns(connection, table):
    cursor = connection.cursor()
    cursor.execute(f"DESCRIBE {table}")
    return [col[0] for col in cursor.fetchall()]


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
        return None


def view_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        print("\nList of available tables: ", end="")
        options = [option[0] for option in tables]
        print(options)

        table = input("Table name: ").lower()
        print("")

        if table not in options:
            print("❌ Invalid table name ❌")
            return None

        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        results = cursor.fetchall()

        headers = [val[0].upper() for val in cursor.description]
        print(tabulate(results, headers=headers, tablefmt="grid"))

    except Error as e:
        print(f'❌ Error: "{e}" ❌')

    finally:
        return None

def add_data(connection, table, rows, data, added, get_id = False):
    '''Add a row of data to the database'''
    try:
        if not is_valid_table(connection, table):
            print("❌ Invalid table name ❌")
            return None

        valid_columns = get_valid_columns(connection, table)
        for col in rows.replace("(", "").replace(")", "").split(","):
            if col.strip() not in valid_columns:
                print(f"❌ Invalid column: {col} ❌")
                return None

        cursor = connection.cursor()
        parameters = ['%s'] * len(data)

        query = f"INSERT INTO {table} {rows} VALUES ({", ".join(parameters)})"
        cursor.execute(query, data)
        connection.commit()
        print(f'✅ {added} added to database ✅')

        if get_id:
            query = f"SELECT id, name FROM {table} WHERE name = %s"
            cursor.execute(query, (data[0],))
            result = cursor.fetchone()
            return result[0] if result else None

        return None

    except Error as e:
        print(f'❌ Error: "{e}" ❌')
        return None


def update_data(connection, table, rows, data, id_name, updated):
    '''Update a row of data in the database'''
    try:
        if not is_valid_table(connection, table):
            print("❌ Invalid table name ❌")
            return None

        valid_columns = get_valid_columns(connection, table)

        for col in rows:
            if col not in valid_columns:
                print(f"❌ Invalid column: {col} ❌")
                return None

        if id_name not in valid_columns:
            print(f"❌ Invalid column: {id_name} ❌")
            return None

        cursor = connection.cursor()
        parameters = [f"{row} = %s" for row in rows]

        query = f"UPDATE {table} SET {', '.join(parameters)} WHERE {id_name} = " + "%s"
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
        if not is_valid_table(connection, table):
            print("❌ Invalid table name ❌")
            return None

        cursor = connection.cursor()
        query = f"DELETE FROM {table} WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        print('✅ Successfully deleted data from database ✅')

    except Error as e:
        print(f'❌ Error: "{e}" ❌')

    finally:
        return None