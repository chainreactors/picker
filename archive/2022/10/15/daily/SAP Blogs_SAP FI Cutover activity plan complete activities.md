---
title: SAP FI Cutover activity plan complete activities
url: https://blogs.sap.com/2022/10/14/sap-fi-cutover-activity-plan-complete-activities/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:25.484602
---

# SAP FI Cutover activity plan complete activities

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP FI Cutover activity plan complete activities

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66056&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP FI Cutover activity plan complete activities](/t5/enterprise-resource-planning-blog-posts-by-members/sap-fi-cutover-activity-plan-complete-activities/ba-p/13538228)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66056)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66056)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13538228)

‎2022 Oct 14
8:35 PM

[13
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66056/tab/all-users "Click here to see who gave kudos to this post.")

57,270

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)
* [FIN Asset Accounting](https://community.sap.com/t5/c-khhcw49343/FIN%2520Asset%2520Accounting/pd-p/253758978139952938680563247610563)
* [FIN General Ledger](https://community.sap.com/t5/c-khhcw49343/FIN%2520General%2520Ledger/pd-p/141573396494884189617506284133567)
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)
* [FIN Asset Accounting

  Software Product Function](/t5/c-khhcw49343/FIN%2BAsset%2BAccounting/pd-p/253758978139952938680563247610563)
* [FIN General Ledger

  Software Product Function](/t5/c-khhcw49343/FIN%2BGeneral%2BLedger/pd-p/141573396494884189617506284133567)
* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)

View products (7)

***Introduction***

ABC SAP Implementation Project will replace some of ABC’s existing legacy applications with SAP. This cutover approach document defines how existing ABC business processes, operations, systems, and data will be transitioned to SAP. It also focuses on both the technical and system processes required to have the SAP production system operational along with the interim process, procedures and governance measures that will need to be put in place by XXXXXX (cutover date) to ensure the transition is as smooth as possible.

***Purpose***

This document aims to identify and describe all tasks associated with the project cutover. In addition, it outlines the objectives, scope, approach, responsibilities and resources associated with cutover activities. This document will be used as a key communication tool to project teams regarding cutover activities.

To ensure consistency in communication, the following terminology will be used to describe the stages of implementation:

**Cutover** represents the period immediately prior to go-live. It includes the set of activities required to prepare the SAP production system and transition data and processes from the legacy environment to SAP production.

**Go-live** is the point in time when the production system becomes available to end-users.

**Post-implementation** support is the period immediately following go-live where the project will be primarily responsible for coordinating and managing support activities. After this initial period, primary responsibility will transfer to ABC’s IT support function.

**Handover** Refers to the project phase where project deliverables and responsibilities will be transferred to ABC.

***Objectives of Cutover***

The overall objective of the cutover activity is to transition ABC operations from operating its business systems and using legacy applications, to operating its business using SAP.

The overall guiding principles for cutover are to:

* Ensure users are without the Legacy system for as short a time as possible

* Ensure no parallel processing of data is to occur after cutover period

* Follow techniques that are consistent, tested, tried and true

* Minimize the disruption to ABC’s business operations during the cutover process

* Ensure appropriate and timely communication and escalation process throughout the implementation period. This includes a clear process for the escalation of issues and decision making in a timely manner during this complex period

* Minimize the risk of having a non-planned, non-considered or uncontrolled situation occur during the implementation process

* Ensure appropriate engagement and support of ABC’s stakeholders to facilitate the resolution of issues, acceptance of risks and availability for decision making necessary during the implementation process

The specific cutover objectives are:

* To prepare the SAP Enterprise Resource Planning (ERP) production environments for cutover and go live.

* To provide Business Area or profit center wise Trial balance

* To migrate all system configuration from test to the production environment.

* To ensure that SAP batch jobs are scheduled.

* To successfully convert all data (albeit on different dates).

* To ensure verification and signoff of converted data by appropriate business users and project resources.

* To decommission redundant legacy systems.

***Cutover Roles and Responsibilities***

*Data Owners*

* Process Owners/core team Provide signoff on the final load files before their final load into SAP

* Ensure that data extraction and transformation activities are executed to schedule, as detailed in the project plan

* Provide sign-off and approval of all data objects

* Continuously monitor local changes in the enterprise and asses any impact on SAP data

* Assist in the facilitation of dual data maintenance activities in both the legacy and SAP applications during the cutover period

*Data Validation*

* Prepares appropriate validation/reconciliation plans to ensure high standards of data quality within the SAP system

* Works with the cutover manager to ensure appropriat...