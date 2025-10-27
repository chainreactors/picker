---
title: SAP Central Finance – Mapping enablers – Part 2 of 2 – Enable Transports for Value Mapping
url: https://blogs.sap.com/2023/07/16/sap-central-finance-mapping-enablers-part-2-of-2-enable-transports-for-value-mapping/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:37.926409
---

# SAP Central Finance – Mapping enablers – Part 2 of 2 – Enable Transports for Value Mapping

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP Central Finance - Mapping enablers - Part 2 of...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67834&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Central Finance - Mapping enablers - Part 2 of 2 - Enable Transports for Value Mapping](/t5/enterprise-resource-planning-blog-posts-by-members/sap-central-finance-mapping-enablers-part-2-of-2-enable-transports-for/ba-p/13559881)

![Subhrangsu](https://avatars.profile.sap.com/3/c/id3c1d9ec8dfeca278d14331de7a2b29ac6d3a8cc8a6d64573ea927409362c4826_small.jpeg "Subhrangsu")

[Subhrangsu](https://community.sap.com/t5/user/viewprofilepage/user-id/156458)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67834)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67834)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559881)

‎2023 Jul 16
7:23 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67834/tab/all-users "Click here to see who gave kudos to this post.")

3,578

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)

View products (2)

# Introduction

This is the second of the two-part blog series where we discuss some of the key enablers of Mapping in Central Finance. In the [first blog](https://blogs.sap.com/2023/07/15/sap-central-finance-mapping-enablers-part-1-of-2-enable-audit-log-for-key-mapping/), we discussed configuration steps to enable change logs for Key Mappings. In this blog, we turn our attention to Value Mappings.

Yet again, we will dive straight into the technical details of the mapping enablers. As mentioned in my previous [blog](https://blogs.sap.com/2023/07/15/sap-central-finance-mapping-enablers-part-1-of-2-enable-audit-log-for-key-mapping/), for introduction to the concepts of Central Finance, in general, and mapping, in particular, there is a significant amount of information on this site, but I can recommend the following two blogs for familiarising yourselves with the concepts.

* [Central Finance Overview](https://blogs.sap.com/2019/11/29/central-finance-an-overview/) from vinay.dhamnani

* [Introduction to Mapping](https://blogs.sap.com/2020/03/11/sap-central-finance-cfin-introduction-part-2-mapping/) from zhengzhang.lu

In this two-part blog series, we will explore the following in detail. If you have read my first blog of this series, you may find some of the information here repetitive. It was done consciously so that both of these blogs can be read independently dependent on the challenge the reader may want to solve.

* **Part 1 - Key Mapping - Enable Audit Log for Key Mapping**

* **Part 2 - Value Mapping - Enable Transports for Value Mapping**

# Details

**Part 2 – Value Mapping - Enable Transports for Value Mapping**

Value Mappings are maintained in the Central Finance system primarily for Enterprise Structure (Company Codes, Controlling Area etc.) or Reference Data (Payment Terms, Payment Methods, Document Types etc.). Key Mappings, on the other hand, are mostly maintained for Master Data objects (Customers, Vendors, G/L Accounts, Materials etc.).

Value Mappings are mostly configured in the Development system and transported through the landscape into Production. It makes sense as the target mapping objects (such as Company Codes, Payment Terms etc.) are also configured in the Development system, and captured in transports before they move to Test or Production. Master Data is usually created directly in the Production system and does not necessarily need any transports from Development. Hence mapping between source Master Data and CFIN equivalents is maintained directly in Production via Key Mappings.

***Methods to Configure Value Mapping***

Value Mapping can be configured in a few different ways. One option is to use the "Maintain Value Mapping" configuration node via Transaction **CFINIMG**. However, a more user-friendly option, in my personal opinion, is to use Transaction **FINS\_CFIN\_MAP\_MANAGE.** This transaction allows the users to download a CSV template, populate it with the source and target values, and upload them to the Central Finance system. Please note, loading value mapping via FINS\_CFIN\_MAP\_MANAGE has some limitations, for example, when mapping entities have contexts and they differ in source and Central Finance, this method will not work. However, in scenarios where it works, I find it the more user-friendly and swift way.

In the following figure, I have taken the liberty of showcasing, with a dash of artistic charm, the user experience for configuring Value Mapping via Transactions CFINIMG and FINS\_CFIN\_MAP\_MANAGE. Both have their perks and limitations.

![](/legacyfs/online/storage/blog_attachments/2023/07/CFINIMG-vs-FINS_CFIN_MAP_MANAGE.jpg)

CFINIMG vs FINS\_CFIN\_MAP\_MANAGE

On a vanilla Central Finance system, the configuration of Value Mapping does not come transport enabled. For example, in Transaction **FINS\_CFIN\_MAP\_MANAGE**if you select any Value Mapping entity, choose the "Upload Mapping" radio button, enter a file name and remove the "Test Run" option, by default, you will not find any placeholder for adding a Customizing Transport Request (please refer to the image below). This blog provides a quick overview of the changes required in your Development environment (configuration client) to enable the transportability of value mappings.

![](/legacyfs/online/storage/blog_attachments/2023/07/FINS_CFIN_MAP_MANAGE-No-Transport.jpg)

FINS\_CFIN\_MAP\_MANAGE Screen without a Transport Prompt

# Configuration Steps

Changes are required in configuration settings for 3 Maintenance Views and 1 View Cluster as follows:

1. Maintenance View: ***MDGV\_VM\_CODELIST**(Assign Code Lists to Elements and Systems)*

2. Maintenance View: ***MDGV\_CCODEMAP** (Define Code-Mapping (Client-Dependent))*

3. Maintenance View: ***MDGV\_CMAPCONTEXT** (Assign Code Lists (Client-Dependent))*

4. View Cluster: ***MDGVC\_CMAPPING**(Configure Code Lists and Value Mapping (client depend.))*

Please note, the changes recommended in this blog are only required in your Development environment and configuration client. You wouldn't want to create Customising Requests in your non-Golden clients.

**Step 1: *Change the "Current Settings" Configuration for Maintenance Objects***

**Step 1.1**: Launch Transaction Code **SOBJ** (Maintenance Object Attributes)

Launch Transaction Cod SOBJ. On the next screen, click on "Edit"

![](/legacyfs/online/storage/blog_attachments/2023/07/SOBJ.jpg)

Transaction SOBJ

**Step 1.2**: Navigate to "Current Settings"

Repeat this step 4 different...