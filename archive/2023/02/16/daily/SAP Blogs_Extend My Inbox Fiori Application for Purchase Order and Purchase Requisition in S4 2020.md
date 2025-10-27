---
title: Extend My Inbox Fiori Application for Purchase Order and Purchase Requisition in S4 2020
url: https://blogs.sap.com/2023/02/15/extend-my-inbox-fiori-application-for-purchase-order-and-purchase-requisition-in-s4-2020/
source: SAP Blogs
date: 2023-02-16
fetch_date: 2025-10-04T06:45:46.080697
---

# Extend My Inbox Fiori Application for Purchase Order and Purchase Requisition in S4 2020

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Extend My Inbox Fiori Application for Purchase Ord...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163438&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extend My Inbox Fiori Application for Purchase Order and Purchase Requisition in S4 2020](/t5/technology-blog-posts-by-members/extend-my-inbox-fiori-application-for-purchase-order-and-purchase/ba-p/13569928)

![irfan_gokak](https://avatars.profile.sap.com/d/f/iddfa43f8031b7087ac135c9ff9487e7b3a0d5287444609e92e1d5070b93594ba9_small.jpeg "irfan_gokak")

[irfan\_gokak](https://community.sap.com/t5/user/viewprofilepage/user-id/206822)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163438)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163438)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569928)

‎2023 Feb 15
10:51 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163438/tab/all-users "Click here to see who gave kudos to this post.")

8,131

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori tools](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520tools/pd-p/73555000100800002345)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Fiori tools

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Btools/pd-p/73555000100800002345)

View products (5)

Recently I did extension for My Inbox Fiori application for Purchase Order and Purchase Requisition approvals. As beginner, I did not know where to start initially. After some research I found a blog from **ragini.upadhyay (<https://blogs.sap.com/2018/06/02/fiori-my-inbox-2.0-extend-approve-purchase-order-s4-hana-1610/>)** which was well explained but I had to struggled a lot. There are few places where this solution wasn’t accurate and wasn’t working. This might be because of the S4 version. Then I found some workaround and finally I’m able to achieve it. Let’s hear it…

## Requirement:

Display approvers along with status in detail screen for both purchase order and purchase requisition.

![](/legacyfs/online/storage/blog_attachments/2023/02/PO_PROBLEM_STATEMENT.png)

Requirement for Purchase Order Approval

![](/legacyfs/online/storage/blog_attachments/2023/02/PR_PROBLEM_STATEMENT.png)

Requirement for Purchase Requisition Approval

## Technical Details:

My Inbox detail screen for PR & PO is cds annotation based. In this case, annotations is being loaded from service model and below links are loading these annotations in the app.

### Annotation Purchase Order:

```
/sap/opu/odata/IWFND/CATALOGSERVICE;v=2/Annotations(TechnicalName='C_PURREQUISITION_FS_ANNO_MDL',Version='0001')/$value
```

### Annotation Purchase Requisition:

```
/sap/opu/odata/IWFND/CATALOGSERVICE;v=2/Annotations(TechnicalName='C_PURCHASEORDER_FS_ANNO_MDL',Version='0001')/$value
```

### Standard CDS View for Extenstion:

**PR** - **C\_PurchaseOrderFs**

**PO** - **C\_PurRequisitionFs**

### Standard Tables:

**PR** – **EBAN** (PR Header Details and Release Strategy) -> **T16FS** (Release Codes from Release Strategy) -> **T16FD** (Release Codes from Release Group) -> **T16FW** (User Id’s from Release Codes) -> **USR21** (Personnel Number from User Id) -> ADRP (User Full Name from Personal Number)

**PO** - **EKKO** (PO Header Details) ->  **T16FS** (Release Codes from Release Strategy) -> **T16FD** (Release Codes from Release Group) -> **T16FW** (User Id’s from Release Codes) -> **USR21** (Personnel Number from User Id) -> ADRP (User Full Name from Personal Number)

## Purchase Order Approvals (4 Levels)

* Create CDS View **ZCDS\_PUR\_ORD\_APP** to read **Approver ID** from **T16FW**. Joining **EKKO** on **T16FW** and **T16FD**.

```
@AbapCatalog.sqlViewName: 'ZSQ_PURORD_APP'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'CDS for PO Approvals'

define view ZCDS_PUR_ORD_APP as select from ekko as _PurOrd

left outer join     t16fs   as      _RelStat        on      _PurOrd.frggr   = _RelStat.frggr

                                                    and     _PurOrd.frgsx   = _RelStat.frgsx

left outer join     t16fw   as      _RoleRelCode    on      _PurOrd.frggr = _RoleRelCode.frggr

left outer join     t16fd   as      _RelCodeDesc    on      _PurOrd.frggr = _RelCodeDesc.frggr

                                                    and _RoleRelCode.frgco = _RelCodeDesc.frgco

{

    _PurOrd.ebeln,

    _PurOrd.frggr,

    _PurOrd.frgsx,

    _PurOrd.frgke,

    _PurOrd.frgzu,

    _RoleRelCode.objid,

    _RoleRelCode.otype,

    _RelCodeDesc.frgct,

    _RelCodeDesc.frgco,

    _RelStat.frgc1,

    _RelStat.frgc2,

    _RelStat.frgc3,

    _RelStat.frgc4

}
```

Result of **ZCDS\_PUR\_ORD\_APP** (Showing approvers in multiple rows)

**Objid** = User ID

**Frgct** = User Position

![](/legacyfs/online/storage/blog_attachments/2023/02/PO_APP_MULTI_ROWS.png)

Approvers in Multiple Rows

* Now we need to Create CDS view **ZCDS\_PUR\_ORD\_APP\_F** to convert multiple rows into single row. Also, association added to read user full name from CDS **ZCDS\_USER\_DET**.

Example:

![](/legacyfs/online/storage/blog_attachments/2023/02/CURRENT_RESULT.png)

Current Result for Multiple Rows

![](/legacyfs/online/storage/blog_attachments/2023/02/EXPECTED_RESULT.png)

Converting to Single Row

Here we go...

```
@AbapCatalog.sqlViewName: 'ZSQ_PO_APPF'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'PO Approvals Final V2'

define view ZCDS_PUR_ORD_APP_F as select from ZCDS_PUR_ORD_APP

association [1..1] to     ZCDS_USER_DET           as      _UserDet           on      ZCDS_PUR_ORD_APP.objid = _UserDet.UserId {

    ebeln,

    max( case frgco when frgc1 then objid end ) as ApproverID1,

    max( case frgco when frgc2 then objid end ) as ApproverID2,

    max( case frgco when frgc3 then objid end ) as ApproverID3,

    max( case frgco when frgc4 then objid end ) as ApproverID4,

    max( case frgco when frgc1 then frgct end ) as ApprPosition1,

    max( case frgco when frgc2 then frgct end ) as ApprPosition2,

    max( case frgco when frgc3 then frgct end ) as ApprPositi...