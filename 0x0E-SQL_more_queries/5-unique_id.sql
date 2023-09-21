-- creates the table unique_id.
-- does not fail if it already exists.
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
