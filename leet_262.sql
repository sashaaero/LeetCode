# https://leetcode.com/problems/trips-and-users/
# Runtime: 191 ms, faster than 73.16% of MySQL online submissions for Trips and Users.
select distinct Request_at Day,
     round ((select count(*)
     from Trips join Users Clients on Client_Id = Clients.Users_Id
     where Request_at = t.Request_at
     and Clients.Banned = "No"
     and Status like "ca%") /
     (select count(*)
     from Trips join Users Clients on Client_Id = Clients.Users_Id
     where Request_at = t.Request_at
     and Clients.Banned = "No"
     ), 2)
      `Cancellation Rate`
from Trips t
where Request_at between "2013-10-01" and "2013-10-03";