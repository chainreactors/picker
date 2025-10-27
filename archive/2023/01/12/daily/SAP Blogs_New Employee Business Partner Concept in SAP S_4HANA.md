---
title: New Employee Business Partner Concept in SAP S/4HANA
url: https://blogs.sap.com/2023/01/11/new-employee-business-partner-concept-in-sap-s-4hana/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:22.063914
---

# New Employee Business Partner Concept in SAP S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* New Employee Business Partner Concept in SAP S/4HA...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53015&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [New Employee Business Partner Concept in SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-sap/new-employee-business-partner-concept-in-sap-s-4hana/ba-p/13567357)

![amitdhar](https://avatars.profile.sap.com/b/e/idbe6ff344b43715f4a45968201c481da5883c828497c75fef975e04f0c2ef994a_small.jpeg "amitdhar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[amitdhar](https://community.sap.com/t5/user/viewprofilepage/user-id/6846)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53015)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53015)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567357)

‎2023 Jan 11
8:38 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53015/tab/all-users "Click here to see who gave kudos to this post.")

29,072

* SAP Managed Tags
* [SAP S/4HANA business partner](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520business%2520partner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)
* [SAP S/4HANA Cloud for enterprise portfolio and project management](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520for%2520enterprise%2520portfolio%2520and%2520project%2520management/pd-p/50d750e2-9a5f-462e-8001-ac7ff1800174)
* [SAP Portfolio and Project Management for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Portfolio%2520and%2520Project%2520Management%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000245)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [HCM Processes and Forms](https://community.sap.com/t5/c-khhcw49343/HCM%2520Processes%2520and%2520Forms/pd-p/728841321694667382679749409993833)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud for enterprise portfolio and project management

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2Bfor%2Benterprise%2Bportfolio%2Band%2Bproject%2Bmanagement/pd-p/50d750e2-9a5f-462e-8001-ac7ff1800174)
* [HCM Processes and Forms

  Software Product Function](/t5/c-khhcw49343/HCM%2BProcesses%2Band%2BForms/pd-p/728841321694667382679749409993833)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Portfolio and Project Management for SAP S/4HANA

  SAP Portfolio and Project Management](/t5/c-khhcw49343/SAP%2BPortfolio%2Band%2BProject%2BManagement%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000245)
* [SAP S/4HANA business partner

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bbusiness%2Bpartner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)

View products (6)

**Introduction**

In this blog you will get an overview and understand concept of “New Employee Business Partner Model in SAP S/4HANA”

**Overview**

* The Employee business partner is mandatory in SAP S/4HANA.

* Customers, vendors, employees, and so on are represented as roles within the business partner..

* The new employee business partner data model was introduced as of release SAP S/4HANA 2020 and an external worker i.e. vendors, customers can be represented in the new data model as of release SAP S/4HANA 2021.

* The business user is linked to the Employee business partner.

* Employees are maintained as business partners in SAP S/4HANA for non-HCM processes and employee records from SAP HCM or other HR solutions are synchronized to business partners in SAP S/4HANA.

**Characteristics of the new Employee Business Partner Model**

* One business partner per natural person with role Employee is created.

* Separate business partners are created for every employment, unlike in the old model.

* Employment BP can have vendor or other roles assigned based on business requirement.

* One-to-one relation exists between employment (personnel number) and business partner with role Employment.

**Why a New Data Model?**

* Missing relationship between business partner in role Employee and business partner in role Vendor.

* Missing ability to properly reflect concurrent and global employment of business partners in role Employee.

* Missing flexibility regarding business partner handling in role Employee and thus missing data accuracy.

* Missing functionality to specify a main personnel number for business partners in role Employee.

**Availability of new data model**

* New employee business partner data model is available as of SAP S/4HANA 2020 FPS00 OP.

* Down port is possible for 1809 SP06 and 1909 SP04 and higher releases (SAP Note 2954033).

* Business function /SHCM/EE\_BP\_1 has to be switched on for the new data model to be active.

* This business function is not switched on by default in the SAP S/4HANA system.

* Activation of this business function is irreversible.

* Move to the new business partner data model is recommended as future developments in this area will be considered only in the new model

**Challenges in current Data Model**

* Employee role cannot be updated with a different contract.

* No proper reflection of employment.

* Private address data, bank details, and workplace related information cannot be updated properly Flexibility to change user assignment missing for customers coming from ERP.

* Existing data model cannot adequately handle concurrent or multiple employments

**New Employee Business Partner Data Model**

* Employment role is introduced in the new data model.

* One-to-one relation exists between employment (personnel number) and BP with role Employment.

* BP instance with role Employment has direct relationship to BP with role Employee.

* New data model is more flexible.

* Possible to ensure the lifecycle of an employee even after contract/employment changes.

**Path to New Employee Business Partner Model**

Below are the list of  4 starting points to move to new employee business partner model. For each starting point, the transition path is explained with details.

![](/legacyfs/online/storage/blog_attachments/2023/01/Path-to-the-new-employee-Business-partner-model.jpg)

**ERP HCM integration NOT active**

![](/legacyfs/online/storage/blog_attachments/2023/01/ERP-HCM-Integration-not-Active.jpg)

**ERP HCM integration is active**

![](/legacyfs/online/storage/blog_attachments/2023/01/ERP-HCM-Integration-is-Active.jpg)

**SAP S/4HANA greenfield**

![](/legacyfs/online/storage/blog_attachments/2023/01/SAP-S4HANA-Greenfield.jpg)

**SAP S/4HANA upgrade from below 2020**

![](/lega...