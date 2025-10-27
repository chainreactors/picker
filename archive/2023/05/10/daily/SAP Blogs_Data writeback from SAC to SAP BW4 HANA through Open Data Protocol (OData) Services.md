---
title: Data writeback from SAC to SAP BW4 HANA through Open Data Protocol (OData) Services
url: https://blogs.sap.com/2023/05/09/data-writeback-from-sac-to-sap-bw4-hana-through-open-data-protocol-odata-services/
source: SAP Blogs
date: 2023-05-10
fetch_date: 2025-10-04T11:39:22.145240
---

# Data writeback from SAC to SAP BW4 HANA through Open Data Protocol (OData) Services

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Data writeback from SAC to SAP BW4 HANA through Op...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163248&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data writeback from SAC to SAP BW4 HANA through Open Data Protocol (OData) Services](/t5/technology-blog-posts-by-members/data-writeback-from-sac-to-sap-bw4-hana-through-open-data-protocol-odata/ba-p/13568555)

![shreyas_s](https://avatars.profile.sap.com/b/7/idb7616a798304adad2409d4be70e06cf132bd59a892e54b37460c8fffeef2bf12_small.jpeg "shreyas_s")

[shreyas\_s](https://community.sap.com/t5/user/viewprofilepage/user-id/139683)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163248)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163248)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568555)

‎2023 May 09
10:43 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163248/tab/all-users "Click here to see who gave kudos to this post.")

16,617

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)

View products (2)

The purpose of this article is to explain the integration mechanism between two SAP platforms - SAP Analytics Cloud (SAC) and SAP BW/4 HANA (SAP Business Warehouse) through OData (Open Data Protocol) services that provides data writeback feature. This integration opens a plethora of opportunities for businesses to make informed decisions with advanced and flexible analytic capabilities.

**Introduction to SAP Analytics Cloud and SAP BW/4 HANA:**

SAP Analytics Cloud (SAC) is a cloud-based business intelligence and analytics platform developed by SAP. It is a software as a service (SaaS) tool that combines planning, reporting and predictive analytics into a single solution. SAC provides a user-friendly and interactive interface for data analysis, allowing users to visualize and explore data in real-time with the help of charts, tables, and graphs.

One of the key functionalities of SAP Analytics Cloud (SAC) is that it provides the possibility to build own planning models and applications natively within SAC. During project implementation, there will certainly be a need to export data in SAC models to SAP Business Warehouse which we call as SAP BW or SAP BW/4 HANA.

SAP BW is a data warehousing and analytics solution provided by SAP that enable organizations to store, access, and analyze large amounts of data from multiple sources. It also provides real-time data analysis and decision-making capabilities to organizations. SAP has provided data storage objects in BW system which physically stores data in transparent tables and is referred to as advanced data store object (ADSO)

**What is OData Services?**

OData (Open Data Protocol) services is a standard protocol for creating and consuming RESTful (Representational State Transfer) web services.

RESTful web services use HTTP methods such as GET, POST, PUT, and DELETE to perform operations on data.

SAP provides OData services for accessing and manipulating data in SAP systems using URL based service calls. It enables cloud-based and mobile solutions to access SAP data seamlessly using a uniform format.

The SAP NetWeaver Gateway acts as a mediator between various systems and applications. Through push mechanism, the data gets written from SAC to BW/4 HANA ADSO

The entire process of data flow from BW to SAC and data writeback from SAC to BW is illustrated in the below diagram

![](/legacyfs/online/storage/blog_attachments/2023/05/SAC-BW-HANA-dataflow.png)

Data flow from BW to SAC and data writeback from SAC to BW

**Why OData Services?**

The reason to choose OData Services as data transfer mechanism is because of the following benefits

* **Standardized Interface:** OData services provide a simple and uniform way for accessing and manipulating data in SAP systems

* **Integration:** It enables broad integration across products between non-SAP and SAP applications easily

* **Implementation flexibility:** OData services can be implemented in various programming languages and can interact with different system components

* **Data security:** OData services in SAP have robust security mechanisms to ensure that only authorized users can access and manipulate data

* **Metadata consistency:** OData services follow a unified metadata format, ensuring that data consistency is maintained across different systems and applications

**How to establish connection from SAC to SAP BW/4 HANA through OData Services?**

The OData services connection works in such a way that, one connection can be used to create any number of export jobs in SAC which can writeback data to different target ADSOs. Below are the steps involved in establishing connection from SAC to SAP BW/4 HANA ADSO

* Decide the SAC planning model from where the data needs to be sent to BW/4 HANA ADSO

* Login to SAC, open the SAC planning data model and select “data management” workspace

* Create export job under “Export Jobs” section by selecting export data mechanism as “OData Services”

* The system will ask for the connection to be used while creating the export job. This connection would already be present in SAC created using the data service URL. If not available, a new connection needs to be created with the help of SAP basis team

* Now select the target ADSO by choosing the corresponding technical name, perform field mapping from SAC as source to ADSO table as target

* Save the export job and execute it in SAC. The data starts getting transferred to ADSO in BW/4 HANA

**Design considerations for OData Services during data writeback**

We need to keep in mind certain parameters from design perspective while using OData Services as data writeback from SAC to BW/4 HANA

* Only an administrator at SAC side can trigger the export jobs created through OData services

* Only write interface enabled ADSOs of type Standard Datastore Object are supported. Planning Mode ADSO is not supported

* Compounding characteristics in ADSO cannot be handled in any special way. All the superior characteristics, along with the compounding characteristic should be mapped in SAC

* Before data export, SAC always converts fiscal dimension to calendar dimension. Hence, fiscal period characteristic in ADSO is not exposed for export. You can map only 0CALMONTH but not 0FISCPER from SAC to BW ADSO

* Export of Account calculations in SAC model is currently not supported

* Measure should be defined in ADSO by only these types of fields: CURR, QUAN and FLTP or a Key Figure

* Dimension should be defined in ADSO by types of fields: CHAR, CUKY, UNIT, ...