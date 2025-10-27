---
title: SAP S/4HANA Service Reporting Framework (RFW)
url: https://blogs.sap.com/2022/10/25/sap-s-4hana-service-reporting-framework-rfw/
source: SAP Blogs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:33.927234
---

# SAP S/4HANA Service Reporting Framework (RFW)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Service Reporting Framework (RFW)

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/47314&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Service Reporting Framework (RFW)](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-service-reporting-framework-rfw/ba-p/13533126)

![smid](https://avatars.profile.sap.com/9/f/id9f12d8f127fdd7859d3d4512662f64e55f188534d9b7d23dd3883bb1229100f7_small.jpeg "smid")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[smid](https://community.sap.com/t5/user/viewprofilepage/user-id/145508)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=47314)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/47314)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13533126)

‎2022 Oct 25
8:05 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/47314/tab/all-users "Click here to see who gave kudos to this post.")

4,012

* SAP Managed Tags
* [SAP CRM Service Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520CRM%2520Service%2520Manager/pd-p/67837800100800006431)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [CRM Analytics](https://community.sap.com/t5/c-khhcw49343/CRM%2520Analytics/pd-p/487591118709456302511762181002127)
* [CRM Service](https://community.sap.com/t5/c-khhcw49343/CRM%2520Service/pd-p/336839465795980684603250734763165)

* [SAP CRM Service Manager

  SAP CRM Service Manager](/t5/c-khhcw49343/SAP%2BCRM%2BService%2BManager/pd-p/67837800100800006431)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [CRM Analytics

  Software Product Function](/t5/c-khhcw49343/CRM%2BAnalytics/pd-p/487591118709456302511762181002127)
* [CRM Service

  Software Product Function](/t5/c-khhcw49343/CRM%2BService/pd-p/336839465795980684603250734763165)

View products (4)

## Introduction

With SAP S/4HANA Service, several new transactional business objects were introduced in SAP S/4HANA. All these transactions are based on the so-called One Order Model, which is one of the foundations of the VDM layer for Service and Solution Business. In the recent years, we’ve seen a high focus on analytical, reporting, or search capabilities which essentially all have one goal: scan the high volume of transactions in a customer system and extract either aggregated figures or transactions with given attributes. The rise of SAP HANA has emphasized this even more; it is now possible to run transactional and analytical applications on the same data basis and fetch search and analytical data using the new ABAP-based CDS technology that includes all needed features for security and authorization. As a consequence, the Reporting Framework had to be enabled for SAP S/4HANA as **Smart and Dynamic Central Search tool** for all One-Order Objects in Q2C and ASM

## Why You Can’t Use SAP CRM Reporting Framework in SAP S/4HANA Service

Though there are already quite a few apps and features in SAP S/4HANA Service that use the SAP CRM Web Client UI, SAP S/4HANA cannot use the CRM Reporting Framework (RFW) 1:1 for the following main reasons:

* Different Data model between CRM objects and CRM S/4HANA objects​​

* CRM Master Data are replaced by S/4HANA Master Data  ​

* Not all CRM features of the application processes are supported in SAP S/4HANA.

* Furthermore, some attributes available in SAP CRM data models have been replaced by Sales attributes re-used in SAP S/4HANA Service.

* Likewise, the CRM master data, such as business partner, product (replaced by material), IBASE (replaced by equipment), and functional location have been replaced by SAP S/4HANA’s master data, therefore requiring data extraction to utilize SAP S/4HANA’s master data extractors

* Transaction-related master data is replaced by SAP S/4HANA’s master data objects, such as IBASE, and functional location.

* Database access in SAP S/4HANA is based on the technology SAP ABAP CDS instead of the OPEN SQL statements

* The basic tool for synchronization and distribution of data between different components of an SAP CRM solution, SAP CRM Middleware, is not available in SAP S/4HANA, hence the CRM Bdoc cannot be used any more either.

These technological and conceptual differences mean that if you want to continue using the Reporting Framework functionality in SAP S/4HANA, you need to switch to the new SAP S/4HANA Reporting Framework based on the Core Data Services (CDS) technology.

## SAP S/4HANA Reporting Framework: Overview

RFW is a smart and Dynamic Central Search tool for all One-Order Objects in Q2C and ASM with main characteristics:

* All **Advanced searches of One-Order** **WebUI** **applications** use this tool in On-Premise deployment

* Used for **data determination** by related objects, **Product proposals & Where-used list** of One-Order objects and Interaction center (IC),..

* Used by Account management and interaction History in On-Premise deployment

* **Extensibility** of any One-Order application is automatically supported by this tool

* **Authorizations** of all business users are supported out-of-the-box via reading the user authorization profiles on the fly and include it in SELECT statement

* **Archiving** Search of all One-Order objects in On-Premise deployment is also supported

### Technical Perspective

From the technical perspective, SAP S/4HANA Service enables the following:

* Take leverage of facilities provided by SAP S/4HANA CDS views

* Reduce database access from two classical steps and merge them into one database access

* Reduce the number of database calls to fetch results

* Run transactional and analytical applications on the same data basis

* Get rid of object-specific locator list classes and make the framework generic to handle all scenarios.

### Main Characteristics of the Reporting Framework

#### Selection Level and Flexibility

Currently, SAP S/4HANA RFW doesn’t support all the features and the flexibility of the SAP CRM RFW. The most important characteristic with regard to the flexibility of the SAP CRM RFW is that the application that calls RFW can explicitly decide about the selection level/focus (header, item) during the creation of an RFW instance. This can be done in two ways:

* By setting an RFW instance parameter IV\_ITEM\_SELECT, IV\_ONLY\_MAIN\_ITEM

* By setting the suffix “I” after the selection field’s name (like STATUS\_I) and by adding an entry in the table CRMC\_REPDY. Without the suffix I, the selection semantics will focus on the header level by default by selecting only documents where the status is set on header.

This flexibility is still not supported by the new SAP S/4HANA RFW. The selection focus is currently controlled by the entry in table CRMS4\_RF\_REPDY based on the value “U” of “CALL FOR WHERE”. For example, if you take the entry of the field STAT\_OPEN, the selection semantics will consider th...