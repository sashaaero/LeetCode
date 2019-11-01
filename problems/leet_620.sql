# https://leetcode.com/problems/not-boring-movies/

select *
from cinema
where cinema.id % 2 = 1 and cinema.description <> 'boring'
order by cinema.rating desc