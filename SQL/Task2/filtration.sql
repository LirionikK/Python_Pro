-- всі продукти дорожче за 500
SELECT id, name, price FROM products WHERE price>=500;

-- всі замовлення, які були створені після 1 січня 24 року
SELECT id, customer_id, product_id, order_date FROM orders WHERE order_date>'2024-01-01';

-- всі замовлення, де кількість товарів більша за 1
SELECT id, customer_id, product_id, order_date FROM orders WHERE quantity>1;

-- всі постачальники в кого людина для звʼязку - "Vlad Ushakov"
SELECT id, name, contact_name FROM suppliers WHERE contact_name='Vlad Ushakov';