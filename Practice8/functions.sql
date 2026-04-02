CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook                              
    WHERE phonebook.name ILIKE '%' || pattern || '%'    --Filters rows where the name matches the pattern (case-insensitive).
       OR phonebook.phone LIKE '%' || pattern || '%';   --any symbol+pattern+any symbol
END;                               
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;