# Write your MySQL query statement below
-- SELECT 
-- case 
-- when income < 20000 then "Low Salary"  
-- when  income between 20000 and 50000 then  "Average Salary"
-- else 
-- "High Salary"
-- end as category 
-- from accounts  ;

-- SELECT 
--     CASE 
--         WHEN income < 20000 THEN 'Low Salary'
--         WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
--         WHEN income > 50000 THEN 'High Salary'
--         ELSE '0'
--     END AS category
-- FROM Accounts;



select "Low Salary" as category,
count(*) as accounts_count
from Accounts
where income<20000
union all
select "Average Salary" ,
COUNT(*) as accounts_count
from Accounts
where income between 20000 and 50000
union all
select "High Salary",
count(*) as accounts_count
from Accounts
where income>50000;



