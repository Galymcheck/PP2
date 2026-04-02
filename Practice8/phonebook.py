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

conn = get_connection()
cur = conn.cursor()

with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice8/functions.sql", "r", encoding="utf-8") as f:
    sql = f.read()

statements = sql.split("\n\n")

for stmt in statements:
    stmt = stmt.strip()
    if stmt:
        cur.execute(stmt)

conn.commit()
cur.close()
conn.close()


conn = get_connection()
cur = conn.cursor()

with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice8/procedures.sql", "r", encoding="utf-8") as f:
    sql = f.read()

statements = sql.split("\n\n")    #The SQL file is split using empty lines (\n\n) as separators

for stmt in statements:
    stmt = stmt.strip()
    if stmt:
        cur.execute(stmt)

conn.commit()
cur.close()
conn.close()


create_table()

def call_search():
    pattern = input("Enter search pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()       # get all lines at once as a list.

    for row in rows:
        print(row)


def add_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def insert_many():
    names = ["Alice", "Bob", "Charlie"]
    phones = ["111111", "22", "333333"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))

    conn.commit()
    cur.close()
    conn.close()

    print("Batch insert done!")


def get_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_user():
    value = input("Enter name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")



while True:
    print("\n--- PhoneBook (Practice 8) ---")
    print("1. Search contacts")
    print("2. Add or update contact")
    print("3. Insert several contacts (phone length > 5)")
    print("4. Get contacts (pagination)")
    print("5. Delete contact")
    print("6. Show all contacts")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        call_search()
    elif choice == "2":
        add_or_update()
    elif choice == "3":
        insert_many()
    elif choice == "4":
        get_paginated()
    elif choice == "5":
        delete_user()
    elif choice == "6":
        show_contacts()
    elif choice =="7":
        break