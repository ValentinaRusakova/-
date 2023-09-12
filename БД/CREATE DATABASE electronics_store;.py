CREATE DATABASE electronics_store;

CREAT TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    date_added DATE
);

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY);

CREATE TABLE product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

ALTER TABLE categories
ADD COLUMN name VARCHAR(255) NOT NULL;

INSERT INTO products(name,description,price,stock)
VALUES ('iPhone 12 Pro Max', 'Смартфон с OLED дисплеем и тройной камерой', 1099.99, 100),
('Samsung Galaxy S21 Ultra', 'Смартфон с AMOLED дисплеем и четырехкамерной системой', 1199.99, 50),
('Huawei P40 Pro', 'Смартфон с OLED дисплеем и 5G модулем', 999.99, 75),
('Xiaomi Mi 11', 'Смартфон с AMOLED дисплеем и тремя камерами', 899.99, 120),
('Canon EOS R5', 'Фотоаппарат с 45-мегапиксельной матрицей и видеосъемкой в 8К', 3899.99, 20),
('Nikon Z7 II', 'Фотоаппарат с 45-мегапиксельной матрицей и двумя слотами для карт памяти', 2999.99, 30);

INSERT INTO categories (name)
VALUES ('Смартфоны'), ('Фотоаппараты');

INSERT INTO product_categories (product_id, category_id)
VALUES (1,1), (2,1), (3,1), (4,1), (5,2), (6,2);

SELECT p.name AS product_name, c.name AS category_name
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON c.id = pc.category_id;

SELECT p.*FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON c.id = pc.category_id AND c.name = "Смартфоны"
WHERE p.price < 1000
ORDER BY p.price DESC
LIMIT 10;

SELECT p.name AS product_name, c.name AS category_name, stock, price
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
WHERE STOCK > 0
ORDER BY price ASC
LIMIT 5;

SELECT c.*FROM categories c
JOIN product_categories pc ON c.id = pc.category_id
WHERE pc.product_id = 1
ORDER BY c.name ASC
LIMIT 8;

ALTER TABLE product_categories
ADD CONSTRAINT fk_product_id
FOREIGN KEY (product_id) REFERENCES progucts(id),
ADD CONSTRAINT fk_category_id
FOREIGN KEY (category_id) REFERENCES categories(id);

CREANE TABLE orders (
    id INT AUNO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    older_date DATE NOT NULL,
    total DECIMAL (10,2) NOT NULL
);

SELECT p.name, c.name AS category
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON pc.category_id = c.id;

SELECT p.name, c.name AS category
FROM product_categories pc
LEFT JOIN products p ON pc.product_id = p.id
JOIN categories c ON pc.category_id = c.id;

SELECT p.name, c.name AS category
FROM product_categories pc
JOIN categories c ON pc.category_id = c.id
RIGHT JOIN products p ON pc.product_id = p.id;

SELECT CONCAT(p.name, '-', c.name) AS product_category,
       DATE(p.date_added) AS added_date,
       SUM(p.price * p.stock) AS total_value
       FROM products p
       JOIN product_categories pc ON p.id = pc.product_id
       JOIN categories c ON pc.category_id = c.id
       GROUP BY p.name, c.name, p.date_added;

SELECT c.name AS category, COUNT(p.id) AS product_count
FROM categories c
JOIN product_categories pc ON c.id = pc.category_id
JOIN products p ON pc.product_id = p.id
GROUP BY c.id;

SELECT c.name AS category, AVG(p.price) AS avg_price
FROM categories c
JOIN product_categories pc ON c.id = pc.category_id
JOIN products p ON pc.product_id = p.id
GROUP BY c.id;

SELECT *
FROM products
ORDER BY price DESC;

SELECT *
FROM products
ORDER BY name ASC;

SELECT *
FROM products
ORDER BY price DESC, stock ASC;

CREATE TABLE products_backup (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL,
  date DATE
);

INSERT INTO products_backup (id, name, description, price, stock)
SELECT id,name,description ,price ,stock FROM products;

CREATE TABLE categories_backup (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO categories_backup (id,name)
SELECT id,name FROM categories;

 CREATE TABLE product_categories_backup(
     product_id INT ,
     category_id INT ,
     PRIMARY KEY(product_id ,category_id),
      FOREIGN KEY(product_id ) REFERENCES   `products`(`id`) ON DELETE CASCADE ON UPDATE CASCADE ,
      FOREIGN KEY(category_Id ) REFERENCES `categories`(`Id`)ON DELETE CASCADE ON UPDATE CASCADE 

 );

 INSERT INTO product_categories_Backup(product_Id ,category_Id )
 SELECT * from Product_Categories;
