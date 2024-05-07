-- інформація про найдорожчий продук
SELECT id, name, price FROM products
WHERE price = (SELECT MAX(price) FROM products);

-- середня ціна всіх товарів
SELECT AVG(price) FROM products;

-- сума всіх замовлень юзера з айді 1
SELECT SUM(price * quantity) FROM orders, products
WHERE customer_id=1;
