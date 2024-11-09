
use AdventureWorks2019;
-- TASK1A
-- 1.	provides information about product’s subcategory, product’s colour and total sales value; please do not use pivoting here – this will be our base query for the pivot.
SELECT
    PS.Name AS [Product Sub Category Name],
    P.Color,
    SUM(SOD.UnitPrice * SOD.OrderQty) AS TotalSalesValue
FROM
    Production.Product AS P 
INNER JOIN 
    Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID 
INNER JOIN 
    Sales.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID 
GROUP BY 
    PS.Name,		
	P.Color;

	-- 2.	provides information about total sales value for different colours of different product subcategories; please put colours on columns, products’ subcategory names on rows, and total sales value as values; use the query from the previous point.
	SELECT 
    [Product Sub Category Name],
    COALESCE([Red], 0) AS [Red], 
    COALESCE([Blue], 0) AS [Blue], 
    COALESCE([Yellow], 0) AS [Yellow], 
    COALESCE([Black], 0) AS [Black], 
    COALESCE([White], 0) AS [White],
    COALESCE([Grey], 0) AS [Grey],
    COALESCE([Multi], 0) AS [Multi],
    COALESCE([Silver], 0) AS [Silver],
    COALESCE([Silver/Black], 0) AS [Silver/Black]
FROM 
    (SELECT
        PS.Name AS [Product Sub Category Name],
        P.Color,
        SUM(SOD.UnitPrice * SOD.OrderQty) AS TotalSalesValue
    FROM
        Production.Product AS P
    INNER JOIN 
        Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID 
    INNER JOIN 
        Sales.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID 
    GROUP BY 
        PS.Name,
        P.Color) AS SourceTable
PIVOT 
    (SUM(TotalSalesValue) 
     FOR Color IN ([Red], [Blue], [Green], [Yellow], [Black], [White], [Grey],[Multi],[Silver],[Silver/Black])) AS PivotTable;

	 --a.	please prepare a version of this query, where only subcategories from category Bike are presented.
	 SELECT 
    [Product Sub Category Name],
    COALESCE([Red], 0) AS [Red], 
    COALESCE([Blue], 0) AS [Blue], 
    COALESCE([Yellow], 0) AS [Yellow], 
    COALESCE([Black], 0) AS [Black], 
    COALESCE([White], 0) AS [White],
    COALESCE([Grey], 0) AS [Grey],
    COALESCE([Multi], 0) AS [Multi],
    COALESCE([Silver], 0) AS [Silver],
    COALESCE([Silver/Black], 0) AS [Silver/Black]
FROM 
    (SELECT
        PS.Name AS [Product Sub Category Name],
        P.Color,
        SUM(SOD.UnitPrice * SOD.OrderQty) AS TotalSalesValue
    FROM
        Production.Product AS P
    INNER JOIN 
        Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID 
	INNER JOIN 
        Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID 
    INNER JOIN 
        Sales.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID 
    WHERE
        PC.Name = 'Bikes'  
    GROUP BY 
        PS.Name,
        P.Color) AS SourceTable
PIVOT 
    (SUM(TotalSalesValue) 
     FOR Color IN ([Red], [Blue], [Green], [Yellow], [Black], [White], [Grey],[Multi],[Silver],[Silver/Black])) AS PivotTable;

	

*/
--TASK 1B
/*
1.	provides different product’s price categories:
a.	ListPrice < 20.00 – Inexpensive
b.	20.00 < ListPrice < 75.00 – Regular
c.	75 < ListPrice < 750.00 – High
d.	750.00 < ListPrice – Expensive
*/
SELECT 
    P.ProductID, 
    P.Name AS ProductName,
    PC.Name AS [Product Category Name], 
    PS.Name AS [Product SubCategory Name], 
    P.Color,
    P.Weight,
    SOH.Status,
    SOH.SalesOrderID AS [SalesOrderID],
    YEAR(SOH.OrderDate) AS [Year], 
    MONTH(SOH.OrderDate) AS [Month],
    DAY(SOH.OrderDate) AS "Day",
    SUM(SOD.OrderQty) AS [Volume],
    SUM(SOD.LineTotal) AS [Sales Amount],
    COUNT(DISTINCT SOD.SalesOrderID) AS [Number of Orders],
	P.ListPrice,
    CASE 
        WHEN AVG(P.ListPrice) < 20.00 THEN 'Inexpensive'
        WHEN AVG(P.ListPrice) >= 20.00 AND AVG(P.ListPrice) < 75.00 THEN 'Regular'
        WHEN AVG(P.ListPrice) >= 75.00 AND AVG(P.ListPrice) < 750.00 THEN 'High'
        ELSE 'Expensive'
    END AS PriceCategory
FROM 
    Production.Product AS P
INNER JOIN 
    Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID
INNER JOIN 
    Production.ProductCategory AS PC ON PS.ProductCategoryID = PC.ProductCategoryID
INNER JOIN
    Sales.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID
INNER JOIN 
    Sales.SalesOrderHeader AS SOH ON SOH.SalesOrderID = SOD.SalesOrderID
GROUP BY
    P.ProductID, 
    P.Name, 
    PC.Name, 
    PS.Name, 
    P.Color,
    P.Weight, 
    P.ListPrice, -- Include ListPrice column here
    SOH.Status, 
    SOH.SalesOrderID,
    YEAR(SOH.OrderDate),
    MONTH(SOH.OrderDate),
    DAY(SOH.OrderDate);

	
	-- 2.	provides information about total volume of product for different price categories and different product categories – use price categories in columns, product categories in rows, and total volume as values (0 - never sold a product from a given category); please use CASE to put years on columns
	
	SELECT 
    [Product Category Name],
    [Year],
    COALESCE([Inexpensive], 0) AS [Inexpensive],
    COALESCE([Regular], 0) AS [Regular],
    COALESCE([High], 0) AS [High],
    COALESCE([Expensive], 0) AS [Expensive]
FROM (
    SELECT
        PC.Name AS [Product Category Name],
        YEAR(SOH.OrderDate) AS [Year],
        CASE
            WHEN P.ListPrice < 20.00 THEN 'Inexpensive'
            WHEN P.ListPrice >= 20.00 AND P.ListPrice < 75.00 THEN 'Regular'
            WHEN P.ListPrice >= 75.00 AND P.ListPrice < 750.00 THEN 'High'
            ELSE 'Expensive' 
        END AS [Price Category],
        SOD.OrderQty AS [Total Volume]
    FROM
        Production.Product AS P 
        INNER JOIN Sales.SalesOrderDetail AS SOD ON P.ProductID = SOD.ProductID 
        INNER JOIN Sales.SalesOrderHeader AS SOH ON SOD.SalesOrderID = SOH.SalesOrderID 
        INNER JOIN Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID 
        INNER JOIN Production.ProductCategory AS PC ON PS.ProductCategoryID = PC.ProductCategoryID 
) AS SourceData
PIVOT (
    SUM([Total Volume])
    FOR [Price Category] IN ([Inexpensive], [Regular], [High], [Expensive])
) AS PivotTable
ORDER BY 
    [Product Category Name],
    [Year];


	--TASK1c

	-- 1.	provides total sales amount for different product categories along with a total value of sales for all categories.

SELECT 
    COALESCE(PC.Name, 'Products with a null category') AS [Product Category],
    SUM(SOD.UnitPrice * SOD.OrderQty) AS [Total Sales Amount]
FROM 
    Sales.SalesOrderDetail AS SOD
INNER JOIN 
    Production.Product AS P ON SOD.ProductID = P.ProductID
INNER JOIN 
    Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID
INNER JOIN 
    Production.ProductCategory AS PC ON PS.ProductCategoryID = PC.ProductCategoryID
GROUP BY 
    ROLLUP (PC.Name);

	-- 2.	provides total sales amount for each product category and color of products (include also products without specified color), for each color, total for each category and total sales amount:
	SELECT 
    COALESCE(PC.Name, 'TotalSalesAmount of AllCategories') AS [Product Category],
    COALESCE(P.Color, 'No Color Specified') AS [Product Color],
    SUM(SOD.UnitPrice * SOD.OrderQty) AS [Total Sales Amount]
FROM 
    Production.Product AS P
INNER JOIN 
    Production.ProductSubcategory AS PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID
INNER JOIN 
    Production.ProductCategory AS PC ON PS.ProductCategoryID = PC.ProductCategoryID
LEFT JOIN
	Sales.SalesOrderDetail SOD ON P.ProductID = sod.ProductID 
GROUP BY 
    PC.Name, P.Color WITH ROLLUP;

	-- 2a.	Please use grouping function to identify the total sales amount from the sales amount for products without specified color:

	SELECT
    pc.Name AS [Product Category Name],
    COALESCE(p.Color, 'No Color Specified') AS [Product Color],
    SUM(sod.UnitPrice * sod.OrderQty) AS [Total Sales Amount]
FROM
    Production.Product AS p
    INNER JOIN Production.ProductSubcategory AS ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID 
    INNER JOIN Production.ProductCategory AS pc ON ps.ProductCategoryID = pc.ProductCategoryID 
    LEFT JOIN Sales.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID 
GROUP BY 
    GROUPING SETS (
        (PC.Name, P.Color),
        (PC.Name)
    )
HAVING
    P.Color IS NULL;

	--1C 3.	provides total sales amount for different products (use product’s name) in different product categories and subcategories – please provide sales summaries for each category and subcategory and a total value.
SELECT 
    (CASE
                WHEN PS.Name IS NULL THEN PC.Name
                ELSE PS.Name
            END) AS [Product Subcategory Name],
    PC.Name AS [Product Category Name],
    P.Name AS [Product Name],
    SUM(SOD.UnitPrice * SOD.OrderQty) AS [Total Sales Amount]
FROM 
    Production.Product AS p
LEFT JOIN 
    Production.ProductSubcategory AS ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID 
LEFT JOIN 
    Production.ProductCategory AS pc ON ps.ProductCategoryID = pc.ProductCategoryID 
INNER JOIN 
    Sales.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID 
GROUP BY 
    GROUPING SETS (
        (PC.Name, P.Name, PS.Name),
        (PC.Name, P.Name),
		(PC.Name)
    );


	-- TASK2
-- 	1.	Prepare the report without using windowed functions (OVER clause)

SELECT
    CONCAT(p.FirstName, ' ', p.LastName) AS [Sales Person Name],
    soh.SalesPersonID AS [Employee ID],
    YEAR(soh.OrderDate) AS [Year],
    SUM(sod.UnitPrice * sod.OrderQty) AS [Sub Total],
    COUNT(DISTINCT soh.SalesOrderID) AS [Number of Orders]
FROM
    Sales.SalesOrderHeader soh
    INNER JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID 
    INNER JOIN Person.Person p ON soh.SalesPersonID = p.BusinessEntityID
GROUP BY
    CONCAT(p.FirstName, ' ', p.LastName),
    soh.SalesPersonID,
    YEAR(soh.OrderDate)
ORDER BY
    [Employee ID],
    [Year];


-- 2.	Prepare the report using windowed functions (OVER clause)
SELECT
    [Sales Person Name],
    [Employee ID],
    [Year],
    SUM([Sub Total]) OVER (PARTITION BY [Employee ID], [Year]) AS [Sub Total],
    COUNT([Sub Total]) OVER (PARTITION BY [Employee ID], [Year]) AS [Number of Orders]
FROM (
    SELECT
        CONCAT(p.FirstName, ' ', p.LastName) AS [Sales Person Name],
        soh.SalesPersonID AS [Employee ID],
        YEAR(soh.OrderDate) AS [Year],
        SUM(sod.UnitPrice * sod.OrderQty) AS [Sub Total]
    FROM
        Sales.SalesOrderHeader soh
        INNER JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID 
        INNER JOIN Person.Person p ON soh.SalesPersonID = p.BusinessEntityID
    GROUP BY
        CONCAT(p.FirstName, ' ', p.LastName),
        soh.SalesPersonID,
        YEAR(soh.OrderDate)
) AS SalesData
ORDER BY
    [Employee ID],
    [Year];



	--2.3.	Prepare the report by using CTE, where first you aggregate the sales data to establish yearly performance metrices, and only then attaching the details of the sales person 

	WITH SalesSummary AS (
    SELECT
        soh.SalesPersonID AS [Employee ID],
        YEAR(soh.OrderDate) AS [Year],
        SUM(sod.UnitPrice * sod.OrderQty) AS [Sub Total],
        COUNT(DISTINCT soh.SalesOrderID) AS [Number of Orders]
    FROM
        Sales.SalesOrderHeader soh
        INNER JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID 
    GROUP BY
        soh.SalesPersonID,
        YEAR(soh.OrderDate)
),
SalesData AS (
    SELECT
        CONCAT(p.FirstName, ' ', p.LastName) AS [Sales Person Name],
        ss.[Employee ID],
        ss.[Year],
        ss.[Sub Total],
        ss.[Number of Orders]
    FROM
        SalesSummary ss
        INNER JOIN Person.Person p ON ss.[Employee ID] = p.BusinessEntityID
)
SELECT
    [Sales Person Name],
    [Employee ID],
    [Year],
    [Sub Total],
    [Number of Orders]
FROM
    SalesData
ORDER BY
    [Employee ID],
    [Year];