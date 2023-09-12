import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute ('''CREATE TABLE IF NOT EXISTS products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    date_added DATE);''')
conn.commit()

cur.execute ('''CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY);''')
conn.commit()

cur.execute ('''CREATE TABLE IF NOT EXISTS product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);''')
conn.commit()

#cur.execute ('''ALTER TABLE categories
#ADD COLUMN name VARCHAR(255) NOT NULL;''')
#conn.commit()

cur.execute ('''INSERT INTO products(name,description,price,stock)
VALUES ('iPhone 12 Pro Max', 'Смартфон с OLED дисплеем и тройной камерой', 1099.99, 100),
('Samsung Galaxy S21 Ultra', 'Смартфон с AMOLED дисплеем и четырехкамерной системой', 1199.99, 50),
('Huawei P40 Pro', 'Смартфон с OLED дисплеем и 5G модулем', 999.99, 75),
('Xiaomi Mi 11', 'Смартфон с AMOLED дисплеем и тремя камерами', 899.99, 120),
('Canon EOS R5', 'Фотоаппарат с 45-мегапиксельной матрицей и видеосъемкой в 8К', 3899.99, 20),
('Nikon Z7 II', 'Фотоаппарат с 45-мегапиксельной матрицей и двумя слотами для карт памяти', 2999.99, 30);
''')
conn.commit()

cur.execute ('''INSERT INTO categories (name)
VALUES ('Смартфоны'), ('Фотоаппараты');
''')
conn.commit()

cur.execute ('''INSERT INTO product_categories (product_id, category_id)
VALUES (1,1), (2,1), (3,1), (4,1), (5,2), (6,2);
''')
conn.commit()

cur.executemany ('INSERT INTO products VALUES (?, ?, ?, ?);')
cur.executemany ('INSERT INTO categories VALUES (?, ?, ?, ?);')
cur.executemany ('INSERT INTO product_categories VALUES (?, ?, ?, ?);')
conn.comit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)