-- Create table If Not Exists Ads (ad_id int, user_id int, action enum('Clicked', 'Viewed', 'Ignored'));
-- insert into Ads (ad_id, user_id,action) values ('1', '1', 'Clicked');
-- insert into Ads (ad_id, user_id,action) values ('2', '2', 'Clicked');
-- insert into Ads (ad_id, user_id,action) values ('3', '3', 'Viewed');
-- insert into Ads (ad_id, user_id,action) values ('5', '5', 'Ignored');
-- insert into Ads (ad_id, user_id,action) values ('1', '7', 'Ignored');
-- insert into Ads (ad_id, user_id,action) values ('2', '7', 'Viewed');
-- insert into Ads (ad_id, user_id,action) values ('3', '5', 'Clicked');
-- insert into Ads (ad_id, user_id,action) values ('1', '4', 'Viewed');
-- insert into Ads (ad_id, user_id,action) values ('2', '11', 'Viewed');
-- insert into Ads (ad_id, user_id,action) values ('1', '2', 'Clicked');

-- A company is running Ads and wants to calculate the performance of each Ad.
-- Performance of the Ad is measured using Click-Through Rate (CTR) where:
-- ctr = 0 if Number of clicks for ad + Number of Views for ad = 0
-- ctr = (Number of clicks) / (Number of clicks + Number of view)
-- Write an SQL query to find the ctr of each Ad.
-- Round ctr to 2 decimal points. Order the result table by ctr in descending order and by ad_id in ascending order in case of a tie.

-- have to join the original table, otherwise the ad_id =5 is excluded 
select DISTINCT ad_id,ifnull(ctr,0.00) ctr
from ads
left join(
select ad_id, round(100 * sum(case when action = 'Clicked' then 1 else 0 end)/count(*),2) ctr
from ads
where action in ('Clicked','Viewed')
group by ad_id) temp
using(ad_id)
ORDER BY ctr desc;

-- Ref.
select ad_id, ifnull(round(100*clicked/total,2),0.00) ctr
from
(select ad_id, sum(case when action in ('Clicked') then 1 else 0 end) as clicked
from ads
group by ad_id) as cl
join
(
Select ad_id, sum(case when action in ('Clicked','Viewed') then 1 else 0 end) as total
from ads
group by ad_id) as tot
using(ad_id)
order by ctr desc;


