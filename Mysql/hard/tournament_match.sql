-- 1194.Tournament Winners
-- Create table If Not Exists Player (player_id int,group_id int);
-- insert into Player (player_id,group_id) values ('15', '1');
-- insert into Player (player_id,group_id) values ('25', '1');
-- insert into Player (player_id,group_id) values ('30', '1');
-- insert into Player (player_id,group_id) values ('45', '1');
-- insert into Player (player_id,group_id) values ('10', '2');
-- insert into Player (player_id,group_id) values ('35', '2');
-- insert into Player (player_id,group_id) values ('50', '2');
-- insert into Player (player_id,group_id) values ('20', '3');
-- insert into Player (player_id,group_id) values ('40', '3');

-- Create table If Not Exists Matches (match_id int,first_player int,second_player int,first_score int,second_score int);
-- insert into Matches (match_id,first_player,second_player,first_score,second_score) values ('1', '15', '45', '3', '0');
-- insert into Matches (match_id,first_player,second_player,first_score,second_score) values ('2', '30', '25', '1', '2');
-- insert into Matches (match_id,first_player,second_player,first_score,second_score) values ('3', '30', '15', '2', '0');
-- insert into Matches (match_id,first_player,second_player,first_score,second_score) values ('4', '40', '20', '5', '2');
-- insert into Matches (match_id,first_player,second_player,first_score,second_score) values ('5', '35', '50', '1', '1');

/* The winner in each group is the player who scored the maximum total points within the group.
-- -- In the case of a tie, the lowest player_id wins.
-- -- Write an SQL query to find the winner in each group. */ 

/*
Algorithm
step-1: get player-score table based on first_score and second_score respectively
step-2: based on group id, rank/order players in each group
step-3: find player with max score in each group
*/

with scores as (
    select group_id, player_id, sum(score) as score
    from (
        select p.group_id, p.player_id, m.first_score as score
        from Player p
        join Matches m
        on p.player_id = m.first_player
        union all
        select p.group_id, p.player_id, m.second_score as score
        from Player p
        join Matches m
        on p.player_id = m.second_player
    ) tmp
    group by group_id, player_id
)

select group_id, player_id
from (
    select group_id, player_id, 
        rank() over (partition by group_id order by score desc, player_id) as 'rk'
    from scores
) tt
where rk = 1
