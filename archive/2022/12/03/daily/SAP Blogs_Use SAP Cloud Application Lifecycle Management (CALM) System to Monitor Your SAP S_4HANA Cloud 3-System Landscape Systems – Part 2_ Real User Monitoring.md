---
title: Use SAP Cloud Application Lifecycle Management (CALM) System to Monitor Your SAP S/4HANA Cloud 3-System Landscape Systems – Part 2: Real User Monitoring
url: https://blogs.sap.com/2022/12/02/use-sap-cloud-application-lifecycle-management-calm-system-to-monitor-your-sap-s-4hana-cloud-3-system-landscape-systems-part-2-real-user-monitoring/
source: SAP Blogs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:42.716279
---

# Use SAP Cloud Application Lifecycle Management (CALM) System to Monitor Your SAP S/4HANA Cloud 3-System Landscape Systems – Part 2: Real User Monitoring

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Use SAP Cloud Application Lifecycle Management (CA...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52764&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Use SAP Cloud Application Lifecycle Management (CALM) System to Monitor Your SAP S/4HANA Cloud 3-System Landscape Systems – Part 2: Real User Monitoring](/t5/enterprise-resource-planning-blog-posts-by-sap/use-sap-cloud-application-lifecycle-management-calm-system-to-monitor-your/ba-p/13565608)

![George_Yu1](https://avatars.profile.sap.com/5/b/id5b9dd4200223161a1181616aedbbafc80631106e3147acc2728d1ee8f02e8f6b_small.jpeg "George_Yu1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[George\_Yu1](https://community.sap.com/t5/user/viewprofilepage/user-id/131765)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52764)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52764)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565608)

‎2022 Dec 02
7:53 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52764/tab/all-users "Click here to see who gave kudos to this post.")

5,176

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (3)

# Introduction

In my previous blog [Use SAP Cloud Application Lifecycle Management (CALM) System to Monitor Your SAP S/4HANA Cloud 3-Sys...](https://blogs.sap.com/2022/10/31/use-sap-cloud-application-lifecycle-management-calm-system-to-monitor-your-sap-s-4hana-cloud-3-system-landscape-systems-part-1-setup/), I detailed the steps to set up CALM for a 3-system landscape systems.  It discussed the special handling of different errors which are usually not documented in SAP Help Portal documentations.

In this blog, I intend to discuss the usage of one of the CALM App ***Real User Monitoring***, part of CALM for Operations.

## What is Real User Monitoring

When discussing this topic, we should keep four key points in mind:

* The monitoring is from end user’s perspective, in terms of system performance. In other words, how the business user feels when they use the system.

* The being monitored systems only send technical performance data to the CALM (network performance, CPU, memory usage, response time, etc.). There is no business-related data (transactional and master data) sent to the CALM.

* Performance data collected are following types

  + SAPUI5 or Fiori

  + SAP Web Dynpro

  + SAP GUI for HTML

  + HTTPS

  + HTTP

  + Dialog

  + RFCS

  + RFC

  + WS

* How real? How often the monitoring data is sent over is controlled by the Communication Arrangement I explained in Part 1 blog. It is usually set as 1 min.

## Technology behind Real User and Performance Monitoring

The real user monitoring is from end user perspective, i.e., how the performance is measured on the end user browser.  For example, the end user feels the system is slow today, and we can quantify that in Real User Monitoring.  In addition, we can compare today’s performance with the past performance, or set up an alert if the performance trend goes to a wrong direction.

These being monitored systems can be individual ones, or a set of systems integrated together to perform one business scenario, such as Source to Pay when integrating SAP Ariba with SAP S/4HANA Cloud.

![](/legacyfs/online/storage/blog_attachments/2022/12/Overview-of-CALM-Capabilities.png)

Overview of CALM Capabilities

To achieve this, we deploy a so-called SAP Passport technology in this setup. SAP Passport is an end-to-end tracing technology.  When an end user accesses SAP S/4HANA Cloud system via a desktop web browser, a Root Context ID is generated. This frontend action triggers a backend transaction which has its own Transaction ID.  If the backend transaction triggers another transaction in its own system and/or a satellite system, there is another Transaction ID generated. Now we correlate all three ID’s (Root Context ID and Transaction ID’s) together to reflect an end user performance experience. Different end users run different transactions, there are different sets of IDs being correlated.

![](/legacyfs/online/storage/blog_attachments/2022/12/SAP-Passport-Technology.png)

SAP Passport Technology

For the same action, such as a purchase order creation, the transaction types are fixed. We can keep a history of this type of transaction type set for the performance comparison purpose. Let’s say, if the average purchase order creation time is 0.5 sec, but one user experiences 2 sec; that indicates a poor performance, and an investigation is warranted.

# Bells and Whistles of Real User Monitoring

## Data Volume Limit and Data Retention Period

The CALM system provides 8 GB HANA DB memory to store all the data from the systems it monitors. The users can specify the duration of data retention. It is 7 days by default.  Any data above the retention period will become part of aggregated data, used as benchmark to compare with the real time data.

If you use one single CALM system for many cloud-based and non-cloud-based systems, you can request more HANA DB memory with additional CALM subscriptions when you reach the 8 GB memory limit.

## Real User Monitoring Scope Definition

Under the SAP Cloud ALM for Operations, launch ***Real User Monitoring*** Fiori App. First, let’s explain the initial screen after it has been setup.

As explained previously, we have a 3-System Landscape to monitor: Development Tenant (VOR-80), Configuration Tenant (VOR-100), Test Tenant (VP6-100) and Production Tenant (VP7-100). They are all included under my watchful eyes!

![](/legacyfs/online/storage/blog_attachments/2022/12/Using-CALM-to-Monitor-Four-Tenants-within-a-S4HC-3-System-Landscape.png)

Using CALM to Monitor Four Tenants within a S4HC 3 System Landscape

In the below figure, all four systems are included, registered as services. At the time of screenshot was taken, most of them are in green status.

![](/legacyfs/online/storage/blog_attachments/2022/12/Home-View-of-Real-User-Monitoring-App.png)

Home View of Real User Monitoring App

## Explanations of Top Menu Bar

There are many buttons/icons on the top menu bar. I am going to explain them on...