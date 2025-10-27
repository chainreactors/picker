---
title: S/4 Hana Enforcement Actions and Debt Set Relationships
url: https://blogs.sap.com/2022/11/13/s-4-hana-enforcement-actions-and-debt-set-relationships/
source: SAP Blogs
date: 2022-11-14
fetch_date: 2025-10-03T22:41:02.398248
---

# S/4 Hana Enforcement Actions and Debt Set Relationships

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* S/4 Hana Enforcement Actions and Debt Set Relation...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67676&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4 Hana Enforcement Actions and Debt Set Relationships](/t5/enterprise-resource-planning-blog-posts-by-members/s-4-hana-enforcement-actions-and-debt-set-relationships/ba-p/13558817)

![iandsalveson](https://avatars.profile.sap.com/b/2/idb239f8f9e03e44b60d54eb1f80628c5481c3e3ee674d158c35dc04b144e67798_small.jpeg "iandsalveson")

[iandsalveson](https://community.sap.com/t5/user/viewprofilepage/user-id/42374)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67676)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67676)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558817)

‎2022 Nov 13
9:28 AM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67676/tab/all-users "Click here to see who gave kudos to this post.")

1,630

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

## Introduction

The purpose of this article is to explore the relationship that exists between a DCM Debt Set and an enforcement action. These new entities within S/4 Hana essentially act as an adapter or bridge between the worlds of CRM and PSCD. The new capabilities of the Debt Set and Enforcement actions means that complex transactional processing can be managed by one order object entities with the added benefit of linkages to financial processing where appropriate.

### Debt Set

A Debt Set entity has been introduced which essentially acts as a container to group like fica items for a specific debtor together. A debt set may also be categorised by utilising the concept of a debt set type.

##### Debt Set Configuration

If a debt set object is to be utilised in the S/4Hana landscape there is a certain amount of configuration that is required, namely, defining a debt set type and a number range to be utilised by the debt set type.

###### Debt Set Number Range Configuration

|
 IMG Path |
 Contract Accounts Receivable and Payable > Business Transactions > Dunning > Dunning by Collection Strategy > Debt Collection Management > Define Number range for Debt Set Type |

|
 Purpose |
 In this Customizing activity, you define the number range intervals for debt set types. |

###### Debt Set Type

|
 IMG Path |
 Contract Accounts Receivable and Payable > Business Transactions > Dunning > Dunning by Collection Strategy > Debt Collection Management > Define Debt Set Type |

|
 Purpose |
 In this Customizing activity, you define debt set types. Debt sets group liabilities to handle them together in the context of debt collection management. |

###### Debt Set Persistent tables

* DFKK\_DCM\_DS\_H     – Debt Set Header

* DFKK\_DCM\_DS\_I       – Debt Set Items

* DFKK\_DCM\_DS\_CLS – Debt Set Classifications

The details of the debt set header and Items are shown below in diagram 1.

```
@EndUserText.label : 'Debt set header'

@AbapCatalog.enhancementCategory : #EXTENSIBLE_CHARACTER_NUMERIC

@AbapCatalog.tableCategory : #TRANSPARENT

@AbapCatalog.deliveryClass : #A

@AbapCatalog.dataMaintenance : #RESTRICTED

define table dfkk_dcm_ds_h {

  key mandt           : mandt not null;

  key debt_set_number : dcm_debt_set_number_kk not null;

  debt_set_type       : dcm_debt_set_type_kk;

  debtor              : dcm_debt_set_debtor_kk;

  description         : dcm_debt_set_description_kk;

  protection          : dcm_ds_protection_kk;

  lifecycle_status    : dcm_ds_lifecycle_status_kk;

  collection_strategy : strat_cm_kk;

  collection_step     : step_cm_kk;

  created_at          : timestamp;

  created_by          : uname;

  changed_at          : timestamp;

  changed_by          : uname;

}

@EndUserText.label : 'Debt set item'

@AbapCatalog.enhancementCategory : #EXTENSIBLE_CHARACTER

@AbapCatalog.tableCategory : #TRANSPARENT

@AbapCatalog.deliveryClass : #A

@AbapCatalog.dataMaintenance : #RESTRICTED

define table dfkk_dcm_ds_i {

  key mandt           : mandt not null;

  @AbapCatalog.foreignKey.screenCheck : false

  key debt_set_number : dcm_debt_set_number_kk not null

    with foreign key dfkk_dcm_ds_h

      where mandt = dfkk_dcm_ds_i.mandt

        and debt_set_number = dfkk_dcm_ds_i.debt_set_number;

  key opbel           : opbel_kk not null;

  key opupw           : opupw_kk not null;

  key opupk           : opupk_kk not null;

  key opupz           : opupz_kk not null;

}
```

Diagram 1

### Enforcement Action

An example for an enforcement action could be say a wage garnishee which encompasses all of the customer's outstanding receivables. In such an example all of the debtor's existing debt sets would be assigned to the wage garnishee enforcement action. Note: It is also possible to assign a debt set to more than one enforcement action.

A new enforcement action object is available in the S/4Hana system and the existing one order framework can be utilised to process the enforcement action. A new standard transaction type of  DMEA has been delivered and the details of the standard template can be seen in diagram 2.

Note: Never modify the standard transaction type DMEA. If variations are required to the standard then copy the standard DMEA transactions to a custom transaction type and then make configuration changes. There are many CRM blogs on how to create a status profile or action profile.

###### Enforcement Action Configuration

|
 IMG Path |
 Service>Transactions>Basic Setting>Define Transactions Types |

|
 Purpose |
 In this Customizing activity, you define transaction type |

![](/legacyfs/online/storage/blog_attachments/2022/11/DMEA-1.jpg)

Diagram 2

###### Enforcement Action Persistent Table

* CRM4SD\_DMEA\_H

```
@EndUserText.label : 'Enforcement Action Header'

@AbapCatalog.enhancementCategory : #EXTENSIBLE_CHARACTER_NUMERIC

@AbapCatalog.tableCategory : #TRANSPARENT

@AbapCatalog.deliveryClass : #A

@AbapCatalog.dataMaintenance : #RESTRICTED

define table crms4d_dmea_h {

  key include crms4s_key_h not null;

  include crms4s_dmea_h_orderadm_h;

  include crms4s_dmea_h_ea_h;

  include crms4s_dmea_h_partner;

  include crms4s_dmea_h_dates;

  include crms4s_dmea_h_orgman;

  include crms4s_dmea_h_status;

  include crms4s_dmea_h_incl_eew_ps;

}
```

###

### Relationship Diagram

The diagram below(diagram 4) demonstrates the relationships between a debt set and enforcement actions. The persistent table that realises the linkages between an enforcement action and a debt set is CRMS4D\_EXT\_REF(diagram 3).

```
@E...