-- Get student id, name and avg score
select a.s_id, a.s_name,b.avg_score
from student a
join 
(select s_id,avg(s_score) as avg_score 
from score
group by s_id having avg_score >= 85) as b
using (s_id);

