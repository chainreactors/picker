---
title: SAP CPI / PI – Hybrid concept to Data Base – Batch and Stored Procedure
url: https://blogs.sap.com/2023/06/25/sap-cpi-pi-hybrid-concept-to-data-base-batch-and-stored-procedure/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:45:57.609099
---

# SAP CPI / PI – Hybrid concept to Data Base – Batch and Stored Procedure

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP CPI / PI - Hybrid concept to Data Base - Batch...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163347&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CPI / PI - Hybrid concept to Data Base - Batch and Stored Procedure](/t5/technology-blog-posts-by-members/sap-cpi-pi-hybrid-concept-to-data-base-batch-and-stored-procedure/ba-p/13568990)

![rhviana](https://avatars.profile.sap.com/1/2/id1293610da630b8bdcc225f1ffcef912b628a41620563b195ef4f9c2c9d4de7b6_small.jpeg "rhviana")

[rhviana](https://community.sap.com/t5/user/viewprofilepage/user-id/160570)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163347)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163347)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568990)

‎2023 Jun 25
10:08 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163347/tab/all-users "Click here to see who gave kudos to this post.")

4,477

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (3)

Hello Folks,

One more interesting blog and sharing the knowledge and experience with you, about integration of SAP CPI and SQL JDBC to use batch mode and stored procedure.

Maybe comes in your mind the question, why needs stored procedure ?

**If yes I will tell you later...**

I'm not going to explain deep the concept of hybrid, setup of SAP PI/PO, bussiness process, stored procedure details in data base, step by step because there is many bogs about those topics that easily you can find the list below:

Worth to mention another blogs and helps in relation to this topic:

* **Stored Procedure:**

* + <https://blogs.sap.com/2020/07/05/sap-cpi-executing-stored-procedure-in-jdbc-adapter/>

* **Step by Step JDBC:**

* + [https://blogs.sap.com/2021/09/30/sap-cloud-integration-cpi-jdbc-adapter-step-by-step-guide-pre-requi...](https://blogs.sap.com/2021/09/30/sap-cloud-integration-cpi-jdbc-adapter-step-by-step-guide-pre-requisites-and-configuration-jdbc-batch-insert-cpi/)

* **Upsert Single Builk:**

  + [https://blogs.sap.com/2022/02/26/sap-cpi-jdbc-adapter-upsert-single-bulk-using-direct-sql-splitter-a...](https://blogs.sap.com/2022/02/26/sap-cpi-jdbc-adapter-upsert-single-bulk-using-direct-sql-splitter-and-stored-procedure-with-xml-payload-without-looping/)

* **SAP Course view:**

  + <https://developers.sap.com/tutorials/btp-integration-suite-execute-batch-payload.html>

* **JDBC Demo**

  + <https://blogs.sap.com/2019/02/19/cloud-integration-a-simple-demo-scenario-using-the-jdbc-adapter/>

* **Note:**

  + <https://userapps.support.sap.com/sap/support/knowledge/en/3073748>

* **Help SAP:**

  + <https://help.sap.com/docs/cloud-integration/sap-cloud-integration/payload-and-operation>

* **PI/PO Runtime:**

  + <https://blogs.sap.com/2019/04/03/sap-cpi-scenario-on-pipo-on-premise-runtime/>

* **SAP GuideLines Hybrid:**

  + <https://www.sap.com/documents/2020/11/400ae14b-bf7d-0010-87a3-c30de2ffd8ff.html>

## **Introduction:**

---

The blog is to present the overvire of integration in Hybrid concept implementation ( SAP CPI responsible for development -  SAP PI/PO Runtime responsible to receive and send the message across the applications on-premise.

#### Why this definition ? Advantages ?

The definition is because those applications are running on-premise under the same network, but thinking forward with possible migration from on-premise to on-cloud project.

#### Advantages:

* Same network ( Avoid externalize calls between on-prem and on-cloud )

* Avoid network issues

* Faster

* Security

* Migration to Cloud

* Reliable

* Others...

---

> ### **OOOO... I almost forgot, start to think in the future with SAP about ground to ground integrations using the Edge Integration Cell - Neuron Edge**

* [SAP Integration Suite enhanced for today’s digital processes – SAP TechEd 2022 Edition](https://blogs.sap.com/2023/01/30/sap-integration-suite-enhanced-for-todays-digital-processes-sap-teched-2022-edition/)

* [Update on SAP’s Integration Strategy – SAP TechEd 2022 Highlights](https://blogs.sap.com/2022/11/21/update-on-saps-integration-strategy-sap-teched-2022-highlights/)

---

**To-Be - Neuron Edge:**

Neuro Edge you can provide to your customer ON-PREMISE to ON-PREMISE with public cloud for example, this service bring this capabilities all in cloud:

* On-premise for SAP integration Suite could tenant ( Not more on-premise SAP PI )

* Customer move from SAP PI/PO to SAP Integration Suite

* On-premise API Gateway

* Event security bridge from SAP "Legacy" to Event Mesh or NO-SAP event brokers

The Neuro Edge is made for groud to ground implementations where you have SAP Integration Suite in the private cloud this contains some components for integration to holding integrations Ground-Ground.

**Low footprint, high performance, pervasive, reliable.**

Also interesting that you can have many instances of Edge as the sample of tenant spread around the world supporting the ground to ground integrations:

![](/legacyfs/online/storage/blog_attachments/2023/06/Edge.png)

I will explore this topic in future blog.

---

## Integration architecture perspective - On-prem to On-prem:

---

The scenario is the integration of SAP with JDBC, as you can see in the diagram I'm still using the real SAP PI runtime and not the new SAP offering for this which they call it as **"Neuron Edge"** as I explained above.

**AS-IS - PI Runtime:**

![](/legacyfs/online/storage/blog_attachments/2023/06/BlogJDBC.png)

The SAP PI/PO will be responsible to receive the call, proceed with the transformation of message from XML to SAP XML SQL format and decide if the stored procedure should be call or not depends of the case.

Ok, I almost forgot after this diagram, let's remind the topic why the designer is JDBC call + stored procedure ?

It's because the SAP JDBC adapter does not support UPDATE\_INSERT operation in the HANA  ASE database tables, Microsoft SQL Service and others, **note that SQL XML payload is supported in INSERT, UPDATE and DELETE modes only.**

The statement has the same format as for the UPDATE action. Initially, the same action is executed as for UPDATE. If no update to the database table can be made for this action (the condition does not apply to any tab...