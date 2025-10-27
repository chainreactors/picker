---
title: A Customer Journey through the SAP S/4HANA Cloud 3 System Landscape (3SL) Upgrade & Hotfix Process
url: https://blogs.sap.com/2023/04/20/a-customer-journey-through-the-sap-s-4hana-cloud-3-system-landscape-3sl-upgrade-hotfix-process/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:17.566819
---

# A Customer Journey through the SAP S/4HANA Cloud 3 System Landscape (3SL) Upgrade & Hotfix Process

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* A Customer Journey through the SAP S/4HANA Cloud 3...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51251&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [A Customer Journey through the SAP S/4HANA Cloud 3 System Landscape (3SL) Upgrade & Hotfix Process](/t5/enterprise-resource-planning-blog-posts-by-sap/a-customer-journey-through-the-sap-s-4hana-cloud-3-system-landscape-3sl/ba-p/13556372)

![seanhughes1](https://avatars.profile.sap.com/c/b/idcb1888bf0734b7f8ad50ad7ff7c5528517e7a831b72dead895cafa2741e6d052_small.jpeg "seanhughes1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[seanhughes1](https://community.sap.com/t5/user/viewprofilepage/user-id/14174)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51251)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51251)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556372)

‎2023 Apr 21
12:35 AM

[16
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51251/tab/all-users "Click here to see who gave kudos to this post.")

3,754

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Extensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP Central Business Configuration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Central%2520Business%2520Configuration/pd-p/c73809a2-f698-412f-9bcb-dd423592ac49)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Extensibility

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BExtensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP Central Business Configuration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BCentral%2BBusiness%2BConfiguration/pd-p/c73809a2-f698-412f-9bcb-dd423592ac49)

View products (3)

The 3SL Upgrade Process has been designed to not impact customer projects during the upgrade of the customer landscape. After the upgrade of the Test system, unlike in 2 System Landscape environments, all kinds of transports (CBC Business Config, fine tuning, developer extensibility & key-user extensibility) can still be transported into the P System.

In order to better understand this process, this document will take you through the journey of an 3SL S/4HANA Cloud Upgrade with our fictional customer – QWERTY Utilities. In this case we will use the SAP S/4HANA Cloud 2302 upgrade as an example.

![](/legacyfs/online/storage/blog_attachments/2023/04/1-52.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/1-5-1.png)

As the QWERTY Utilities team approach their first release they note the release dates that were sent via email **6 weeks prior to the test upgrade**. Their next release is the 2302 release in which their Test system will be upgraded on 28/29 January.
Since QWERTY Utilities are based in Europe they look at the release schedule and note that the **upgrade pre-processing** is due to begin around 18:00 UTC on Thursday, 26th January. During this time there is no downtime but they take note of the following limitation:

* No ATO Transport Processing is possible

The next milestone in the upgrade of their test system occurs around 04:00 UTC on Saturday, January 28th when the SAP S/4HANA Cloud Software is upgraded in the Test System. The **downtime** for the Test system upgrade takes approximately 2 hours but may take longer if any issues are encountered.
During this time the following limitation is in place:

* No logon to SAP S/4HANA Cloud tenant(s) possible

Once the Software upgrade is complete **SAP finalizes SAP S/4HANA Cloud tenant processing** this takes roughly an hour but can take longer if issues occur.

* Log on to SAP S/4HANA Cloud Tenants is possible, but it is important to wait until the upgrade completion status mail is sent

![](/legacyfs/online/storage/blog_attachments/2023/04/2-25.png)

**Period Between Test upgrade and Development and Production Upgrade**

Unlike with 2SL there are minimal limitations on Customers to bring transports into their P-System. During this period customers can test developer extensibility accordingly and perform other project specific activities accordingly.

Some limitations exist around transport of certain items during this period, the most up to date information on these limitations can be found in the Release Restriction note for the corresponding release. For example 2302 - <https://launchpad.support.sap.com/#/notes/3273553>

During this period, regression testing should be performed via the Test Automation tool. The SAP S/4HANA Cloud Test Automation Tool provides our SAP S/4HANA Cloud Essential customers the necessary feature set to create an automated regression suite for their testing needs. The tool is a no-code, no-installation, cloud native solution. The solution comes bundled with more than 300+ standard pre-delivered test automates based on the SAP Best Practice Processes.

If a regression issue is identified a support incident should be opened with the prefix “[R]” in the title. This helps SAP Product Support to recognize and prioritize regression incidents accordingly.

**Production and Development System Upgrade**

The first milestone that QWERTY Utilities need to consider in the upgrade of their Productive landscape for 2302 is the S/4HANA Cloud lock phase which begins at 18:00 UTC on Thursday, February, 16th. In the 24 hours leading up to this Customers are discouraged from triggering large deployments as the Cluster’s Database is upgraded.

Once the **lock phase** is triggered the following limitations are put in place:

* Deployments to Development & Productive Systems are disabled

* No ATO Transport processing is possible in Development or Productive Systems

* From the final hours of the lock phase (circa 07:00 UTC, customizing is set to read-only. This is to avoid any blocking of the software change (Upgrade & Update process) which could happen due to ongoing deployments.

The Software Upgrade process to 2302 for Production

* Logon to SAP S/4HANA Developer & Productive Tenants are not possible

* Deployments to Development & Productive Systems are disabled

* No ATO Transport processing is possible in Development or Productive Systems

* In the Central Business Configuration (CBC) tenant Organizational structure enhancements, adding new scope or country are possible until the content update is triggered and the CBC Project is locked.

Once the **Software Upgrade** process is complete SAP upgrades the **Business Configuration content** and finalis...