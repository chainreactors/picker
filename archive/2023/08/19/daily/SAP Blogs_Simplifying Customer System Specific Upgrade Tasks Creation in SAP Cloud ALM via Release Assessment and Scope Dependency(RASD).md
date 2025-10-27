---
title: Simplifying Customer System Specific Upgrade Tasks Creation in SAP Cloud ALM via Release Assessment and Scope Dependency(RASD)
url: https://blogs.sap.com/2023/08/18/simplifying-customer-system-specific-upgrade-tasks-creation-in-sap-cloud-alm-via-release-assessment-and-scope-dependencyrasd/
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T12:00:03.943573
---

# Simplifying Customer System Specific Upgrade Tasks Creation in SAP Cloud ALM via Release Assessment and Scope Dependency(RASD)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Simplifying Customer System Specific Upgrade Tasks...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51801&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Simplifying Customer System Specific Upgrade Tasks Creation in SAP Cloud ALM via Release Assessment and Scope Dependency(RASD)](/t5/enterprise-resource-planning-blog-posts-by-sap/simplifying-customer-system-specific-upgrade-tasks-creation-in-sap-cloud/ba-p/13559974)

![Farooq](https://avatars.profile.sap.com/d/a/iddaaf3020d892cfbf11180ebcec64a742870e02e7af5d9edb94fe78cee573aad0_small.jpeg "Farooq")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Farooq](https://community.sap.com/t5/user/viewprofilepage/user-id/11373)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51801)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51801)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559974)

‎2023 Aug 18
9:40 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51801/tab/all-users "Click here to see who gave kudos to this post.")

1,886

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (3)

**Edit 12/08/2024**

With the release of 2402.1 version of SAP S/4HANA Cloud Public Edition, all changes (Deletions/Deprecations/Changes) related to extensibility objects have been moved to the page [Overview of Extensibility Objects](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/1df8b8b1799a4d07899d9fb6c72835cf.html?parentHref=%2Fwhats-new%2F7d3d11840a6543329e72391cf4d48e2d%3FCategory%3DExtensibility%2520%2528incl.%2520API%2520and%2520CDS%2529%26Version%3DSAP%2520S%252F4HANA%2520Cloud%25202402.1%2520%2528HFC5%2529%26locale%3Den-US&parentName=What%27s%20New%20Viewer%20-%20SAP%20S%2F4HANA%20Cloud). This now includes objects covering both Key User Extensibility and Developer Extensibility. We have updated the CALM excel template accordingly to accommodate these changes. This blog is updated to reflect these changes

**Introduction**

The Release Assessment and Scope Dependency (RASD) team has been tirelessly working on incorporating new features and improvements into the application to cater to our valued customers’ needs.

We are excited to announce that starting from the 2308 release, all customers will have access to a new feature: create ‘SAP Cloud ALM’ upgrade-related tasks through the ‘Release Assessment and Scope Dependency’ application.

**Kindly Note:** This feature is exclusively available for tasks related to upgrades on SAP S/4HANA Cloud, public edition.

**Release Assessment and Scope Dependency**:  SAP S/4HANA Cloud, public edition follows half yearly release cycle with Continuous Feature Delivery(CFD) between releases. During these releases, there can be new features, enhancements in the existing features, or deprecations. These changes often have a day-one impact on customers, requiring a systematic approach to handle them effectively. To address these challenges, one can use Release Assessment and Scope Dependency (RASD). The application provides personalized information for each customer, to ensure they see only the information relevant to their scopes.

**SAP Cloud ALM**: During the upgrade, there can be new functionality, roles or catalogs, etc need to be adapted. The SAP Cloud ALM tool allows for managing the upgrade cycle efficiently by providing an option to initiate an upgrade project, generate sub-tasks within the project, and allocate tasks to team members for individual handling.

While SAP Cloud ALM provides common upgrade tasks applicable to all customers, Release Assessment and Scope Dependency (RASD) provides customer-specific details, thereby enhancing the capabilities of SAP Cloud ALM. Within SAP Cloud ALM, the manual creation of upgrade tasks can lead to missing out on certain tasks that are specific to customer usage. RASD streamlines this process by automating the generation of upgrade tasks, empowering users to craft multiple tasks simultaneously, and focusing on the exact areas that matter most – the day-one impacts. In the current release, the application extends support for creating SAP Cloud ALM upgrade tasks exclusively for cards labeled “Usage-based Impact” and “Usage-based Catalogs”.

For more information about ***Release Assessment and Scope Dependency*** and ***Cloud ALM***, refer to the below resources:

**Release Assessment and Scope Dependency :**

+ Blog: [Release Assessment and Scope Dependency (RASD) | Your Questions Answered](https://blogs.sap.com/2023/02/10/release-assessment-and-scope-dependency-rasd-2.0-your-questions-answered/)

+ Blog: [Release Assessment and Scope Dependency Tool (RASD) Released to Customers](https://blogs.sap.com/2022/08/19/rasd-2.0-released-to-customers/)

+ Blog: [What’s New in the Release Assessment and Scope Dependency (RASD)](https://blogs.sap.com/2022/12/14/whats-new-in-the-release-assessment-and-scope-dependencyrasd-2.0/)

**Cloud ALM**

+ Blog: [End-to-End Story for Implementation in SAP Cloud ALM](https://blogs.sap.com/2023/01/04/end-to-end-story-for-implementation-in-sap-cloud-alm/)

+ Blog: [SAP Cloud ALM Activation](https://blogs.sap.com/2021/11/29/sap-cloud-alm-activation/)

+ Blog: [How to Manage SAP S/4HANA Cloud Upgrade 2308 in SAP Cloud ALM](https://blogs.sap.com/2023/07/25/how-to-manage-sap-s-4hana-cloud-upgrade-2308-in-sap-cloud-alm/)

**Note:**Release Assessment and Scope Dependency is available for **SAP S/4HANA Cloud, Public edition**only.

To help you get started, we have outlined the step-by-step process below:

**Pre-requisites:**

+ Ensure you have a valid Customer-linked S-User ID to access the ‘Release Assessment and Scope Dependency’ app.

+ Ensure you have access to the SAP Cloud ALM tenant and authorization.

**Step 1:** Log in to the [Release Assessment and Scope Dependency](https://release-assessment-v2.cfapps.eu10.hana.ondemand.com/cp.portal/site#sapcomrasd-Display?sap-ui-app-id-hint=sapcomrasd) using a customer-linked S-User ID.

![Farooq_1-1723359725628.png](/t5/image/serverpage/image-id/149942iD572A84A67F9235E/image-size/large?v=v2&px=999 "Farooq_1-1723359725628.png")

*Release Assessment an...