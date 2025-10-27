---
title: Step by Step Guide – Running Automation Script in SAP Cloud ALM
url: https://blogs.sap.com/2023/07/11/step-by-step-guide-running-automation-script-in-sap-cloud-alm/
source: SAP Blogs
date: 2023-07-12
fetch_date: 2025-10-04T11:54:53.189227
---

# Step by Step Guide – Running Automation Script in SAP Cloud ALM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Step by Step Guide - Running Automation Script in ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67439&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Step by Step Guide - Running Automation Script in SAP Cloud ALM](/t5/enterprise-resource-planning-blog-posts-by-members/step-by-step-guide-running-automation-script-in-sap-cloud-alm/ba-p/13555569)

![sonam_kukreja](https://avatars.profile.sap.com/0/b/id0b7bc5a6d68d88d648de90b3c7dd7db9110e6f1e19e206f9b52ae8c48623fb20_small.jpeg "sonam_kukreja")

[sonam\_kukreja](https://community.sap.com/t5/user/viewprofilepage/user-id/150827)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67439)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67439)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555569)

‎2023 Jul 11
9:23 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67439/tab/all-users "Click here to see who gave kudos to this post.")

8,213

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [test automation tool for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/test%2520automation%2520tool%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [test automation tool for SAP S/4HANA Cloud

  Software Product Function](/t5/c-khhcw49343/test%2Bautomation%2Btool%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (3)

# Introduction

In this blog post, I want to share my recent experience of working on an S/4HANA Cloud implementation for a well-known customer in Australia. During this project, my role was to conduct testing using the SAP Cloud automation tool. As we were following the best practices implementation for the customer for phase 1, the testing scope was limited to automation testing using the best practices script.

Throughout the project, I gained valuable insights and learning opportunities that I believe could be beneficial to others who are planning to undertake similar projects. In this blog post, I will focus on sharing these learnings in the hopes of helping others, especially those who are new to the field.

So, if you are someone who is interested in SAP Cloud automation testing or is planning to undertake a similar project, then keep reading to learn more about my experiences and the valuable lessons I learned on this project.

For the purpose of this blog, I have chosen the best practice BD9, which is "Sell from Stock."

To better understand the process, I encourage users to go through the process first to become familiar with this well-known process in the S/4HANA space.

[Sell from Stock (BD9) (ondemand.com)](https://education.hana.ondemand.com/education/pub/s4/index.html?library=library.txt&show=book!BO_343579C1CFDE56B0)

# Pre-Requisites

To start with the SAP S/4HANA Cloud tenant should be Integrated with SAP Cloud ALM. This has been covered quite in detail in other blog posts.

[Integrating SAP Cloud ALM and the Test Automation Tool [TAT] for SAP S/4 HANA Cloud | SAP Blogs](https://blogs.sap.com/2022/06/20/integrating-sap-cloud-alm-and-the-test-automation-tool-tat-for-sap-s-4-hana-cloud/)

# Test Preparation

### Test Preparation

As with any test planning exercise, we will start the test preparation work on our BD9 script. As its a standard best practice item, the test case can be created directly in Cloud ALM using the steps below

![](/legacyfs/online/storage/blog_attachments/2023/07/1-35.png)

Test Preparation

### Create New Automated Type Test Case

As stated earlier, for the purpose of this blog we are going to use the solution process BD9.

![](/legacyfs/online/storage/blog_attachments/2023/07/2-18.png)

Create Auto Test Case

### Synchronize Test Cases

After creating the test case in Cloud ALM, synchronize it with your S/4HANA test tenant, where the SAP S/4HANA Cloud Automation tool will run. Press the button below to synchronize the test case.

![](/legacyfs/online/storage/blog_attachments/2023/07/3-18.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/4-15.png)

Synchronize CALM Content with S/4 Tenant

The above step will generate a test plan automatically which can be viewed inside the **Test Your Processes** app. Details in the later section of this blog.

# Design Time: Create, Manage and Customize your end-to-end Processes

As part of the design phase you can use the **Manage Your Test Processes** Fiori App to create and manage end-to-end test process.

Every test process is a set of one or more process steps and a process step is a series of actions which we will see in a bit more detail in subsequent steps. As part of the design work, the automation tester will spend considerable time in customizing and adapting the process steps and actions within them to align with the business process and requirements. Further, the effort will be spent on setting up test data containers relevant for the solution process and its associated data variants.

### Create Test Data Container

The test data container are added to the test process and customers can create their own test data containers where needed. Please note that standard test data containers can be enhanced with additional fields if needed by your business process. SAP has provided lots of standard SAP TDC to support the various S/4HANA business processes and most of the time they have enough attributes within a container to support the test process.

The standard best practice scripts, comes with the appropriate Test Data Container. For BD9, the test data container is *Sales Order Management and Processing*

![](/legacyfs/online/storage/blog_attachments/2023/07/5-15.png)

Test Data Container

### Create Variants for Test Data Container

With the variants feature, flexibility is offered to the customers in terms of re-using the same container with different sets of data. For instance, one can maintain different variants for different company codes and each variant will have its own set of data that will be used in the end-to-end process.

The variants can be accessed by clicking the test data container inside the Manage Your Test Processes App.

![](/legacyfs/online/storage/blog_attachments/2023/07/6-11.png)

Test Data Container

In my project, I had to run the BD9 process across multiple company codes and hence I created multiple variants for the test process.

Each variant based on its company code can have its own set of dat...