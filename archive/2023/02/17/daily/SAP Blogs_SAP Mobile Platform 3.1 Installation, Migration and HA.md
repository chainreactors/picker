---
title: SAP Mobile Platform 3.1 Installation, Migration and HA
url: https://blogs.sap.com/2023/02/16/sap-mobile-platform-3.1-installation-migration-and-ha/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:51:59.843814
---

# SAP Mobile Platform 3.1 Installation, Migration and HA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Mobile Platform 3.1 Installation, Migration an...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163432&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Mobile Platform 3.1 Installation, Migration and HA](/t5/technology-blog-posts-by-members/sap-mobile-platform-3-1-installation-migration-and-ha/ba-p/13569908)

![](/skins/images/E8A536C0D834652C9A43FCC2963C1D98/responsive_peak/images/icon_anonymous_profile.png)

Former Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163432)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163432)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569908)

‎2023 Feb 16
11:58 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163432/tab/all-users "Click here to see who gave kudos to this post.")

2,564

* SAP Managed Tags
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP Mobile Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Platform/pd-p/01200615320800002636)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP Mobile Platform

  SAP Mobile Platform](/t5/c-khhcw49343/SAP%2BMobile%2BPlatform/pd-p/01200615320800002636)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)

View products (3)

SAP Mobile Platform (formerly Sybase Unwired Platform) is a mobile enterprise application platform designed to simplify the task of creating applications that connect business data to mobile devices for workflow management and back-office integration.

**Scenarios: Below scenarios where SAP Mobile platform can be used and can be implemented**

* No Back-end

* OData service in SAP Cloud platform

* SAP Gateway OData Service on-premise

* 3rd Party Back-end System on-premise

Here are some important ports which is used in different communications in SMP. Please ensure they are not blocked in firewall else Mobile platform cockpit cannot be opened.
![](/legacyfs/online/storage/blog_attachments/2023/02/Picture1-56.png)

**How to Start and Stop SAP Mobile Platform Server?**

Open a terminal window, navigate to <SMP\_HOME>/Server/, and run **go.sh**

To run the server in the background, run **go.sh –background**

The server has not fully started until you see the message: **The SMP server has initialized and is ready**

Similarly to stop the application open a terminal window, navigate to <SMP\_HOME>/Server/, and execute **Stop.sh**

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-30.png)

**Installation:**

Pre-requisites for Installation

Before we begin with SMP installation please ensure below rpm packages are available in OS environment. If not, they can be installed using below commands:

* yum install redhat-lsb

* yum install redhat-lsb-core

* yum install jre

* lsb\_release –v

Now download the media from SAP market place and extract it on server.To perform the Installation run the below command – ./**SilentInstall\_Linux.sh**

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture3-24.png)

First login screen

**HA Setup**

We have use an active-passive solution for SMP servers with a normal network load balancer that will forward all requests to the one running SMP server; then SAP basis team has to ensure that in case of failure SMP is restarted manually on 2nd server.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-23.png)

Load Balancer and SMP

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture5-12.png)

**Migration**

1.**Install HANA database on primary site** with same version as of CMO.

2.**Install HANA database on secondary site** with same version as of CMO.

3.**Configure HSR between primary and secondary** site and configure pacemaker.

4.Again using HSR, **copy all the data from CMO to FMO**.

5.**Install the SMP application on Primary and secondary** using physical hostname as shown previous slides.

6.Then these two **application will be up and running as independent clusters**, however only one will be up at a time.

7.If in case primary application goes down, we have to bring up the application on secondary site and request will be routed to secondary using ILB.

**Important Notes:**

1.If you do default installation, then it **automatically installs** **SQLanywhere** **database**. However we need to customize the script and mention as existing database as HANA/Oracle.

2.When we did the migration, we observed that most of the configuration comes after DB replication. But, there were some SMP certificates which has to be regenerated using **keygen tool and signed and uploaded back to the server**

3.While installation, there was a property called Developer install or production install where you need to set it as true. When we are installing a development system, we need to make **the parameter production install as true.**

4.Setting up of backend communication by **adding** **sapmsXX****in /****usr****/sap/services**.

**Conclusion:**

We know that SAP Mobile Platform 3.1 became obsolete in Nov 2022, but this solution can be used in higher and lower versions. It supports various Databases like oracle, MSSQL, Hana, ASE etc. Customers can chose the deployment scenarios based on their business requirements and implement HA for SMP systems.

References: help.sap.com

Please provide your valuable feedback and suggestions.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsap-mobile-platform-3-1-installation-migration-and-ha%2Fba-p%2F13569908%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  10 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Transforming Healthcare Procurement: Lessons from Our S/4HANA MM Implementation](/t5/technology-q-a/transforming-healthcare-procu...