---
title: SAP Central Finance – Mapping enablers – Part 1 of 2 – Enable Audit Log for Key Mapping
url: https://blogs.sap.com/2023/07/15/sap-central-finance-mapping-enablers-part-1-of-2-enable-audit-log-for-key-mapping/
source: SAP Blogs
date: 2023-07-16
fetch_date: 2025-10-04T11:52:24.598507
---

# SAP Central Finance – Mapping enablers – Part 1 of 2 – Enable Audit Log for Key Mapping

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP Central Finance - Mapping enablers - Part 1 of...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67833&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Central Finance - Mapping enablers - Part 1 of 2 - Enable Audit Log for Key Mapping](/t5/enterprise-resource-planning-blog-posts-by-members/sap-central-finance-mapping-enablers-part-1-of-2-enable-audit-log-for-key/ba-p/13559868)

![Subhrangsu](https://avatars.profile.sap.com/3/c/id3c1d9ec8dfeca278d14331de7a2b29ac6d3a8cc8a6d64573ea927409362c4826_small.jpeg "Subhrangsu")

[Subhrangsu](https://community.sap.com/t5/user/viewprofilepage/user-id/156458)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67833)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67833)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559868)

‎2023 Jul 15
2:07 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67833/tab/all-users "Click here to see who gave kudos to this post.")

3,969

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)

View products (2)

# Introduction

In this two-part blog series, we dive straight into the technical details of the Central Finance Mapping enablers. As avid followers of this transformative solution, we assume that you are already well-versed in the capabilities and benefits of SAP Central Finance. If you are new to the subject and need an introduction to the wonders of Central Finance, there is a plethora of information on this website, but I can recommend [this blog post](https://blogs.sap.com/2019/11/29/central-finance-an-overview/) from vinay.dhamnani for a comprehensive overview.

In SAP Central Finance, mapping emerges as a critical component, playing a pivotal role in the seamless conversion of data from source systems to the unified landscape of CFIN.  As organisations embark on their CFIN journey, mapping takes centre stage, ensuring the accurate translation of financial information and the preservation of data integrity. zhengzhang.lu has written a detailed blog on SAP Central Finance Mapping which you can read [here](https://blogs.sap.com/2020/03/11/sap-central-finance-cfin-introduction-part-2-mapping/). I will start this blog series from where he concludes.

In this two-part blog series, we will explore the following in detail.

* **Part 1 - Key Mapping - Enable Audit Log for Key Mapping**

* **Part 2 - Value Mapping - Enable Transports for Value Mapping**

# Details

**Part 1 - Key Mapping - Enable Audit Log for Key Mapping**

Value Mappings are maintained in the Central Finance system primarily for Enterprise Structure (Company Codes, Controlling Area etc.) or Reference Data (Payment Terms, Payment Methods, Document Types etc.). Key Mappings, on the other hand, are mostly maintained for Master Data objects (Customers, Vendors, G/L Accounts, Materials etc.).

Value Mappings are mostly configured in the Development system and transported through the landscape into Production. It makes sense as the target mapping objects (such as Company Codes, Payment Terms etc.) are also configured in the Development system, and captured in transports before they move to Test or Production. Master Data is usually created directly in the Production system and does not necessarily need any transports from Development. Hence mapping between source Master Data and CFIN equivalents is maintained directly in Production via Key Mappings.

Since Key Mappings are not transported, the only possibility of tracking changes, deletions or additions is via change logs. However, change logs are not active for Key Mappings by default. This blog describes the various configuration steps required to enable Audit Log or Change Log for Key Mapping.

# Configuration Steps

Change Logs are activated at a “**Mapping Context**” level and not at the level of individual Key Mapping IDs. Transaction Code **FINS\_CFIN\_MAP\_MANAGE**is usually used as the central point to display, upload, download or delete mapping in Central Finance. But the Mapping entity displayed here is the Key Mapping ID, for example, CUSTOMER\_ID for Customer Numbers in the screenshot below. Hence, as a starting point, it is important to identify the Mapping Contexts corresponding to the relevant Key Mapping IDs. For example, the change log for Customer Numbers is activated at the Mapping Context or Main Context 'BusinessPartner' level.

![](/legacyfs/online/storage/blog_attachments/2023/07/FINS_CFIN_MAP_MANAGE.jpg)

Mapping Entity to Main Context

In this section, we will first explore the steps of identifying the Main Context corresponding to the Key Mapping ID (Steps 1 and 2) before we discuss how to activate the Change Logs for those objects (Steps 3 and 4).

![](/legacyfs/online/storage/blog_attachments/2023/07/Blog-Pic-1.jpg)

Identification of Mapping Contexts

**Step 1:** Identify **Business Object Type** for relevant Key Mapping IDs.

**SPRO Path**: *Cross-Application Components >**Processes and Tools for Enterprise Applications* *> Master Data Governance >**Central Governance >* *Key Mapping >* *Enhance Key Mapping Content >**Define Business Object Identifiers*

![](/legacyfs/online/storage/blog_attachments/2023/07/Blog-Pic-2-Step-1-1.jpg)

Identify Business Object Type

**Step 2:** Identify the **Main Contexts** to which relevant **Business Object Types** are assigned

SPRO Path: *Cross-Application Components >* *Processes and Tools for Enterprise Applications >* *Master Data Governance >* *Central Governance >* *Key Mapping >* *Enhance Key Mapping Content >**Assign Business Objects to Main Contexts*

Please Note: More than one Key Mapping ID or Business Object Type can be associated with one Main Context. In that case, when we activate the Change Log, it will activate it for all associated Key Mapping IDs.

![](/legacyfs/online/storage/blog_attachments/2023/07/Blog-Pic-3-Step-2-1.jpg)

Identify Main Contexts

**Step 3:** Define **Mapping Contexts** for UKMS or ensure they exist for relevant **Business Object Types**

SPRO Path: *Cross-Application Components >* *Processes and Tools for Enterprise Applications >* *Master Data Governance >* *Central Governance >* *Key Mapping >* *Define a Mapping Context for UKMS >**Define Mapping Contexts*

Please Note: Usually these should exist in the system by default

![](/legacyfs/online/storage/blog_attachments/2023/07/Blog-Pic-4-Step-3.jpg)

Define Mapping Contexts

**Step 4:** Activate **Change Logs** for **Mapping Contexts** corresponding to relevant **Business Object Types**

SPRO Path: *Cross-Application Components ...