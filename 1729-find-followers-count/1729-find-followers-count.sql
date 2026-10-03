# Write your MySQL query statement below
SELECT f1.user_id , COUNT(f1.follower_id) AS followers_count
FROM Followers f1
GROUP BY user_id
ORDER BY user_id