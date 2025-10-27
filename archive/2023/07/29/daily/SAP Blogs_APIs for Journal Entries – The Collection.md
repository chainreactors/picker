---
title: APIs for Journal Entries – The Collection
url: https://blogs.sap.com/2023/07/28/apis-for-journal-entries-the-collection/
source: SAP Blogs
date: 2023-07-29
fetch_date: 2025-10-04T11:52:45.241782
---

# APIs for Journal Entries – The Collection

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* APIs for Journal Entries – The Collection(updated ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162895&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [APIs for Journal Entries – The Collection(updated July, 2025)](/t5/technology-blog-posts-by-sap/apis-for-journal-entries-the-collection-updated-july-2025/ba-p/13565258)

![Hazel](https://avatars.profile.sap.com/8/6/id8607ef9494d657c07428a81caa963be09c8207636e8b464164a907d3e1bd38c8_small.jpeg "Hazel")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Hazel](https://community.sap.com/t5/user/viewprofilepage/user-id/153491)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162895)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162895)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565258)

‎2023 Jul 28
8:03 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162895/tab/all-users "Click here to see who gave kudos to this post.")

15,658

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (2)

This blog provides a comprehensive collection of APIs for Journal Entries. Whether you are using SAP S/4HANA Cloud or SAP S/4HANA, this blog will equip you with all the necessary resources to effectively utilize and troubleshoot our API.

### 1.) Introduction

Learn about the different APIs available for journal entries, including synchronous and asynchronous options. Find the links to the latest business documents for both SAP S/4HANA Cloud and SAP S/4HANA.

+ Journal Entry - Post (Synchronous)
  Post journal entries synchronously from external systems to your SAP S/4HANA Cloud system using this inbound service. You can extend this service according to your business needs. This service is based on the SOAP protocol and published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/JOURNALENTRYCREATEREQUESTCONFI/overview) and [SAP S/4HANA](https://api.sap.com/api/OP_JOURNALENTRYCREATEREQUESTCONF_IN/overview)

+ Journal Entry - Post (Asynchronous)
  Post journal entries asynchronously from external systems to your SAP S/4HANA Cloud system using this inbound service. This service is published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/JOURNALENTRYBULKCREATIONREQUES/overview) and [SAP S/4HANA](https://api.sap.com/api/OP_JOURNALENTRYBULKCREATIONREQUEST_IN/overview)

+ Journal Entry - Change (Asynchronous)
  Change part of the header or item information of existing journal entries using this inbound service. This service is based on the SOAP protocol and published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/JOURNALENTRYBULKCHANGEREQUEST_/overview) and [SAP S/4HANA](https://api.sap.com/api/OP_JOURNALENTRYBULKCHANGEREQUEST_IN/overview)

+ Journal Entry – Clearing (Asynchronous)
  Clear journal entries from SAP S/4HANA Cloud asynchronously using this inbound service. This service supports G/L account clearing, customer account clearing, and vendor account clearing. This service is based on the SOAP protocol and published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/JOURNALENTRYBULKCLEARINGREQUES/overview) and [SAP S/4HANA](https://api.sap.com/api/OP_JOURNALENTRYBULKCLEARINGREQUEST_IN/overview)

+ Journal Entry by Ledger - Post (Asynchronous)
  Post journal entries asynchronously by ledger from external systems to your SAP S/4HANA Cloud system using this inbound service. This service is based on the SOAP protocol and published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/JOURNALENTRYBULKLEDGERCREATION/overview) and [SAP S/4HANA](https://api.sap.com/api/OP_JOURNALENTRYBULKLEDGERCREATIONREQ_IN/overview)

+ Operational Journal Entry Item - Read (A2X)
  Extract operational journal entry item data to an external system using this inbound service. This service is based on the OData protocol and can be consumed in Fiori apps and on other user interfaces.This service only extracts journal entries with an entry view and is not designed to extract large data volumes.This service is published on the SAP API Business Hub. [SAP S/4HANA Cloud](https://api.sap.com/api/API_OPLACCTGDOCITEMCUBE_SRV/overview) and [SAP S/4HANA](https://api.sap.com/api/API_OPLACCTGDOCITEMCUBE_SRV/overview)

### 2.) Setting Up

Before you start using our API, you'll need to set it up. Here's how you can enable API functions on SAP S/4HANA Cloud and SAP S/4HANA.

+ [How to setup the Web Service Configuration of Journal Entry API for S/4 HANA On-Premise System](https://blogs.sap.com/2020/12/17/how-to-setup-the-web-service-configuration-of-journal-entry-api-for-s-4-hana-on-premise-system/)(added December 17, 2020)

+ [Guidelines for configuring Communication Scenario Finance – Posting Integration (SAP\_COM\_0002)](https://blogs.sap.com/2019/09/06/guidelines-for-configuring-communication-scenario-finance-posting-integration-sap_com_0002/)(added September 6, 2019)

### 3.) Testing the API

+ You can test our API using SOAPUI or POSTMAN. Here's how: [Guidelines for Testing Journal Entry API with SOAPUI and Checking Response Message](https://blogs.sap.com/2019/09/10/guidelines-for-testing-journal-entry-api-with-soapui-and-checking-response-message/)(added September 10, 2019)

+ For asynchronous testing and verifying outbound messages, refer to this blog: [Guidelines for Enabling Outbound API Journal Entry – Change Confirmation (Asynchronous)](https://blogs.sap.com/2019/11/26/guidelines-for-enabling-outbound-api-journal-entry-change-confirmation-asynchronous/)(added November 26, 2019)
+ Set up a service on *SAP Integration Suite* that handles journal entry confirmation messages via outbound service, refer to this blog: [Deploying a SOAP Service for Confirmation of Journal Entry Asynchronous SOAP API via Outbound Servic](https://community.sap.com/t5/technology-blog-posts-by-sap/deploying-a-soap-service-for-confirmation-of-journal-entry-asynchronous/ba-p/14137489) (added July, 2025)
+ How to enable S/4 HANA outbound services, refer to this blog: [How to Enable S/4 HANA Outbound Service for Journal Entry - Post (Asynchronous)](https://community.sap.com/t5/technology-blog-posts-by-sap/how-to-enable-s-4-hana-outbound-service-for-journal-entry-post-asynchronous/ba-p/14132392)(added Ju...