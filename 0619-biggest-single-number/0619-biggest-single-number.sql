# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN 
(SELECT DISTINCT(num) AS f
FROM MyNumbers
GROUP BY num
HAVING COUNT(num)=1)

