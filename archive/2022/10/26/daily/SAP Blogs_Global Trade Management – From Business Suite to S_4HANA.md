---
title: Global Trade Management – From Business Suite to S/4HANA
url: https://blogs.sap.com/2022/10/25/global-trade-management-from-business-suite-to-s-4hana/
source: SAP Blogs
date: 2022-10-26
fetch_date: 2025-10-03T20:53:41.984632
---

# Global Trade Management – From Business Suite to S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Global Trade Management - From Business Suite to S...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66626&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Global Trade Management - From Business Suite to S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/global-trade-management-from-business-suite-to-s-4hana/ba-p/13545083)

![peter_langner](https://avatars.profile.sap.com/a/9/ida901bdfce8798b27aba9053267d47291d40923454844ca206d82493cbbac8e81_small.jpeg "peter_langner")

[peter\_langner](https://community.sap.com/t5/user/viewprofilepage/user-id/569)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66626)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66626)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545083)

‎2022 Oct 25
4:46 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66626/tab/all-users "Click here to see who gave kudos to this post.")

8,295

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Global Trade Management](https://community.sap.com/t5/c-khhcw49343/Global%2520Trade%2520Management/pd-p/080b2b57-ba1b-4be4-97c5-4349c86388a0)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Global Trade Management

  Software Product Function](/t5/c-khhcw49343/Global%2BTrade%2BManagement/pd-p/080b2b57-ba1b-4be4-97c5-4349c86388a0)

View products (2)

If you are already using SAP Global Trade Management (GTM)  within the SAP Business Suite then you may want to know, what is new with SAP S/4HANA Global Trade Management.

Or maybe you have already implemented SAP GTM in SAP S/4HANA and you are planning a release change and want to know now, what is new from the past years?

Based on community interest on both of these scenarios, I am inspired to share this update with you.

Let us start from the beginning...

First, the good news! SAP Global Trade Management became part of the SAP S/4HANA core and is shipped to customers with the very first Release 100. A few highlights to consider:

**Business Partner, Material, Credit Check**

SAP GTM integrates the business partner, and it is adapted to the longer material number. Since only SAP Financial Supply Chain Management (FSCM) credit check is allowed in SAP S/4HANA, you can now use scope, which is identical to the SD (Sales & Distribution) credit check in SAP ECC, with the license you already own.

**Only SAP S/4HANA on premise**

SAP GTM is only available with SAP S/4HANA on premise and SAP S/4HANA private cloud. Not in S/4HANA public Cloud. The reason is, that there are no best practice processes defined and there are also no native SAP Fiori apps.

**SAP Fiori Apps are available**

With SAP S/4HANA new SAP Fiori apps available, but there are only two native apps. The standard transactions from SAP GUI are rendered as Web HTML. You are not able to maintain the typical SAP GTM user parameters for the organizational data ion the Fiori launchpad.

Two new business roles are defined:

+ Trader and
+ Trading Manager

|  |  |  |  |
| --- | --- | --- | --- |
| **Role-ID** | **Role Name** | **Technical Business Role** | **Role Description** |
| **R0071** | Trader | SAP\_BR\_TRADER | Buys and sells physical products. |
| **R0215** | Trading Manager | SAP\_BR\_TRADING\_MANAGER | Responsible for trading business. |

With release S/4HANA 2022 SAP has delivered the first two native fiori apps: The *Manage Trading Contract* App (App-ID: F6649) and the *Schedule Follow-On Document Processing* App (App ID: F6438).

**Some functions were deleted or deactivated**

No Retail calculation is possible because Retail was delivered later than SAP GTM within SAP S/4HANA. It is deactivated and should not be used anymore. If you are already using it in the Business Suite, it can be migrated, but should be replaced afterwards.

Invoice Forecasting, logistical options, raw exposer update and differential invoice are Commodity Management Function, and therefore not part of SAP GTM core anymore. If you need them, you must implement the respective SAP S/4HANA component.

Also, the Trading Contract@Web code was deleted in SAP S/4HANA.

**New Implementation Guide (IMG)**

In the SAP GTM IMG (Implementation Guide) the nodes of the deleted functions were removed here as well. Furthermore, the remaining entries were restructured.

![](/legacyfs/online/storage/blog_attachments/2022/10/2022-10-17-18_07_57-Introducing-Global-Trade-Management-in-S4-HANA.docx-Word-1.png)

*SAP ECC IMG left and SAP S/4HANA IMG on the right*

**Database Field Changes within Global Trade Management**

If you have own custom code, you might have to adjust your code to the new database design to avoid syntax or processing problems.

In the following tables the primary key as well as the field DOCUMENT and PRED\_DOCUMENT have changed:

|  |  |
| --- | --- |
| **Table** | **Description** |
| WBASSOC | Global Trade: Association Table |
| WBGT | Global Trade: Generic Document Information |
| WBHF | Trading Contract: Document Flow |
| WBIT | Association Item at Step Level |

Furthermore, the table KONDIND (General Document Index for Conditions) is not used anymore. Instead of, the fields are available in table KONH (Conditions (Header)) directly.

For more details as well as how to deal with these changes please read [SAP-Note 2198031](https://launchpad.support.sap.com/#/notes/2198031).

**O****bsolete Reports, Transactions and PFCG Roles**

The following Transactions and their reports are obsolete or replaced by a new version:

|  |  |  |  |
| --- | --- | --- | --- |
| **Obsolete Report** | **Obsolete TCode** | **Successor Report** | **Successor TCode** |
| RWB2B001 - Trading Contract: General Document Overview | WB24 | RWB2BREL - Trading Contract: Follow on document processing | WBRR |
| RWB2B001 - Trading Contract: General Document Overview | WB25\_COMP | RWB2BMAS - Mass Processing (Release and Status update) | WB24N |
| WB2B\_CREATE\_TC\_USER - Create User for TC At Web | WB2B\_NETUSER |  |  |

The following transactions are obsolete:

|  |  |  |
| --- | --- | --- |
| **Obsolete TCode** | **Description** | **Successor TCode** |
| POFO1 | Create Portfolio | POFO31 |
| POFO2 | Change Portfolio | POFO32 |
| POFO3 | Display Portfolio | POFO33 |

The PFCG Roles SAP\_EP\_LO\_WB20N\_N and SAP\_EP\_LO\_WBCB are obsolete. Please use PFCG Role SAP\_EP\_LO\_WB20N or SAP\_EP\_LO\_WZR0N instead.

See also [SAP-Note 2204137](https://launchpad.support.sap.com/#/notes/2204137) for more details.

**Process Detail Folder**

Process Detail Folder on Trading Contract Item Level is deprecated because the displayed data are providing on other screens as well. So, there is no business needed to display the same information on an additional screen as well.

**Letter of Credit**

Letter of Credit functionality of Foreign Trade Application is no longer support withi...