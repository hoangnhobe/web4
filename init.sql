CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Thêm sản phẩm mẫu
INSERT INTO products (name, price) VALUES
('Laptop Dell', 1200.00),
('Chuột Logitech', 25.00),
('Bàn phím cơ', 55.50);