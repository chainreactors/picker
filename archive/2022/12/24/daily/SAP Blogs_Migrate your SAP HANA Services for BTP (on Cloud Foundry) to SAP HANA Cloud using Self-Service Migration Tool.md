---
title: Migrate your SAP HANA Services for BTP (on Cloud Foundry) to SAP HANA Cloud using Self-Service Migration Tool
url: https://blogs.sap.com/2022/12/23/migrate-your-sap-hana-services-for-btp-on-cloud-foundry-to-sap-hana-cloud-using-self-service-migration-tool/
source: SAP Blogs
date: 2022-12-24
fetch_date: 2025-10-04T02:25:29.466573
---

# Migrate your SAP HANA Services for BTP (on Cloud Foundry) to SAP HANA Cloud using Self-Service Migration Tool

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Migrate your SAP HANA Services for BTP (on Cloud F...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164950&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrate your SAP HANA Services for BTP (on Cloud Foundry) to SAP HANA Cloud using Self-Service Migration Tool](/t5/technology-blog-posts-by-sap/migrate-your-sap-hana-services-for-btp-on-cloud-foundry-to-sap-hana-cloud/ba-p/13571116)

![jinheejeong](https://avatars.profile.sap.com/3/e/id3e4164cf6d070f46942aef25adb8a68517c576f8ce69317afd6f9d53720473eb_small.jpeg "jinheejeong")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jinheejeong](https://community.sap.com/t5/user/viewprofilepage/user-id/159990)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164950)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164950)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571116)

‎2022 Dec 23
10:38 AM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164950/tab/all-users "Click here to see who gave kudos to this post.")

8,535

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (1)

In this blog, you will learn how to migrate instances from **HANA Services for BTP (on Cloud Foundry)** to **SAP HANA Cloud** by using **Self-Service Migration tool**. You can find [a detailed guide](https://help.sap.com/docs/HANA_CLOUD/3c53bc7b58934a9795b6dd8c7e28cf05/b9cf1ab6d1864ca2996e82b73d14e3e8.html) in Help Portal as well.

1. [Benefits of migration to SAP HANA Cloud](#benomigtshc)

2. [Pre-requisites and disclaimers to use the tool](#pradtuttabc)

3. [Part 1: Detecting and handling incompatibilities](#dtahdicabc)

4. [Part 2: Migrating database](#migdbabc)

5. [Additional tips and resources](#addtpsabc)

## 1. Benefits of migration to SAP HANA Cloud

**[SAP HANA Cloud](https://www.sap.com/products/technology-platform/hana.html)** is a cloud-native database-as-a-service (DBaaS) for modern applications and analytics across all enterprise data. SAP HANA Cloud provides exciting new innovations and features that were not offered by SAP HANA Service on Cloud Foundry (CF) such as pay-per-usage billing, multi-tier storage, including a petabyte scale built-in data lake allowing you to scale computing and storage resources separately and elastically. SAP HANA Cloud also offers automated near-zero downtime upgrades, HA/DR (up to 99.99% SLA), and availability in a large variety of regions via four different cloud service providers, including Microsoft Azure, Google Cloud Platform (GCP), Amazon Web Services (AWS) and Alibaba Cloud. Last but not least, you can also achieve Total Cost Ownership (TCO) benefits, as it is cheaper to run comparable workloads on SAP HANA Cloud versus HANA Services on CF. You can always use [Capacity Unit Estimator](https://hcsizingestimator.cfapps.eu10.hana.ondemand.com/) to anticipate the cost benefits you will have depending on your SAP HANA Cloud configuration. The [guide document](https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/a43859a94085464683f6fef248894ec4.html) and [blog post](https://blogs.sap.com/?p=1650346?source=email-global-notification-bp-new-in-tag-followed) for this estimator tool are also provided.

SAP provides a **Self-Service Migration Tool** (hereinafter Self-Service tool) to help your migration journey to be easy and smooth. This tool:

* **automates key migration tasks** to reduce the cost and effort of migration,

* **reduces uncertainties** and helps to **plan/prepare for migration** by identifying potential issues upfront,

* is provided **free of charge** in SAP Business Technology Platform (BTP),

* **doesn't require additional storage** for migration and SAP manages the secure temporary storage for export and import.

Here is a high-level overview of the objects that can be migrated with the Self-Service migration tool.![](/legacyfs/online/storage/blog_attachments/2022/12/MicrosoftTeams-image-1.png)

The tool handles the migration of

**1) HANA Service Database such as catalog, data, and secure store** and

**2) SAP HANA Schemas & HDI Containers Service Instances with HDI-Shared, Schema and Secure Store Plan**.

The tool guides you through five phases: PLAN, PREPARE, EXECUTE, VALIDATE, and FINALIZE. You will learn each phase in a minute.

## 2. Pre-requisites and disclaimers to use the tool

In regard to the Self-Service tool, there are several pre-requisites and disclaimers as below.

* The tool only supports the migration of an SAP HANA Service database instance that was provisioned in the CF environment in regions run by AWS.

* The migration is available only within the same cloud database provider. For example, if you have HANA Service on AWS, you can migrate to SAP HANA Cloud on AWS only.

* The SAP HANA Service instance must be running SAP HANA Database Revision 53 or greater.

* Self-Service migration is an offline migration, which means the downtime for migration needs to be planned. The preparation steps can be performed prior to actual data migration.

* Some parts of your database setup cannot be migrated by the tool and must be handled manually. (e.g., Application code, Client-side SQL statements)

* Cloud Foundry extension landscapes are not supported.

Now that you have acquainted yourself with these pre-requisites, let's move on to actual migration planning and execution. Each and every step will be presented with the screenshots, so that you can easily follow the process.

## 3. Part 1: Detecting and handling incompatibilities

1) Go to **SAP BTP cockpit** and log in into your global account and sub account, and click ***Instances and Subscriptions*** in the navigation bar on the left. ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-23-at-17.18.56.png)

2) You can find the detailed information of the sub account. If the provider is AWS, Azure, Alibaba Cloud or GCP, you are running on "Cloud Foundry". Otherwise, you are running in an SAP data center which uses the "Neo" platform as a service. This blog is about migration steps for **Cloud Foundry** case, and the tool supports all cloud service providers except for GCP.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-23-at-17.19.59.png)

3) When you click the Space that you want to migrate, you will see the source HANA Service database. You can also find HANA Schema & HDI Containers Service Instances with Schema, HDI and Secure Store plans which are bound to source HANA Service. Now, click ***SAP HANA Cloud*** in the left-side navigation bar.![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-23-at-17.28.37.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-23-at-17.30.24.png)

4) ...