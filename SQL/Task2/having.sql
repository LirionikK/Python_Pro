-- SQL-запит, який показує користувачів, які позичили більше 5 книг
SELECT user_name, COUNT(*) FROM loans
INNER JOIN users ON loans.user_id = users.user_id
GROUP BY user_name
HAVING COUNT(*) > 5;

-- SQL-запит, який виводить жанри, для яких у бібліотеці є більше 10 книг
SELECT genre, COUNT(*) FROM books
GROUP BY genre
HAVING COUNT(*) > 10;

-- SQL-запит, який показує бібліотечні філії, де працює більше 5 працівників
SELECT library_branch, COUNT(*) FROM employees
GROUP BY library_branch
HAVING COUNT(*) > 5;