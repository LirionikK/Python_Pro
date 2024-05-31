-- SQL-запит, який виводить повний список імен усіх користувачів та працівників
SELECT user_name FROM users
UNION
SELECT employee_name FROM employees;

-- SQL-запит, який об'єднує список усіх країн, з яких є користувачі, та країн, де працюють працівники
SELECT country FROM users
UNION
SELECT country FROM employees;

-- SQL-запит, який виводить імена, які є і серед користувачів, і серед працівників
SELECT user_name FROM users
INTERSECT
SELECT employee_name FROM employees;

-- SQL-запит, який виводить країни, з яких є як користувачі, так і працівники
SELECT country FROM users
INTERSECT
SELECT country FROM employees;

-- SQL-запит, який виводить імена користувачів, які не використовуються працівниками
SELECT user_name FROM users
EXCEPT
SELECT employee_name FROM employees;

-- SQL-запит, який виводить країни, з яких є користувачі, але не працівники
SELECT country FROM users
EXCEPT
SELECT country FROM employees;