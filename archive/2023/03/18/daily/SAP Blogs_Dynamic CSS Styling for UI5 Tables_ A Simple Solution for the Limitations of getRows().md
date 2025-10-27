---
title: Dynamic CSS Styling for UI5 Tables: A Simple Solution for the Limitations of getRows()
url: https://blogs.sap.com/2023/03/17/dynamic-css-styling-for-ui5-tables-a-simple-solution-for-the-limitations-of-getrows/
source: SAP Blogs
date: 2023-03-18
fetch_date: 2025-10-04T09:57:23.300414
---

# Dynamic CSS Styling for UI5 Tables: A Simple Solution for the Limitations of getRows()

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Dynamic CSS Styling for UI5 Tables: A Simple Solut...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158196&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Dynamic CSS Styling for UI5 Tables: A Simple Solution for the Limitations of getRows()](/t5/technology-blog-posts-by-sap/dynamic-css-styling-for-ui5-tables-a-simple-solution-for-the-limitations-of/ba-p/13551287)

![leonikussmaul](https://avatars.profile.sap.com/e/1/ide1ccb8e7edbe7b23a231000fee2b918f5a1d36d7000dfe1e8784e9f59fb55426_small.jpeg "leonikussmaul")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[leonikussmaul](https://community.sap.com/t5/user/viewprofilepage/user-id/126740)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158196)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158196)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551287)

‎2023 Mar 17
5:55 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158196/tab/all-users "Click here to see who gave kudos to this post.")

3,154

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (4)

If you have ever attempted to dynamically apply custom CSS to a UI5 table control, you may have encountered some challenges. In this article, we will explore a simple approach that can be helpful for some UI5 tables bound to a JSON model and using a relatively small dataset.

# Limitations of getRows()

Suppose you want to use a Grid Table control (sap.ui.table.Table) and retrieve the rows of your table. In that case, you would usually use the getRows() method. However, this method has a limitation: it only returns the rows that are currently rendered in the table, which is also known as the visible row count. This is a well-known behavior documented in this [SAP Knowledge Base Article](https://userapps.support.sap.com/sap/support/knowledge/en/2988183).

### What about getContextByIndex()?

The above article suggests using the getContextByIndex() method as an alternative if needed. However, this method returns the context, and you cannot add a CSS style class to the Table context itself, making it less useful for dynamic CSS styling.

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-16-at-13.45.47.png)

Error when trying to apply CSS to the Table Context

On the other hand, applying CSS to a specific row using the getRows() method is effortless. For example, you can add a background color to a specified table row:

```
this.getView().byId("sTableId").getRows()[i].addStyleClass("backgroundColor");
```

```
.backgroundColor {

  background: #4cba6b; width: 100%; height: 100%;

}
```

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-16-at-13.44.34.png)

# How to manipulate the getRows() API

However, a problem arises when the colored row moves as you scroll down the table. This is because getRows() has returned only the visible row count, where we applied the style class. So, how can we dynamically manipulate the number of visible rows shown in the table rather than the standard count of 10?

The Grid Table control provides the visibleRowCount property, which can be bound to the length of Rows via expression binding. When you bind the visibleRowCount property to a JSON model with the rows property inside, which holds all the data for the rows, the getRows() method returns all the rows of the table, enabling you to apply CSS to all rows of the table.

Here's an example of how to bind the visibleRowCount property to a JSON model:

```
<table:Table

id="sTableId"

rowsUpdated="onRowsUpdated"

visibleRowCount="{= ${tablemodel>/rows}.length }">
```

In this example, we have bound the visibleRowCount property to a JSON model named 'tablemodel' with the rows property inside, which holds all the data for the rows. Expression binding is used to calculate the length of the rows property.

# Rows vs. Cells

Similarly, you can apply your CSS to a specific cell aggregation rather than the entire row.

```
oTable.getRows()[i].mAggregations.cells[j].addStyleClass("backgroundColor");
```

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-16-at-13.32.56.png)

In conclusion, using the visibleRowCount property and expression binding to dynamically manipulate the number of visible rows shown in the table enables you to apply CSS dynamically to all rows of the table. You can also apply CSS to specific cell aggregations, enabling you to customize the table to meet your needs.

Happy CSSing!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fdynamic-css-styling-for-ui5-tables-a-simple-solution-for-the-limitations-of%2Fba-p%2F13551287%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Secure Your Digital Journey with SAP CIAM](/t5/technology-blog-posts-by-sap/secure-your-digital-journey-with-sap-ciam/ba-p/14232983)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [The Ultimate Guide to SAP S/4HANA Master Data - Part 5](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-part-5/ba-p/14229426)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [How to Handle Cross-Global Account Subscriptions and Customer-Managed HANA in CAP SaaS?](/t5/technology-q-a/how-to-handle-cross-global-account-subscriptions-and-customer-managed-hana/qaq-p/14218979)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions...