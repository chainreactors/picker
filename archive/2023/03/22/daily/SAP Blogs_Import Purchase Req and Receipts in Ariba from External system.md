---
title: Import Purchase Req and Receipts in Ariba from External system
url: https://blogs.sap.com/2023/03/21/import-purchase-req-and-receipts-in-ariba-from-external-system/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:14:49.832763
---

# Import Purchase Req and Receipts in Ariba from External system

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Import Purchase Req and Receipts in Ariba from Ext...

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1817&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Import Purchase Req and Receipts in Ariba from External system](/t5/spend-management-blog-posts-by-members/import-purchase-req-and-receipts-in-ariba-from-external-system/ba-p/13547879)

![former_member44048](https://avatars.profile.sap.com/former_member_small.jpeg "former_member44048")

[former\_member44048](https://community.sap.com/t5/user/viewprofilepage/user-id/44048)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1817)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1817)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13547879)

‎2023 Mar 21
11:38 PM

[4
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1817/tab/all-users "Click here to see who gave kudos to this post.")

6,338

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [SAP Integration Suite, managed gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite%252C%2520managed%2520gateway/pd-p/73554900100800000194)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Integration Suite, managed gateway for spend management and SAP Business Network](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite%252C%2520managed%2520gateway%2520for%2520spend%2520management%2520and%2520SAP%2520Business%2520Network/pd-p/73554900100800000872)
* [SAP Ariba Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Procurement/pd-p/73554900100700001921)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP Integration Suite, managed gateway

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite%25252C%2Bmanaged%2Bgateway/pd-p/73554900100800000194)
* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite, managed gateway for spend management and SAP Business Network

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite%25252C%2Bmanaged%2Bgateway%2Bfor%2Bspend%2Bmanagement%2Band%2BSAP%2BBusiness%2BNetwork/pd-p/73554900100800000872)
* [SAP Ariba Procurement

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BProcurement/pd-p/73554900100700001921)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (7)

**Understanding Problem Statement**

“Nothing is impossible” if we think in positive way. Yes, there will be many hurdles to achieve final goal.

Solutioning in customer digital transformation landscape is very complicated day by day as, many customers want to leverage their skills set and systems to be get connected with new age cloud technology. To achieve this there are many middleware’s need to be incorporated in solution map. Middleware are the backbone of every interface that uses exchange of data across multiple systems.

As my personal journey with SAP ARIBA skill set as procurement domain expert with many customers there were always a common question comes from across all “*Is there a possibility to integrate my Purchase Requisitions from my non-SAP system in to SAP ARIBA ??”* Answer to this question is “Yes”.

There are ways and considerations which will change as per customer landscape and existing system compatibility. This blog can be treated as reference to an approach details and build need to work by individual implementation consultant.

We have observed if non-SAP application can be connected to other tools than SAP ARIBA then why not SAP ARIBA. It will certainly possible. So, I will explain understanding on solution that we build on well known telecommunication customer for Procure to Order operation (PR, PO, GR)

**Assumption** –

* WSDL or Technical JSON structure are customer specific so not discussed in detail in this blog

* Field mapping with non-SAP to SAP Ariba system will also differ from customer to customer so not discussed in this blog.

* There might be many other success stories for the scenario but as a System Implementation partner, It’s an achievement that we have deployed E2E scenario in business Procurement area.

* This blog is written from more Functional, or process point of view and not technical setup of SAP CPI is explained.

* Solution that we discussed is only limited to “Create/ new” operation for its lifecycle and no EDIT or Change nor GR reversals are considered as a part of this interface to keep solution easy and simple. However, this would be possible with little extra efforts and extra time.

It is team effort, so we required a skillful resource on project SAP ARIBA, SAP CPI or PI/PO ad SAP ABAP, SAP Ariba support team (Activation of API).

**Prerequisite for the process –**

* Master data (commodity code, company code, plant, users etc.) must be in sync with non-SAP system and transformation layer system and in SAP ARIBA and SAP S4 or SAP ECC system.

* Transformation logic for field mapping must be decided and communicated to get it sent from interface.

* Configuration in SAP CPI and SAP ARIBA (Core Administration>Integration Manager>Endpoint Set up and mark the task Import PR and Import GR on Webservice mode) must be there.

[Import Requisition(s)](https://s1.ariba.com/Buyer/Main/aw?awh=r&awssk=MtxDOnS2&realm=HcltechDSAPP-c1-T)

[Export Response for Import Requisitions Task Status Asynchronously](https://s1.ariba.com/Buyer/Main/aw?awh=r&awssk=MtxDOnS2&realm=HcltechDSAPP-c1-T)

[Import Receipts from an External Application](https://s1.ariba.com/Buyer/Main/aw?awh=r&awssk=MtxDOnS2&realm=HcltechDSAPP-c1-T)

* API must be activated within SAP ARIBA realm so ready to consume.

* Requisitions with Item category “M” or Material based Requisitions are considered for this interface.

**High Level Process flow is shown as below**

* ![](/legacyfs/online/storage/blog_attachments/2023/03/IMPORT-PR-NEW.jpg)

Let us now discuss the above flow in details

We are discussing the encircled part of solution. There are 3 steps in this E2E solution as

1) Create PR in non-SAP system and send it to SAP ARIBA

2) Retrieve the PR status and SAP PO number and send ba...