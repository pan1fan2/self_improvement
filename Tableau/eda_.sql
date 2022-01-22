use sales;
-- select d.year year, sum(tr.sales_amount) sum
-- from transactions tr
-- join date d
-- on tr.order_date = d.date
-- GROUP BY d.year;

SELECT DISTINCT product_code from transactions where market_code = 'Mark001';


-- Show total revenue in year 2020, January Month
SELECT SUM(tr.sales_amount) 
FROM transactions tr
INNER JOIN date d
ON tr.order_date = d.date 
where d.year=2020 and d.month_name="January" and (tr.currency="INR" or tr.currency="USD");

-- Show total revenue in year 2020 in Chennai
SELECT SUM(transactions.sales_amount) 
FROM transactions 
INNER JOIN date 
ON transactions.order_date=date.date 
where date.year=2020 and transactions.market_code="Mark001";