# Write your MySQL query statement below
Select E1.employee_id,E1.name,count(E2.employee_id) as reports_count,ROUND(avg(E2.age)) as  average_age

From Employees E1 INNER JOIN Employees E2
on E1.employee_id=E2.reports_to
group by E1.employee_id ,E1.name
order by employee_id ;