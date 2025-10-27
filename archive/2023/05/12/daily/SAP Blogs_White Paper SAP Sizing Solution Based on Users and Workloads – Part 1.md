---
title: White Paper SAP Sizing Solution Based on Users and Workloads – Part 1
url: https://blogs.sap.com/2023/05/11/white-paper-sap-sizing-solution-based-on-users-and-workloads-part-1/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:39.464523
---

# White Paper SAP Sizing Solution Based on Users and Workloads – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* White Paper SAP Sizing Solution Based on Users and...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162909&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [White Paper SAP Sizing Solution Based on Users and Workloads – Part 1](/t5/technology-blog-posts-by-members/white-paper-sap-sizing-solution-based-on-users-and-workloads-part-1/ba-p/13566512)

![aprao](https://avatars.profile.sap.com/1/d/id1dfd26151ea643961fb2ee8035c2b00e3d17720953e491da3095c658cfaf6311_small.jpeg "aprao")

[aprao](https://community.sap.com/t5/user/viewprofilepage/user-id/139458)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162909)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162909)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566512)

‎2023 May 11
7:13 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162909/tab/all-users "Click here to see who gave kudos to this post.")

1,839

* SAP Managed Tags
* [SAP NetWeaver Application Server](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server/pd-p/01200615320800000352)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP NetWeaver Application Server

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer/pd-p/01200615320800000352)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (3)

### Introduction

The purpose of this blog is to help customers to understand the concept of sizing based on SAP Workloads.
The sizing procedure helps customers to determine the correct resources required by an application within the customer’s business context.
I wanted to share to make it easier for any beginner wishing to prepare the Sizing Report.

### **What is SAPS**

SAPS is the standard SAP Benchmark of performance measurement ( i.e. measurement of CPU power). SAPS is an acronym word for – SAP Application Performance Standard (SAPS).

It is a hardware-independent unit of measurement that describes the performance of a system operation in the SAP environment. It is derived from the Sales and Distribution (SD) benchmark.

Hardware vendors do a benchmark on their hardware for SAP as per their methodology to see how many SD users can be supported. Each module has a weightage. The number of users in each module is converted to several Normalized SD (NSD) and SAPS value can be obtained.

### **SAP QuickSize****r**

Standard SAP sizing tool is available in SAP Marketplace called Quicksizer. However, SAP standard tool is for estimate only and is not accurate. It does not benefit customers to get the exact sizing solution.

The sizing solution in the Quicksizer tool is based on the number of concurrent users in each module, the approximate number of objects created in each module, and an approximate number of line items created every hour.

However, practically, only business functionality who are familiar with business transactions may provide information regarding the estimate number of objects created per hour in each module-wise and the estimate number of line items created or processed in every hour. Basis or System Administration or technical consultants are not sure what data to be entered to fill up the sizing in the Quicksizer tool.

The question is whether it is mandatory to fill up the standard SAP Quicksizing tool?. The answer is No.

However, this is advisable to fill up the standard SAP Quicksizing exercise on the SAP Marketplace website.

SAP strongly advises customers to contact various Hardware vendors and obtain sizing Questionnaires form from each vendor. Filled-up Questionnaires form will be sent back to their hardware vendors.

There is no need to enter several objects and/or line number of items created or processed in every hour.

Hardware vendors have their own default values. They recommend configurations with sufficient headroom to avoid resource bottlenecks.

Basis consultants from the implementation partner can assist customers to filled-up up questionnaires form and also choosing the correct hardware configuration.

Hardware vendors cannot help you estimate the impact of workload and infrastructure changes in deployed environments.

### **Limitations in using SAPQuick Sizing Tool**

The sizing calculation is not accurate. It is an estimate. SAP advises customers to contact Hardware suppliers to provide sizing solutions based on the customer’s requirements. Every Hardware supplier has its own sizing methodology.

Quicksizer estimates are based on assumptions – SAP assumptions about resource requirements based on transaction volumes generated by the user and the hardware vendor’s assumption about how deployed applications will use system resources.

Quicksizer cannot help you estimate the impact of workload and infrastructure changes in deployed environments. When the CIO asks, “What will it take to support another five hundred users?” or “Can we do multiple application and infrastructure configurations?”

#### Inaccurate:

No consideration of workload and infrastructure changes while sizing capacity and performance. Accuracy has been estimated at 20%. Hence it would be difficult to obtain the exact accuracy of the SAPS value.

The following lists are not taken into account in SAP Quicksizer calculation.

* Unicode

* Custom Objects

* Workload (batch processing, print)

* Interface

**Conclusion:**

Quicksizer estimates are based on assumptions

Quicksizer cannot help you estimate the impact of workload and infrastructure changes in deployed environments.

The next article, “White Paper SAP Sizing Solution Based on Users and Workloads – Part 2”, describes SAPS Sizing Methodology and Users classification.

**Reference:**

<https://www.sap.com/about/benchmark/sizing.html>

<http://service.sap.com/quicksizer>   – For Sizing exercises, the QuickSizer tool from SAP MarketPlace

Thanks for reading!

Follow for more such posts by clicking on FOLLOW => aprao

Please share your thoughts and feedback on this blog in a comment.

Prasad Rao

* [SAP Quick Sizer](/t5/tag/SAP%20Quick%20Sizer/tg-p/board-id/technology-blog-members)
* [sap sizing](/t5/tag/sap%20sizing/tg-p/board-id/technology-blog-members)
* [SAPQuick Sizing Tool](/t5/tag/SAPQuick%20Sizing%20Tool/tg-p/board-id/technology-blog-members)
* [saps](/t5/tag/saps/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members...