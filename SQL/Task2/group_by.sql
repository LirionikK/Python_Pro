-- SQL-запит, який виводить кількість книг, які були позичені кожним користувачем
SELECT user_name, COUNT(*) FROM loans
INNER JOIN users ON loans.user_id = users.user_id
GROUP BY user_name;

--  SQL-запит, який виводить кількість книг кожного жанру в бібліотеці
SELECT genre, COUNT(*) FROM books
GROUP BY genre;

-- SQL-запит, який показує кількість працівників в кожній бібліотечній філії
SELECT library_branch, COUNT(*) FROM employees
GROUP BY library_branch;