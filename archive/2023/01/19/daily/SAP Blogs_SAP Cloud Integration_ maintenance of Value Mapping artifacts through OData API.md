---
title: SAP Cloud Integration: maintenance of Value Mapping artifacts through OData API
url: https://blogs.sap.com/2023/01/18/sap-cloud-integration-maintenance-of-value-mapping-artifacts-through-odata-api/
source: SAP Blogs
date: 2023-01-19
fetch_date: 2025-10-04T04:16:50.446488
---

# SAP Cloud Integration: maintenance of Value Mapping artifacts through OData API

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Cloud Integration: maintenance of Value Mappin...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163159&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud Integration: maintenance of Value Mapping artifacts through OData API](/t5/technology-blog-posts-by-members/sap-cloud-integration-maintenance-of-value-mapping-artifacts-through-odata/ba-p/13567824)

![PiotrRadzki](https://avatars.profile.sap.com/7/1/id71bb6e4ed9428b556c2b9086b9ef0a581a7859e697fd8e9ce793504f5f2e1d35_small.jpeg "PiotrRadzki")

[PiotrRadzki](https://community.sap.com/t5/user/viewprofilepage/user-id/120998)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163159)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163159)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567824)

‎2023 Jan 18
8:41 PM

[25
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163159/tab/all-users "Click here to see who gave kudos to this post.")

18,897

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

Are you curious how to maintain your Value Mapping objects in Cloud Integration in a non-manual and automatic way with data from external systems, applications or remote locations?

**Look no more! You have found the right place!**

But let's start from the beginning…

## Introduction

Value Mapping (VM) is a very well-known and useful integration artifact that is consumed in most Integration Scenarios. Experienced Integration Developers are familiar and often use this object for mappings and conversions. If you are the lucky one and already have experience with VM objects you may want to skip this unit and jump directly to the core and Scenario unit.

Value Mapping in SAP Cloud Integration similarly to how it was in SAP PI/PO provides functionality to store bidirectional value mapping entries stored in containers identified with a unique pair of Source/Target Agency and Identifiers. VM artifact can be then used in the Message Mapping step or in Groovy Script to retrieve target values based on source value of the field. Simple example of Value Mapping conversion might be Country ISO code conversion between ISO alpha-3 and ISO alpha-2 code.

Example:

From the source system we receive Country code as “POL” (alpha-3 ISO code) but for integration purposes we need to convert it to “PL” (alpha-2 ISO code) as target system process and understand only alpha-2 ISO codes. For that purpose we can implement Message Mapping or Groovy Script in our iFlow that will call VM artifact and convert into target value based on provided source value. Such VM objects can be maintained with Country code conversion for reusability purposes by multiple iFlows at the same time.

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-10-14_09_31-ecPC-IntegrationDevelopment-Desktop-and-94-more-pages-Osoba-1-Microsoft​-Edg.png)

In this way we will be able to use beforehand prepared value mapping entries. Information stored in a VM object is providing bidirectional mapping functionality, it means we can convert both ways from source to target and from target to source values.

Value Mapping objects might be used for more complex scenarios and use cases for example to store some Integration Flow (iFlow) related attributes needed in runtime for dynamic configuration, determination or for message routing purposes.

For detailed documentation on Value Mapping object in Cloud Integration please refer to official SAP documentation:

[Creating Value Mapping | SAP Help Portal](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/25eff9b4884d4f6e859e6ebf898dcb71.html)

[Configuring Value Mappings | SAP Help Portal](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/6c8847fe8dcc459580a63194fc55d5b3.html)

Above documentation provides detailed procedure on how to maintain Value Mapping artifacts and VM entries through WebUI of Cloud Integration.

If you want to check how to integrate and maintain Cloud Integration VM objects with data coming from 3rd party systems using SAP Cloud Integration OData API you are in the right place! Please continue with reading this blog - I promise it will not be (so) long reading.

## Scenario

In this use case scenario let's assume we want to replicate Customer master data from SAP backend system to 3rd party system using SAP Cloud Integration as middleware. Due to the nature and capabilities of the target system this had to be a custom iFlow as no standard content was available.

As part of Customer master data entity on the target system side there are several fields that require conversion but not only to different readable values but also into system specific GUID format (for example 825f1c22-162e-e011-8836-1200c2992223). These target system GUID values could unexpectedly change on the target system, therefore automatic updating of value mapping is the main prerequisite for the orchestration. I was looking for a generic and standard approach as it is required to convert multiple fields in such a way. To handle this requirement in the best way and to not impact performance of the replication process I’ve chosen a Value Mapping object in SAP Cloud Integration. This object fits well with the requirement of storing source to target field values conversions.

Ultimate goal is to be able to automatically update and deploy VM artifacts with new/updated value mapping entries coming from 3rd party systems so it can be then used in the Customer master data replication process. In this Blog I will focus on one field that is converted in such a way and will present the approach to maintain a VM object with external values using a separate scheduled process. ![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-11-08_26_32-STADA_TIAC_Integration_v1.pptx-PowerPoint.png)

## Implementation

Currently SAP Cloud Integration provides an already impressive number of internal OData API's to handle objects and internal operations on Cloud Integration artifacts. You can find always up to date list of Integration Content API here: [Overview | Integration Content | SAP API Business Hub](https://api.sap.com/api/IntegrationContent/overview)

New features are coming on a regular basis so if you want to stay up to date with the new Cloud Integration API's and features coming in then follow Release Notes for Cloud Integration.

In this blog I will focus on Integration Content - Value Mapping related operations. API Reference contains an already long list of AP...