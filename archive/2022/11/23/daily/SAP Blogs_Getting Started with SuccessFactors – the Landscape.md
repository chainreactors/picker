---
title: Getting Started with SuccessFactors – the Landscape
url: https://blogs.sap.com/2022/11/22/getting-started-with-successfactors-the-landscape/
source: SAP Blogs
date: 2022-11-23
fetch_date: 2025-10-03T23:29:09.189047
---

# Getting Started with SuccessFactors – the Landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Getting Started with SuccessFactors – Basics and i...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5887&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Getting Started with SuccessFactors – Basics and introduction to the Landscape](/t5/human-capital-management-blog-posts-by-sap/getting-started-with-successfactors-basics-and-introduction-to-the/ba-p/13554679)

![orkuntuerkmen](https://avatars.profile.sap.com/4/c/id4c3e9f367c9af2b3f225acf2bababf0c17a7cea77a9e403da9f8ce0d4ffdc932_small.jpeg "orkuntuerkmen")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[orkuntuerkmen](https://community.sap.com/t5/user/viewprofilepage/user-id/23353)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5887)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5887)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554679)

‎2022 Nov 22
8:32 PM

[21
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5887/tab/all-users "Click here to see who gave kudos to this post.")

12,943

* SAP Managed Tags
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors Mobile](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Mobile/pd-p/67838200100800005707)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)

* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors Mobile

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BMobile/pd-p/67838200100800005707)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (4)

## Overview

I received similar questions about SAP SuccessFactors (SF) landscape from our partners and customers; therefore, I decided to write a blog about common cross-customer questions.

This blog is intended for customer admins, and consultants new to SAP SuccessFactors.

The intent is to provide information in a simple way via a FAQ-kind structure. Feel free to share your opinion and areas for improvement and request the next blog topic.

### What is SAP SuccessFactors, SAP SF?

SAP SuccessFactors is a cloud-born, cloud-based software for Human Experience Management(HXM) using the Software as a service (SaaS) model. It was founded in 2001 and acquired by SAP SE in 2011/12. ([What is HMX, how it differs from HCM, and why it matters?](https://www.sap.com/documents/2020/02/903820b9-857d-0010-87a3-c30de2ffd8ff.html))

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP-Successfactors.jpg)

### What is Software as a Service (SaaS) model that SAP SF is using?

Software as a service (SaaS) works through the cloud delivery model. Typically, SaaS apps are web or mobile apps that users can access via a web browser. SAP or one of its hosting partners (so-called Hyperscalers; Microsoft Azure, Goole Cloud, Amazon AWS or Ali Cloud) host the SF application and related data.

![](/legacyfs/online/storage/blog_attachments/2022/11/Cloud-Classification-and-Responsibilities.jpg)

### Where are the DataCenters and their Disaster Recovery sites?

SAP SF introduces new Data centers or migrates some of its own data centers to hyperscalers. The most up-to-date list can be found at [SAP Trust Center](https://www.sap.com/about/trust-center/data-center.html?mode=solution&currentLevel=world&solutionId=ACE362) or [SAP KBA 2215682](https://userapps.support.sap.com/sap/support/knowledge/en/2215682)

![](/legacyfs/online/storage/blog_attachments/2022/11/Data-Center-locations.jpg)

### Can customers or SAP change the DataCenter assignment?

The dataCenter is part of the subscription agreement, but customers can request an instance migration. ([2453663 - SuccessFactors Instance Migration procedure](https://userapps.support.sap.com/sap/support/knowledge/en/2453663)). DC migration within the same country could be initiated/ executed by SAP as well for operational reasons.

### What are the details about IT infrastructure management?

Per SaaS standards, SAP does not provide servers, storage, or networking details. All of these could be modernized. All details about cloud operations and 3rd party reports can be found at [SAP Trust Center](https://www.sap.com/about/trust-center/cloud-operations.html)

### What are the details about System management?

Per SaaS standards, SAP does not provide the system, database, operating system, virtualization details, or patch levels. All of these could be modernized. For example, SAP SF used to run on Oracle DB and migrated to SAP HANA DB in 2018/19. Details and 3rd party audit reports could be found at [SAP Trust Center](https://www.sap.com/about/trust-center/cloud-operations.html)

### What is the Patch, built, service pack, and batch Number?

The Software change management is done centrally and version details are shown when you click your picture upper right corner and select "software version information"

e.g. Release: b2205.20221110071101. The first two numbers are the calendar year, and the following two numbers are the release details. The 05 is for the year's first release, and 11 stands for the second release, followed by patch details.

### What are the Supported Desktop Browsers for SAP SuccessFactors?

SuccessFactors supports the following browsers: Google Chrome, Microsoft Edge, Mozilla Firefox, and Safari by Apple. We support browser versions that are still supported by their developers. If its developer no longer supports your browser version, it may not be supported by SAP SuccessFactors.

Moreover, supported Mobile Browsers (as of 2022), Safari by Apple for iOS 13.0 +, Google Android 7.0 + default browser, Google Chrome for Android. If you want mobile access, please use the SAP SuccessFactors Mobile Application. Not all features and tasks are supported on mobile devices.

### Any hardware or browser requirements for using SAP SuccessFactors?

We recommend the following settings for optimum performance,

Network bandwidth (bandwidth that is required to surf the Internet 400kbit+), recommended available cache size for the browser up to 250MB (SAP SuccessFactors is a Web 2.0 application. We recommend allowing browser caching). adobe acrobat reader and java runtime environment 1.6+ should be installed. javascript, [cookies](ht...