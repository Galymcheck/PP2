-- Table that stores contact groups (categories like Family, Work, etc.)
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,        -- unique identifier for each group (auto-increment)
    name VARCHAR(50) UNIQUE NOT NULL  -- group name must be unique and cannot be NULL
);


-- Main table that stores contact information
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,        -- unique contact ID
    name VARCHAR(100),            -- contact full name
    email VARCHAR(100),           -- contact email address
    birthday DATE,                -- contact birth date stored in DATE format
    group_id INTEGER REFERENCES groups(id)  -- foreign key linking contact to a group
);


-- Table that stores multiple phone numbers for each contact (1-to-many relationship)
CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,         -- unique ID for each phone record
    contact_id INTEGER REFERENCES phonebook(id) ON DELETE CASCADE,
    -- links phone to a contact; if contact is deleted, phones are also deleted

    phone VARCHAR(20) NOT NULL,    -- phone number string (required field)

    type VARCHAR(10) CHECK (
        type IN ('home', 'work', 'mobile')
    ),
    -- restricts phone type to only allowed values

    UNIQUE(contact_id, phone)      -- prevents duplicate phone numbers for same contact
);


-- Predefined default groups inserted into system
INSERT INTO groups (name)
VALUES
    ('Family'),   -- default family group
    ('Work'),     -- default work group
    ('Friend'),   -- default friends group
    ('Other')     -- fallback category for uncategorized contacts
ON CONFLICT (name) DO NOTHING;   -- prevents duplication if script runs multiple times