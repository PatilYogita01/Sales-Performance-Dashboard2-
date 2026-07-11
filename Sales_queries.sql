-- ============================================
-- Sales Performance Dashboard SQL Queries
-- ============================================

-- 1. View Complete Dataset
SELECT * FROM sales;

-- 2. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;

-- 3. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM sales;

-- 4. Total Orders
SELECT COUNT(Order_ID) AS Total_Orders
FROM sales;

-- 5. Average Sales Per Order
SELECT ROUND(AVG(Sales),2) AS Average_Sales
FROM sales;

-- 6. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM sales;

-- 7. Sales by Region
SELECT Region,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 8. Profit by Region
SELECT Region,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 9. Sales by Category
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 10. Profit by Category
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 11. Top 10 Products by Sales
SELECT Product,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 10;

-- 12. Top 10 Customers by Sales
SELECT Customer_Name,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 13. Monthly Sales Trend
SELECT MONTH(Order_Date) AS Month,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY MONTH(Order_Date)
ORDER BY Month;

-- 14. Monthly Profit Trend
SELECT MONTH(Order_Date) AS Month,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY MONTH(Order_Date)
ORDER BY Month;

-- 15. Highest Selling Product
SELECT Product,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 1;

-- 16. Highest Profit Region
SELECT Region,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;

-- 17. Customer Purchase Summary
SELECT Customer_Name,
       COUNT(Order_ID) AS Orders,
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;

-- 18. Product-wise Quantity Sold
SELECT Product,
       SUM(Quantity) AS Quantity_Sold
FROM sales
GROUP BY Product
ORDER BY Quantity_Sold DESC;

-- 19. Average Profit by Category
SELECT Category,
       ROUND(AVG(Profit),2) AS Average_Profit
FROM sales
GROUP BY Category;

-- 20. Profit Margin
SELECT
ROUND((SUM(Profit)/SUM(Sales))*100,2) AS Profit_Margin_Percentage
FROM sales;
