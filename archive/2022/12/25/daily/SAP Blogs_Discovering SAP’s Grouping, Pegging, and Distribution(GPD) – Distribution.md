---
title: Discovering SAP’s Grouping, Pegging, and Distribution(GPD) – Distribution
url: https://blogs.sap.com/2022/12/24/discovering-saps-grouping-pegging-and-distributiongpd-distribution/
source: SAP Blogs
date: 2022-12-25
fetch_date: 2025-10-04T02:29:29.623532
---

# Discovering SAP’s Grouping, Pegging, and Distribution(GPD) – Distribution

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Discovering SAP’s Grouping, Pegging, and Distribut...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67617&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Discovering SAP’s Grouping, Pegging, and Distribution(GPD) – Distribution](/t5/enterprise-resource-planning-blog-posts-by-members/discovering-sap-s-grouping-pegging-and-distribution-gpd-distribution/ba-p/13557904)

![Varsha2](https://avatars.profile.sap.com/1/b/id1b232997e0a80011fb183658dc62168ce69eea38dff47c9ce59b57cff074b2c1_small.jpeg "Varsha2")

[Varsha2](https://community.sap.com/t5/user/viewprofilepage/user-id/134589)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67617)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67617)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557904)

‎2022 Dec 24
12:43 AM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67617/tab/all-users "Click here to see who gave kudos to this post.")

3,457

* SAP Managed Tags
* [Aerospace and Defense](https://community.sap.com/t5/c-khhcw49343/Aerospace%2520and%2520Defense/pd-p/192814547175000220653543)
* [Industrial Manufacturing](https://community.sap.com/t5/c-khhcw49343/Industrial%2520Manufacturing/pd-p/42513095034597134398119)
* [MAN (Manufacturing)](https://community.sap.com/t5/c-khhcw49343/MAN%2520%28Manufacturing%29/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)

* [Aerospace and Defense

  Industry](/t5/c-khhcw49343/Aerospace%2Band%2BDefense/pd-p/192814547175000220653543)
* [Industrial Manufacturing

  Industry](/t5/c-khhcw49343/Industrial%2BManufacturing/pd-p/42513095034597134398119)
* [MAN (Manufacturing)

  Software Product Function](/t5/c-khhcw49343/MAN%2B%252528Manufacturing%252529/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)

View products (3)

Welcome to the third blog of the series on understanding GPD – Distribution.

Part 1 - [Grouping](https://blogs.sap.com/2021/12/30/discovering-grouping-pegging-and-distributiongpd-grouping/?preview_id=1465070&preview=true)

Part 2 - [Pegging](https://blogs.sap.com/2022/06/03/discovering-saps-grouping-pegging-and-distributiongpd-pegging/?preview_id=1551230&preview=true)

The purpose is to help gain a high level understanding of how distribution component functions within SAP GPD.

Distribution - distributes the individual / actual costs from the Group WBS elements (grouped replenishments) back to the individual WBS elements (original requirement). It picks up the quantities assigned during pegging for which the costs are to be distributed.

It is a common approach to use Production Orders, Purchase Orders as the objects where the actual cost distribution could be made from, while the list could also include:

* Commitments and Payments

* Stock Values

* Valuated Stock

* WIP

### Pre-requisite:

1. WBS elements are assigned to Group WBS element.

2. Distribution profile for the Group WBS element to define the values to be distributed.

3. Requirements planning is executed.

4. Pegging against the appropriate

###

### Application:

Customising: SPRO→ Project System → Financials → Period End Closing → Single Functions → Distribution

While distribution could be implemented for both valuated and non valuated stock, SAP recommends not going for valuated stock due to business process and technical complexities.

For non-valuated stock, goods movement do not have values and the overall costs are still associated with the Group WBS elements. Distributed values can then be used further for processes such as resource-related billing, surcharge or discount settlement. Only GPD distributed costs should be billed to the customer.

Below image highlights the difference mainly between Internal Procurement (Production Orders),  External Procurement (Purchase Orders) and the value distribution that it can have. We will leave Valuated stock out of scope for this blog.

![](/legacyfs/online/storage/blog_attachments/2022/12/Distribution-Valuated-and-NonValuated-Stock.png)Source: help.sap.com. (n.d.). *SAP Help Portal*. [online] Available at: [https://help.sap.com/docs/SAP\_ERP\_SPV/cfff13ea14f3430488af41bbc02dbb69/18f5c353b677b44ce10000000a174...](https://help.sap.com/docs/SAP_ERP_SPV/cfff13ea14f3430488af41bbc02dbb69/18f5c353b677b44ce10000000a174cb4.html).‌

### Reports:

Two standard reports: RDISALL (transaction DIS01) and RDISALL2 (transaction DIS01N, an advanced version of RDISALL)  are available for triggering cost distribution. When you run DIS01N, depending on the combination of entries in Group WBS and Replenishment object below combinations are possible:

|
 Grouping WBS Element | |
 Replenishment Object |
 Behaviour |
 Exclude |

|
 Include |
 Exclude |
 Include |

|
 Blank |
 Blank |
 Blank |
 Blank |
 All the costs on all the grouping WBS elements and their associated replenishment objects are distributed |

|
 Entered |
 Blank |
 Blank |
 Blank |
 All the costs on the selected grouping WBS elements and their associated replenishment objects are distributed |

|
 Blank |
 Entered |
 Blank |
 Blank |
 All the costs on the grouping WBS elements except those selected are distributed |

|
 Entered |
 Entered |
 Blank |
 Blank |
 All the costs on the selected grouping WBS elements and their associated replenishment objects are distributed |

|
 Blank |
 Blank |
 Entered |
 Blank |
 All costs on the selected replenishment objects are distributed |

|
 Entered |
 Blank |
 Entered |
 Blank |
 All costs on the selected replenishment objects are distributed |

|
 Blank |
 Entered |
 Entered |
 Blank |
 All costs on the selected replenishment objects are distributed |

|
 Entered |
 Entered |
 Entered |
 Blank |
 All costs on the selected replenishment objects are distributed |

|
 Blank |
 Blank |
 Blank |
 Entered |
 All costs on the grouping WBS elements except those for the selected replenishment objects are distributed |

|
 Entered |
 Blank |
 Blank |
 Entered |
 All the costs on the selected grouping WBS elements except those for the selected replenishment objects are distributed |

|
 Blank |
 Entered |
 Blank |
 Entered |
 All the costs on the grouping WBS elements except those for the selected grouping WBS elements and the selected replenishment objects are distributed |

|
 Entered |
 Entered |
 Blank |
 Entered |
 All the costs on the selected grouping WBS elements except those for the selected replenishment objects are distributed |

|
 Blank |
 Blank |
 Entered |
 Entered |
 All costs on the selected replenishment objects are distributed. Replenishment object include/exclude must be mutually exclusive |

|
 Entered |
 Blank |
 Entered |
 Entered |
 All costs on the selected replenishment objects are distributed |

|
 Blank |
 Entered |
 Entered |
 Entered |
 All costs on the selected replenishment objects are distributed |

|
 Entered |
 Entered |
 Entered |
 Entered |
 All costs on the selected replenishment objects are distributed |

Source: help.sap.com. (n.d.). *SAP Help Portal*. [online] Avail...