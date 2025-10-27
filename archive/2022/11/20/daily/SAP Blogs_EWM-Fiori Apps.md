---
title: EWM-Fiori Apps
url: https://blogs.sap.com/2022/11/19/ewm-fiori-apps/
source: SAP Blogs
date: 2022-11-20
fetch_date: 2025-10-03T23:16:55.714743
---

# EWM-Fiori Apps

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* EWM-Fiori Apps

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4640&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [EWM-Fiori Apps](/t5/supply-chain-management-blog-posts-by-members/ewm-fiori-apps/ba-p/13554068)

![Narasimha](https://avatars.profile.sap.com/8/6/id86eeea52b1a32d196fa1a2cdbe4dac2d17041e9b1591b363f2d72303b40bd863_small.jpeg "Narasimha")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Narasimha](https://community.sap.com/t5/user/viewprofilepage/user-id/14917)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4640)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4640)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554068)

‎2022 Nov 19
3:39 PM

[12
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4640/tab/all-users "Click here to see who gave kudos to this post.")

25,367

* SAP Managed Tags
* [EWM - Master Data](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Master%2520Data/pd-p/428351855965480178787051895911518)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [MM Inventory Management](https://community.sap.com/t5/c-khhcw49343/MM%2520Inventory%2520Management/pd-p/402489426158095572469338199787586)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [EWM - Master Data

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BMaster%2BData/pd-p/428351855965480178787051895911518)
* [MM Inventory Management

  Software Product Function](/t5/c-khhcw49343/MM%2BInventory%2BManagement/pd-p/402489426158095572469338199787586)

View products (3)

**Purpose**: Most EWM consultants and end users use the EWM warehouse to monitor transactions for reports. This blog post series aims to create awareness among the EWM community on SAP Fiori apps which are highly intuitive and visually more appealing.

### **1 St App**- Warehouse KPI operations. [SAP Help  Link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/9576ccb7c6b44c16afc20c3df7a28101.html)

To understand implementation details, go through [Fiori App Library Link](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F4162')/S29)

There is one [blog post](https://blogs.sap.com/2020/11/03/implementing-operative-ewm-reports-in-s4-using-fiori/) on this. Please go through the blog post to understand how such apps are built.

Although the SAP link has complete details on the feature, copying important features here for quick reference.

You can use this app to view the following main KPIs:

* The number of outbound delivery order items with goods issue by actual goods issue time

* The number of overdue outbound delivery order items without goods issue by ship-to party

* The number of blocked outbound delivery order items by planned goods issue time

* The number of outbound delivery order items without pick warehouse tasks by planned goods issue time

* The number of outbound delivery order items without goods issue by planned goods issue time

* The number of outbound delivery order items without goods issue by ship-to party

* The number of open pick warehouse tasks by activity area

* The number of outbound delivery order items by goods issue status

* The number of open putaway warehouse tasks by activity area

* The number of open warehouse tasks by activity area

* The number of open warehouse tasks by overdue time in hour

* The number of open warehouse tasks by warehouse process type

* The number of open warehouse tasks by warehouse process category

In addition, the app supports many other technical features.

The main screenshot of the App looks like the one below.

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_01.png)

The cards can be managed through the Mange card section as below.

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_02.png)

###

### 2nd App: Process Warehouse Tasks

App reference: [1-SAP Fiori app reference for technical details.](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F4595')/S24OP)

[SAP App Documentation](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9832125c23154a179bfa1784cdc9577a/29ddb6cf9c2242f5a8ff4e67986fa219.html?version=2021.000)

Helpful blog posts: [Main blog post](https://blogs.sap.com/2020/10/08/sap-extended-warehouse-management-2020-development-overview-part-1-improved-user-experience/)

[SAP Note on the app](https://userapps.support.sap.com/sap/support/knowledge/en/3189208)

SAP app document has detailed features of the app. The below content is just for quick reference from app documentation.

With this app, you can process warehouse tasks for different warehouse process categories, for example, picking, putaway, and internal movements. In the overview screen, you can view all relevant information about the warehouse tasks in your warehouse. You can directly choose one or multiple warehouse tasks for confirmation or cancellation. You can print a warehouse task list with this app. You can also view the details of a warehouse task or handle an exception.

## Key Features

You can use this app to:

* View the details of warehouse tasks, for example, source storage type

* Confirm warehouse tasks

* Print warehouse task lists

* Process warehouse tasks for batch-managed products

* Filter warehouse tasks, for example, by status

* Handle exceptions based on specific warehouse process category

* Cancel warehouse tasks

* Navigate to the Manage Product Master Data app for additional information about products

  You may need additional authorizations to use this app.

Screenshots of the app

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_04.png)

You can view Confirm/Cancel/Print buttons as actions against the warehouse tasks that gets listed.

The detailed information for each task selected looks like the one below

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_05.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_06.png)

This app all warehouse activities such as Putaway/Picking and internal movements. There are individual apps, too, to carry out these warehouse tasks.

## 3rd App: Fiori App – **Production Materials Request**

Learn to use the app in detail by going through  [blog post](https://blogs.sap.com/2020/04/11/s-4hana-embedded-extended-warehouse-management-ewm-production-integration/)

Some of the other EWM Apps available are shown below, and depending on the comments, I will detail them in the next blog posts. Another way to track EWM apps is - Go to the Fiori browser - Filter role "Warehouse\*", you will get all the Fiori apps.

![](/legacyfs/online/storage/blog_attachments/2022/11/1118_3.jpg)

5 Comments

You must be a registered user t...