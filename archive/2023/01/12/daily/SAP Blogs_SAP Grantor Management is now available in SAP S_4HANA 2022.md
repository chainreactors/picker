---
title: SAP Grantor Management is now available in SAP S/4HANA 2022
url: https://blogs.sap.com/2023/01/11/sap-grantor-management-is-now-available-in-sap-s-4hana-2022/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:14.177055
---

# SAP Grantor Management is now available in SAP S/4HANA 2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Grantor Management is now available in SAP S/4...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51290&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Grantor Management is now available in SAP S/4HANA 2022](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-grantor-management-is-now-available-in-sap-s-4hana-2022/ba-p/13556669)

![diego_gaudenzi](https://avatars.profile.sap.com/f/d/idfde140df806617ccc815c04b6d2c4dc04323a54c79047f3b377cb8e16ec60f3d_small.jpeg "diego_gaudenzi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[diego\_gaudenzi](https://community.sap.com/t5/user/viewprofilepage/user-id/194694)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51290)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51290)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556669)

‎2023 Jan 11
9:11 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51290/tab/all-users "Click here to see who gave kudos to this post.")

6,152

* SAP Managed Tags
* [Public Sector](https://community.sap.com/t5/c-khhcw49343/Public%2520Sector/pd-p/130110653021563432906662)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [Public Sector

  Industry](/t5/c-khhcw49343/Public%2BSector/pd-p/130110653021563432906662)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (2)

Dear Readers,

Back in October 2022 SAP released the SAP S/4HANA 2022 (major release) and as part of this release you can find SAP Grantor Management. In this blog I will discuss the key features, benefits and roadmap of this solution.

First of all,  in case you are not familiar with SAP Grantor Management, here a series of great blogs published several years ago about the SAP Grantor Management solution based on CRM that explain the core functionalities that are still very relevant except some areas like Change Request and Web Request that are not available in the new S/4HANA 2022 Grantor Management solution:

[Introduction to SAP Grantor Management – Part I | SAP Blogs](https://blogs.sap.com/2013/08/12/introduction-to-sap-grantor-management-part-i/)

[Introduction to SAP Grantor Management – Part II | SAP Blogs](https://blogs.sap.com/2013/08/13/introduction-to-sap-grantor-management-part-ii/)

[Introduction to SAP Grantor Management – Part III | SAP Blogs](https://blogs.sap.com/2013/08/13/introduction-to-sap-grantor-management-part-iii/)

[Introduction to SAP Grantor Management – Part IV | SAP Blogs](https://blogs.sap.com/2013/08/14/introduction-to-sap-grantor-management-part-iv/)

Now the rest of this blog post will cover what the new S/4HANA Grantor Management on-premise solution has to offer; let's start with the main features available in S/4HANA Grantor Management 2022 FPS0:

**Key Features**

* Grantor Programs\*

* Grantor Applications

* Grantor Agreements

* Integration with AP/AR and PSCD

* Integration with Funds Management:

* Budget Control System (BCS)

* Budget Encumbrance (Earmarked Funds)

\*Integration with Business Partners, Attachments, Notes are not ready on the first release - see roadmaps below

**Deployment Scenarios**

There are now three deployment options:

* **Side-by-side**: CRM-system connected via CRM middleware to a S/4HANA system (all releases). The S/4HANA system is only used as ECC system

* **NEW -** **S/4 only**: The E2E Grantor Management processes from Grantor Program, Applications up to invoicing and pay-out run in a single S/4HANA system

* **NEW** **- Hybrid scenario\***: Combination of side-by-side and S/4 only.

\*For some Grantor Programs and the related Applications/Agreements, a separate CRM-system is used while for other Grantor Programs the S/4HANA system is used. Budget reservation and FI-processes all run in the same S/4HANA system, regardless in which system the Grantor Programs / Applications / Agreements are located.

**New features:**

* Enable Contract account (aka Business Agreement in CRM) on the UI for Agreement header and Agreement items

  + In CRM the Business agreement is available only on Header but not for items. If customers want to use different Contract Accounts on items in CRM, the Contract Account must be derived via a BAdI in ERP

* Billing Document Navigation

  + Navigation to PSCD and FI Billing Documents from Transaction History

* Archiving

  + Billing Documents can only be archived if the related Agreement has been archived If a FI-AP/AR document or PSCD document has been archived, an error message is displayed on the UI for the related Agreement. It is not possible to edit the Agreement or Claim apart from setting the status to completed/can be archived. The above features are necessary, since the invoiced amounts of the Agreement are calculated from the related AP&AR / PSCD documents. The invoiced amounts will be wrong if AP&AR / PSCD documents are archived before the Agreement/Claim. Same applies to billing documents

  + ILM\*-rules for Grantor Programs are only applied for the top program of a program hierarchy, e.g. the retention period is calculated for the top program\*ILM-Information Lifecycle Management Archiving

**Major Improvements**

* CRM WebUI powered by Fiori 3

  + Visual harmonization (Belize theme), target mode to embed CRM applications into the Launchpad

* Reduce TCO

  + Simplification of the IT landscape; save hardware costs, operational costs, and time

* No more replication errors

  + No need to wait for replicated errors during the creation of follow-up documents or master data replication

* Synchronous creation of follow-up documents

  + e.g., Funded Program, Earmarked Funds Documents, Billing Documents

* Removal of Master Data Replication (Business Partner, Business Agreement)

  + No more Master Data Replication

* Errors in follow-up documents are visible to the end user as UI error messages

  + No need to look for IDocs/Queues to identify the source of the errors.

* Editing Grantor documents will not be blocked anymore

  + Follow-up documents are not distributed but created instantly

* Re-execution of successor processes can be initiated by the end user

  + If an error occur during the creation of a follow-up document (e.g., earmarked fund, billing), this execution can be triggered from UI once the “issue” has been solved

* Invoices and clearing Information is directly read from FI

  + No more notifications via report are required to inform Grantor Agreements about the creation of invoices or clearings.

**Roadmap**

If you are wondering what is coming on the next releases including S/4HANA FPS1 (February 2023) and S/4HANA 2023 (October 2023)  you can access our roadmap using the following link:

[SAP Road Maps](https://roadmaps.sap.com/welcome) and search for "Grantor Management" as shown on the following screenshot:

![](/le...