---
title: Cross-System Workflow for SAP SuccessFactors Solutions
url: https://blogs.sap.com/2023/03/22/cross-system-workflow-for-sap-successfactors-solutions/
source: SAP Blogs
date: 2023-03-23
fetch_date: 2025-10-04T10:22:11.878642
---

# Cross-System Workflow for SAP SuccessFactors Solutions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Cross-System Workflow for SAP SuccessFactors Solut...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50989&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cross-System Workflow for SAP SuccessFactors Solutions](/t5/enterprise-resource-planning-blog-posts-by-sap/cross-system-workflow-for-sap-successfactors-solutions/ba-p/13554641)

![Sharath_T_N](https://avatars.profile.sap.com/0/9/id09c35c281ee96dafeadca68d7b6c2d9698f33eb3ee8f6ff07c909020ec2f8753_small.jpeg "Sharath_T_N")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Sharath\_T\_N](https://community.sap.com/t5/user/viewprofilepage/user-id/17618)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50989)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50989)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554641)

‎2023 Mar 22
1:51 PM

[19
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50989/tab/all-users "Click here to see who gave kudos to this post.")

7,974

* SAP Managed Tags
* [SAP SuccessFactors Employee Central](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central/pd-p/73555000100800000773)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP SuccessFactors Employee Central integration to SAP Business Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Employee%2520Central%2520integration%2520to%2520SAP%2520Business%2520Suite/pd-p/67837800100800005871)
* [SAP SuccessFactors HCM Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Core/pd-p/67837800100800006332)
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP SuccessFactors Employee Central integration to SAP Business Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral%2Bintegration%2Bto%2BSAP%2BBusiness%2BSuite/pd-p/67837800100800005871)
* [SAP SuccessFactors HCM Core

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BCore/pd-p/67837800100800006332)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [SAP SuccessFactors Employee Central

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BEmployee%2BCentral/pd-p/73555000100800000773)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (7)

## Introduction:

In a core-hybrid landscape, an HR process starts in SAP SuccessFactors Employee Central but ends with follow-up steps in applications like Payroll. HR admins find it difficult to track the end-to-end process. The cross-system workflow solution was envisioned to enable this transparency in the process visualization spanning multiple systems.

Cross-system workflow is a solution that is used to connect processes that span the cloud system(SAP SuccessFactors Employee Central) and SAP HCM on-premises systems or can even be extended to other systems. Some examples of such processes are hiring, promotion, change in the contract, termination, etc. cross-system workflow is the glue to streamline distributed processes, providing end-to-end visibility, and traceability.

Implementation Design Principle (SFIDP) document: [(Cross-System Workflow for SAP SuccessFactors Solutions](https://d.dam.sap.com/s/p/a/Wk4M7Zi)). Implementation Design Principle documents are owned and managed by SAP SuccessFactors Product Management who engage and collaborate with select, interested partners along with SAP Professional Service to tap the rich implementation experience distilled in the document after a formalized product review process before broader publication.

[Link to the document](https://d.dam.sap.com/s/p/a/Wk4M7Zi)

## Solution Overview and Concepts

Below is a visual of how workflows from EC, and SAP ERP HCM are joined using the SAP BTP.

Cross-system workflow for SAP SuccessFactors solutions leverages SAP Process Automation to connect workflows from SAP SuccessFactors Employee Central and SAP ERP HCM. The User Interface developed for the visualization of the cross-system workflow is called the “Worklist”. The worklist will be the central entry point for SAP SuccessFactors Employee Central and SAP ERP admins. There is a process detail page that would show the additional context of the workflow.

The important concept here is that the UIs of the respective systems are called from the central workflow in SAP BTP. So, the data entry screens don’t have to be rebuilt. All the data validations remain on the source system.

![](/legacyfs/online/storage/blog_attachments/2023/03/Figure-1-Cross-system-workflow-Solution-Visualization.png)

Figure 1 Cross-system workflow Solution Visualization

Each step in the Worklist may be executed in SAP SuccessFactors Employee Central or SAP HCM. The important concept here is that the UIs of the respective systems are called from the central workflow in SAP BTP. So, the data entry screens don’t have to be rebuilt. All the data validations will remain on the source system.

### High-level Data flow

![](/legacyfs/online/storage/blog_attachments/2023/03/Data-Flow-Diagram.png)

Figure 2: Data Flow Diagram

SAP Process Automation (Workflow) is used as a glue between the SAP SuccessFactors Employee Central workflow and process and Forms. SAP BTP workflow will be initiated when a cross-system process starts with a workflow in SAP SuccessFactors Employee Central which is triggered when an employee, manager, or HR makes relevant data changes.

SAP Cloud Integration(SCI) flow will serve as the mediator between SAP SuccessFactors Employee Central and SAP BTP workflow.

SCI will be a listener to the SAP SuccessFactors Employee Central workflow. Any changes in the approver list, status, or a move to a different step would trigger an update or initiate SAP BTP workflow. It will also fetch additional data to update the workflow context attributes which are required to build the cross-system Worklist. It will wait for the next notification event once the next processor takes an action in the EC workfl...