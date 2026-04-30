CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    type VARCHAR
)
AS $$
BEGIN
    -- Return a combined view of contacts + their phone numbers
    RETURN QUERY
    SELECT
        p.id,              -- contact ID
        p.name,            -- contact name
        p.email,           -- contact email
        ph.phone,          -- phone number (from phones table)
        ph.type            -- phone type (home/work/mobile)

    FROM phonebook p
    LEFT JOIN phones ph
        ON p.id = ph.contact_id   -- link contact with its phones

    -- Search conditions:
    -- matches against name, email, or phone number
    WHERE
        p.name ILIKE '%' || p_query || '%'      -- case-insensitive name search
        OR p.email ILIKE '%' || p_query || '%'  -- email partial match
        OR ph.phone LIKE '%' || p_query || '%'; -- phone partial match
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts(limit_val INT, offset_val INT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR
)
AS $$
BEGIN
    -- Return contacts with their group information
    RETURN QUERY
    SELECT
        p.id,              -- contact ID
        p.name,            -- contact name
        p.email,           -- contact email
        p.birthday,        -- birthday (DATE type preserved in DB)
        g.name AS group_name  -- group name from groups table

    FROM phonebook p

    LEFT JOIN groups g
        ON p.group_id = g.id   -- link contact to group

    ORDER BY p.id              -- consistent ordering for pagination

    LIMIT limit_val           -- number of rows per page
    OFFSET offset_val;        -- starting position (pagination offset)
END;
$$ LANGUAGE plpgsql;