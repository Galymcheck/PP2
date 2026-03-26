from connect import get_connection

def create_table():
    conn = get_connection()     # connect to the database
    cur = conn.cursor()         # bridge between your code and the database
 
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    );
    """)

    conn.commit()     # Apply changes to the database
    cur.close()       # Close the cursor
    conn.close()      # Close the connection


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()    # Connect to DB
    cur = conn.cursor()        # Create cursor

    cur.execute("""
    INSERT INTO phonebook (name, phone)
    VALUES (%s, %s)
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()       # get all lines at once as a list.

    for row in rows:
        print(row)


def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE phonebook
    SET phone = %s
    WHERE name = %s
    """, (new_phone, name))  # send SQL query for execution.

    conn.commit()

    if cur.rowcount == 0:    # Check if any row was updated
        print("No contact found!")
    else:
        print("Contact updated!")


def delete_contact():
    name = input("Enter name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM phonebook
    WHERE name = %s
    """, (name,))

    conn.commit()

    if cur.rowcount == 0:
        print("No contact found!")
    else:
        print("Contact deleted!")


def search_contacts():
    choice = input("Search by (1) Name or (2) Phone prefix? ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        print("Invalid choice!")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)


import os
import csv
from connect import get_connection

def import_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice7/contacts.csv", newline='', encoding='utf-8') as csvfile: # Open CSV and insert rows into phonebook
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
            INSERT INTO phonebook (name, phone)
            VALUES (%s, %s)
            """, (row['name'], row['phone']))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported successfully!")


# запуск
create_table()

while True:
    print("\n1. Add contact")
    print("2. Show contacts")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Import from CSV")
    print("6. Search contacts")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        import_from_csv()
    elif choice == "6":
        search_contacts()
    elif choice == "7":
        break