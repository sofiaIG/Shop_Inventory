DROP TABLE IF EXISTS plants CASCADE;

DROP TABLE IF EXISTS manufacturers CASCADE;

DROP TABLE IF EXISTS orders CASCADE;

DROP TABLE IF EXISTS customers CASCADE;

DROP TABLE IF EXISTS shipments CASCADE;

DROP TABLE IF EXISTS shipping_companies CASCADE;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE plants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    buying_cost FLOAT,
    selling_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id),
    stock_quantity INT
);

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    order_number TEXT UNIQUE,
    order_date TIMESTAMP NOT NULL,
    plant_id INT REFERENCES plants(id),
    quantity INT,
    customer_id INT REFERENCES customers(id)
);

CREATE TABLE shipping_companies(id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE shipments(
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    shipping_date DATE NOT NULL,
    shipping_company_id INT REFERENCES shipping_companies(id)
);