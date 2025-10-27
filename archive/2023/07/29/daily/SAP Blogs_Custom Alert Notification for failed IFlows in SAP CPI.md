---
title: Custom Alert Notification for failed IFlows in SAP CPI
url: https://blogs.sap.com/2023/07/28/custom-alert-notification-for-failed-iflows-in-sap-cpi/
source: SAP Blogs
date: 2023-07-29
fetch_date: 2025-10-04T11:53:08.405054
---

# Custom Alert Notification for failed IFlows in SAP CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Custom Alert Notification for failed iFlows in SAP...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163458&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Custom Alert Notification for failed iFlows in SAP CPI](/t5/technology-blog-posts-by-members/custom-alert-notification-for-failed-iflows-in-sap-cpi/ba-p/13570031)

![gaganhl](https://avatars.profile.sap.com/c/2/idc2862ba29b502c0a4bf8910930bcedd3fd6b90b5a5617c37990a0215e15bad9c_small.jpeg "gaganhl")

[gaganhl](https://community.sap.com/t5/user/viewprofilepage/user-id/154073)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163458)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163458)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570031)

‎2023 Jul 28
6:48 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163458/tab/all-users "Click here to see who gave kudos to this post.")

7,858

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Alert Notification service for SAP BTP](https://community.sap.com/t5/c-khhcw49343/SAP%2520Alert%2520Notification%2520service%2520for%2520SAP%2520BTP/pd-p/73555000100800001401)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Alert Notification service for SAP BTP

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BAlert%2BNotification%2Bservice%2Bfor%2BSAP%2BBTP/pd-p/73555000100800001401)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (5)

### **Introduction:**

In a project, especially in a structured landscape, the importance of SAP CPI (Cloud Platform Integration) integration cannot be overstated. The successful implementation of SAP CPI integration serves as the cornerstone that holds the entire project together acting as a bridge that links two ends.

However, it’s important to acknowledge the occurrence of failed iFlows within the SAP CPI (Cloud Platform Integration). As organisations rely heavily on smooth and seamless data exchange between applications, identifying and addressing any issues that arise during this process becomes critical to ensuring the overall success of the integration landscape.By proactively addressing these failures, businesses can enhance their operational effectiveness and pave the way for continuous improvement in their data integration endeavors.

### **Scenario :**

This business is focused on providing an automated solution for monitoring and reporting failed integration flows within the SAP CPI (Cloud Platform Integration) tenant. The primary requirement is to send an Excel report to the recipient three times a day. This report will consolidate the data from three different time periods, also allowing the recipient to have a comprehensive view of the integration flow failures in HANA database.

### **Solution :**

The optimal solution to fulfill this scenario involves the creation of a tailored custom integration flow that seamlessly addresses the task of sending the report of failed IFlows via email to the intended recipients. Additionally, the solution incorporates the capability to efficiently post this essential data to the SAP HANA database.

By designing a custom integration flow, we can ensure that the entire process is optimised to meet the unique requirements of the organisation. This tailored approach guarantees a smooth and reliable transfer of the report, allowing to receive timely notifications and insights regarding any failed IFlows within the SAP CPI ecosystem.

### **IFlow Design:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-5.42.16-PM.png)

Image 1

* **Set Timer :** Here you will set the timer as per your time intervals ( example : 4 times per day, lets say its after every 6 hours starting from 01:00 AM and followed by 07:00 AM, 13:00 PM, 19:00 PM )

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-26-at-11.14.34-PM.png)

Image 2

* **Content Modifier :** We will declare headers to store the current date with three different formats.

1. ${date:now:yyyy\_MM\_dd} : Included in the table name while creating the table in HANA database.

2. ${date:now:'T'HH:mm} : Used for routing the initial trigger which creates the table.

3. ${date:now:yyyy-MM-dd'T'00:00:00.000} : Used in filter condition while fetching the message processing logs.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-26-at-11.27.15-PM.png)

Image 3

* **Router :**

1. Route 1 : When the iflow is triggered initially ( example: triggered at 01:00 AM) message routes through Route 1

2. Route 2 : When the iflow is triggered with periodic intervals after the initial trigger ( example at 07:00 AM, 13:00 PM and 19:00 PM ) message routes through Route 2

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-26-at-11.37.43-PM.png)

Image 4

**Route 1 :**

* **Content Modifier :** Here the XML SQL query to create the table respective to the date is included in the body section of the content modifier. ([XML SQL Format](https://help.sap.com/docs/SAP_NETWEAVER_750/5cf7d2de571a45cc81f91261668b7361/2e96fd3f2d14e869e10000000a155106.html?version=7.5.4))

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-4.43.36-PM.png)

Image 5

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-4.42.46-PM.png)

Image 6

* **Request Reply JDBC Adapter :** Connect to HANA Database using JDBC Adapter.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-4.47.19-PM.png)

Image 7

**Route 2 :**

* **Request Reply ODATA V2 Adapter :**

ODATA API used : Message Processing Logs

Pre requisites :

1. Create process integration runtime service in BTP Cockpit with API plan and include MonitoringDataRead role, then create the service key.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-4.58.21-PM.png)

Image 8

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-27-at-4.58.41-PM.png)

Image 9

    2. No...