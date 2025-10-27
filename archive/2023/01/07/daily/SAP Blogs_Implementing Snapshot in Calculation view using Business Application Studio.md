---
title: Implementing Snapshot in Calculation view using Business Application Studio
url: https://blogs.sap.com/2023/01/06/implementing-snapshot-in-calculation-view-using-business-application-studio/
source: SAP Blogs
date: 2023-01-07
fetch_date: 2025-10-04T03:15:01.438024
---

# Implementing Snapshot in Calculation view using Business Application Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Implementing Snapshot in Calculation view using Bu...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161842&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implementing Snapshot in Calculation view using Business Application Studio](/t5/technology-blog-posts-by-sap/implementing-snapshot-in-calculation-view-using-business-application-studio/ba-p/13561822)

![sumitbajaj](https://avatars.profile.sap.com/9/d/id9d74334760dee7dfc1d1df3e82780a3a75b8e430e5c19e42c6f08378e2c5e319_small.jpeg "sumitbajaj")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[sumitbajaj](https://community.sap.com/t5/user/viewprofilepage/user-id/47079)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161842)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161842)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561822)

‎2023 Jan 06
10:06 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161842/tab/all-users "Click here to see who gave kudos to this post.")

2,307

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (4)

In Earlier Versions of HANA, to improve performance of the Model/Calculation view, it was suggested to stage the data in some physical table using a procedure and then create the calculation view on top of that staging table. This help us to fetch huge amount of data quickly as there are no calculations involved.To Avoid this manual work, from Q2/2022 SAP came up with SNAPSHOT option in Calculation view which will help us to speed up queries if the queries do not need to be based on the most current data.

# **Create a Snapshot table**

We define a "snapshot query" directly in the model . To Define/enable snapshot in a model we need to follow below steps:

1. In the calculation view, select the semantics node.

2. On the View Properties tab, choose the Snapshots subtab.

3. Choose + (Add) to add a snapshot query.

A query is added to the list.

4. Select the query to edit the details.

   * In the Query Name field, enter a name for the snapshot query.

   * In the query section, overwrite the default query with the snapshot query.

5. Save and deploy the calculation view.

The snapshot table is created automatically.

6. In the SAP HANA database explorer catalog, find the newly created snapshot table with the following name: ***<calculation\_view\_name>*/*<query\_name>*/SNAP/SNAPSHOT**

7. In the context menu of the snapshot table, choose **Open Data**.

The data shown corresponds to the result of the snapshot query.

![](/legacyfs/online/storage/blog_attachments/2023/01/1.jpg.png)

In Above figure, we can see above sample snapshot scenario.Here Query\_1 is the name of the query using which we want to insert data in snapshot table. Here we can add, remove columns as per our choice and we can also specify Input Parameters and Variables if we want to filter any type of records before inserting them in snapshot table. Once we edit the query we need to deploy the calculation view (**CVR\_ZSUM\_M01\_Q022 copy** in our case).

# **Create an Interface View**

Now we need to create a Interface View that is based on existing Calculation view and Snapshot table.

The generated calculation view makes use of union pruning so that when a query is run on the generated calculation view, either the original calculation view or the snapshot table is accessed depending on the value specified for the input parameter **I\_SOURCE**.

To create an Interface view(Generated Calculation view) follow below steps:

1. In the calculation view (**CVR\_ZSUM\_M01\_Q022 copy** in our case), select the semantics node.

2. On the View Properties tab, choose the **Snapshots** subtab.

3. Select the snapshot query.

4. In the Interface View Name field, enter the name of the calculation view to be generated.

5. Choose Generate interface calculation view.

For example:

The newly generated calculation view is listed in your workspace. It contains a union node with a union between the original calculation view (base view) and the snapshot table.The union node also has a column named **SOURCE**, which is used in the following filter expression: **'$$I\_SOURCE$$'="SOURCE"**. The input parameter **I\_SOURCE** has the default value SNAPSHOT, so the snapshot table is accessed by default. It can be set to BASE (base view) to allow the original calculation view to be accessed.

![](/legacyfs/online/storage/blog_attachments/2023/01/2-8.jpg)

6. Deploy the generated calculation view.

7. In the SAP HANA database explorer catalog, find the generated calculation view and execute a SELECT statement on it, specifying the input parameter as follows:

|
 **Option** |
 **Description** |

|
 **SNAPSHOT** |
 (placeholder."$$I\_SOURCE$$"=>'SNAPSHOT') |

|
 **BASE** |
 (placeholder."$$I\_SOURCE$$"=>'BASE') |

In Below Figure we can see, how interface view is generated

![](/legacyfs/online/storage/blog_attachments/2023/01/3.jpg.png)

Here **CVR\_ZFIAP\_M03\_copy**(Base View) is the original HANA view whose data we want to take snapshot. **CVR\_ZFIAP\_M03\_copy/Query\_1/SNAP/SNAPSHOT**(SnapShot) is the snapshot table which contains data inserted using query defined in Base View. Input Parameter of type Static List is automatically created which help us to do union pruning from Base View/Snapshot Table.

![](/legacyfs/online/storage/blog_attachments/2023/01/4-4.jpg)

# **Procedures and Snapshot tables**

During deployment, procedures are generated for creating, inserting data into, and dropping a "snapshot table" based on the defined snapshot query. The procedures and snapshot table are named according to the following naming conventions:

* Procedures: **<calculation\_view\_name>/<query\_name>/SNAP/SNAPSHOT/CREATE|DROP|INSERT**

* Snapshot table: **<calculation\_view\_name>/<query\_name>/SNAP/SNAPSHOT**

**Note**: Procedures and snapshot tables is coupled to the respective calculation view in wh...