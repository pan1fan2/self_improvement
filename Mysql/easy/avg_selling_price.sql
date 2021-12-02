-- drop table if exists Prices;
-- drop table if exists UnitsSold;
-- Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
-- Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28',5);
-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22',20);
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20',15);
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31',30);
-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', 100);
-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', 15);
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', 200);
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', 30);


-- Write an SQL query to find the average selling price for each product.
-- average_price should be rounded to 2 decimal places.
-- The query result format is in the following example:
select product_id, round(sum(total)/sum(units),2) avg_price
from 
(select product_id, price, units, price*units as total
from Prices
join UnitsSold
using (product_id)
where UnitsSold.purchase_date between Prices.start_date and Prices.end_date) as temp
group by product_id;