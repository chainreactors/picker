---
title: MRP Live by S/4 HANA
url: https://blogs.sap.com/2023/06/07/mrp-live-by-s-4-hana/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:35.924583
---

# MRP Live by S/4 HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* MRP Live by S/4 HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67345&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [MRP Live by S/4 HANA](/t5/enterprise-resource-planning-blog-posts-by-members/mrp-live-by-s-4-hana/ba-p/13554263)

![GaneshMhaske](https://avatars.profile.sap.com/d/0/idd0c46be5ec11017fa2c08db5354afe95ab528b5a92872cd6e1ee29685f0a2db7_small.jpeg "GaneshMhaske")

[GaneshMhaske](https://community.sap.com/t5/user/viewprofilepage/user-id/145541)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67345)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67345)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554263)

‎2023 Jun 07
10:34 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67345/tab/all-users "Click here to see who gave kudos to this post.")

33,152

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

SAP S/4 HANA business suite is based on HANA in-memory platform. It brings several improvements over the conventional ECC business suite.  SAP S/4 HANA brought a simplified approach to various business processes. The details of the simplifications are addressed in the Simplifications list. Simplification lists are release specific and published along with the release of S/4 HANA versions.

In this blog, we are going to see the advancement in SAP material requirement planning procedure.  SAP S/4 HANA features the newly constructed MRP engine called MRP Live aka MD01n. MRP Live is optimized for SAP HANA database. This minimizes the data transfer from the database to the application server and back, which contributes to higher performance. MRP Live comes with additional features including the following:

1. Planning scope is more flexible than classical MRP. Single transaction MD01n covers the functionalities of MD01/MD02/MD03 transactions.

2. Cross plant planning is possible in single MRP Run. The planner can plan a set of materials across plants to the component level. The low-level code calculation decides the planning hierarchy of materials.

MRP Live has some limitations as follows, (*more details are in 1914010 – MD01N: Restrictions for Planning in MRP Live on HANA*)

1. The creation indicator for schedule lines is not supported in Md01n. The system will create a schedule line if a valid agreement exists.

2. MD01n does not write MRP List. SAP suggests using MD04 which shows a more live situation.

3. Make-To-Order, Multilevel sale order specific planning (MD50) is not optimized for S/4 HANA.

4. Project based planning (MD51) is not optimized for S/4 HANA.

5. The creation Indicator for purchase requisition is not supported in MD01n. MRP live doesn’t consider opening period. The system creates the purchase requisition if the procurement type is ‘F’. This will reduce the planned order to purchase requisition conversion step.

These limitations may or may not be addressed in future releases. The classic MRP programs are still part of the S/4 HANA release but not considered for future developments.

**MRP Live Considerations**

Before going to check actual MRP Live screen, we will see the basic necessities to be mapped in the system.

**Simplified Sourcing** – Complexity in master data selection within the planning run is reduced in SAP S/4 HANA under the thought of simplified sourcing.  The sourcing channels are described as below, (refer SAP Note 2268069 for details)

1. Production version (In-house Procurement) – Production version is mandatory if the procurement type is ‘E’ or ‘X’. The production version should be not locked but should be active for automatic sourcing to read in MRP Live. This simplification has discontinued the ‘selection Method’ (MARC-ALTSL) field in MRP4 View. The system picks the first valid production version. For those who are migrating from ECC to S/4 HANA refer SAP Note 2655077 for automatic creation of production version.

2. Purchasing Info Record (External Procurement) – System will consider the valid purchasing info record which has procurement type ‘F’ and ticked for ‘Relevant for automatic sourcing’ in MRP live.

3. Purchasing contracts and delivery schedules are selected in MRP live if maintained as procurement type ‘F’.

4. For material with multiple procurement sources, the system will refer to the quota arrangement maintained in transaction MEQ1. Quota arrangement is an integral part of the MRP live. Field quota arrangement usage (MARC- USEQU) in MRP 2 view is discontinued in SAP S/4 HANA. The rest of the master data definitions and structures are intact and referred in MRP live run.

**Planning file entry** – Planning file entry structure has optimized in S/4 HANA to simplify the planning logic. The ECC planning file tables are replaced with single table PPH\_DBVM. In migration activity, run report PPH\_SETUP\_MRPRECORDS is used to setup consistence planning file entries. Besides the setup report, the PPH\_CONVERT\_MRPRECORDS report will convert existing planning file entries to the PPH\_DBVM table. (*Refer SAP Note 2268088 for more details*)

**Planning Horizon** – Planning horizon is the time axis restriction set in ECC customization. In ECC MRP transactions, the Planning key ‘NETPL’ is used to plan the material demands within the planning horizon. The material demands beyond the planning horizon are not counted in the planning run. This is to enhance processing and reduce the planning run time. SAP S/4 HANA MRP live plans all the materials irrespective of the planning horizon. The planning key ‘NETPL’ is no longer used. Regenerative planning is available for the first time MRP run.

**MRP area planning**The scope of existing MRP area functionality in ECC is broadened to accommodate the similar functionality of storage location planning. In ECC, storage location can be excluded from planning (in case of scrap or rejection location) or planned separately (in case of sub-contractor location). Now in SAP S/4 HANA, storage location level planning control is moved to the MRP area level. Storage location planning is not supported in S/4 HANA. MRP area creation is mandatory for storage locations which are managed separately in planning. Storage locations are assigned to the MRP area and further MRP area is planned as per the business requirement. User can set MRP type = ‘ND’ to exclude the material in planning for that particular MRP area. (Refer SAP Note 2268045 for further details)

For subcontracting planning, user need to create supplier specific MRP area and assign locations managed for the supplier. MRP parameters to be maintained in the MRP area view of the material master. (Refer SAP Note 2268044 for further details)

**Evaluating the material master for MRP Live** – SAP Note 1975704 provides the report PPH\_CHECK\_MRP\_ON\_HA...