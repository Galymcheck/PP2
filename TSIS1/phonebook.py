import csv  # used for reading CSV files for bulk import
from connect import get_connection  # function that creates PostgreSQL connection


def load_sql_file(path):
    # Opens a connection to the database
    conn = get_connection()
    cur = conn.cursor()

    # Reads full SQL file content into a string
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()

    # Executes the whole SQL script at once (schema/functions/procedures)
    cur.execute(sql)

    # Saves all changes in database (DDL or DML operations)
    conn.commit()

    # Closes cursor to free database resources
    cur.close()

    # Closes connection after execution
    conn.close()


def add_or_update():
    # Collecting user input for contact information
    name = input("Enter name: ")
    email = input("Enter email: ")
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    group_id = int(input("Enter group id (1-Family, 2-Work, 3-Friend, 4-Other): "))
    phone = input("Enter phone: ")
    phone_type = input("Enter phone type (home/work/mobile): ")

    # Open database connection
    conn = get_connection()
    cur = conn.cursor()

    # Calling PostgreSQL procedure that inserts or updates contact + phone
    cur.execute("""
        CALL insert_or_update_user(
            %s::text,
            %s::text,
            %s::date,
            %s::int,
            %s::text,
            %s::text
        )
    """, (name, email, birthday, group_id, phone, phone_type))

    # Commit changes so data is saved in DB
    conn.commit()

    # Close cursor
    cur.close()

    # Close connection
    conn.close()

    print("Contact saved!")


def import_from_csv():
    # Open database connection for batch insertion
    conn = get_connection()
    cur = conn.cursor()

    # Open CSV file containing contacts data
    with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS1/contacts.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate through each row in CSV file
        for row in reader:
            # Call DB procedure for each contact record
            cur.execute("""
                CALL insert_or_update_user(
                    %s::text,
                    %s::text,
                    %s::date,
                    %s::int,
                    %s::text,
                    %s::text
                )
            """, (
                row["name"],        # contact name
                row["email"],       # contact email
                row["birthday"],    # birth date
                row["group_id"],    # group identifier
                row["phone"],       # phone number
                row["type"]         # phone type
            ))

    # Save all inserted records into database
    conn.commit()

    # Close cursor
    cur.close()

    # Close connection
    conn.close()

    print("CSV imported successfully!")


def show_contacts():
    # Connect to database
    conn = get_connection()
    cur = conn.cursor()

    # Query joins contacts with groups and phones tables
    cur.execute("""
    SELECT
        p.id,
        p.name,
        p.email,
        p.birthday,
        g.name AS group_name,
        ph.phone,
        ph.type
    FROM phonebook p
    LEFT JOIN groups g
        ON p.group_id = g.id
    LEFT JOIN phones ph
        ON p.id = ph.contact_id
    ORDER BY p.id;
    """)

    # Fetch all query results
    rows = cur.fetchall()

    # Format output so DATE becomes readable string
    for row in rows:
        print(" | ".join(
            str(x.strftime("%Y-%m-%d")) if hasattr(x, "strftime") else str(x)
            for x in row
        ))

    # Close cursor and connection
    cur.close()
    conn.close()


def delete_user():
    # Ask user for identifier (name or phone)
    value = input("Enter name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    # Call procedure that removes user from DB
    cur.execute("CALL delete_user(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")


def search_contacts():
    # Search keyword input
    pattern = input("Enter search pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    # Call SQL function that performs pattern search
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    # Format output with proper date display
    for row in rows:
        print(" | ".join(
            str(x.strftime("%Y-%m-%d")) if hasattr(x, "strftime") else str(x)
            for x in row
        ))

    cur.close()
    conn.close()


def get_paginated():
    # Pagination parameters
    limit_val = int(input("Enter limit: "))
    offset_val = int(input("Enter offset: "))

    conn = get_connection()
    cur = conn.cursor()

    # Call DB pagination function
    cur.execute(
        "SELECT * FROM get_contacts(%s, %s)",
        (limit_val, offset_val)
    )

    rows = cur.fetchall()

    # Print paginated results
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def filter_by_group():
    # Ask group name from user
    group_name = input("Enter group (Family/Work/Friend/Other): ")

    conn = get_connection()
    cur = conn.cursor()

    # Filter contacts by group name using JOIN
    cur.execute("""
        SELECT p.name, p.email, g.name, ph.phone
        FROM phonebook p
        JOIN groups g ON p.group_id = g.id
        LEFT JOIN phones ph ON p.id = ph.contact_id
        WHERE g.name ILIKE %s
    """, (group_name,))

    rows = cur.fetchall()

    # Print filtered results
    for row in rows:
        print(" | ".join(
            str(x.strftime("%Y-%m-%d")) if hasattr(x, "strftime") else str(x)
            for x in row
        ))

    cur.close()
    conn.close()


def search_by_email():
    # Email substring search
    email_part = input("Enter email part: ")

    conn = get_connection()
    cur = conn.cursor()

    # Search using LIKE pattern matching
    cur.execute("""
        SELECT name, email
        FROM phonebook
        WHERE email ILIKE %s
    """, (f"%{email_part}%",))

    rows = cur.fetchall()

    for row in rows:
        print(" | ".join(str(x) for x in row))

    cur.close()
    conn.close()


def sort_contacts():
    # Choose sorting field
    print("Sort by: name / birthday / id")
    field = input("Enter field: ")

    # Validate input to prevent SQL errors
    if field not in ["name", "birthday", "id"]:
        print("Invalid field")
        return

    conn = get_connection()
    cur = conn.cursor()

    # Dynamic ORDER BY query (safe due to validation above)
    query = f"""
        SELECT name, email, birthday
        FROM phonebook
        ORDER BY {field}
    """

    cur.execute(query)
    rows = cur.fetchall()

    # Print sorted data
    for row in rows:
        print(" | ".join(
            str(x.strftime("%Y-%m-%d")) if hasattr(x, "strftime") else str(x)
            for x in row
        ))

    cur.close()
    conn.close()


def paginate_console():
    # Interactive pagination system
    limit_val = int(input("Enter limit: "))
    offset = 0

    conn = get_connection()
    cur = conn.cursor()

    while True:
        # Fetch one page of results
        cur.execute(
            "SELECT * FROM get_contacts(%s, %s)",
            (limit_val, offset)
        )

        rows = cur.fetchall()

        print("\n--- PAGE ---")
        for row in rows:
            print(row)

        # Navigation controls
        action = input("next / prev / quit: ")

        if action == "next":
            offset += limit_val
        elif action == "prev":
            offset = max(0, offset - limit_val)
        elif action == "quit":
            break
        else:
            print("Invalid command")

    cur.close()
    conn.close()


import json  # used for JSON export/import


def export_to_json():
    conn = get_connection()
    cur = conn.cursor()

    # Query full contact dataset including phones and group
    cur.execute("""
        SELECT 
            p.id,
            p.name,
            p.email,
            p.birthday,
            g.name,
            ph.phone,
            ph.type
        FROM phonebook p
        LEFT JOIN groups g ON p.group_id = g.id
        LEFT JOIN phones ph ON p.id = ph.contact_id
        ORDER BY p.id;
    """)

    rows = cur.fetchall()

    data = {}

    # Convert SQL rows into structured JSON format
    for row in rows:
        contact_id = row[0]

        if contact_id not in data:
            data[contact_id] = {
                "name": row[1],
                "email": row[2],
                "birthday": str(row[3]),
                "group": row[4],
                "phones": []
            }

        if row[5]:
            data[contact_id]["phones"].append({
                "phone": row[5],
                "type": row[6]
            })

    # Convert dictionary to list for JSON serialization
    result = list(data.values())

    # Write data to JSON file
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    cur.close()
    conn.close()

    print("Exported to contacts.json")


def import_from_json():
    # Open JSON file containing exported contacts
    with open("contacts.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Connect to database
    conn = get_connection()
    cur = conn.cursor()

    # Iterate through each contact in JSON
    for contact in data:
        name = contact["name"]

        # Check if contact already exists in DB
        cur.execute("SELECT id FROM phonebook WHERE name = %s", (name,))
        existing = cur.fetchone()

        # If contact exists, ask user what to do
        if existing:
            choice = input(f"{name} exists. skip / overwrite? ")

            # Skip importing this contact
            if choice == "skip":
                continue

            # Delete old record before inserting new one
            elif choice == "overwrite":
                cur.execute("DELETE FROM phonebook WHERE id = %s", (existing[0],))

        # Get group ID from group name
        cur.execute("SELECT id FROM groups WHERE name = %s", (contact["group"],))
        group_id = cur.fetchone()[0]

        # Insert new contact into phonebook table
        cur.execute("""
            INSERT INTO phonebook(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (
            name,
            contact["email"],
            contact["birthday"],
            group_id
        ))

        # Get generated contact ID
        contact_id = cur.fetchone()[0]

        # Insert all phone numbers for this contact
        for ph in contact["phones"]:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
            """, (contact_id, ph["phone"], ph["type"]))

    # Save all changes to database
    conn.commit()

    # Close database connection
    cur.close()
    conn.close()

    print("Imported from JSON")


def add_phone():
    # Ask user for contact name and new phone details
    name = input("Enter contact name: ")
    phone = input("Enter phone: ")
    phone_type = input("Enter type (home/work/mobile): ")

    # Open DB connection
    conn = get_connection()
    cur = conn.cursor()

    # Call PostgreSQL procedure to add phone
    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, phone_type))

    # Save changes
    conn.commit()

    # Close resources
    cur.close()
    conn.close()

    print("Phone added!")


def move_to_group():
    # Ask user for contact and target group
    name = input("Enter contact name: ")
    group = input("Enter group (Family/Work/Friend/Other/or new): ")

    # Open DB connection
    conn = get_connection()
    cur = conn.cursor()

    # Call procedure that moves contact to another group
    cur.execute("CALL move_to_group(%s, %s)", (name, group))

    # Save changes
    conn.commit()

    # Close connection
    cur.close()
    conn.close()

    print("Moved!")


# Load database schema (tables creation)
load_sql_file("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS1/schema.sql")

# Load SQL functions (search, pagination, etc.)
load_sql_file("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS1/functions.sql")

# Load stored procedures (insert, delete, move, etc.)
load_sql_file("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS1/procedures.sql")


# Main program loop (console interface)
while True:
    print("\n--- Extended PhoneBook ---")
    print("1. Add or update contact")
    print("2. Show all contacts")
    print("3. Import from CSV")
    print("4. Search contacts")
    print("5. Pagination")
    print("6. Delete contact")
    print("7. Filter by group")
    print("8. Search by email")
    print("9. Sort contacts")
    print("10. Pagination (interactive)")
    print("11. Export to JSON")
    print("12. Import from JSON")
    print("13. Add phone")
    print("14. Move to group")
    print("15. Quit")

    # User selects menu option
    choice = input("Choose: ")

    # Map menu options to functions
    if choice == "1":
        add_or_update()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        import_from_csv()

    elif choice == "4":
        search_contacts()

    elif choice == "5":
        get_paginated()

    elif choice == "6":
        delete_user()

    elif choice == "7":
        filter_by_group()

    elif choice == "8":
        search_by_email()

    elif choice == "9":
        sort_contacts()

    elif choice == "10":
        paginate_console()

    elif choice == "11":
        export_to_json()

    elif choice == "12":
        import_from_json()

    elif choice == "13":
        add_phone()

    elif choice == "14":
        move_to_group()

    elif choice == "15":
        print("Exiting program")
        break

    else:
        print("Invalid option, try again")