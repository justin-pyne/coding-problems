-- Answer:
-- Answer in the case of only 1 max order_number
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1

--Answer in the case of multiple max order_nu,ber
WITH o AS
(
    SELECT customer_number, COUNT(order_number) AS orderNum
    FROM Orders
    GROUP BY customer_number
)

SELECT customer_number
FROM o
WHERE orderNum IN (SELECT MAX(orderNum) FROM o)



-- Prompt:
-- Table: Orders

-- +-----------------+----------+
-- | Column Name     | Type     |
-- +-----------------+----------+
-- | order_number    | int      |
-- | customer_number | int      |
-- +-----------------+----------+
-- order_number is the primary key for this table.
-- This table contains information about the order ID and the customer ID.
 

-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Orders table:
-- +--------------+-----------------+
-- | order_number | customer_number |
-- +--------------+-----------------+
-- | 1            | 1               |
-- | 2            | 2               |
-- | 3            | 3               |
-- | 4            | 3               |
-- +--------------+-----------------+
-- Output: 
-- +-----------------+
-- | customer_number |
-- +-----------------+
-- | 3               |
-- +-----------------+
-- Explanation: 
-- The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
-- So the result is customer_number 3.
 

-- Follow up: What if more than one customer has the largest number of orders, can you find all the customer_number in this case?