-- Procedure that inserts a new contact or updates existing one
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name TEXT,        -- contact name input
    p_email TEXT,       -- contact email input
    p_birthday DATE,    -- contact birth date
    p_group_id INT,     -- foreign key to groups table
    p_phone TEXT,       -- phone number
    p_type TEXT         -- phone type (home/work/mobile)
)
AS $$
DECLARE
    v_contact_id INT;   -- stores found or newly created contact id
BEGIN

    -- Check if contact already exists by name
    SELECT id INTO v_contact_id
    FROM phonebook
    WHERE name = p_name;

    -- If contact does NOT exist → insert new record
    IF v_contact_id IS NULL THEN
        INSERT INTO phonebook(name, email, birthday, group_id)
        VALUES (p_name, p_email, p_birthday, p_group_id)
        RETURNING id INTO v_contact_id;

    -- If contact exists → update existing record
    ELSE
        UPDATE phonebook
        SET email = p_email,
            birthday = p_birthday,
            group_id = p_group_id
        WHERE id = v_contact_id;
    END IF;

    -- Insert phone number into separate phones table
    -- ON CONFLICT prevents duplicate phone entries for same contact
    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type)
    ON CONFLICT (contact_id, phone) DO NOTHING;

END;
$$ LANGUAGE plpgsql;


-- Procedure for inserting multiple contacts at once (bulk import)
CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],       -- array of names
    emails TEXT[],      -- array of emails
    birthdays DATE[],   -- array of birthdays
    group_ids INT[],    -- array of group IDs
    phones TEXT[],      -- array of phone numbers
    types TEXT[]        -- array of phone types
)
AS $$
DECLARE
    i INT;  -- loop index
BEGIN

    -- Loop through all array elements
    FOR i IN 1..array_length(names, 1) LOOP

        -- Validate phone length before inserting
        IF length(phones[i]) < 5 THEN
            RAISE NOTICE 'Invalid phone: %', phones[i];

        -- If valid phone → call single insert/update procedure
        ELSE
            CALL insert_or_update_user(
                names[i],
                emails[i],
                birthdays[i],
                group_ids[i],
                phones[i],
                types[i]
            );
        END IF;

    END LOOP;

END;
$$ LANGUAGE plpgsql;


-- Procedure to delete a contact by name or email
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
DECLARE
    v_id INT;  -- stores matched contact id
BEGIN

    -- Find contact by name OR email
    SELECT id INTO v_id
    FROM phonebook
    WHERE name = p_value
       OR email = p_value;

    -- Delete contact if found
    DELETE FROM phonebook WHERE id = v_id;

END;
$$ LANGUAGE plpgsql;


-- Procedure to add a new phone number to existing contact
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,  -- contact name
    p_phone VARCHAR,         -- new phone number
    p_type VARCHAR           -- phone type
)
AS $$
DECLARE
    v_contact_id INT;  -- resolved contact id
BEGIN

    -- Find contact id from name
    SELECT id INTO v_contact_id
    FROM phonebook
    WHERE name = p_contact_name;

    -- If contact does not exist → throw error
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    -- Insert new phone number for contact
    -- Prevent duplicate phone numbers for same contact
    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type)
    ON CONFLICT (contact_id, phone) DO NOTHING;

END;
$$ LANGUAGE plpgsql;


-- Procedure to move a contact to another group
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,  -- contact name
    p_group_name VARCHAR     -- target group name
)
AS $$
DECLARE
    v_contact_id INT;  -- contact id
    v_group_id INT;    -- group id
BEGIN

    -- Find contact by name
    SELECT id INTO v_contact_id
    FROM phonebook
    WHERE name = p_contact_name;

    -- If contact not found → throw error
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    -- Try to find group by name
    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    -- If group does not exist → create it dynamically
    IF v_group_id IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO v_group_id;
    END IF;

    -- Update contact's group
    UPDATE phonebook
    SET group_id = v_group_id
    WHERE id = v_contact_id;

END;
$$ LANGUAGE plpgsql;