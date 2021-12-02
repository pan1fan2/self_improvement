Select actor_id, director_id, count(*) as count
from actordirector
group by actor_id, director_id
having count >=3