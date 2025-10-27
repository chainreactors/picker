---
title: Difference between $skip and $skiptoken in Odata
url: https://blogs.sap.com/2023/03/26/difference-between-skip-and-skiptoken-in-odata/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:46:08.627074
---

# Difference between $skip and $skiptoken in Odata

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Difference between $skip and $skiptoken in Odata

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161811&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Difference between $skip and $skiptoken in Odata](/t5/technology-blog-posts-by-members/difference-between-skip-and-skiptoken-in-odata/ba-p/13560047)

![nitinksh1](https://avatars.profile.sap.com/a/c/idacef170ce1e7f2f7c7ed45f61d80f3b3b4fa1466fcc18c01a0505b6b26d85535_small.jpeg "nitinksh1")

[nitinksh1](https://community.sap.com/t5/user/viewprofilepage/user-id/45127)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161811)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161811)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560047)

‎2023 Mar 26
12:57 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161811/tab/all-users "Click here to see who gave kudos to this post.")

17,211

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Web%2520Services/pd-p/99891761267046184358097136821575)

* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)
* [NW ABAP Web Services

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BWeb%2BServices/pd-p/99891761267046184358097136821575)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)

View products (4)

## Introduction

When working with large datasets in SAP OData, server-side paging can be a useful technique for improving performance and reducing the amount of data that needs to be transmitted over the network. Two commonly used parameters for server-side paging are `$skip` and `$skiptoken`. While they may seem similar, they serve different purposes and have different use cases.

In this technical blog, we will explore the difference between `$skip` and `$skiptoken` in SAP OData and provide examples of how they can be used in different scenarios. We will also discuss best practices for using these parameters and provide tips for optimizing performance when working with large datasets.

**What is `$skip` :** Please refer to this blog for more details about `$skip` - [Implementing All OData Query/URI Options – Part 2](https://blogs.sap.com/2023/03/26/implementing-all-odata-query-uri-options-part-2/)

**What is `$skiptoken`:** Please refer to this blog for more details about `$skiptoken` [Implementing All OData Query/URI Options – Part 2](https://blogs.sap.com/2023/03/26/implementing-all-odata-query-uri-options-part-2/)

### Difference between `$skip` and `$skiptoken`:

$skip is used to skip a specified number of items in a collection of data before returning the remaining results. For example, if we want to retrieve all employees after skipping the first 10 employees, we would use the following query:

```
/sap/opu/odata/sap/<service_name>/Employees?$skip=10
```

This query would skip the first 10 employees and return the remaining employees in the "Employees" entity set.

On the other hand, $skiptoken is used to enable efficient server-side paging of query results when the size of the data set is too large to be retrieved in a single request. When a server returns a limited number of results along with a $skiptoken value, the client can use this token in a subsequent request to retrieve the next set of results. The $skiptoken value serves as an identifier of the last result returned by the server and helps the server to skip to the next set of results efficiently.

For example, suppose we want to retrieve the first 100 orders from an "Orders" entity set that contains 500 orders. We can use the following query:

```
/sap/opu/odata/sap/<service_name>/Orders?$top=100
```

This query would retrieve the first 100 orders. However, if we want to retrieve the next 100 orders, we would need to use $skiptoken. When the server returns the first 100 orders, it would also return a $skiptoken value that identifies the last order returned. We can then use this $skiptoken value in a subsequent request to retrieve the next 100 orders:

```
/sap/opu/odata/sap/<service_name>/Orders?$top=100&$skiptoken=<skiptoken_value>
```

In this query, `<skiptoken_value>` is the $skiptoken value returned by the server in the previous response. The server would skip the first 100 orders and return the next 100 orders after the order is identified by the $skiptoken value.

Few interesting examples that we could use in an SAP OData technical blog about server-side paging using $skip and $skiptoken:

1. **Retrieving large amounts of data efficiently:** Imagine we have an entity set containing a large number of records, such as a sales order entity set that contains thousands of orders. Instead of retrieving all the orders in a single request, we can use $skip and $skiptoken to retrieve them in smaller, more manageable batches. This can significantly improve performance and reduce the load on the server.

2. **Implementing infinite scrolling:** With server-side paging, we can implement infinite scrolling, where data is loaded dynamically as the user scrolls down a page. This can provide a better user experience and prevent the need to load all the data at once, which can be slow and resource-intensive.

3. **Combining $skip and $filter to retrieve specific data:** We can combine $skip and $filter to retrieve specific data from an entity set. For example, if we have an employee entity set and we want to retrieve all the employees in the sales department after skipping the first 10 employees, we can use the following query:

   ```
   /sap/opu/odata/sap/<service_name>/Employees?$skip=10&$filter=Department eq 'Sales'
   ```

4. Using $skiptoken with SAP Gateway: SAP Gateway provides built-in support for $skiptoken, allowing us to easily implement server-side paging in our OData services. We can use the `go_paging` method in our Gateway class to handle $skiptoken values and efficiently retrieve large amounts of data.

### **Conclusion:**

In conclusion, understanding the difference between `$skip` and `$skiptoken` in SAP OData is crucial when working with large datasets. By using these parameters effectively, developers can improve the performance and scalability of their OData services and provide a better user experience for their customers. By following best practices and optimizing their queries, developers can ensure that their OData services are performing at their be...