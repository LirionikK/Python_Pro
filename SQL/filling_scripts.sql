INSERT INTO public.authors(
	author_name, birth_date, email)
	VALUES ('Charles Dickens', '1912-02-07', 'charles@gmail.com'),
	('Jane Austen', '1775-12-16', 'jane@gmail.com'),
	('J.K. Rowling', '1965-07-31', 'rowling@gmail.com')
;

INSERT INTO public.books(
	title, isbn, copies_available, publication_year, author_id)
	VALUES ('Oliver Twist', 'ISBN-10: 0451524934', 5, '1839', 1),
	('Great Expectations', 'ISBN-13: 9780141439792', 6, '1860', 1),
	('Harry Potter and the Philosophers Stone', 'ISBN-13: 9780553212419', 10, '2000', 3)
;

INSERT INTO public.employees(
	employee_name, "position", salary, phone_number)
	VALUES ('Jack', 'librarian', 5000, '0674512368'),
	('Nick', 'manager', 7000, '0665412368')
;

INSERT INTO public.users(
	user_name, email, phone_number)
	VALUES ('Mary', 'mary@gmail.com', '0504127845'),
	('Andy', 'andy@gmail.com', '0504127457'),
	('Fred', 'fred@gmail.com', '0997412589'),
	('Josh', 'josh@gmail.com', '0680415786')
;

INSERT INTO public.loans(
	user_id, book_id, loan_date, return_date)
	VALUES (1, 2, '2024-04-20', '2024-05-03'),
	(2, 1, '2024-03-21', '2024-04-05'),
	(3, 3, '2024-04-06', '2024-05-01')
;