---
title: Tips to make efficient use of Test Automation Tool in S/4 HANA Public Cloud
url: https://blogs.sap.com/2022/12/29/tips-to-make-efficient-use-of-test-automation-tool-in-s-4-hana-public-cloud/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:17.944607
---

# Tips to make efficient use of Test Automation Tool in S/4 HANA Public Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Tips to make efficient use of Test Automation Tool...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66475&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Tips to make efficient use of Test Automation Tool in S/4 HANA Public Cloud](/t5/enterprise-resource-planning-blog-posts-by-members/tips-to-make-efficient-use-of-test-automation-tool-in-s-4-hana-public-cloud/ba-p/13543567)

![prasadbalaji](https://avatars.profile.sap.com/b/b/idbbaec238fee58ab0ae284de591680873c7ac3e2553266669df7adc1a05d9a86c_small.jpeg "prasadbalaji")

[prasadbalaji](https://community.sap.com/t5/user/viewprofilepage/user-id/134227)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66475)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66475)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543567)

‎2022 Dec 29
8:31 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66475/tab/all-users "Click here to see who gave kudos to this post.")

2,522

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SAP S/4HANA Cloud Public Edition Supply Chain](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Supply%2520Chain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [test automation tool for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/test%2520automation%2520tool%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Supply Chain

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSupply%2BChain/pd-p/253c6759-2b52-46f4-be45-e2ab78f2f420)
* [test automation tool for SAP S/4HANA Cloud

  Software Product Function](/t5/c-khhcw49343/test%2Bautomation%2Btool%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

View products (4)

This blog post is targeted specifically to SAP S/4 HANA Public cloud customers/prospects to let them understand the key steps involved to make efficient use of test automation tool offered by SAP. As we all know SAP S/4 HANA Public cloud promotes implementing SAP best practices to various business processes and from year 2022 the upgrade cycle has moved from Quarterly to Half yearly upgrade for SAP S/4 HANA Public cloud releases .

During the implementation and upgrade schedule, considerable time and effort is required to test all of the required business processes across various business functions to make sure the processes work as per Business requirements and also there is no regression impact due to the upgrade/additional scope items being implemented.

As we normally witness in many projects, project teams tend to test only the specific business scenarios that is being changed or implemented but forget/ignore to test the connected scenarios due to time constraints or lack of knowledge. In order to overcome all these challenges, SAP has come up with the test automation tool that can help to faciliate to automate all of the testing required in a SAP S/4 HANA Public cloud system that saves lot of time and effort for IT and Business stakeholders involved in testing the application

Below are the list of FIORI apps that SAP has provided to set up and execute automated testing in the system environment

![](/legacyfs/online/storage/blog_attachments/2022/12/Automated-Testing.jpg)

FIORI Apps for Automated Testing

* Manage your Test processes - Involves using Standard test scripts or preparing Custom test scripts across various business functions that need to be executed as part of testing. (Business role required for access - SAP\_BR\_ADMIN\_TEST\_AUTOMATION)

* Test your processes - Involves preparing the test plan and data using data variants to execute and analyze test results

* Analyze Automated Test results - Dashboard to view and analyze test results with screenshots and exportable logs captured in the system

* Test Data Container (TDC) - Centralized repository of all test data variants to be used for testing

* Manage Post Upgrade Tests (PUT) - Test processes targeted to test system upgrades

**Manage your test process**

SAP has provided predelivered test scripts for standard business processes across various business functions. Based on the scope items that are activated in the Q-system, the test user will be able to see list of standard test processes. Test user can use these processes As-Is or copy  the standard into a custom processes and modify the process steps as per business requirements. For creation of custom process step, SAP also provided UI recording functionality to record any steps as required. All custom process steps created would need to be adapted for every upgrade release before executing the test script. Apart from these two test processes, SAP delivers post upgrade test (PUT) processes as well that are specifc to upgrades which can be used to run post any system upgrade

**Steps involved to set up Custom Test processes using Manage your test process app**

* Creation of custom test process by copying standard test process

* Changing the visibility to make it visible for test plan creation

* Edit custom test process/process step

**Test your processes**

This is the main application where the user sets up the test plan, Test data containers, Test variants, execute and analyze test results. All of these process steps are detailed out with clear cut guidance in every detail for each step involved.

**Steps involved to set up and execute test plan using Test your process app**

* Create or upload your test plan

* Edit test plan to add/delete test processes

* Edit Action data in process steps (Standard and Custom) using variants

* Execution of Test plan (Schedule and Ad-hoc)

* Analysis of test results (with screenshots and logs) and correction of test plan (as required)

* Download/Print Test plan execution summary and detailed summary

* Re-execute failed test plan as required

Below are some important tips to be considered when using SAP Test Automation tool

**Set you local version**

The test processes are displayed based on the local country version that the user selects in Manage your solution. Pls check and select the correct country for which test processes are to be displayed

**Use ...