---
title: SAP Data Intelligence – What’s New in DI:2023/02
url: https://blogs.sap.com/2023/02/10/sap-data-intelligence-whats-new-in-di2023-02/
source: SAP Blogs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:11.960309
---

# SAP Data Intelligence – What’s New in DI:2023/02

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Data Intelligence – What’s New in DI:2023/02

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163412&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Data Intelligence – What’s New in DI:2023/02](/t5/technology-blog-posts-by-sap/sap-data-intelligence-what-s-new-in-di-2023-02/ba-p/13566966)

![eduardo_haussen](https://avatars.profile.sap.com/0/e/id0e3dcad3e492b67fe199f6463191281b24cf3f05814d2f1b4f2f7491d02d62c2_small.jpeg "eduardo_haussen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[eduardo\_haussen](https://community.sap.com/t5/user/viewprofilepage/user-id/5230)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163412)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163412)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566966)

‎2023 Feb 10
10:29 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163412/tab/all-users "Click here to see who gave kudos to this post.")

2,239

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)

View products (1)

SAP Data Intelligence, cloud edition DI:2023/02 is now available.

Within this blog post, you will find updates on the latest enhancements in DI:2023/02. We want to share and describe the new functions and features of SAP Data Intelligence for the Q1 2023 release.

If you would like to review what was made available in the previous release, please have a look at this [blog post](https://blogs.sap.com/2022/10/31/sap-data-intelligence-whats-new-in-di2022-10/).

## **Overview**

This section will give you a quick preview about the main developments in each topic area. All details will be described in the following sections for each individual topic area.

## **SAP Data Intelligence 2023/02**

![](/legacyfs/online/storage/blog_attachments/2023/02/pic1_DI2302.png)

##

##

## **Connectivity & Integration**

This topic area focuses mainly on all kinds of connection and integration capabilities which are used across the product – for example: in the Metadata Explorer or on operator level in the Pipeline Modeler.

### Support non-basic authentication for Microsoft Exchange e-mail servers in IMAP connections

**USE CASE DESCRIPTION:**

* Support of OAuth2 authentication for Microsoft Exchange e-mail servers in IMAP connections via the authorization method *ms\_client\_credentials*

* Supported OAuth2 authentication methods

  + Client ID + Client Secret

  + **X.509 Certificates**

![](/legacyfs/online/storage/blog_attachments/2023/02/pic2_DI2302.png)

**BUSINESS VALUE – BENEFITS:**

* Usage of non-basic authentication in IMAP connections

### Support HANA Cloud as source in Replication Flows

**USE CASE DESCRIPTION:**

* Allow customers to leverage mass data replication scenarios via Replication Flows using HANA Cloud as a source system

* Data from HANA Cloud can be loaded into any target supported by Replication Flows

* Supporting standard functionalities offered by Replication Flows such as parallelization and resilience

![](/legacyfs/online/storage/blog_attachments/2023/02/pic3_DI2302.png)

**BUSINESS VALUE – BENEFITS:**

* Customers can realize mass data ingestion from HANA Cloud in a simplified way compared to pipelines

* Lower TCO & TCD for data replication scenarios from HANA Cloud as a source

###

### Provide additional runtime metrics for ODP in Generation 2

**USE CASE DESCRIPTION:**

* Provide additional important information for end-users in the process logs when extracting data via ODP interface by showing the number of replicated records from the ODP source object for the generation 2 “Read Data from SAP System” operator

![](/legacyfs/online/storage/blog_attachments/2023/02/pic4_DI2302.png)

**BUSINESS VALUE – BENEFITS:**

* Seamless user experience when using the Read Data from SAP System operator by showing similar metrics for all use cases (CDS View, table via SLT and ODP extraction)

##

## **Pipeline Modelling**

This topic area covers new operators or enhancements of existing operators. Improvements or new functionalities of the Pipeline Modeler and the development of pipelines.

### Possibility to connect own Docker registries with SAP Data Intelligence Cloud

**USE CASE DESCRIPTION:**

* SAP Data Intelligence Cloud is able use external Docker registries that are configured and owned by customers to **pull images** that are used as graph base Docker images

* It is **not possible to push** Docker images that were created in DI Cloud to external registries

* Supported hyperscaler Docker registries:

  + AWS Elastic Container Registry (authentication via [token](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html))

  + Microsoft Azure Container Registry (authentication via [service principals](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal))

  + GCP Container Registry (authentication via [json](https://cloud.google.com/container-registry/docs/advanced-authentication)[-keys](https://cloud.google.com/container-registry/docs/advanced-authentication))

  + GCP Artifact Registry (authentication via [json](https://cloud.google.com/container-registry/docs/advanced-authentication)[-keys](https://cloud.google.com/container-registry/docs/advanced-authentication))

![](/legacyfs/online/storage/blog_attachments/2023/02/pic5_DI2302.png)

**BUSINESS VALUE – BENEFITS:**

* Customers can create their own Docker-based-images for DI Cloud from scratch and can use them in several DI Cloud tenants (e.g. Dev, QA, Prod)

* Make migration from DI on-premise to DI Cloud more seamless

### API extension to improve Pipeline Scheduling

**USE CASE DESCRIPTION:**

* Possibility to set the timeout for graph scheduling via the ***POST /v1/runtime/graphs*** API.
  The Graph turns dead in case it cannot be scheduled within the timeframe that is specified with this new property:

  + New property *scheduleTimeoutSeconds* (minimum value: 240)

* Possibility to retrieve a more detailed context in a new *Reason* property that is retrieved when executing the ***GET /v1/runtime/graphs/’handle’*** API in case a graph could not be scheduled/started properly (e.g., *Unschedulable,…*)

* See also SAP API Business Hub for a full specification of the [Pipeline Engine API for SAP Data Intelligence Cloud](https://api.sap.com/api/vflow/resource)

![](/legacyfs/online/storage/blog_attachments/2023/02/pic6_DI2302.png)

**BUSINESS VALUE – BENEFITS:**

* More flexibility for automatic pipeline scheduling via Pipeline Engine API

### Support GBQ in Generation 1 and Generation 2 Flowagent SQL Executor Operator

**USE CASE DESCRIPTION:**

* Allow Execution of SQL queries against Google Big Query in Generation 1 and Generati...