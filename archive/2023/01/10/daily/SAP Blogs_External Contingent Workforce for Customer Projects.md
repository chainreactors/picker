---
title: External Contingent Workforce for Customer Projects
url: https://blogs.sap.com/2023/01/09/external-contingent-workforce-for-customer-projects/
source: SAP Blogs
date: 2023-01-10
fetch_date: 2025-10-04T03:24:39.813371
---

# External Contingent Workforce for Customer Projects

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* External Contingent Workforce for Customer Project...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52815&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [External Contingent Workforce for Customer Projects](/t5/enterprise-resource-planning-blog-posts-by-sap/external-contingent-workforce-for-customer-projects/ba-p/13565914)

![A__Hammerschmid](https://avatars.profile.sap.com/0/e/id0e75089db40db7fb2bfbdae07478e6b3530864df068954ff1e240015122042ed_small.jpeg "A__Hammerschmid")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[A\_\_Hammerschmid](https://community.sap.com/t5/user/viewprofilepage/user-id/131642)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52815)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52815)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565914)

‎2023 Jan 09
9:35 PM

[24
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52815/tab/all-users "Click here to see who gave kudos to this post.")

7,926

* SAP Managed Tags
* [Professional Services](https://community.sap.com/t5/c-khhcw49343/Professional%2520Services/pd-p/14945408660319805935548)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [Professional Services

  Industry](/t5/c-khhcw49343/Professional%2BServices/pd-p/14945408660319805935548)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

*Relevant for SAP S/4HANA Cloud 2208, public edition.*
*Co-authored by [Stefan Walz](https://www.linkedin.com/in/stefan-walz-430222a3/) and [Andreas Hammerschmidt](https://www.linkedin.com/in/andreas-h-17b08190).*

**Introduction**
External workers play an important role in service centric industries as companies have an increased demand on different talents beyond their traditional internal workforce. SAP S/4HANA Cloud, public edition, offers two ways to procure these external contingent workers for customer projects in the Professional Services scenario. An external worker can be either procured directly on a project or pool-based on a cost center. Both scenarios come with its advantages and disadvantages, which will be elaborated in this blog post in addition to a generic introduction and explanation.
The terms external workforce, contingent worker, subcontractor, and service performer are used synonymously.

**Creation of external workforce**
External workforce can be handled in multiple ways along the Recruit to Retire scenario. To give an example, they can be procured via SAP Fieldglass and [fully integrated](https://help.sap.com/doc/7c3e5e11b132497c8d0fb12caa2d1a58/cloud/en-US/ExternalWorkforceforIntelligentEnterpriseImplementationGuide.pdf) with SAP SuccessFactors Employee Central and SAP S/4HANA Cloud. Alternatively, external workers can also be created through the [Manage Workforce](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0bebd08dffca45afa67b1f751199afd0/bcbc2126696f422f844d5c631ff9cc03.html?&q=manage%20workforce&locale=en-US) or [Import Employees](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0bebd08dffca45afa67b1f751199afd0/1b32df57f8c2073ee10000000a4450e5.html?&q=manage%20workforce&locale=en-US) app, or replicated through an [API](https://help.sap.com/docs/SAP_S4HANA_CLOUD/2de44e75f40842ca93e4b9195b1e5234/781d2571f95749df958d22228d1212bc.html?&q=manage%20workforce&locale=en-US) from an external HR system to SAP S/4HANA Cloud.
Independent of the above possibilities, the following facts are the most important prerequisites to use external workers in the project-based services scenario:

+ The external worker is created as business user and business partner
+ The worker type of the workforce is BBP005 (contingent worker)
+ The external worker needs to be maintained as contingent worker of a domestic supplier
+ A cost center needs to be maintained for the subcontractor if s/he is procured on cost center

*Figure 1: Contingent worker factsheet*

**Overview of end-to-end process**

![Figure 2_jpeg.jpg](/t5/image/serverpage/image-id/150548i9195E3A92A2F50CD/image-size/large?v=v2&px=999 "Figure 2_jpeg.jpg")

*Figure 2: End-to-end object flow for subcontractors*

The contingent worker process starts with a released customer project that is in stage “In Execution” and a fully approved Purchase Order. For each time record of the external consultant, the system automatically creates one service entry sheet and one goods receipt. These documents are always created – independent of the account assignment of the Purchase Order item. Additionally, depending on this account assignment, there is an additional activity allocation posting to the Universal Journal (ACDOCA) through a direct interface from the cross-application timesheet, when the procurement is done on cost center.

The main advantage of this direct creation of the service entry sheet and goods receipt with the time recording is to allow the direct update and deletion of time recordings without the necessity to revoke and delete the service entry sheet manually before. See also deprecated note [2461101](https://launchpad.support.sap.com/#/notes/2461101).

When the automatic creation of a service entry sheet fails, an error log will be written. This log can be checked with the app “Monitor Service Entry Sheets Generation Log”.

![Figure 3.png](/t5/image/serverpage/image-id/150526i1B05C699EF4D345E/image-size/large?v=v2&px=999 "Figure 3.png")

*Figure 3: Application log for automatic service entry sheet generation*

The give an example below, the work package was blocked for financial postings from procurement by using the blocked function “Other Expense Posting”.

![Figure 4.png](/t5/image/serverpage/image-id/150527iC46DE94B4FB626A0/image-size/large?v=v2&px=999 "Figure 4.png")

*Figure 4: Example of detailed log entry if automatic service entry sheet generation fails*

After solving the issue, the automatic service entry sheet creation can be re-triggered with the app “Schedule Purchasing Jobs” (Advanced) using the job template “Automatic Creation of Service Entry Sheets from Time Recording”. The same can be also used for time recordings in previous periods, in which goods receipts cannot be posted anymore. Here, the field “Posting Date for Goods Receipt” allows the goods receipts to be created with a posting date, on which procurement processes are still allowed. The field Service Rendered Date is always updated in ACDOCA for these goods receipts, meaning that in the Journal Entry item and in the subsequent billing processes, there is the information available on which date the services were provided.

**Purchase Requisition and Purchase Order**
Depending on the business needs and processes within the company, purchase requisitions can ...