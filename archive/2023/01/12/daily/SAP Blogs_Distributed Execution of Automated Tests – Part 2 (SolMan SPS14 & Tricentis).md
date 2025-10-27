---
title: Distributed Execution of Automated Tests – Part 2 (SolMan SPS14 & Tricentis)
url: https://blogs.sap.com/2023/01/11/distributed-execution-of-automated-tests-part-2-solman-sps14-tricentis/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:25.761270
---

# Distributed Execution of Automated Tests – Part 2 (SolMan SPS14 & Tricentis)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Distributed Execution of Automated Tests - Part 2 ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158950&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Distributed Execution of Automated Tests - Part 2 (SolMan SPS14 & Tricentis)](/t5/technology-blog-posts-by-sap/distributed-execution-of-automated-tests-part-2-solman-sps14-tricentis/ba-p/13553251)

![valentinb](https://avatars.profile.sap.com/5/3/id5310e3d2cb9bf664c65dad6899740e738b9c02947d1e90c5d326047903ac0b24_small.jpeg "valentinb")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[valentinb](https://community.sap.com/t5/user/viewprofilepage/user-id/713974)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158950)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158950)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553251)

‎2023 Jan 11
8:29 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158950/tab/all-users "Click here to see who gave kudos to this post.")

4,271

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [SOLMAN Process Management](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Process%2520Management/pd-p/876619786935845126962162607976597)
* [SOLMAN Test Suite](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Test%2520Suite/pd-p/132949817163443344955330185779754)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Process Management

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BProcess%2BManagement/pd-p/876619786935845126962162607976597)
* [SOLMAN Test Suite

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BTest%2BSuite/pd-p/132949817163443344955330185779754)

View products (3)

### **BACKGROUND**

Multiple features related to automated test integration have been introduced by SAP Solution Manager 7.2 SPS14 release, including the ability to synchronise execution status of SAP Solution Manager test packages, with the results of automated tests triggered by SAP Enterprise Continuous Testing by Tricentis (ECT). This was described my [previous blog post](https://blogs.sap.com/2022/05/24/integration-of-external-execution-results-for-automated-tests-part-1-solman-sps14-tricentis/).

Now that you are familiar with this new integration, it is then possible to set up a **highly scalable** architecture by using **Distributed EXecution** feature (commonly known as DEX), which allows tests to be **run across all available computing resources**, such as computers on your network or virtual machines on the cloud.

### **WHAT IS DISTRIBUTED EXECUTION (DEX)?**

The purpose of Distributed EXecution (DEX) is to distribute your automated tests to multiple computing resources, called **agents**.

By default, when you execute your tests, SAP Enterprise Continuous Testing by Tricentis (ECT) takes control of your mouse and keyboard, so it can interact with the System Under Test (SUT). Consequently, users can't work on this machine for the duration of the test run. And if you have large test sets, it simply takes too long to run all of them on one machine.

Distributed Execution will **speed up large test runs** and **leaves user machines unblocked**.

In addition, and thanks to the integration, all agent results are returned to SAP Solution Manager.

![](/legacyfs/online/storage/blog_attachments/2023/01/High-level-architecture.png)

The different elements that make up this architecture are described in the table below:

|
 **User Machines (1-n VM/PC)** |
 **Tosca Distribution Server** |
 **Agents (1-n VM/PC)** |

|
 Create Tests    Define & trigger  execution    Synchronize results with SolMan |
 Part of Tosca Server    Distribute tests among agents    Monitor execution & agents |
 Execute the tests    Send results to Tosca Distribution Server |

### **HOW TO SETUP DISTRIBUTED EXECUTION (DEX) ENVIRONMENT?**

#### ![](/legacyfs/online/storage/blog_attachments/2022/12/Architecutre_detaillee.png)

#### **On Tosca Server**

In order to run Distributed Execution, a "DEX Workspace" must be created on Tosca Server. This workspace is a technical workspace, it should not be used as a "working" workspace for users.

The procedure for creating this workspace is the same as for any workspace creation. Simply use the connection string of the common repository.

![](/legacyfs/online/storage/blog_attachments/2022/12/dex_creation2-1.png)

Next, open the "Tricentis Service Configuration" of your Tosca Server. Then go to "Automation Object Service" tab and populate: "Workspace Folder", "Project Root Name", "Workspace Name", "Username", and "Password" fields with those from your DEX Workspace. Then click on "Save".

![](/legacyfs/online/storage/blog_attachments/2022/12/Dex-config.png)

#### **On the Agents**

To start and connect your Agents, right-click the file ToscaDistributionAgent.exe and select "Run as administrator" from the context menu. By default, this file is located on the folder: *"%TRICENTIS\_DEX\_AGENT\_HOME%".*After a few seconds, you should see the agent icon on the Windows taskbar.

![](/legacyfs/online/storage/blog_attachments/2022/12/Agent-successfully-strarted.png)

Agent icon in the Windows taskbar

Right-click the agent icon in the Windows taskbar and select "Configure Agent" from the context menu. This opens Tosca Distribution Agent Configuration window.

In the ToscaDistributionAgent Configuration window, click on "Connect to server" tab and enter the address of the DEX Server:

http://<Tosca Server Gateway IP address or host name>:<Gateway port>/DistributionServerService/CommunicationService.svc

![](/legacyfs/online/storage/blog_attachments/2022/12/connect.png)

Tosca Distribution Agent Configuration

If the connection to the DEX server is successful, the ToscaDistributionAgent configuration window displays a green check mark next to the server address input field. Finally, click on "Save".

You can also check that your agents appear in the "Agent view" tab of your Tosca Server.

![](/legacyfs/online/storage/blog_attachments/2022/12/Agent-view.png)

Agent View

#### **On the user machines**

Go to *Project->Settings->Commander->DistributedExecution->Server*. As the value of the setting "EndpointAddress", enter the address of ToscaGateway Service as follows:

http://<Tosca Server Gateway IP address or hostname>:<port>/DistributionServerService/ManagerService.svc

Go to *Project->Settings->Commander->DistributedExecution->Monitor Url*. As the value of the setting "Url", enter the address of ToscaGateway Service as follows:

http://<Tosca Server Gateway IP address or hostname>:<port>/Monitor/

![](/legacyfs/online/storage/blog_attachments/2022/12/config-tosca.png)

Tosca Settings

### **HOW TO USE DISTRIBUTED EXECUTION (DEX) COMBINED WITH SAP SOLUTION MANAGER INTEGRATION?**

As desc...