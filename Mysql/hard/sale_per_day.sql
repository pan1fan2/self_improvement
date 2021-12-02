-- drop table If Exists Orders;
-- Create table If Not Exists Orders (order_id int,customer_id int,order_date date,item_id varchar(30), quantity int);
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('1', '1', '2020-06-01', '1', '10');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('2', '1', '2020-06-08', '2', '10');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('3', '2', '2020-06-02', '1', '5');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('4', '3', '2020-06-03', '3', '5');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('5', '4', '2020-06-04', '4', '1');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('6', '4', '2020-06-05', '5', '5');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('7', '5', '2020-06-05', '1', '10');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('8', '5', '2020-06-14', '4', '5');
-- insert into Orders (order_id,customer_id,order_date,item_id,quantity) values ('9', '5', '2020-06-21', '3', '5');

-- Create table If Not Exists Items (item_id varchar(30),item_name varchar(30),item_category varchar(30));
-- insert into Items (item_id,item_name,item_category) values ('1', 'LC Alg. Book', 'Book');
-- insert into Items (item_id,item_name,item_category) values ('2', 'LC DB. Book', 'Book');
-- insert into Items (item_id,item_name,item_category) values ('3', 'LC SmarthPhone', 'Phone');
-- insert into Items (item_id,item_name,item_category) values ('4', 'LC Phone 2020', 'Phone');
-- insert into Items (item_id,item_name,item_category) values ('5', 'LC SmartGlass', 'Glasses');
-- insert into Items (item_id,item_name,item_category) values ('6', 'LC T-Shirt XL', 'T-Shirt');

-- You are the business owner and would like to obtain a sales report for category items and day of the week.
-- On Monday (2020-06-01, 2020-06-08) were sold a total of 20 units (10 + 10) in the category Book (ids: 1, 2).
-- On Tuesday (2020-06-02) were sold a total of 5 units  in the category Book (ids: 1, 2).
-- On Wednesday (2020-06-03) were sold a total of 5 units in the category Phone (ids: 3, 4).
-- On Thursday (2020-06-04) were sold a total of 1 unit in the category Phone (ids: 3, 4).
-- On Friday (2020-06-05) were sold 10 units in the category Book (ids: 1, 2) and 5 units in Glasses (ids: 5).
-- On Saturday there are no items sold.
-- On Sunday (2020-06-14, 2020-06-21) were sold a total of 10 units (5 +5) in the category Phone (ids: 3, 4).
-- There are no sales of T-Shirt.

-- testing
-- select * , case when dayname(order_date)='Friday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Friday
-- from orders 
-- right join items 
-- using (item_id)

-- key
with t1 as(
select distinct item_category,
case when dayname(order_date)='Monday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Monday,
Case when dayname(order_date)='Tuesday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Tuesday,
Case when dayname(order_date)='Wednesday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Wednesday,
Case when dayname(order_date)='Thursday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Thursday,
Case when dayname(order_date)='Friday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Friday,
Case when dayname(order_date)='Saturday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Saturday,
Case when dayname(order_date)='Sunday' then sum(quantity) over(partition by item_category,dayname(order_date)) else 0 end as Sunday
from orders o
right join items i
using (item_id))

select item_category as category, sum(Monday) as Monday, sum(Tuesday) as Tuesday, sum(Wednesday) Wednesday, sum(Thursday) Thursday,
sum(Friday) Friday, sum(Saturday) Saturday, sum(Sunday) Sunday
from t1
group by item_category;


