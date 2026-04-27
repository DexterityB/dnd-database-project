import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create database connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='root',
            password='password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def add_runner(connection, name, country):
    """Add a new speedrunner to the database"""
    try:
        cursor = connection.cursor()
        query = "INSERT INTO runners (name, country) VALUES (%s, %s)"
        cursor.execute(query, (name, country))
        connection.commit()
        print(f"✅ Added runner: {name}")
    except Error as e:
        print(f"❌ Error: {e}")

def main():
    print("🎮 Speedrun Database Manager")
    print("=" * 40)
    
    connection = create_connection()
    if not connection:
        return
    
    while True:
        print("\n1. Add Runner")
        print("2. View All Runners")
        print("3. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == "1":
            name = input("Runner name: ")
            country = input("Country: ")
            add_runner(connection, name, country)
        elif choice == "3":
            break
    
    connection.close()

if __name__ == "__main__":
    main()