---
title: SAP Enhancement & Modification Basics – Must read for Functional Consultant
url: https://blogs.sap.com/2022/11/13/sap-enhancement-modification-basics-must-for-read-functional-consultant/
source: SAP Blogs
date: 2022-11-14
fetch_date: 2025-10-03T22:40:49.456456
---

# SAP Enhancement & Modification Basics – Must read for Functional Consultant

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP Enhancement & Modification Basics - Must read ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68506&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Enhancement & Modification Basics - Must read for Functional Consultant](/t5/enterprise-resource-planning-blog-posts-by-members/sap-enhancement-modification-basics-must-read-for-functional-consultant/ba-p/13569818)

![former_member225722](https://avatars.profile.sap.com/former_member_small.jpeg "former_member225722")

[former\_member225722](https://community.sap.com/t5/user/viewprofilepage/user-id/225722)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68506)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68506)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569818)

‎2022 Nov 13
4:42 PM

[24
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68506/tab/all-users "Click here to see who gave kudos to this post.")

72,433

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)
* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)
* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)

View products (7)

## **Introduction**

This document will help functional consultant to understand the difference between enhancement and modification. What kind of enhancement are available and how to search the one based on requirement.

## Purpose

There are many businesses requirement which are not possible in SAP standard and we need to do enhancement or modification with the help of technical team. This document will help functional consultant to understand the available type of enhancement and how can he/she search those as per business requirement.

## Scope

We will cover different types of available enhancement and how to use it.

## **Enhancement**

SAP object is the object that is delivered or created by SAP.  Customer object is the object that is created by a customer.

Enhancement is a way to add or change the SAP object functionality without modifying the SAP object.

Below are the types of enhancement available in SAP -

1. Data dictionary enhancement

2. Customer Exit

3. BTE

4. BADI

**Data dictionary enhancement**

We can enhance SAP standard table or structure by using two ways,

1. Append structure

2. Customising include

Append structure and customising include allow us to enhance SAP standard tables or structures by adding fields to them.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-at-9.56.51-PM.png)

We can enhance table or structure by using customising include only if the table or a structure has customising include Statement.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-at-9.57.07-PM.png)

**Use – If there is a requirement to save some additional fields.**

**Customer Exit**

Customer exit is one type of SAP enhancement. With customer exit we can enhance the SAP standard program without modifying SAP Object.

There are three type of customer exit -

1. Functional Exit

2. Menu Exit

3. Screen Exit

We can see the list of customer exit by transaction code SMOD.

1. Debuting the program and create a breakpoint for command call customer function.

2. Search in program “call customer-function”.

3. Use transaction SMOD

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-at-9.57.26-PM.png)

**Use- If there is a requirement to apply some validation on field, want to substitute values during the posting or need some additional screen during any transaction etc.**

**Business transaction event (BTE)**

BTE is a type of enhancement which is basically developed for FI module. BTE is based upon function module, but it is different from customer exit.

In customer exit only SAP and Customer is involved unlike BTE where partner is also involved other than SAP and customer. So not only customer can modify the SAP program, but other partner firm can also modify the standard logic in BTE.

There are 2 types of BTE interface

1. Process Interface - Can influence the SAP standard object

2. Publish and subscribe interface - Cannot influence the SAP Standard object.

Enter T-code – FIBF , you can find both type of BTE.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-at-9.57.51-PM.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-13-at-9.58.05-PM.png)

**Use- Can be used in FI reports, payment advise, dunning, validation, and substitution.**

**Business Add-in (BADI)**

When SAP developers were creating SAP standard program, they found that customer may need different logic in the future, So they created BADI and also an interface.

1. BADI is based on object-oriented programming.

2. We can see list of existing BADI by t code SE18.

3. We can implement the BADI by t code SE19.

We can search BAdI Name is used for classical and Enhancement spot used for new.

You can check the documentation related to BAdI and used those as per your requirement.

![](/legacyfs/online/storage/blog_attachments/20...