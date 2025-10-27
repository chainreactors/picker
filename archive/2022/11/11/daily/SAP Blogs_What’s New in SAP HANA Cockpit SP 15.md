---
title: What’s New in SAP HANA Cockpit SP 15
url: https://blogs.sap.com/2022/11/10/whats-new-in-sap-hana-cockpit-sp-15/
source: SAP Blogs
date: 2022-11-11
fetch_date: 2025-10-03T22:22:40.048387
---

# What’s New in SAP HANA Cockpit SP 15

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* What's New in SAP HANA Cockpit SP 15

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161214&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What's New in SAP HANA Cockpit SP 15](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-hana-cockpit-sp-15/ba-p/13560151)

![jose_at_sap](https://avatars.profile.sap.com/6/9/id69e5e04e847b22f71de0e15390965c5da62d170f7fa7e14bd1710a3777393308_small.jpeg "jose_at_sap")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jose\_at\_sap](https://community.sap.com/t5/user/viewprofilepage/user-id/122786)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161214)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161214)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560151)

‎2022 Nov 10
8:44 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161214/tab/all-users "Click here to see who gave kudos to this post.")

2,227

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

SAP HANA cockpit SP 15 continues its tradition of delivering new innovations in the areas of SAP HANA administration & monitoring, user management & security, and backup & recovery, as well as introducing new functionality in the SAP HANA database explorer tool. The complete list of SAP HANA cockpit SP 15 features is available in the [What’s New in the SAP HANA Cockpit 2.0](https://help.sap.com/docs/SAP_HANA_COCKPIT/a1199348948f4579b6bc3b7153999749/a06d81e04d6847bcb0a1bfad9dd13ee3.html?version=2.15.0.0&locale=en-US) section of the SAP Help Portal. This blog entry highlights and demonstrates the key new functionality delivered in that version of the SAP HANA cockpit.

I'd like to acknowledge the following colleagues who also contributed content and video demos to this post: Abbey Israel, Gurvick Ghai and Dan van Leeuwen.

# SAP HANA Administration and Monitoring

## New Card to Manage SAP HANA Native Storage Extension Operations

|
 All SAP HANA Native Storage Extension (NSE) administrative tasks are moved to a dedicated card in the SAP HANA cockpit Overview page. A dedicated NSE card simplifies administration and improves the user experience by enabling cockpit users to manage all NSE operations from a centralized application. The new NSE card provides the following functionality:    * Display the host count  * Monitor the total data size on disk of all column store tables and the total page loadable data size on disk that could be loaded into buffer cache  * Monitor the buffer cache size information of the selected host  * Display the NSE Advisor configuration status     Clicking on specific sections in the NSE card and/or using the meatballs menu (…) navigates to other applications that manage aspects of your NSE deployment, such as buffer cache monitoring, table load monitoring, load unit configuration and NSE Advisor configuration. |
 ![](/legacyfs/online/storage/blog_attachments/2022/11/NSE_Card.png) |

Here's a short demonstration of this feature:

## Statement Thread Limit Support for Hierarchical Workload Classes

The [upcoming SAP HANA 2.0 SPS 07](https://blogs.sap.com/2022/07/21/announcing-the-planned-release-of-sap-hana-2.0-sps-07/) plans to support statement thread limit on hierarchical workload classes. [SAP HANA Cloud](https://www.sap.com/products/technology-platform/hana.html) already does it and you can define such a limit in the SAP HANA cockpit when creating a workload class. Administrators can take advantage of this functionality to improve resource management, remove limitations in hierarchical workload classes for more efficient implementation, and reduce the total cost of ownership. In the cockpit, when creating a new workload class, you can specify a value for the statement thread limit (in addition to the statement memory limit). Further, when creating workload class, the cockpit displays warning messages when users enter invalid entries in an effort to reduce human error.

|
 **Create Parent Workload Class** |
  |
 **Create Child Workload Class** |

|
 ![](/legacyfs/online/storage/blog_attachments/2022/11/CreateWorkloadClass-Parent.png) |
  |
 ![](/legacyfs/online/storage/blog_attachments/2022/11/CreateWorkloadClass-Child.png) |

## Import Workload Classes to Multiple Databases

The SAP HANA cockpit SP 15 enables administrators to import workload classes to one or more databases at the same time. This feature greatly improves management of large-scale SAP HANA deployments by reducing the number of operations needed to perform this task against multiple databases. Prior to importing the workload class to one or more databases, you are presented with a preview dialog indicating the before and after result of the operation. After importing, a dialog displays whether the operation succeeded or failed. If the import fails, you’ll see the appropriate error message for the database(s) affected.

![](/legacyfs/online/storage/blog_attachments/2022/11/ImportWorkloadClasses.png)

Here's a short demonstration of this feature:

## Manage Parameter Comments in Configuration Templates

Parameter comments are now viewable and editable when managing configuration templates. Database administrators who wish to leverage parameter comments for documenting the reasoning behind a configuration change can now do so when applying configuration templates against one or more databases. Editing a parameter comment in an existing configuration template is also useful for documenting the result of applying that parameter; for example, if that result was not expected but didn’t cause any issues.

![](/legacyfs/online/storage/blog_attachments/2022/11/EditTemplate-ChangeComment.png)

Here's a short demonstration of this feature:

## Compare Configurations Between Multiple Databases

The feature to compare configurations now allows users to compare configurations between the source database and one or more target databases. Previously, you could only compare configurations between the source and one target database. This feature can be extremely useful to quickly check a large number of SAP HANA databases for specific configuration parameters, as doing so one database at a time would be very time consuming. Also, it’s possible to compare configurations between the source databases and all databases inside a cockpit group, resulting in improved management of SAP HANA databases inside key groups such as ‘production’.

![](/legacyfs/online/storage/blog_attachments/2022/11/CompareConfig-MultipleDBs.png)

When comparing configurations against many databases, a new dialog is presented to show the differences between the source and target databases.

![](/legacyfs/online/storage/blog_attachments/2022/11/CompareConfig-MultipleDBs-Result.png)

Here's a short demonstration of this featur...