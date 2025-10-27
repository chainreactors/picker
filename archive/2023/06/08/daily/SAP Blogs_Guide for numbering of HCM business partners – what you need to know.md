---
title: Guide for numbering of HCM business partners – what you need to know
url: https://blogs.sap.com/2023/06/07/guide-for-numbering-of-hcm-business-partners-what-you-need-to-know/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:28.150485
---

# Guide for numbering of HCM business partners – what you need to know

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Guide for numbering of HCM business partners - wha...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50154&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Guide for numbering of HCM business partners - what you need to know](/t5/enterprise-resource-planning-blog-posts-by-sap/guide-for-numbering-of-hcm-business-partners-what-you-need-to-know/ba-p/13548975)

![former_member845991](https://avatars.profile.sap.com/former_member_small.jpeg "former_member845991")

[former\_member845991](https://community.sap.com/t5/user/viewprofilepage/user-id/845991)

Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50154)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50154)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548975)

‎2023 Jun 07
10:51 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50154/tab/all-users "Click here to see who gave kudos to this post.")

12,207

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

# Introduction

There are a lot of possibilities to configure numbering of the business partners and the vendors which are created during the synchronization from HCM. Therefore, there are some pitfalls along the way for wrong adjustment and invalid customizing.  To prevent this, I created this all-in-one guide so that everyone should be able to configure the Number Range needed and solve some common issues.

Please enjoy.

# General

If you synchronize an employee whose personnel number (PERNR) has no corresponding Business Partner (BP) (and vendor) a new Business Partner will be created. Therefore, you have the possibility to configure which number the BP (and Vendor) have. The central table to configure this, is the **System table T77S0** which can be maintained via transaction SM30. The Corresponding switches are all part of the **group HRALX**.

The **Switch PNUMB** allows you to configure the mode by which the number of the BP with role Employee (BUP003) is determined. **PSUBG** determines the Business Partner Group which is used for the creation process of Business Partner with role Employee (BUP003).

The **Switches ENUMB** and **ESUBG** behave like PNUMB and PSUBG but allow the configuration of the numbering for the Business Partner with role Employment (BUP010). Or in VMODE 1/VMODE2 the numbering of the BP with (only) the Vendor role. Since this role is only available in the new data model for employee business partners (Business Function /SHCM/SFWS\_SC\_EE\_BP\_01) it is not relevant if you still use one of the old models (VMODE1/VMODE2).

In addition to these 4 switches in table T77S0 there are also configurations which need to be done in transaction SPRO. In this blog, I will list them according to their functionality. A cheat sheet where the customizing functions can be found in the IMG hierarchy can be found later in this document.

First, we have the customizing function that allows you to define BP number ranges which can be assigned to the BP grouping. Further named as **Customizing Function BP Number Range**. The possibilities you have for the Number Ranges depend on the mode you selected via Switch **HRALX PNUMB** (ENUMB) and will be further described in the mode section of this document. In general, it is recommended that the number ranges start with XX00000000 and ending with XX99999999. The X can be any letter or number you like. For example, DE00000000 – DE99999999 or 0100000000 - 0999999999. A negative example which is possible in some modes, but highly not recommended, is 0000000010-A1000099999 or AABBCC003399-ZZZZZZZZZZ.

The second customizing function allows you to define and assign BP groupings. Further named as **Customizing Function BP Grouping**. Here you can create a grouping for the Business Partner and assign a Business Partner Number Range to the grouping. It is recommended that every group has its own number range. If you use a grouping for number range assignment it must have the same name as the number range assigned. So, you can in fact only do groupings with 2-character signs length. By default, you need to configure only one grouping for the Business Partner with role Employee (BUP003) which matches the configuration in switch HRALX PSUBG. If you use the new model, a second group should be created for the Business Partner in role Employment (BUP010) which matches your entry in Switch HRALX ESUBG. By default, these two groupings should be enough for a successful system configuration, but in some advanced cases you may want to further classify Employee and Employment Business Partner in multiple groupings at your own responsibility. Therefore, you can create for example a further grouping especially for Employee BP with home address in Germany. If you want to use these additional groupings, you must implement a BAdI implementation for **BADI\_FITV\_VENDOR\_SYNC->MODIFY\_COMPLETE\_DATA** or **/SHCM/B\_EE\_BP\_SYNC->MODIFY\_GROUPING\_NUMBER** if you are on release 2022 or further. In this BAdI implementation you can overwrite the grouping used for the creation according to your needs. Please be aware that the grouping of a BP could not be changed once the BP is created. So, be careful.

During the first synchronization of a PERNR to a Business Partner, not only the Business Partner is created. According to your customizing also a Vendor (Supplier) will be created. It is also possible to configure the numbering of newly created vendors. Therefore, you can define number ranges for vendor via the **Customizing Function Vendor Number Range.** These Number Ranges need to be assigned to a Vendor Grouping via **Customizing Function Vendor Grouping**.

At last, you need to assign the Vendor Grouping to a Business Partner grouping via **Customizing Function Mapping BP to Vendor.** For example, if a business Partner of grouping AA is created the vendor Group BBBB is used for creating the according vendor.

In general, there are two possibilities how the vendor number can be determined. If you use an internal number range for the vendor number range, the next free number of this range will be used for the vendor. It is recommended that the v...