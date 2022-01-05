-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key of this table.
-- This table shows the activity of players of some game.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.

-- Create table If Not Exists Activity (player_id int,device_id int,event_date date,games_played int);
-- insert into Activity (player_id,device_id,event_date,games_played) values ('1', '2', '2016-03-01', '5');
-- insert into Activity (player_id,device_id,event_date,games_played) values ('1', '2', '2016-05-02', '6');
-- insert into Activity (player_id,device_id,event_date,games_played) values ('2', '3', '2017-06-25', '1');
-- insert into Activity (player_id,device_id,event_date,games_played) values ('3', '1', '2016-03-02', '0');
-- insert into Activity (player_id,device_id,event_date,games_played) values ('3', '4', '2018-07-03', '5');

/* Question 511: Write an sql query that reports the first login data for each player */
select player_id, min(event_date) as first_login
from Activity
group by player_id;

/* Question 512: Write an sql query that reports the device that is first logged in for each player */
-- Approach 1:
-- select ac.player_id, Activity.device_id
-- from Activity
-- join 
-- (
-- select player_id, min(event_date) as first_login
-- from Activity
-- group by player_id
-- order by first_login) ac
-- on ac.player_id = Activity.player_id
-- where Activity.event_date =ac.first_login

-- Approach 2:
select player_id,device_id
from
	(select player_id,device_id,
	rank() over(partition by player_id order by event_date) as rnk
	from Activity) tmp
where rnk = 1;

/* Q534: Write an SQL query that reports for each player and date, how many games played so far by the player. 
That is, the total number of games played by the player until that date. Check the example for clarity.*/
SELECT player_id, event_date,
SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity;

/* Q550: Write an SQL query that reports the fraction of players that logged in again on the day after the day they first logged in, 
rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days 
starting from their first login date, then divide that number by the total number of players.*/
-- Upate table info.
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE Activity
-- SET event_date = '2016-03-02'
-- WHERE
--    player_id = 1 AND
--    games_played = 6;
-- SET SQL_SAFE_UPDATES = 1;

-- ignore!
-- SELECT player_id,event_date,
-- LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS leadDate,
-- LAG(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS lagDate
-- FROM Activity

SELECT ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id), 2) AS fraction FROM Activity AS a
LEFT JOIN
(SELECT player_id, MIN(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS first_login FROM Activity) AS b
ON a.player_id = b.player_id
and DATEDIFF(a.event_date, b.first_login) = 1;






