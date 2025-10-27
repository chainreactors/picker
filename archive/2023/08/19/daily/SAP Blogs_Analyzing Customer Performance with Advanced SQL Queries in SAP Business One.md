---
title: Analyzing Customer Performance with Advanced SQL Queries in SAP Business One
url: https://blogs.sap.com/2023/08/18/analyzing-customer-performance-with-advanced-sql-queries-in-sap-business-one/
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T11:59:40.050018
---

# Analyzing Customer Performance with Advanced SQL Queries in SAP Business One

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Analyzing Customer Performance with Advanced SQL Q...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/69120&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Analyzing Customer Performance with Advanced SQL Queries in SAP Business One](/t5/enterprise-resource-planning-blog-posts-by-members/analyzing-customer-performance-with-advanced-sql-queries-in-sap-business/ba-p/13579652)

![shahmed](https://avatars.profile.sap.com/d/1/idd1028f20bb172035d8c84924ef6c7f2b4a80a2e1f780fcfa28c3bf317b7cc59e_small.jpeg "shahmed")

[shahmed](https://community.sap.com/t5/user/viewprofilepage/user-id/423987)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=69120)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/69120)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13579652)

‎2023 Aug 31
9:14 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/69120/tab/all-users "Click here to see who gave kudos to this post.")

2,259

* SAP Managed Tags
* [SQL](https://community.sap.com/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SQL

  Programming Tool](/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)

View products (2)

With businesses that continue to grow and automation of processes is taking place, it is important to take a deep dive to gain insights into customer’s behaviour and its performance that can have a significant impact on the outcome on the business. SAP Business One has that flexibility and it also provides tools to extract key information from our data that can help us make informed decisions. Through this blog, we will try to explore and advanced SQL query that can help us analyze different aspects of business partner.

**Introduction:**Businesses pay utmost importance on customer relationship and utilise that effectively for their business growth and success. SAP Business one allows us to dig deep into our customer data which helps us understand the purchasing behaviour, their credit utilization, payment terms and average pay days. In this below discussion, we will try to go through a comprehensive SQL query that allows us to have insights into customer patterns.

**The Query:**

```
-- Declare the period of analysis

DECLARE @StDt DateTime

DECLARE @EndDt DateTime

-- Define/Set the start and end dates for the analysis

SET @StDt = DATEFROMPARTS(YEAR(GETDATE()), 1, 1) -- Start of the current year

SET @EndDt = GETDATE() -- Current date

-- Calculate the average pay days using a Common Table Expression (CTE)

;WITH AvgDaysToPay AS (

SELECT

T4.CardCode,

T4.CardName,

AVG(CASE WHEN T4.DocDate = T1.DocDate THEN 0  -- Same day payment, 0 days to pay

ELSE DATEDIFF(DAY, T4.DocDate, T1.DocDate)

END) AS 'AverageDaysToPay'

FROM OCRD T0

INNER JOIN ORCT T1 ON T0.CardCode = T1.CardCode

INNER JOIN RCT2 T3 ON T3.DocNum = T1.DocNum

INNER JOIN OINV T4 ON T4.DocEntry = T3.DocEntry AND T3.InvType = '13'

WHERE

(T4.DocDate BETWEEN @StDt AND @EndDt)

GROUP BY T4.CardCode, T4.CardName),

-- Subquery that calculates AvgDaysToDN and AvgDaysToInvoice

-- This query is not time restricted

OrderDeliveryInvoice AS (

SELECT DISTINCT

T7.Cardcode,

T3.[DocDate] AS OrderDate,

T5.DocDate AS DeliveryNoteDate,

T7.Docdate AS InvoiceDate

FROM OPKL T0

right outer JOIN PKL1 T1 ON T0.AbsEntry = T1.AbsEntry

right outer JOIN RDR1 T2 ON T2.LineNum = T1.OrderLine AND T1.OrderEntry = T2.DocEntry AND T1.BaseObject = 17

right outer JOIN ORDR T3 ON T3.DocEntry = T2.DocEntry

LEFT outer JOIN DLN1 T4 ON T4.BaseEntry = T2.DocEntry AND T4.BaseLine = T2.LineNum AND T4.BaseType = T3.ObjType

LEFT outer JOIN ODLN T5 ON T5.DocEntry = T4.DocEntry

LEFT outer JOIN INV1 T6 ON T6.BaseEntry = T4.DocEntry AND T6.BaseLine = T4.LineNum AND T6.BaseType = T5.ObjType

LEFT outer JOIN OINV T7 ON T7.DocEntry = T6.DocEntry

WHERE  T3.[CANCELED] = 'N'  AND T7.Cardcode IS NOT NULL )

-- Main query that analyzes customer performance and join with the subquery

SELECT

T2.CardCode [Customer Code],

T2.CardName [Customer Name],

RANK() OVER (ORDER BY ISNULL((ArInvoices.ArcLineTotal - ISNULL(ArCredits.ArcLineTotal, 0)), 0) DESC) AS CustomerRank,

T3.GroupName [Group Name],   T2.[CreditLine] AS [Credit Limit],

(ISNULL((SELECT SUM(Balance) FROM OCRD WHERE CardCode = T2.CardCode), 0) / NULLIF(T2.[CreditLine], 0)) * 100 [Credit Utilization %],

T1.PymntGroup AS [Payment Terms],   T2.[Currency],

T4.SlpName [Sales Employee Name],

ISNULL((SELECT SUM(Balance) FROM OCRD WHERE CardCode = T2.CardCode), 0) [Current Receivables],

CASE

WHEN ISNULL(ArInvoices.ArcLineTotal, 0) = 0 THEN NULL

ELSE CAST(CEILING((ISNULL((SELECT SUM(Balance) FROM OCRD WHERE CardCode = T2.CardCode), 0) / ISNULL(ArInvoices.ArcLineTotal, 0)) * DATEDIFF(DAY, @StDt, @EndDt)) AS INT)

END [Accounts Receivable Days],

AvgDaysToPay.AverageDaysToPay,

ISNULL(ArInvoices.ArcLineCount, 0) [A/R Invoices],

ISNULL(ArCredits.ArcLineCount, 0) [A/R Credits],

ISNULL((ISNULL(ArInvoices.ArcLineTotal, 0) - ISNULL(ArCredits.ArcLineTotal, 0)), 0) [Total Net Sales],

ISNULL((ISNULL(ArInvoices.ArcGrssProfit, 0) - ISNULL(ArCredits.ArcGrssProfit, 0)), 0) [Gross Profit],

CASE

WHEN ArInvoices.ArcLineCount = 0 THEN NULL

ELSE (ISNULL((ISNULL(ArInvoices.ArcGrssProfit, 0) - ISNULL(ArCredits.ArcGrssProfit, 0)), 0) / NULLIF((ISNULL(ArInvoices.ArcLineTotal, 0) - ISNULL(ArCredits.ArcLineTotal, 0)), 0)) * 100

END [Gross Profit %],

OrderDeliveryAvg.AvgDaysToDN,

OrderDeliveryAvg.AvgDaysToInvoice

FROM

[dbo].[OCRD] T2

LEFT JOIN [dbo].[OCRG] T3 ON T2.GroupCode = T3.GroupCode

LEFT JOIN [dbo].[OSLP] T4 ON T2.SlpCode = T4.SlpCode

LEFT JOIN [dbo].[OCTG] T1 ON T2.GroupNum = T1.GroupNum

LEFT JOIN (

-- Subquery that calculates total AR invoices and their attributes

SELECT

T0.CardCode,

COUNT(DISTINCT T0.DocNum) AS ArcLineCount,

SUM(CASE WHEN (T1.[Quantity] = 0 AND (T1.[StockPrice] * T1.[Quantity]) = 0)

THEN T1.[LineTotal] ELSE (T1.[INMPrice] * T1.[Quantity]) END) AS ArcLineTotal,

SUM(T1.GrssProfit) AS ArcGrssProfit

FROM

[dbo].[OINV] T0

INNER JOIN [dbo].[INV1] T1 ON T0.DocEntry = T1.DocEntry

WHERE

T0.DocDate BETWEEN @StDt AND @EndDt

AND T0.[CANCELED] = 'N'

GROUP BY

T0.CardCode  ) ArInvoices ON T2.CardCode = ArInvoices.CardCode

LEFT JOIN (

-- Subquery that calculates the total AR credits and their attributes

SELECT

T0.CardCode,

COUNT(DISTINCT T0.DocNum) AS ArcLineCount,

SUM(CASE WHEN (T1.[Quantity] = 0 AND (T1.[StockPrice] * T1.[Quantity]) = 0)

THEN T1.[LineTotal] ELSE (T1.[INMPrice] * T1.[Quantity]) END) AS ArcLineTotal,

SUM(T1.GrssProfit) AS ArcGrssProfit

FROM

[dbo].[ORIN] T0

INNER JOIN [dbo].[RIN1] T1 ON T0.DocEntry = T1.DocEntry

WHERE

T0.DocDate BETWEEN @StDt AND @EndDt

AND T0.[CANCELED] = 'N'

GROUP BY

T0.CardCode

) ArCredits ON T2.C...