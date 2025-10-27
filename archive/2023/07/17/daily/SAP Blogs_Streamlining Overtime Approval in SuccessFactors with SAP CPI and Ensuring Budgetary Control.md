---
title: Streamlining Overtime Approval in SuccessFactors with SAP CPI and Ensuring Budgetary Control
url: https://blogs.sap.com/2023/07/16/streamlining-overtime-approval-in-successfactors-with-sap-cpi-and-budget-validation/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:32.395455
---

# Streamlining Overtime Approval in SuccessFactors with SAP CPI and Ensuring Budgetary Control

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Streamlining Overtime Approval in SuccessFactors w...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161873&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Streamlining Overtime Approval in SuccessFactors with SAP CPI and Ensuring Budgetary Control](/t5/technology-blog-posts-by-members/streamlining-overtime-approval-in-successfactors-with-sap-cpi-and-ensuring/ba-p/13560285)

![RubaElhafiz](https://avatars.profile.sap.com/3/1/id316a0a921f0566f2f9e6efd9c6bde8eb4310d118b9009fde2f47192853c0e386_small.jpeg "RubaElhafiz")

[RubaElhafiz](https://community.sap.com/t5/user/viewprofilepage/user-id/142008)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161873)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161873)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560285)

‎2023 Jul 16
8:10 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161873/tab/all-users "Click here to see who gave kudos to this post.")

3,964

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

**Introduction:**

Managing and controlling overtime requests efficiently is crucial for any organization to ensure appropriate resource allocation and maintain budgetary discipline. This blog post will explore how SAP Cloud Platform Integration (CPI) can be leveraged to automate and streamline the overtime approval process in SAP SuccessFactors. We will focus on integrating SAP CPI with SuccessFactors to automatically approve or reject overtime requests based on the availability of the budget.

**\*\* Kindly note that this blog specifically describes how to customize the iflow, and it uses customized SuccessFactors APIs**

**Approach:**

Using SAP SuccessFactors, we will create a user that will be used by CPI and serve as the second approver to the overtime request workflow. We will concentrate on establishing a CPI user as the second approver to evaluate budget availability before accepting or rejecting overtime requests. Before we get into the technical details, let's go over the redesigned overtime approval protocol in SuccessFactors:

* An employee submits an overtime request through the SuccessFactors user interface.

* The request is initially routed to the employee's immediate supervisor or manager (first approver).

* After the first approver reviews the request, it is forwarded to a CPI user designated as the second approver.

* The CPI user performs budgetary control to determine the availability of the budget for the requested overtime.

* Based on the budget availability, the CPI user decides whether to approve or reject the request.

* The decision is communicated back to the employee, and if approved, the overtime is processed accordingly.

**SuccessFactors side:**

* Create a user for CPI

* Give the user all the needed permission

* Make sure that your Admin Center > Object definitions of your custom entity (e.g., cust\_Overtimepreapprovalparent) is set with "Pending Data" equals to "Yes". Check: <https://me.sap.com/notes/0002604638>

**CPI side:**

Step (1): Insert the CPI’s user credentials:

Go to monitor > Security Material

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-19.png)

Create > User Credentials

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-14.png)

Fill up the fields using the credentials specification that was produced in SuccessFactors and choose the type: SuccessFactors. For example:

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-11.png)

Deploy and create a new user but this time the type should be User Credentials, and the user should be put as user@companyid as shown in the following photo:

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture4-9.png)

Deploy

Step (2):  Build the iflow

Start the iflow by adding a Timer to trigger the iflow

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-10.png)

As per the business request, the Timer will be set to recur every 30 sec

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture6-11.png)

Then, the Timer will be connected to the Request-Reply, and the Request Reply and a “Receiver will be connected using a SuccessFactors adapter

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture7-8.png)

Choose the Message Protocol to be OData V2

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture8-7.png)

Configure the adapter:

Connection: Choose the address depending on the data center and the environment by pressing the select button.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture9-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture10-5.png)

Then enter the Credential Name field using the previously established SuccessFactors type one.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture11-5.png)

Processing:

Operation Details: Get

Resource Path: Select

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture12-7.png)

This step depends on the name of the overtime approve request API in the SuccessFactors, in our case the API name is: cust\_Overtimepreapprovalparent, in this API there are the following fields:

* cust\_overtimeamount: it displays the cost of the requested overtime

* externalCode: contains the ID of the employee that requested the overtime

From the wfRequestNav, the following field will be fetched:

* currentStepNum: indicates the number of the current step in the workflow

* externalCode: unique number for each request

* wfRequestId: the id of the workflow of the overtime request

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture13-8.png)

**\*\* Fill in the Custom Query Options as recordStatus=pending**

Choose the Pagination to be Client

![](/legacyfs/online/storage/blog_attachments/2023/07/Capture-11.png)

Add General splitter

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture15-2.png)

Configure the splitter as per the received XML, to process each request individually

![](/legacyfs/online/storage/blog_attachments/2023/07/Capture-12.png)

Add Content Modifier

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture17-2.png)

Add the currentStepNum, wfRequestId, overtimeAmount, and the externalCode of the ...