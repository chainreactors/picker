---
title: External Workforce and Customer Role in New Employee Business Partner Data Model
url: https://blogs.sap.com/2023/04/07/external-workforce-and-customer-role-in-new-employee-business-partner-data-model/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:15.544465
---

# External Workforce and Customer Role in New Employee Business Partner Data Model

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* External Workforce and Customer Role in New Employ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51355&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [External Workforce and Customer Role in New Employee Business Partner Data Model](/t5/enterprise-resource-planning-blog-posts-by-sap/external-workforce-and-customer-role-in-new-employee-business-partner-data/ba-p/13556997)

![Nicole1](https://avatars.profile.sap.com/f/7/idf7b0e2873294db87d481ea2d0c364260b35f16932a3de0c89541d838f8318281_small.jpeg "Nicole1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Nicole1](https://community.sap.com/t5/user/viewprofilepage/user-id/27750)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51355)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51355)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556997)

‎2023 Apr 07
8:58 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51355/tab/all-users "Click here to see who gave kudos to this post.")

9,463

* SAP Managed Tags
* [SAP S/4HANA business partner](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520business%2520partner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [HCM (Human Capital Management)](https://community.sap.com/t5/c-khhcw49343/HCM%2520%28Human%2520Capital%2520Management%29/pd-p/26220882342286075781792349618930)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [HCM (Human Capital Management)

  Software Product Function](/t5/c-khhcw49343/HCM%2B%252528Human%2BCapital%2BManagement%252529/pd-p/26220882342286075781792349618930)
* [SAP S/4HANA business partner

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bbusiness%2Bpartner/pd-p/e5aee8fa-b65f-4af6-9f57-9d0a05b033bc)

View products (3)

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**Update July 2023:**

**New** Cookbook: [Employee Business Partner Integration as of SAP S/4HANA 2020 with new data model](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_1751%20S4HANA_HRBP_Cookbook_NEW_FINAL.pdf)

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

As an addition to the SAP Blog [New Employee Business Partner Data Model in SAP S/4HANA 2020OP](https://blogs.sap.com/2021/08/16/new-employee-business-partner-data-model-in-sap-s-4hana-2020-on-premise/), let's take a closer look here on the External Workforce and the role **Customer** within the New Employee Business Partner Data Model. Both functionalities require the active Business Function /SHCM/EE\_BP\_1. Furthermore, the focus in this SAP Blog is on SAP S/4HANA on premise and SAP S/4HANA Cloud, private edition.

## External Workforce

In the first part we will focus on the External Workforce and the integration to the corresponding business partner objects. In general, there exist several ways how the External Workforce data can be created and maintained in a SAP system landscape:

![](/legacyfs/online/storage/blog_attachments/2023/03/ExtWF-Creation.png)

Creation of External Workforce for new employee business partner model

Possible scenarios for creation of an external worker from outside a SAP S/4HANA system are shown on the left side of the graphic above with SAP Fieldglass, SAP SuccessFactors, SAP HCM on a separate instance or a 3rd party system. The right side of the graphic shows the local creation scenario with a SAP S/4HANA system running SAP HCM embedded on the same instance.

For our integration scenario with the new employee business partner model, the External Workforce data is stored in the end in the corresponding HCM tables/infotypes of the SAP S/4HANA system and synchronized from there into the Business Partner data model. Usually, an external employee is differentiated in infotype 0001 (Organizational Assignment) with a special Employee Group (field PERSG) from an internal employee. In a standard implementation, Employee Group “9” (External Employee) is used to determine the external employee.
In case the customer business processes differentiate here, SAP provides BAdI /SHCM/B\_EXTERNAL\_EMPLOYEE to distinguish external from internal employees. Method SET\_PERNR\_AS\_EXTERNAL provides the option to override the standard Employee Group and IS\_PERNR\_EXTERNAL determines if a personnel number is an external one.
To support the business processes around the External Workforce, infotype 3435 (Supplier) stores the supplier which is the external worker’s employer. Furthermore, newly introduced infotype 3406 (Service Cost Level) can be used to locally store the service cost level and is enabled for maintenance via transaction PA30.

During the BP synchronization process the role **Service Performer** (BBP005) is added to the BP representing the external employee and a separate Business Partner instance is created with role **External Employment** (BUP011) for each external contract. The external employment BP is linked to the leading BP instance via BUT050/HCM002 (External Employment) association. Therefore, it is handled like the synchronization process of internal employees.
Every external employment instance will reflect the external supplier’s belonging to that contract, associated via a newly introduced BUT050/HCM003 (Service Performer Contract) relationship.
The relationship category Service Performer (BUR025) links the external employee BP to the Business Partner of the external supplier. This ensures the compatibility as every consumer can access the data as before, and new consumers can access the external supplier in an improved way, using the new external employment object.

![](/legacyfs/online/storage/blog_attachments/2023/03/ExtWF_NewDatamodel.png)

External Worker in new employee business partner model

During the employee lifecycle it could be that an external becomes an internal employee and vice versa. Depending on the business processes on the customer side, an existing BP instance with role BUP010 could also be reused to assign role **External Employment**. This is the case if for example, the employee keeps the personnel number over the employee lifecycle.

![](/legacyfs/online/storage/blog_attachments/2023/03/ExtWF_EmployeeLifecycle-4.png)

External Workforce in employee lifecycle

Concluding, with the external worker functionality available as of SAP S/4HANA 2021 FPS0, a Business Partner employment instance can reflect

* Only internal employment with role BUP010

* Only external employment with role BUP011

* Or both, then the instance carries bo...