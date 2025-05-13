-- SQLite Online: Sales Data Analysis Queries
-- First, create and populate the orders table

-- Create table structure
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);

-- Insert sample data
INSERT INTO orders (customer, amount, order_date) VALUES
('Alice', 5000, '2024-03-01'),
('Bob', 8000, '2024-03-05'),
('Alice', 3000, '2024-03-15'),
('Charlie', 7000, '2024-02-20'),
('Alice', 10000, '2024-02-28'),
('Bob', 4000, '2024-02-10'),
('Charlie', 9000, '2024-03-22'),
('Alice', 2000, '2024-03-30');

-- Task 1: Calculate the total sales volume for March 2024
-- Expected Result: 27,000
SELECT 
    SUM(amount) as total_sales_march_2024
FROM orders
WHERE 
    order_date >= '2024-03-01' 
    AND order_date <= '2024-03-31';

-- Task 2: Find the customer who spent the most overall
-- Expected Result: Alice (20,000)
SELECT 
    customer,
    SUM(amount) as total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;

-- Alternative query for Task 2 that shows all customers ranked by spending:
SELECT 
    customer,
    SUM(amount) as total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC;

-- Task 3: Calculate the average order value for the last three months
-- Expected Result: 6,000
SELECT 
    AVG(amount) as average_order_value
FROM orders;

-- Alternative for Task 3 with more details:
SELECT 
    COUNT(*) as total_orders,
    SUM(amount) as total_sales,
    AVG(amount) as average_order_value,
    MIN(amount) as minimum_order,
    MAX(amount) as maximum_order
FROM orders;

-- Bonus queries for additional analysis:

-- Monthly sales breakdown
SELECT 
    strftime('%Y-%m', order_date) as month,
    COUNT(*) as order_count,
    SUM(amount) as monthly_total,
    AVG(amount) as monthly_average
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;

-- Customer analysis with order details
SELECT 
    customer,
    COUNT(*) as order_count,
    SUM(amount) as total_spent,
    AVG(amount) as avg_order_value,
    MIN(amount) as min_order,
    MAX(amount) as max_order
FROM orders
GROUP BY customer
ORDER BY total_spent DESC;

-- Verify all data in the table
SELECT * FROM orders
ORDER BY order_date;