---
title: SAP CO Cutover activity plan complete activities- Controlling Activities
url: https://blogs.sap.com/2022/10/18/sap-co-cutover-activity-plan-complete-activities-controlling-activities/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:14:50.154802
---

# SAP CO Cutover activity plan complete activities- Controlling Activities

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP CO Cutover activity plan complete activities- ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66930&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CO Cutover activity plan complete activities- Controlling Activities](/t5/enterprise-resource-planning-blog-posts-by-members/sap-co-cutover-activity-plan-complete-activities-controlling-activities/ba-p/13548887)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66930)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66930)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548887)

‎2022 Oct 18
7:04 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66930/tab/all-users "Click here to see who gave kudos to this post.")

8,626

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Controlling/pd-p/165905235116577077914579113243106)
* [FIN Cost Object Controlling](https://community.sap.com/t5/c-khhcw49343/FIN%2520Cost%2520Object%2520Controlling/pd-p/251991085556036308395324851400611)
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)
* [Implementation Methodologies](https://community.sap.com/t5/c-khhcw49343/Implementation%2520Methodologies/pd-p/104367144430565227162334366685847)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BControlling/pd-p/165905235116577077914579113243106)
* [Implementation Methodologies

  Topic](/t5/c-khhcw49343/Implementation%2BMethodologies/pd-p/104367144430565227162334366685847)
* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)
* [FIN Cost Object Controlling

  Software Product Function](/t5/c-khhcw49343/FIN%2BCost%2BObject%2BControlling/pd-p/251991085556036308395324851400611)

View products (7)

## **Purpose**

This document aims to identify and describe all tasks associated with the project cutover related to SAP Controlling. In addition, This document will be used as a key communication tool to project teams regarding cutover activities.

## **Introduction**

A number of steps need to be executed in order to deliver a fully operational S/4 HANA system in the live production environment. The Cutover Strategy seeks to explain the sequence of activities required to achieve this and propose drawing up of a schedule for the tasks, dates, data conversion and the upload of the necessary balances and open items into the production system.

There are two types of data involved in a SAP system: Master Data and Transaction Data.

* **Master Data**

Application master data tends to be static once defined. Most master data can be driven by the Legacy applications. Examples include cost center, profit center, bills of materials, resource etc.

* **Transactional data**

This type of data covers current and outstanding transaction data that needs to be captured from the Old system and defined to the SAP applications for business process completion. Examples include open purchase orders, open accounting documents, initial stocks and so on.

## **Intended Audience**

This document to be used to communicate the cut over strategy to the Project Management and Steering Committee and obtain important business decisions required to carry out activities involved in cut over. It is to be used to communicate to all team members the strategy to be followed for cut over.

## **Master Data**

It should always be remembered that “Data *Migration Makes or Breaks the Project*. “

Following are the pre-requisite steps in Data Migration with elaboration on the same:

* **Data Identification – Implementation partner Team**

* **Data Preparation – Client Team**

* **Data Sanitization – Client Team**

* **Data Conversion - Client Team**

* **Data Upload – Client Team**

**Approach :** Data collection will be done in excel & upload will be done through LTMC, LSMW, BAPI & Transport request for respective element etc.

Below are the list of master data in controlling –

**Statistical Key Figure (SKF)**

SKF data will be created manually

Dependency – N/A

**Profit Center Hierarchy**

Profit Center Hierarchy will be created as per finalized organisation structure.

Dependency – N/A

**Profit Center**

Profit center will be created as per finalized organisation structure by LTMC (Migration Tool).

Dependency – Segment

**Cost Center Hierarchy**

Cost Center Hierarchy will be created as per finalized organisation structure.

Dependency – N/A

**Cost Center**

Cost center will be created as per finalized organisation structure by LTMC (Migration Tool).

Dependency – Profit Center

**Activity Types**

Activity will be created manually by KP26

Dependency – GL Master(FI)

**Activity Rates**

Planned Activity Quantities against each Activity Type/Cost Centre Combination AND Costs per Cost Centre/Cost Element combination needs to be uploaded by LTMC.

Dependency – Cost Center

**Cost Center Budgeting (If Applicable)**

Uploaded by FIORI APP.

Dependency – Cost Center

**Assessment cycle**

Manual Activity

Dependency – Cost Center

## **Transactional Data**

1. Perform Standard Cost Release  for all the FG/SFG materials through CK40N manually.

2. Overhead rate calculation: Overhead rates to be calculated for FG products need to finalized and maintained in S/4 HANA so that during product costing these rates are calculated.

3. Internal Order Available Budget values till XXXXXX will be transferred to new system with new Internal Order Codes. Old Internal Order number  will be stored in New Internal order Master for future comparative reference by LSMW or LTMC (Migration Tool).

Above are the general CO cutover activities which might be helpful to understand and conclude your cutover plan.

Please share your feedback and let me know incase you need blog on any specific topic.

**Please follow my blog for FI cutover activities -**

<https://blogs.sap.com/2022/10/14/sap-fi-cutover-activity-plan-comp...