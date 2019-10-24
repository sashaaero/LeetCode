# https://leetcode.com/problems/human-traffic-of-stadium/
# Runtime: 186 ms, faster than 41.74% of MySQL online submissions for Human Traffic of Stadium.

select *
from stadium s
where people > 99 
and 
((exists 
    (select *
    from stadium si
    where people > 99 and id = s.id-1)
and exists
    (select *
    from stadium si
    where people > 99 and id = s.id-2))
or
(exists 
    (select *
    from stadium si
    where people > 99 and id = s.id-1)
and exists
    (select *
    from stadium si
    where people > 99 and id = s.id+1))
or
(exists 
    (select *
    from stadium si
    where people > 99 and id = s.id+1)
and exists
    (select *
    from stadium si
    where people > 99 and id = s.id+2)))