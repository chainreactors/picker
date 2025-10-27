---
title: Tricentis Test Automation for SAP Cloud ALM (TTA for Cloud ALM)
url: https://blogs.sap.com/2023/07/21/tricentis-test-automation-for-sap-cloud-alm-tta-for-cloud-alm/
source: SAP Blogs
date: 2023-07-22
fetch_date: 2025-10-04T11:54:00.473479
---

# Tricentis Test Automation for SAP Cloud ALM (TTA for Cloud ALM)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Tricentis Test Automation for SAP Cloud ALM (TTA f...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159870&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Tricentis Test Automation for SAP Cloud ALM (TTA for Cloud ALM)](/t5/technology-blog-posts-by-members/tricentis-test-automation-for-sap-cloud-alm-tta-for-cloud-alm/ba-p/13548634)

![Delia_Barabasy](https://avatars.profile.sap.com/e/3/ide321a0b5c3d13779d2c0dbf791414ccb429cd600ae439a5f3f778dfdde4fec6d_small.jpeg "Delia_Barabasy")

[Delia\_Barabasy](https://community.sap.com/t5/user/viewprofilepage/user-id/149312)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159870)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159870)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548634)

‎2023 Jul 21
9:03 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159870/tab/all-users "Click here to see who gave kudos to this post.")

8,090

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

# An introduction to Tricentis Test Automation for SAP Cloud ALM (TTA for Cloud ALM)

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-07-20-at-16.10.43.png)

## **SAP Partnership with Tricentis**

Tricentis, a renowned testing software provider with a global customer base, has joined forces with SAP to deliver Tricentis test Automation for SAP Cloud ALM. Tricentis brings its expertise in advanced test automation, including model-based testing, and now offers its cloud-based solution.

Since 2020, SAP has been reselling Tricentis solution and has established a long-term roadmap for joint development.

With prior knowledge on Tosca and the documentation available on the TTA tenant I created the first test cases and tested the integration. Today, I share with you a sneak peek into this new collaboration.

##

## **Continuous Test Automation**

Before I jump into the tool and features, I would like to clarify a few terminologies first.

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-07-20-at-16.14.06.png)

### **Glossary**

SAP Enterprise Continuous Testing by Tricentis:

* Current product from Tricentis (Tosca) resold by SAP under a Solution Extension (SOlEx) agreement.

* Acronym: ECT

SAP Test Automation by Tricentis

* Future SAAS/Cloud product from Tricentis, will be resold by SAP. Based on tricentis Test Automation

* Acronym: none

Tricentis Test Automation for SAP Solution Manager:

* An OEM offering from SPA to the enterprise support customers

* This is a subset of ECT in terms of functionalities

* Acronym: TTA for SAP Solution Manager

Tricentis Test Automation for SAP Cloud ALM:

* Will be an OEM offering from SAP to the enterprise support customers

* This will be a subset of SAP Test Automation by Tricentis

* Acronym: TTA for SAP Cloud ALM

Various tools assist us in identifying what needs to be tested, assessing its functionality, scalability, and data accuracy. The image below illustrates the names of these tools (including both SAP and Tricentis) and how they contribute to the testing process.

![](/legacyfs/online/storage/blog_attachments/2023/07/Screenshot-2023-07-26-at-14.00.42.png)

## **SAP Cloud ALM and Tricentis Test Automation: The Why?**

Let's first clarify the question of why test cases should be automated:

* Time savings through automated test execution.

* Error reduction through precise and consistent test execution

* Scalability for increasing requirements and test environments

* Repeatability of tests as often as required

* Efficient execution of regression tests

### **SAP Cloud ALM and Tricentis Testautomation**

Next is a brief explanation of what is available on the Cloud ALM side and the Tricentis Cloud side. The integration is done through test automation APIs that are publicly accessible.

**Separation of duties:  SAP Cloud ALM vs Tricentis test Automation Cloud**

When it comes to integration, SAP aims for a clear separation of duties. Under SAP Cloud ALM, we have management entities for business processes, requirements, user stories, and defects, all linked to both manual and automated test cases. For automated test cases, SAP utilizes the destination framework and the Test Automation Endpoint with test automation APIs to connect to a test automation provider, in this case, Tricentis. SAP Cloud ALM primarily focuses on orchestration, but execution is also possible from this platform. Additionally, reporting and triggering of test cases from Tricentis are available within SAP Cloud ALM.

For each SAP Cloud ALM tenant, there will be one corresponding Tricentis tenant. The automated test cases are maintained on the Tricentis side, and using Transformation APIs, only the necessary information is synchronized. On the Tricentis side, we have the destination for test automation, including test automation authoring, maintenance, adjustments, and execution.

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-07-20-at-16.21.25.png)

**Agents**

In Tricentis Test Automation for SAP Cloud ALM, the execution of tests is facilitated by an Automation Agent. This agent functions as a program that can be installed on your local or virtual machine, or even within a container. The Agents establish a connection with your Tricentis Test Automation for SAP instance and remain ready to receive and execute tests at all times.

On the Tricentis side there will be an execution grid which allows you to manage the agents.

The Agents can be On-Premise (for example, on Customer Landscape) or on Cloud called Hosted execution Agents (TTA side). The Hosted Agents a not available today but are planned for 2024.

There are two types of Agents: **private** and **shared**. These agents are the same just configured differently.

1. Private Agents. You can use the private agent to run a test locally and the results of the tests are visible only to you.

2. Shared Agents. With the shared agent you can have multiple users running tests in the same test environment. This allows you to work on your machine while the tests run on a different machine.

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-07-20-at-16.22.12.png)

## **Execute an Automated Test Case from SAP Cloud ALM**

![](/legacyfs/online/storage/blog_attachments/2023/06/Screenshot-2023-06-29-at-12.18.42.png)Before starting to execute your Test Case make sure the Status of your Test Case in Test Preparation is set to “Prepared”. If it is not set to “Prepared” you won’t be able to see it here.

To run your Test you must open “Test Execution” in SAP Cloud ALM.

1. First, we want to filter the test cases after Project, Scope, Solution Process if necessary.

2. Another useful filter is to choose Automated under Test Cases.

3. Press E...