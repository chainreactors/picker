---
title: monthly totals and grand totals using grouping sets extension
url: https://blogs.sap.com/2022/11/10/monthly-totals-and-grand-totals-using-grouping-sets-extension/
source: SAP Blogs
date: 2022-11-11
fetch_date: 2025-10-03T22:22:45.089777
---

# monthly totals and grand totals using grouping sets extension

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* monthly totals and grand total

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46067&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [monthly totals and grand total](/t5/application-development-and-automation-blog-posts/monthly-totals-and-grand-total/ba-p/13537712)

![mk3](https://avatars.profile.sap.com/5/3/id53f450f7a3eb8841f7463877e60422b7c6101e92c7c2e380299013fb111d3cec_small.jpeg "mk3")

[mk3](https://community.sap.com/t5/user/viewprofilepage/user-id/40838)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46067)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46067)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13537712)

‎2022 Nov 10
8:15 PM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46067/tab/all-users "Click here to see who gave kudos to this post.")

3,687

* SAP Managed Tags
* [SQL](https://community.sap.com/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)

* [SQL

  Programming Tool](/t5/c-khhcw49343/SQL/pd-p/122888716930844301706258287775555)

View products (1)

Hello everyone,

Many users, when looking at a query report, wish that monthly totals and grand totals are also displayed. There are a number of ways on how this can be achieved, some of which are,

1) Copy and paste the query report to a spreadsheet and use the spreadsheet inbuilt function to do the monthly total.

2) Use the inbuilt SAP function by pressing the ctrl button on the keyboard and then right clicking your mouse over the column/s to be totaled. Thereafter, filter them month by month.

3) Use union all statement.

SELECT NULL, NULL, NULL, sum ( \* ) AS total

FROM Customers

UNION ALL

SELECT City, State, NULL, sum ( \* ) AS total

FROM Customers

GROUP BY City, State

UNION ALL

SELECT NULL, NULL, CompanyName, sum ( \* ) AS total

FROM Customers

GROUP BY CompanyName;

However, it has two major drawbacks:

* The query is quite lengthy.

* The query is slow because SQL Server needs to execute all subqueries and combines the result sets into a single one.

4) Another lesser known method to get the totals and grand totals is by the use of GROUP BY extensions. The GROUP BY extensions consists of ROLLUP, CUBE and GROUPING SETS. These are used to solve the two major drawbacks that arise when using Union all statement to obtain subtotals and totals.

But first, what is GROUP BY clause?

The standard GROUP BY clause of a SELECT statement allows you to group rows in the result set according the grouping expressions you supply.

Data is aggregated for the columns provided by the GROUP BY clause. Important to note that the data will not be ordered in the GROUP BY columns and you need to explicitly order them by using the ORDER BY clause.

**Important points for the GROUP BY SQL Statement:**

* The GROUP BY clause can only be used in a SQL SELECT statement.

* The GROUP BY clause must be after the WHERE clause. (If one exists.)

* The GROUP BY clause must be before the ORDER BY clause. (If one exists.)

* To filter the GROUP BY results, you must use the HAVING clause after the GROUP BY.

* The GROUP BY clause is often used in conjunction with an aggregate function such as COUNT, MIN, MAX, AVG, or SUM.

* Each table or view column in any ***nonaggregate expression in the SELECT list must be included in the GROUP BY list***

* Except for TEXT, NTEXT, and IMAGE, any column can be called in the GROUP BY clause.

Traditionally, GROUP BY is used to aggregate data. However, ROLLUP, CUBE and GROUPING SETS extensions are used to return different aggregate values. ROLLUP will provide the aggregation in the provided order of the columns while CUBE will provide different combinations of the provided columns and GROUPING SETS has the option of aggregation in a customized manner. By using the GROUPING function, more options for the above features can be derived.

a) ROLLUP extension:

You can specify a hierarchy of grouping attributes using the ROLLUP clause.

A common requirement of many applications is to compute subtotals of the grouping attributes ***from left-to-right***, in sequence. This pattern is referred to as a hierarchy because the introduction of additional subtotal calculations produces additional rows with finer granularity of detail.

GROUP BY ROLLUP creates a group for each combination of column expressions. In addition, it "rolls up" the results into subtotals and grand totals. To do this, it moves ***from right-to-left*** decreasing the number of column expressions over which it creates groups and the aggregation(s).

The column order affects the ROLLUP output and can affect the number of rows in the result set.

For example, GROUP BY ROLLUP (col1, col2) creates groups for each combination of column expressions in the following lists.

* col1, col2

* col1 NULL

* NULL, NULL--This is the grand total

b) CUBE extension:

GROUP BY CUBE creates groups for all possible combinations of columns. For GROUP BY CUBE (col1, col2) the results have groups for unique values of

* col1, col2

* NULL, col2

* col1, NULL

* NULL, NULL--This is the grand total

c) GROUPING SETS extension:

The GROUP BY GROUPING SETS clause allows you to group your results multiple ways, without having to use multiple SELECT statements to do so.

Multiple groupings using GROUPING SETS:

SELECT City, State, CompanyName, COUNT( \* ) AS Cnt

FROM Customers

WHERE State IN ( 'MB' , 'KS' )

GROUP BY GROUPING SETS( ( City, State ), ( CompanyName ) , ( ) );

**GROUP BY GROUPING SETS ( )**

If you use an empty GROUPING SETS specification '( )' in the GROUP BY clause, this results in a grand total row for all things that are being totaled in the results. This is useful as one of the elements of a GROUPING SET.

**Correct syntax**

Grouping syntax is interpreted differently for a GROUP BY GROUPING SETS clause than it is for a simple GROUP BY clause. For example, GROUP BY (X, Y) returns results grouped by distinct combinations of X and Y values. However, GROUP BY GROUPING SETS (X, Y) specifies two individual grouping sets, and the result of the two groupings are unioned together. That is, results are grouped by (X), and then unioned to the same results grouped by (Y).

To avoid any ambiguity for complex expressions, use parentheses around each individual grouping set in the specification whenever there is a possibility for error. For example, while both of the following statements are correct and semantically equivalent, the seco...