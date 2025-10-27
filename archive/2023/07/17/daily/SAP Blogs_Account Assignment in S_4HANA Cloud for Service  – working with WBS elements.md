---
title: Account Assignment in S/4HANA Cloud for Service  – working with WBS elements
url: https://blogs.sap.com/2023/07/16/account-assignment-in-s-4hana-cloud-for-service-working-with-wbs-elements/
source: SAP Blogs
date: 2023-07-17
fetch_date: 2025-10-04T11:52:26.182367
---

# Account Assignment in S/4HANA Cloud for Service  – working with WBS elements

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Account Assignment in S/4HANA Cloud for Service -...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51848&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Account Assignment in S/4HANA Cloud for Service - working with WBS elements](/t5/enterprise-resource-planning-blog-posts-by-sap/account-assignment-in-s-4hana-cloud-for-service-working-with-wbs-elements/ba-p/13560327)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51848)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51848)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560327)

‎2023 Jul 16
10:59 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51848/tab/all-users "Click here to see who gave kudos to this post.")

3,686

* SAP Managed Tags
* [SAP S/4HANA Cloud for enterprise portfolio and project management](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520for%2520enterprise%2520portfolio%2520and%2520project%2520management/pd-p/50d750e2-9a5f-462e-8001-ac7ff1800174)
* [SAP S/4HANA Cloud Public Edition Service](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Service/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition Service

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BService/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)
* [SAP S/4HANA Cloud for enterprise portfolio and project management

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2Bfor%2Benterprise%2Bportfolio%2Band%2Bproject%2Bmanagement/pd-p/50d750e2-9a5f-462e-8001-ac7ff1800174)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (3)

In this blog post, I would like to demonstrate how the assignment of costs and revenues works in service transactions in S/4HANA Cloud. I’ll be using the service orders and service contracts as examples of service transaction to illustrate how the costs and revenues from these transactions are carried over into Finance and assigned to the relevant controlling objects.

Let’s first start with a detailed introduction of all the different combinations that are possible for the assignment of costs and revenues when considering service orders and service contracts. This is crucial to consider, as there are multiple accounting assignment objects available to book the costs and revenues against – for example Cost Centers, Sales Orders, Service Orders, Service Contracts or project WBS (Work breakdown structure) elements. For the service transactions, we consider only the objects Service Order, Service Contract and WBS elements.
Please note: in LoB service management in S/4HANA public Cloud, only the Service orders and service contracts can be used as “real” account assignment objects, the WBS element is purely a **statistical** account assignment object.

To understand the impact of the various combinations involved, I’ve setup the following transactional data:

* Two service contracts: 1 with a WBS element, 1 without a WBS element

* 4 service orders, with the combinations listed below:

|
 Service Order (SO) |
 WBS element in SO |
 Service Contract |
 WBS Element in Service Contract |
 WBS element that is booked statistically |

|
 X |
 - |
 - |
 - |
 - |

|
 X |
 R.000004 |
 - |
 - |
 R.000004 |

|
 X |
 - |
 X |
 - |
 - |

|
 X |
 R.000004 |
 X |
 - |
 - |

|
 X |
 - |
 X |
 R.000004 |
 R.000004 |

|
 X |
 R.000007 |
 X |
 R.000004 |
 R.000004 |

The table above details the different possibilities of account assignment objects in service orders. Let’s break down the meaning of these results:

1. Order without a contract => specification of the WBS element in the order has relevance (statistical booking of costs and revenues). The real account assignment is still against the service order.

2. Order with a contract (but the contract has no WBS element) => The WBS element (or in this case lack of a WBS element) in the contract has precedence over any WBS element entered in the service order. Due to this, even if a WBS element is specified in the order at (only possible on header level), it is of no relevance (not even statistically). Here too, the real account assignment is against the service order.

3. Order with contract (contract has a WBS element) => WBS element from the contract is statistically booked, regardless of whether a different WBS element or no WBS element at all is specified in the order. The real account assignment is still against the service order.

4. From the points 2 and 3, one can conclude that the topic of WBS elements in the service order no longer has any relevance as soon as a service contract is determined. Regardless of what is shown on the Service Order UI, a statistical booking is done against the WBS element from the contract. If the contract doesn’t specify a WBS element but, this still has precedence and there will be no statistical booking, even if a WBS element is specified on the service order.

Finally, a special case to consider, which is not listed in the table above. This is a sort of “mixed” service order, in which only item 10 is linked to a contract (with or without a WBS element) and item 20 is not linked to a contract. In this special case, the account assignment takes place as follows:

* Item 10: if the determined contract has a WBS element, the statistical booking is done against this. If not, there is no statistical booking.

* Item 20: if a WBS element is additionally assigned to the service order item, the statistical booking is done against this if there is no WBS element additionally specified in the service order, there is no statistical booking.

\*Note: in order to get an insight into how the costs and revenues are assigned to account assignment objects, use the app “Display Line Items in General Ledger”. There add the search filter “Service Document” where you can enter a service order ID to display the results for. Change the "Status" field to show All Items. After clicking "Go", click “Expand All” to show the individual journal entries.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-20.png)

Finally add the table filter columns “Account Assignment”, “Service Contract” and “WBS Element is Stat.” to view the desired results.

![](/legacyfs/online...