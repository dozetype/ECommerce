-- Create the database
CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

-- Drop existing tables if they exist
-- DROP TABLE IF EXISTS order_items, orders, customers, products;

-- Products table, used for storing all items in the app
-- name: name of the item | price: price of the item | stock: quantity available
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

-- Customers table, for storing every customers info
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Orders table
-- customer_id: linked to customer table's id | order_date: time
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Order Items table
-- order_id: track which order its from | product_id: used to identify item
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK(quantity>0),
    FOREIGN KEY (order_id) REFERENCES orders(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

ALTER TABLE products ADD UNIQUE (name);
ALTER TABLE customers ADD UNIQUE (email);

-- Sample Data
INSERT IGNORE INTO products (name, price, stock) VALUES 
('Laptop', 800.00, 10),
('Phone', 500.00, 20),
('Headphones', 50.00, 100),
('Tablet', 300.00, 15),
('Smartwatch', 200.00, 25),
('Bluetooth Speaker', 75.00, 40),
('External Hard Drive', 120.00, 30),
('Gaming Mouse', 45.00, 60),
('Keyboard', 35.00, 70);

INSERT IGNORE INTO customers (name, email) VALUES 
('Alice Smith', 'alice@example.com'),
('Bob Johnson', 'bob@example.com'),
('Carol White', 'carol@example.com'),
('David Lee', 'david@example.com'),
('Eva Green', 'eva@example.com'),
('Frank Harris', 'frank@example.com');

INSERT IGNORE INTO orders (customer_id, order_date) VALUES
(1, '2025-05-01 10:30:00'),
(2, '2025-05-02 15:45:00'),
(3, '2025-05-03 09:20:00'),
(1, '2025-05-04 18:05:00'),
(4, '2025-05-05 11:00:00');

INSERT IGNORE INTO order_items (order_id, product_id, quantity) VALUES
-- Order 1 (Alice)
(1, 1, 1),  -- Laptop
(1, 3, 2),  -- Headphones

-- Order 2 (Bob)
(2, 2, 1),  -- Phone
(2, 5, 1),  -- Gaming Mouse

-- Order 3 (Carol)
(3, 4, 1),  -- Tablet

-- Order 4 (Alice)
(4, 6, 2),  -- Smartwatch
(4, 3, 1),  -- Headphones

-- Order 5 (David)
(5, 1, 1),  -- Laptop
(5, 7, 1);  -- Bluetooth Speaker

select * from products;
SELECT * From customers;