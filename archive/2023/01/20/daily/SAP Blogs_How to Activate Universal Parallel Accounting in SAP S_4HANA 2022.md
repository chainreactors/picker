---
title: How to Activate Universal Parallel Accounting in SAP S/4HANA 2022
url: https://blogs.sap.com/2023/01/19/how-to-activate-universal-parallel-accounting-in-sap-s-4hana-2022/
source: SAP Blogs
date: 2023-01-20
fetch_date: 2025-10-04T04:22:53.539321
---

# How to Activate Universal Parallel Accounting in SAP S/4HANA 2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to Activate Universal Parallel Accounting in S...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68122&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Activate Universal Parallel Accounting in SAP S/4HANA 2022](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-activate-universal-parallel-accounting-in-sap-s-4hana-2022/ba-p/13563825)

![ProfessorDLR](https://avatars.profile.sap.com/f/8/idf89ddb65375e0da0768dec1900a471296d0ee35fe2a1da59f54c0068a6ae123a_small.jpeg "ProfessorDLR")

[ProfessorDLR](https://community.sap.com/t5/user/viewprofilepage/user-id/834939)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68122)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68122)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563825)

‎2023 Jan 19
8:10 PM

[13
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68122/tab/all-users "Click here to see who gave kudos to this post.")

28,477

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

View products (4)

Universal parallel accounting is a powerful feature in SAP S/4HANA 2022  that allows companies to maintain multiple accounting representations or views in parallel, each with its own specific chart of accounts, currency, and legal requirements.

This feature can be used to support various business scenarios, such as consolidation, intercompany transactions, statutory reporting, and management reporting, among others. With universal parallel accounting, companies can efficiently manage their financial data and comply with different accounting standards and regulations, while leveraging the benefits of SAP's integrated system.

In this blog we will explore how to activate the business function Universal Parallel Accounting (FINS\_PARALLEL\_ACCOUNTING\_BF) in SAP S/4HANA 2022 along with UPA fiori tiles

### 1. Prerequisites & Pre Checks:

The FINS\_PARALLEL\_ACCOUNTING\_BF business function can only be activated in a system that has no existing material or asset master data and no transactional data and that meets certain Customizing requirements to ensure data consistency.

This business function is valid for the entire system, but it must be activated only once in one client. It is important to run all checks in all clients of the system landscape to ensure that there is no transactional data and all prerequisites are met. This includes all systems that are connected to the system where the business function is being activated through transports.

**Before activating the FINS\_PARALLEL\_ACCOUNTING\_BF business function, the following steps must be completed for every client in the system environment:**

* Build the latest SAP S/4HANA 2022 version you can get a trial version from SAP CAL

* Take the Backup of the system you have

* Verify that the material ledger is not active for any plant in the system.

* Ensure that there is no transactional data, cost rates, settlement-relevant account assignment objects, or asset master data present.

  + Note: If there is existing data in a test system, it can be reset using program Reset Transaction Data (SAPF020, transaction OBR1).

* Run the transaction Check Ledger Customizing for UPA (FINS\_CUST\_CONS\_C\_UPA) to ensure that the central prerequisites for activating Universal Parallel Accounting (FINS\_PARALLEL\_ACCOUNTING\_BF) are met, such as the use of only single-valuation ledgers.

### 2. Activation:

* Go to transaction ***SFW5*** --> ENTERPRISE\_BUSINESS\_FUNCTIONS

![](/legacyfs/online/storage/blog_attachments/2023/01/1-14.jpg)

sfw5

* Select (***Check*** ) the FINS\_PARALLEL\_ACCOUNTING\_BF and Click on Activate Changes

![](/legacyfs/online/storage/blog_attachments/2023/01/2-15.jpg)

* Please ensure that the Job **SFW\_ACTIVATE\_SF0X** is finished in **SM37**

![](/legacyfs/online/storage/blog_attachments/2023/01/2.1.jpg)

* Once UPA activation is done in Green field implementation you can proceed to implement other business functions related to Finance,Logistics & MDG.

### 3. Post Activation Steps:

* Go to Transaction SFW5 and check the status of FINS\_PARALLEL\_ACCOUNTING\_BF which should be "***Business func. will remain activated***"

![](/legacyfs/online/storage/blog_attachments/2023/01/3-10.jpg)

* Assign the FIORI Business Roles to the user. You can refer [SAP Fiori Apps Library](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/)

* I have assigned the below roles for my test user

FUCN\_ACCOUNTANT
SAPOS\_SD\_LORD\_ODATA\_ORDER
SAPOS\_SD\_SOFM\_INVOICE
SAP\_BCV\_USER
SAP\_BC\_SEFS\_ADMIN
SAP\_BC\_SES\_ADMIN
SAP\_BPR\_PPM
SAP\_BR\_ANALYTICS\_SPECIALIST
SAP\_BR\_AP\_MANAGER\_US
SAP\_BR\_BPC\_EXPERT
SAP\_BR\_BUPA\_MASTER\_SPECIALIST
SAP\_BR\_CASH\_SPECIALIST
SAP\_BR\_DIVISION\_ACCOUNTANT
SAP\_BR\_INVENTORY\_ACCOUNTANT
SAP\_BR\_OVERHEAD\_ACCOUNTANT
SAP\_BR\_PRODN\_ACCOUNTANT
SAP\_BR\_PROJ\_FIN\_CONTROLLER
SAP\_BR\_PROJ\_LOG\_CONTROLLER
SAP\_BR\_PURCHASER
SAP\_BR\_REV\_ACCOUNTANT
SAP\_BR\_SALES\_ACCOUNTANT
SAP\_CO\_OM\_PEREND\_ABM\_COLL
SAP\_CPR\_BCV\_USER
SAP\_CPR\_USER
SAP\_ESH\_CR\_ADMIN
SAP\_ESH\_CUST\_QUERY\_LOG
SAP\_ESH\_DISPLAY\_QUERY\_LOG
SAP\_ESH\_LOCAL\_ADMIN
SAP\_ESH\_REORG\_QUERY\_LOG
SAP\_ESH\_SEARCH\_CATEG
SAP\_ESH\_SEARCH\_CDS
SAP\_ESH\_SEARCH\_USER
SAP\_ESH\_TRANSPORT
SAP\_FLP\_ADMIN
SAP\_FLP\_USER
SAP\_FND\_TCR\_T
SAP\_MDGA\_MENU
SAP\_MDG\_ADMIN
SAP\_RPM\_BCV\_USER
SAP\_SFIN\_ACC\_CLOSING
SAP\_XRPM\_USER

* Now Login to Fiori Using the FIORI  URL <https://<<hostname>>:<<https> port>>/sap/bc/ui5\_ui5/ui2/ushell/shells/%20abap/FioriLaunchpad.html

* Go to App finder

![](/legacyfs/online/storage/blog_attachments/2023/01/4-12.jpg)

* Now You can see the UPA tiles On and working

![](/legacyfs/online/storage/blog_attachments/2023/01/4.1-scaled.jpg)

### 4. Issues & Fixes

**Error1:** Currency type for controlling  not allowed for ledger FINS\_PARALLEL\_ACCOUNTING\_BF

![](/legacyfs/online/storage/blog_attachments/2023...