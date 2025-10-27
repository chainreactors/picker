---
title: Shelf-Life Planning within SAP IBP Response & Supply Planning
url: https://blogs.sap.com/2023/03/31/shelf-life-planning-within-sap-ibp-response-supply-planning/
source: SAP Blogs
date: 2023-04-01
fetch_date: 2025-10-04T11:20:59.375149
---

# Shelf-Life Planning within SAP IBP Response & Supply Planning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Shelf-Life Planning within SAP IBP Response & Supp...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4608&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Shelf-Life Planning within SAP IBP Response & Supply Planning](/t5/supply-chain-management-blog-posts-by-members/shelf-life-planning-within-sap-ibp-response-supply-planning/ba-p/13552080)

![former_member566926](https://avatars.profile.sap.com/former_member_small.jpeg "former_member566926")

[former\_member566926](https://community.sap.com/t5/user/viewprofilepage/user-id/566926)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4608)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4608)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552080)

‎2023 Mar 31
9:29 PM

[10
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4608/tab/all-users "Click here to see who gave kudos to this post.")

7,984

* SAP Managed Tags
* [SAP Integrated Business Planning for response and supply](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520response%2520and%2520supply/pd-p/ad3b7f3b-110d-4d49-9b0a-6ca8b89b1b04)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP Integrated Business Planning for response and supply

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bresponse%2Band%2Bsupply/pd-p/ad3b7f3b-110d-4d49-9b0a-6ca8b89b1b04)

View products (4)

### **Overview**

* **Shelf-Life Planning** is a feature introduced as part of SAP IBP 2211 release within the Response & Supply Planning module (Order-based planning). In order to use this feature, the IBP Planning Area must be based on the SAP7F model entity and use RTI for data integration between IBP and S/4 (or ECC) systems.

* It's a critical feature for companies that manage the shelf life of their products, therefore it is addressing industries that deal with perishable goods such as **P****harmaceuticals, Food and Beverages, and Chemicals.**

Some of the reasons why IBP Shelf-Life Planning is such a compelling proposition:

* **Cost saving & minimize waste:** Using FEFO (First Expiry First Out), companies can efficiently manage their inventory by automatically shipping the batches that are closer to their expiration date, thus reducing obsolete inventory and excess production.

* **Compliance with regulations:** Many industries are highly regulated and require companies to manage the shelf life of their products, as some of the goods can only be shipped with a predefined amount of shelf life remaining.

### **Features**

- **Supply & Deployment planning engines** that use **finite heuristic** have been enhanced to consider Shelf-Life information. Integrating Shelf-Life planning information in the planning processes allows the system to consider **Minimum Remaining Shelf Life (MRSL) requirement of the customer demand** and **reduces the risk of scrap/wastage**.

- Finite Heuristic engine, both for supply planning & deployment planning, has been enhanced to match **Minimum Remaining Shelf-Life (MRSL) requirements of independent demands** and **expiration dates of supply/receipt elements**.

- Shelf-Life planning within IBP Response & Supply follows **FEFO (First Expire, First Out) approach**. In case of multiple supply elements available, the system picks the one which is **set to expire at the earliest**.

- With the planning run profile (PRP) closely integrated with Finite Heuristic, **demand streams for a customer can be prioritized** and **matched with competing batch stock**. For instance, stock getting expired earliest is matched with a sales order demand instead of a forecast. The goal is to match least remaining shelf-life supply with prioritized demand.

- If a Shelf-Life requirement of a **demand cannot be met**, the system generates a **gating factor record “Projected Stock – Shelf Life”** and this can be shared with the supply planner for further analysis.

- Apps like **Intelligent Visibility** can help to **efficiently handle alerts** generated for **demands with shelf-life requirements enabled**.

### **Process Flow**

![](/legacyfs/online/storage/blog_attachments/2023/03/Process-Flow-2.png)

Figure 1: Process Flow (Click to enlarge)

### **Master Data**

1) *Product*: This MDT has been enhanced to include 2 attributes: “Shelf-Life Planning Active” and “Minimum Remaining Shelf Life”

![](/legacyfs/online/storage/blog_attachments/2023/03/MDT-Product-1.png)

Figure 2: Master Data - Product (Click to enlarge)

2) *Location Product*: This MDT has also been enhanced to include both shelf-life related attributes as mentioned in Product MDT.

![](/legacyfs/online/storage/blog_attachments/2023/03/MDT-Location-Product-1.png)

Figure 3: Master Data - Location Product (Click to enlarge)

3) *Transportation Lanes*: RTI generates Transportation Lane based on Purchase Info Record and copies its value into this MDT, including the Remaining Shelf-Life information.

![](/legacyfs/online/storage/blog_attachments/2023/03/MDT-Transportation-Lane-1.png)

Figure 4: Master Data - Transportation Lane (Click to enlarge)

4) *Production Data Structures*: RTI generates PDS in IBP based on Production version (combination of BOM and Master Recipe / Routing). Attribute of the PDS “Shelf Life of Planned Production” gets populated based on MRSL maintained in S/4 material master.

![](/legacyfs/online/storage/blog_attachments/2023/03/MDT-PDS-1.png)

Figure 5: Master Data - Production Data Structure (PDS) (Click to enlarge)

### **Transaction Data**

1) *Forecast*: As shown below, there is a forecast requirement of 5 PC on 01.04.2023. MRSL requirement of this forecast is determined as 120 (Picked from S/4 material master). This means the supply element (existing one or new one generated) should have expiration date of atleast 30.07.2023 (01.04.2023 + 120 days) or later.

![](/legacyfs/online/storage/blog_attachments/2023/03/TD-Forecast-1.png)

Figure 6: Transaction Data - Forecast (Click to enlarge)

2) *Sales Order*: As shown below, there is a Sales Order of qty 10 PC with material availability date (MAD) as 17.04.2023. MRSL requirement of this sales order is determined as 44 days (This is calculated as a difference between SLED of batch [31.05.2023] assigned and MAD [17.04.2023]). This means the supply elem...