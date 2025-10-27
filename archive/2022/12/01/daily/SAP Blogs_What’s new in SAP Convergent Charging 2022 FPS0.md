---
title: What’s new in SAP Convergent Charging 2022 FPS0
url: https://blogs.sap.com/2022/11/30/whats-new-in-sap-convergent-charging-2022-fps0/
source: SAP Blogs
date: 2022-12-01
fetch_date: 2025-10-04T00:11:06.305621
---

# What’s new in SAP Convergent Charging 2022 FPS0

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* What’s new in SAP Convergent Charging 2022 FPS0

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7969&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What’s new in SAP Convergent Charging 2022 FPS0](/t5/financial-management-blog-posts-by-sap/what-s-new-in-sap-convergent-charging-2022-fps0/ba-p/13562110)

![AbhijeetDhar](https://avatars.profile.sap.com/c/4/idc47f081da8ceb69e0f3f6f41fe2e2120b02f1416a279e1db7a2904fd2dd71550_small.jpeg "AbhijeetDhar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AbhijeetDhar](https://community.sap.com/t5/user/viewprofilepage/user-id/643514)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7969)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7969)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562110)

‎2022 Nov 30
9:57 PM

[3
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7969/tab/all-users "Click here to see who gave kudos to this post.")

1,938

* SAP Managed Tags
* [SAP Convergent Charging](https://community.sap.com/t5/c-khhcw49343/SAP%2520Convergent%2520Charging/pd-p/01200314690800001318)
* [SAP Billing and Revenue Innovation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Billing%2520and%2520Revenue%2520Innovation%2520Management/pd-p/73554900100700003121)

* [SAP Convergent Charging

  SAP Billing and Revenue Innovation Management](/t5/c-khhcw49343/SAP%2BConvergent%2BCharging/pd-p/01200314690800001318)
* [SAP Billing and Revenue Innovation Management

  Software Product](/t5/c-khhcw49343/SAP%2BBilling%2Band%2BRevenue%2BInnovation%2BManagement/pd-p/73554900100700003121)

View products (2)

### **New Release**

PUBLIC

![](/legacyfs/online/storage/blog_attachments/2022/11/Header-Picture1-1.png)

### **November 2022**

Dear Convergent Charging and BRIM community, we are delighted to announce our new release of **SAP Convergent Charging 2022 FPS0**. Based on the market trend and feedback from our customers, we have introduced new capabilities such as RESTful APIs for integration of charging services, High availability for the cockpit, new metrics for license monitoring and many more new innovations.

This blog provides you with the latest and greatest SAP CC 2022 FPS0 highlights of our pricing and charging platform, part of the [SAP Billing and Revenue Innovation Management (BRIM) suite](https://www.sap.com/products/billing-revenue-innovation-management.html).

---

### **NEW RESTful APIs FOR EVENT AND SESSION BASED CHARGING**

As part of this new release, SAP Convergent Charging brings new upgrades to the integration capabilities of the charging services. Our customers can now take advantage of our new RESTful APIs for event and session based rating which makes the integration more secure, robust and faster. The new RESTful APIs are now available in the SAP API Business Hub​.

This new feature will allow you to:

+ Simplify integration with SAP CC using SAP API Business Hub

+ Secured, faster and lighter than SOAP API

![](/legacyfs/online/storage/blog_attachments/2022/11/API-Hub-3.png)

API Business Hub for Charging Service REST APIs

 You can learn more about the New RESTful APIs by navigating to the following link on the [SAP API Business Hub](https://api.sap.com/package/SAPConvergentCharging/overview).

---

### **HIGH AVAILABILITY SUPPORT FOR THE COCKPIT**

SAP Convergent Charging Cockpit now supports the High Availability feature. Our customers can now configure the Apache Server to implement the active-passive failover process for the Cockpit.​ This feature improves the usability of the SAP Convergent Charging cockpit significantly.

Key Benefits for our Cockpit customers are as follow:

+ Support of active-passive failover process

+ Support of the same database management systems that are used in the Core Server

+ New RDBMS for the Cockpit Database and retiring of H2 embedded database

![](/legacyfs/online/storage/blog_attachments/2022/11/Tomcat-servers-are-configured-in-active-passive-failover.png)

Tomcat servers configured in active-passive failover

 For more information on this new feature, please visit the following link: [Enable High-availability support for the Cockpit](https://help.sap.com/docs/Convergent_Charging/d1d04c0d65964a9b91589ae7afc1bd45/e5ae179688ee41f9b77aa2c147b32859.html?locale=en-US).

---

### **NEW METRICS FOR SYSTEM LICENSE MONITORING**

As part of this release, we have introduced new metrics to support the monitoring of SAP Convergent Charging licenses within the Cockpit user interface. These metrics can be viewed in the Display System Status app available in the Cockpit.
By using these new metrics, our customers can conduct regular monitoring of their SAP CC licenses to ensure that the system does not stop due to the expiration of the license.

New JMX metrics introduced to monitor the license of a CC instance are as below:​

+ **ExpiredInDays**: provides the number of days remaining before license expiration​

+ **LicenseType**: indicates whether the license is permanent or temporary​

+ **HardwareKey**: the hardware on which SAP CC instance is installed

![](/legacyfs/online/storage/blog_attachments/2022/11/Cockpit.png)

License Expiry details in the Cockpit User Interface

 For more details please visit our SAP help page on [Metric Reference and Performance Troubleshooting](https://help.sap.com/docs/Convergent_Charging/9a13fa923bef4356b4209b9b45b7a8b4/e5439ec0f8404d1b9a15e1263f1561bd.html?version=latest).

---

### **OTHER ENHANCEMENTS**

In addition to the features mentioned above, SAP Convergent Charging 2022 FPS0 also introduces other enhancements:

+ **Product Availability Matrix**

  * With this release SAP CC now supports installation of the core database on the latest version of IBM DB2 11.5 version.

---

### **MORE INFORMATION**

SAP Convergent Charging 2022 FPS0 has been released to customers on Nov 18th, 2022 and is available on the [SAP Software Download Center](https://support.sap.com/en/my-support/software-downloads.html).

For more information on SAP Convergent Charging 2022 FPS0, check out the following links:

+ [What’s New in 2022 FPS0](https://help.sap.com/docs/Convergent_Charging/a432b344476a4421abe0629f8f162721?locale=en-US&state=PRODUCTION&version=2022.0)

+ [Release Information Note (RIN) for SAP Convergent Charging 2022](https://launchpad.support.sap.com/#/notes/3198100)

+ [Product Page on SAP Help Portal](https://help.sap.com/docs/Convergent_Charging?locale=en-US)

+ [Questions and Answers for SAP Convergent Charging in SAP Community](https://answers.sap.com/tags/01200314690800001318)

Labels

* [Product Updates](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap/label-name/product%20updates)

* [ccblogs](/t5/tag/ccblogs/tg-p/board-id/financial-management-blog-sap)

You must be a ...