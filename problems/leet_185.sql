/* https://leetcode.com/problems/department-top-three-salaries/ */
/* Runtime: 766 ms, faster than 78.08% of MS SQL Server online submissions for Department Top Three Salaries. */
select d.Name Department, e.Name Employee, Salary
from Employee e join Department d on e.DepartmentId = d.Id
where Salary in (
    select distinct top 3 Salary 
    from Employee 
    where DepartmentId = d.Id
    order by Salary desc   
    )

