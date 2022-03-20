DROP TABLE plant;
DROP TABLE manufacturer;



CREATE TABLE manufacturer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);

CREATE TABLE plant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    manifacturers_id INT REFERENCES manufacturer(id)
);
 