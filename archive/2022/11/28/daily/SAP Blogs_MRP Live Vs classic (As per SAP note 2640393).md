---
title: MRP Live Vs classic (As per SAP note 2640393)
url: https://blogs.sap.com/2022/11/27/mrp-live-vs-classic-as-per-sap-note-2640393/
source: SAP Blogs
date: 2022-11-28
fetch_date: 2025-10-03T23:55:02.289575
---

# MRP Live Vs classic (As per SAP note 2640393)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* MRP Live Vs classic (As per SAP note 2640393)

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67789&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [MRP Live Vs classic (As per SAP note 2640393)](/t5/enterprise-resource-planning-blog-posts-by-members/mrp-live-vs-classic-as-per-sap-note-2640393/ba-p/13559764)

![Narasimha](https://avatars.profile.sap.com/8/6/id86eeea52b1a32d196fa1a2cdbe4dac2d17041e9b1591b363f2d72303b40bd863_small.jpeg "Narasimha")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Narasimha](https://community.sap.com/t5/user/viewprofilepage/user-id/14917)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67789)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67789)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559764)

‎2022 Nov 27
5:35 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67789/tab/all-users "Click here to see who gave kudos to this post.")

14,352

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)

View products (1)

**Purpose:**

There are many blog posts on this subject. However, I was not aware that SAP note exists on this subject. For the benefit of all the consultants who may not have access to SAP notes, I am putting the contents of the note here. This is the most asked question while implementing S4H.

2640393 - **Differences between t-code MD01N and classic MRP t-codes MD01/MD02/MD03**

Version 6 Type SAP Knowledge Base Article.

Language English Master Language English.

Release Status Released to Customer Category Problem.

Component PP-MRP (Material Requirements Planning) Released On 14.04.2021.

Please find the original document at <https://launchpad.support.sap.com/#/notes/2640393>
Symptom
MRP live (T-code MD01N) is suggested to run MRP on S/4HANA systems. This KBA explains differences between t-code MD01N and classic MRP t-codes MD01/MD02/MD03.
Environment

• SAP ERP Production Planning (PP)
• SAP Enhancement package for SAP ERP, version for SAP HANA
• SAP S/4HANA, on-premise

|
 Feature |
 Classic MRP (t-codes    MD01/MD02/MD03) |
 MRP live (t-code MD01N) |
 Related Note/KBA |

|
 MRP list |
 MRP parameter "Create MRP list" can be used to control whether MRP list should be created. |
 No MRP lists are written by MRP live as MRP lists were intended for checking the MRP result. MRP lists were used to find materials with issues quickly. MRP lists are snapshots of the material supply and demand situation at the time of the last MRP run. The snapshot is often outdated. With HANA, stock/requirements lists can be read with high speed. MRP cockpit can be used to determine materials with late supply issues in real-time. T-code md\_mrp\_force\_classic shows all master data related issues(like no production version found). In SAP S/4HANA there is no    need for outdated MRP lists. |
 2268085 - S4TWL    - MRP live on SAP HANA - MD01N 2554382 - MRP List (MD05)    can't be found after MRP Live run 2327795 - MRP on HANA:    Requirements aggregated on the MRP List |

|
 Scope of planning |
 MRP parameter "Scope of planning" can be used to combine a group of plants or    MRP areas. |
 Scope of planning is not supported. MRP Live can plan many materials in many plants. It always plans all MRP Areas. |
  |

|
 creation indicators |
 Classic MRP has a complicated set of rules for instructing the MRP run to create either purchase requisitions or planned orders for externally procured materials. MRP    parameters "Create purchase |
 MRP live on HANA always creates purchase requisitions for externally procured materials and schedule lines if there is valid scheduling agreement or source list with scheduling agreement. MRP live on HANA always creates planned orders for inhouse    production materials. |
 2268085 - S4TWL    - MRP in HANA |

|
  |
 req." and "Schedule lines" can    be used. |
  |
  |

|
 opening period |
 In classic MRP, parameter "Creation indicator for Purchase Requisitions" can be set as 2:Purchase requisitions in    opening period. |
 MRP live on HANA doesn't consider opening period. |
 2490226 - MRP    Live does not Consider Opening Period |

|
 planning horizon |
 MRP parameter "Processing key" NETPL can be set on ERP systems, but it is removed in S/4HANA systems. |
 MRP live doesn't support planning horizon |
 2270241 - S4TWL    - Planning Horizon 2639021 -    Planning horizon /    procesing key NETPL in S/4 |

|
 processing key |
 MRP parameter "Processing key" NETPL can be set on ERP systems, but it is removed in S/4HANA systems. |
 The indicator "Regenerative planning" in MRP live replaces the MRP parameter "Processing key". If it is set, it works similar like processing key = NEUPL in classic    MRP. |
  |

|
 scheduling |
 On ERP systems, if MRP parameter "Scheduling" is set to "2 Lead Time Scheduling and Capacity Planning", Detailed planning, Rate-based planning, Rough-Cut Planning are all supported. On S/4HANA systems only detailed    scheduling is supported. |
 On S/4HANA systems only detailed scheduling is supported. If Rate-based and rough-cut routings are maintained in the production version, exception message MD425 occurs "62: Scheduling: Master data inconsistent (P2)". MRP live also supports advanced planning for PP/DS. |
 2270240 - S4TWL    - Rate and Rough- Cut Planning |

|
 planning mode |
 Classic MRP t-codes have 3 options for planning mode: 1 Adapt planning data (normal mode) 2 Re-explode BOM and routing 3 Delete and recreate planning data |
 No planning mode 2. Planning mode 1 works different from classic MRP. For planning mode 1, either 100% reuse or delete and re- create. AMDP BADI PPH\_MRP\_REUSE\_BADI can be used to influence system behavior. |
 2583090 - MD01N    deletes purchase requisitions and recreate them with planning mode 1    2469065 -    MD01n: New internal BADI for Reuse Check |

|
 simulation |
 T-code MD02 has 2 indicators "Simulation mode" and "Display results prior to saving" to simulate MRP run. T-code MD03 has an indicator "Display    results prior to saving". |
 MRP live doesn't have simulation mode. |
  |

|
 BOM    components |
 T-code MD02 can be used to run MRP for single-item, multi- level. There is also an indicator "Also plan unchanged components". |
 MRP live has an indicator "BOM components" if components are also to be planned. Indicator "Also plan unchanged components" is added to MRP live by note 2584201. If change number is involved in BOM changes, please check KBA 2611243 to make sure MRP live works correctly. |
 2584201 -    Enabling Plan also unchanged components for MRP Live 2611243 - T-code    MD01N doesn't consider ...