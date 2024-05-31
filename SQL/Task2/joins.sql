-- Пов'яжіть таблиці users та borrow_records, використовуючи INNER JOIN на id користувача 
-- та user_id запису про позичання. Виведіть імена користувачів (first_name, last_name) та borrow_date.
SELECT users.user_name, loans.loan_date
FROM users
INNER JOIN loans ON users.user_id = loans.user_id;

-- Додайте до попереднього запиту групування по користувачам (first_name, last_name). 
-- Виведіть імена користувачів та кількість їхніх записів про позичання.
SELECT users.user_name, COUNT(*)
FROM users
INNER JOIN loans ON users.user_id = loans.user_id
GROUP BY users.user_name;

-- До попереднього запиту додайте сортування за кількістю записів про позичання 
-- від більшого до меншого (DESC) і обмежте вивід першими 10 результатами. 
SELECT users.user_name, COUNT(*)
FROM users
INNER JOIN loans ON users.user_id = loans.user_id
GROUP BY users.user_name
ORDER BY COUNT(*) DESC
LIMIT 10;

-- Виведіть інформацію про всіх користувачів і книги, які вони позичили (якщо позичили). 
-- Для цього використайте LEFT JOIN між таблицями users, borrow_records, book_copies та books.
SELECT users.user_name, books.title, loans.loan_date FROM users
LEFT JOIN loans ON  users.user_id = loans.user_id
LEFT JOIN books ON  loans.book_id = books.book_id
ORDER BY user_name;

-- Додайте до попереднього запиту умову вибірки лише тих користувачів, 
-- які позичили хоча б одну книгу (WHERE books.title IS NOT NULL).
SELECT users.user_name, books.title, loans.loan_date FROM users
LEFT JOIN loans ON  users.user_id = loans.user_id
LEFT JOIN books ON  loans.book_id = books.book_id
WHERE books.title IS NOT NULL
ORDER BY user_name;

-- Додайте до попереднього запиту агрегатну функцію для підрахунку кількості книг, 
-- які позичив кожен користувач.
SELECT users.user_name, COUNT(title) FROM users
LEFT JOIN loans ON  users.user_id = loans.user_id
LEFT JOIN books ON  loans.book_id = books.book_id
WHERE books.title IS NOT NULL
GROUP BY user_name;

-- Використайте FULL JOIN для з'єднання таблиць employees та library_branches, 
-- виведіть імена співробітників та назву філії, в якій вони працюють.
SELECT employee_name, branch_name FROM employees
FULL JOIN library_branches ON employees.branch_id = library_branches.branch_id;

-- Додайте до попереднього запиту з'єднання з третьою таблицею users, 
-- з'єднайте її по country, а потім відфільтруйте результат, 
-- щоб показати лише тих користувачів і співробітників, які проживають у США.
SELECT employee_name, branch_name FROM employees
FULL JOIN library_branches ON employees.branch_id = library_branches.branch_id
FULL JOIN users ON employees.country = users.country
WHERE employees.country = 'USA' AND users.country = 'USA';