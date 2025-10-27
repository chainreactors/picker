---
title: What’s New in SAP HANA Cloud in December 2022
url: https://blogs.sap.com/2022/12/29/whats-new-in-sap-hana-cloud-in-december-2022/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:20.365519
---

# What’s New in SAP HANA Cloud in December 2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* What’s New in SAP HANA Cloud in December 2022

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159278&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What’s New in SAP HANA Cloud in December 2022](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-hana-cloud-in-december-2022/ba-p/13554309)

![thomashammer](https://avatars.profile.sap.com/a/3/ida34a102f8474a9f4b03519682640828a0a7b2e42b8f8a73da35a7089abb5df3b_small.jpeg "thomashammer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[thomashammer](https://community.sap.com/t5/user/viewprofilepage/user-id/122781)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159278)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159278)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554309)

‎2022 Dec 29
7:41 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159278/tab/all-users "Click here to see who gave kudos to this post.")

4,229

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (3)

New Year’s Eve is just around the corner, but for now, we are happy to announce the last quarterly release of SAP HANA Cloud in 2022 today. As always, with this blogpost I am aiming to give you a summary of the broad variety of innovations that have been introduced to our flagship product SAP HANA Cloud in the fourth quarter of this year.

![](/legacyfs/online/storage/blog_attachments/2022/12/image001.png)

In case you want to get a condensed overview of the most exciting features, you should have a look at my [person highlights video](https://youtu.be/fpFsSdijpcE) on our SAP HANA Cloud YouTube [playlist](https://www.youtube.com/playlist?list=PLWV533hWWvDm-wgDJUTFE12xgSTfoZ-R1).

# Updates to the SAP HANA Cloud tooling

## Renovated Tooling for SAP HANA Cloud

With the Q4 release of *SAP HANA Cloud*, there have been some updates performed to our cloud administration & monitoring tools. I am excited to share that our offered tools are evolving to become a unified environment, including capabilities provided by *SAP HANA database explorer*, *SAP HANA cockpit* & *SAP HANA Cloud Central*. Instead of releasing new tooling, we will strengthen the already very powerful *SAP HANA Cloud Central* by integrating required functionalities to monitor and administrate your database landscape.

The renovated *SAP HANA Cloud Central* improves your user experience with a more intuitive approach for managing your landscapes and offers a couple of benefits you can take advantage of:

+ First, you don’t need multiple tools anymore, a single interface is now sufficient to perform all your database administration & monitoring tasks.

+ Second, with the updated tooling, there are significant performance improvements resulting ultimately in greater productivity.

+ And finally, you don’t need to learn yet another tool as you can apply what you have learned so far. We just moved functionalities from three separate tools into one unified one.

This initial delivery will integrate selected functionality of the *SAP HANA cockpit* into *SAP HANA Cloud Central*, with subsequent versions incorporating more and more features from the *SAP HANA Cockpit* and from *SAP HANA Database Explorer*. Get all the detail in jose\_at\_sap’ [blogpost](https://blogs.sap.com/2022/12/05/sap-hana-cloud-central-gets-renovated/).

### Display of the end-of-maintenance date

We are staying in the administration and monitoring sphere for a little longer. Since our Q4 2022 release of *SAP HANA Cloud*, the **end-of-maintenance date** will be displayed when provisioning a new instance. Also, of course you can view the end-of-maintenance date when examining the details of an existing instance.

Informing the *SAP HANA Cloud* administrators about the end-of-maintenance date for their instances earlier significantly improves their user experience and eases landscape maintenance. Additionally, it helps to reduce effects any downtimes when encouraging unplanned upgrades of instances running out of maintenance.

![](/legacyfs/online/storage/blog_attachments/2022/12/scale-down.png)

*End-of-Maintenance date in SAP HANA Cloud Central*

### Self-Service for memory scale-down

Since the Q4 release of SAP HANA Cloud, you can now scale-down the memory of provisioned SAP HANA database instances of SAP HANA Cloud autonomously. You therefore gain the flexibility to decrease the volume of the memory of SAP HANA Cloud according to your individual needs without having to open a ticket.

![](/legacyfs/online/storage/blog_attachments/2022/12/scale-down2.png)

Memory Scale-Down Self-Service in SAP HANA Cloud Central

## SAP HANA Database Explorer

Using the *SAP HANA Database Explorer,* you can browse and work with *SAP HANA* database objects e.g., tables, stored procedures, importing and exporting data, executing SQL statements, working with multi-model data such as graph, spatial and JSON collections, viewing trace files, and troubleshooting.

### JSON Collection viewer

We are always striving to improve our tooling. Therefore, there have been a couple new features now included into the *SAP HANA Database Explorer*. New features include three new menu options to generate SQL statements for JSON collections: CREATE, SELECT, INSERT. Moreover, a JSON viewer was integrated.

![](/legacyfs/online/storage/blog_attachments/2022/12/image002.png)

### Data Lake Relational Engine

There have also been a couple of enhancements to the *SAP HANA Cloud, data lake relational engine*. The new features include statement library support and run statements, in the background and against multiple instances.

Additionally, you can now choose setting for auto-commit, auditing and query plans.

![](/legacyfs/online/storage/blog_attachments/2022/12/image003.png)

## SAP HANA Client

As for the *SAP HANA Client*, the installer now natively supports Apple ARM64. This brings improved performance and simplicity when working with the *SAP HANA Client* on Apple ARM64 machines.

For full details of the supported platforms of the *SAP HANA Client,* please see [3165810 - SAP HANA Client Supported Platforms](https://launchpad.support.sap.com/#/notes/3165810) and reference the 2.15 or QRC ...