DROP TABLE plants;
DROP TABLE manufacturers;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id)
);
