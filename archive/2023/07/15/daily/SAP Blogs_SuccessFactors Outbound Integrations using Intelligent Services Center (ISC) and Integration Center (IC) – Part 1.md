---
title: SuccessFactors Outbound Integrations using Intelligent Services Center (ISC) and Integration Center (IC) – Part 1
url: https://blogs.sap.com/2023/07/14/successfactors-outbound-integrations-using-intelligent-services-center-isc-and-integration-center-ic-part-1/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:52:51.611026
---

# SuccessFactors Outbound Integrations using Intelligent Services Center (ISC) and Integration Center (IC) – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* SuccessFactors Outbound Integrations using Intelli...

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5007&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SuccessFactors Outbound Integrations using Intelligent Services Centre (ISC) and Integration Centre (IC) – Part 1](/t5/human-capital-management-blog-posts-by-members/successfactors-outbound-integrations-using-intelligent-services-centre-isc/ba-p/13559383)

![amomin86](https://avatars.profile.sap.com/d/7/idd77e0d2b3293558e0e69848ff2ef916d5b539df76a025070c779a0844556179e_small.jpeg "amomin86")

[amomin86](https://community.sap.com/t5/user/viewprofilepage/user-id/40473)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5007)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5007)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559383)

‎2023 Jul 14
7:26 PM

[15
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5007/tab/all-users "Click here to see who gave kudos to this post.")

6,135

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (2)

Hello Friends,

Welcome to my blog series on the topic of “SuccessFactors Outbound Integrations using Intelligent Services Centre (ISC) & Integration Centre (IC)". In this post, I will delve into the details so we can understand different scenarios that can be addressed with the use of either Intelligent Service Centre (ISC) only or in combination with Integration Centre (IC).

**Scenarios****1. SF Outbound Data Comparison i.e., ISC Vs IC**
2. SF Outbound Filter Comparison i.e., ISC EC Business Rule Filter Vs IC Filter
3. SF Cross Portlet Update i.e., Integration Centre Vs Middleware System

**Target Audience**This blog post is specifically designed for customers using SuccessFactors Intelligent Services Centre or Integration Centre (IC) for Outbound Integrations and it may help the following participants.

* Admin

* Developers

* Consultants

**Architecture Diagram**This Architecture diagram is to highlight different systems and functionalities used by each of these systems.![](/legacyfs/online/storage/blog_attachments/2023/07/1-12.jpg)

Intelligent Services Centre (ISC): Monitors the business events and accordingly triggers actions configured/activated in this respective Service. ISC Performs XML data transfer to External Service Endpoints (like SAP Cloud Integration or Third-Party Application) or ISC can trigger Integration Centre Artefact for the given Entity Record based on the Event.

Integration Centre (IC): Performs XML, JSON, and CSV data transfer to respective External Service Endpoints (like SAP Cloud Integration or Third-Party Applications) or stores files onto SFTP Server.

SAP Cloud Integration: Performs data transformation and transfers it to Third Party or may also update data from Third Party into SuccessFactors via ODATA API.

Events: Events are basically system monitoring different actions performed by Admin, Employee, etc.

### **Scenario 1: SF Outbound Data Comparison i.e., ISC Vs IC**

We will compare the outbound data generated by Intelligent Services Centre and Integration Centre.
We are using SAP CPI as External Service Endpoint.

We are using the Event “Change in Job Title” in Intelligent Services Centre to perform 2 Actions.

Scenario 1A: SF ISC -> SAP CPI
Scenario 1B: SF ISC -> SF IC -> SAP CPI![](/legacyfs/online/storage/blog_attachments/2023/07/2-8.jpg)

**Configuration Steps**
1. Goto Intelligent Services Centre and search for Event “Change in Job Title”.![](/legacyfs/online/storage/blog_attachments/2023/07/3-4.jpg)

**Scenario 1A**: SF ISC to SAP CPI

1. Click on Event Connector and select new Event Connector

![](/legacyfs/online/storage/blog_attachments/2023/07/4-4.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/5-4.jpg)

2. Enter SAP CPI Inbound Service Endpoint and Credential details and Save Flow. ![](/legacyfs/online/storage/blog_attachments/2023/07/6-2.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/7-2.jpg)

**Scenario 1B**: SF ISC to SF Integration Centre to SAP CPI
1. Click Integration to Add Integration via Integration Centre Artefact Creation.![](/legacyfs/online/storage/blog_attachments/2023/07/8-1.jpg)

2. Click Create New Integration![](/legacyfs/online/storage/blog_attachments/2023/07/9-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/10.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/11.jpg)

3. Insert 3 Sibling Elements each for UserId, StartDate, Event Reason resp.![](/legacyfs/online/storage/blog_attachments/2023/07/12.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/13.jpg)

4. Click on Field Mapping Icon on the top right and drag the field Start Date from Left Column (EmpJob) to the field StartDate in the central column. This is to map fields. Perform the same for a User ID to UserId and Event Reason to Event Reason resp.![](/legacyfs/online/storage/blog_attachments/2023/07/14.jpg)

5. Click next on Response Fields and Filter screens as we don’t need to configure anything here.![](/legacyfs/online/storage/blog_attachments/2023/07/15.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/16.jpg)

6. Enter CPI Service Endpoint and Credential details.![](/legacyfs/online/storage/blog_attachments/2023/07/17.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/18.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/19.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/20.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/21.jpg)

Now there are 2 configs done here and this is how it looks.

Scenario 1A: SF ISC to SAP CPI
Scenario 1B: SF ISC to SF IC to SAP CPI![](/legacyfs/online/storage/blog_attachments/2023/07/22.jpg)

**Data Change Steps to Trigger Event**There are different ways to trigger Promotion but since we are testing, we will use a quick method.

1. Goto Employee Profile – Job Information – History – Click Insert![](/legacyfs/online/storage/blog_attachments/2023/07/23.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/24.jpg)

2. Enter the Effective date, Event, and new Position so Job Title is also changed which is good to trigger the Event we selected in ISC.![](/legacyfs/online/storage/blog_attachments/2023/07/26.jpg)

**Data Comparison for Payloads Received in CPI**Intelligent Services Centre is calling Listener 5 Service and Integration Centre is calling Listener 4 Service. B...