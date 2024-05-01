CREATE TABLE authors(
 	author_id SERIAL PRIMARY KEY,
 	author_name VARCHAR(100) NOT NULL,
	birth_date DATE,
	email VARCHAR(100)
);

CREATE TABLE books(
 	book_id SERIAL PRIMARY KEY,
 	title VARCHAR(100) NOT NULL,
 	ISBN VARCHAR(50),
	copies_available INT,
	publication_year INT,
	author_id INT,
	FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE employees(
 	employee_id SERIAL PRIMARY KEY,
 	employee_name VARCHAR(100) NOT NULL,
	position VARCHAR(40) NOT NULL,
	salary INT NOT NULL,
	phone_number VARCHAR(20)
);

CREATE TABLE users(
 	user_id SERIAL PRIMARY KEY,
 	user_name VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone_number VARCHAR(20)
);

CREATE TABLE loans(
 	loan_id SERIAL PRIMARY KEY,
	user_id INT,
	book_id INT,
	loan_date DATE NOT NULL,
	return_date DATE NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (book_id) REFERENCES books(book_id)
);
