---
title: Configuration & Business Case of SAP S/4HANA Advanced ATP (AATP) with Business Process Scheduling (BPS) and Alternative-Based Confirmation (ABC)
url: https://blogs.sap.com/2023/03/12/configuration-business-case-of-sap-s-4hana-advanced-atp-aatp-with-business-process-scheduling-bps-and-alternate-base-confirmation-abc/
source: SAP Blogs
date: 2023-03-13
fetch_date: 2025-10-04T09:25:12.627763
---

# Configuration & Business Case of SAP S/4HANA Advanced ATP (AATP) with Business Process Scheduling (BPS) and Alternative-Based Confirmation (ABC)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Config & Business Case of SAP S/4HANA Advanced ATP...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53377&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Config & Business Case of SAP S/4HANA Advanced ATP with BPS and ABC](/t5/enterprise-resource-planning-blog-posts-by-sap/config-amp-business-case-of-sap-s-4hana-advanced-atp-with-bps-and-abc/ba-p/13570398)

![Mrinal_Chanda](https://avatars.profile.sap.com/5/b/id5b951ed7356cbbc794982e9186833423c9f327cdbb765611136e821f12041e2a_small.jpeg "Mrinal_Chanda")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Mrinal\_Chanda](https://community.sap.com/t5/user/viewprofilepage/user-id/146047)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53377)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53377)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570398)

‎2023 Mar 12
3:38 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53377/tab/all-users "Click here to see who gave kudos to this post.")

13,200

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA for advanced ATP](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520for%2520advanced%2520ATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA for advanced ATP

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bfor%2Badvanced%2BATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (5)

**\*\*\*\*\*\*\*\*\*\*\*Updated as per 2502 release \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

In today's fast-paced and highly competitive business world, efficient and effective management of business processes has become more critical than ever before. The modern supply chain is a complex network of interrelated business processes, from sales to procurement and production to warehousing. As companies strive to meet customer demand while keeping costs low, there is a growing need for advanced technologies that can optimize these processes and improve overall efficiency.

In this blog, we will explore how SAP S/4HANA Advanced ATP (AATP) with Business Process Scheduling (BPS) and Alternative Based Confirmation(ABC) can help businesses to achieve their supply chain goals by improving their increased scheduling precision and optimizing resource utilization.

Let’s understand few basic points –

What is AATP in S/4HANA ?

Advanced ATP is a process in S/4HANA that allows businesses to check product availability in real time. While running, this process takes into account various factors such as existing inventory, planned production, and incoming shipments to determine whether a particular product can be delivered to a customer at a specific time. By providing accurate and timely information about product availability, businesses can improve customer satisfaction and reduce the risk of backorders.

What is called BPS & ABC in S/4HANA?

Business process scheduling (BPS) is a method that allows businesses to schedule and manage their processes more efficiently. By using BPS, businesses can optimize their schedules to ensure that they are using their all available resources in the most efficient way possible. This can help to improve overall productivity.

Finally, Alternative based confirmation (ABC) is a feature that is often used in conjunction with advanced ATP and BPS. It allows businesses to get an alternative option when the desired product is not available. This can help to improve customer loyalty & retention, by providing timely delivery of products, which can have a positive impact on the bottom line.

Now let’s see a business case of how they work together S/4HANA.

Let’s assume we have two plants in the USA ( 1710 and US20 respectively) and another plant in Germany (1010) and stocks are available only in US20 and 1010 for 100 quantities each.

Business Case 1: Customer places an order on the US plant (1710) for 100 quantities. The system initially checks stock in the same plant. If it does not have any stock, the system will go nearest other locations in the US that have stock. In this case, the plant, US20, has sufficient stock to provide. With BPS & ABC in place, the system will automatically search for the nearest location to get material and provide a new confirmation date & time as per the selected plant’s settings. In this case, the system will pick 100 stocks from the US20 plant and confirm the order.

![](/legacyfs/online/storage/blog_attachments/2023/03/1-Scenario-1-final-scehdule-line-.jpg)

Figure 1: RACR view of Case 1

![](/legacyfs/online/storage/blog_attachments/2023/03/2-Schedule-line-SO-item-level.jpg)

Figure 2: Schedule line confirmation of Case 1

![](/legacyfs/online/storage/blog_attachments/2023/03/3-8.jpg)

Figure 3: Detailed view of confirmation

Business Case 2: Customer places order of 200 quantity in same 1710 plant. Now as per the above case, the system gets confirmation of a partial 100 quantity from the US20 plant. For the next 100 quantities, the system will go to Germany (1010) plant where stock is available for customers. With the combined capabilities of BPS and ABC, the system generates new schedule line dates and times for both selections of stock. Even while proposing a newly confirmed schedule line from the German plant, the system will honor the respective plant’s activity timing (shipping, loading, issuing time, etc)  and the holiday calendar of that plant's country too.

![](/legacyfs/online/storage/blog_attachments/2023/03/4-7.jpg)

Figure 4: RACR view of Case 2

![](/legacyfs/online/storage/blog_attachments/2023/03/5-5.jpg)

Figure 5: Schedule line view of Case 2

![](/legacyfs/online/storage/blog_attachments/2023/03/6-5.jpg)

Figure 6: Detailed view of Germany plant confirmation

Let’s have a quick check on the configuration part of it :

Configuring Schema: The main objective of BPS is to enhance precision while scheduling and provide flexibility. It helps to decouple business documents from concrete scheduling. Initially, you need to configure the scheduling schema as per your...