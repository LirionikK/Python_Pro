CREATE TABLE customers(
 	id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL,
	email VARCHAR(100)
);

CREATE TABLE products(
 	id SERIAL PRIMARY KEY,
 	name VARCHAR(50) NOT NULL,
	price DECIMAL NOT NULL
);

CREATE TABLE orders(
 	id SERIAL PRIMARY KEY,
 	customer_id INT,
	product_id INT,
	order_date DATE DEFAULT CURRENT_DATE,
	quantity INT,
	FOREIGN KEY (customer_id) REFERENCES customers(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE suppliers(
 	id SERIAL PRIMARY KEY,
 	name VARCHAR(100) NOT NULL,
	contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE product_suppliers(
 	id SERIAL PRIMARY KEY,
 	product_id INT,
	supplier_id INT,
	supply_date DATE DEFAULT CURRENT_DATE,
	FOREIGN KEY (product_id) REFERENCES products(id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

INSERT INTO customers(name, email)
VALUES ('cust1', 'cust1@gmail.com'),
	('cust2', 'cust2@gmail.com'),
	('cust3', 'cust3@mail.com'),
	('cust4', 'cust4@mail.com');

INSERT INTO products(name, price)
VALUES ('prod1', 50),
	('prod2', 80),
	('prod3', 120),
	('prod4', 200),
	('prod5', 5);

INSERT INTO orders(customer_id, product_id, quantity)
	VALUES (1, 2, 3),
	(2, 1, 1),
	(2, 3, 2),
	(3, 1, 1);

INSERT INTO suppliers(
	name, contact_name)
	VALUES ('sup1', 'sup_name1'),
	('sup2', 'sup_name2'),
	('sup3', 'sup_name3'),
	('sup4', 'sup_name4');

INSERT INTO public.product_suppliers(
	product_id, supplier_id)
	VALUES (1, 3),
	(2, 2),
	(3, 1);

-- Cписок всіх продуктів
SELECT id, name, price FROM products;

-- Cписок всіх користувачів, у яких пошта закінчується на "@gmail.com"
SELECT id, name, email FROM customers WHERE email LIKE '%@gmail.com';

-- Загальна кількість замовлень
SELECT COUNT(id) FROM orders;

-- Кількість замовлень, яку зробив юзер з конкретним айді
SELECT COUNT(id) FROM orders WHERE customer_id=2;

-- Всі продукти, які коштують від 10 до 100
SELECT id, name, price FROM products WHERE price BETWEEN 10 and 100;