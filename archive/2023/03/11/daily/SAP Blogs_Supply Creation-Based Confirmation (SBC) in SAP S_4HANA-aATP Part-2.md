---
title: Supply Creation-Based Confirmation (SBC) in SAP S/4HANA-aATP Part-2
url: https://blogs.sap.com/2023/03/10/supply-creation-based-confirmation-sbc-in-sap-s-4hana-aatp-part-2/
source: SAP Blogs
date: 2023-03-11
fetch_date: 2025-10-04T09:15:52.608602
---

# Supply Creation-Based Confirmation (SBC) in SAP S/4HANA-aATP Part-2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Supply Creation-Based Confirmation (SBC) in SAP S/...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52380&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Supply Creation-Based Confirmation (SBC) in SAP S/4HANA-aATP Part-2](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-creation-based-confirmation-sbc-in-sap-s-4hana-aatp-part-2/ba-p/13563499)

![Vasubharadwaj](https://avatars.profile.sap.com/7/7/id77b841123e0d05e8469fa48ad051ee80e4ac6d32b92d07207f02f2d623825bed_small.jpeg "Vasubharadwaj")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Vasubharadwaj](https://community.sap.com/t5/user/viewprofilepage/user-id/121610)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52380)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52380)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563499)

‎2023 Mar 10
8:50 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52380/tab/all-users "Click here to see who gave kudos to this post.")

3,330

* SAP Managed Tags
* [SAP S/4HANA for advanced ATP](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520for%2520advanced%2520ATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)

* [SAP S/4HANA for advanced ATP

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bfor%2Badvanced%2BATP/pd-p/314fb51c-b3d3-4169-a015-fc9e9e510969)

View products (1)

In continuation to my previous blog [SBC-Introduction](https://blogs.sap.com/2023/01/31/supply-creation-based-confirmation-sbc-in-sap-s-4hana-aatp/) I would like to explain sample MTO scenario in SBC functionality .

Just to give you insight about the SBC scenario consider a Bike Manufacturing company in plant/001

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.1.png)

Figure1: SBC + PAL scenario to support the Business Requirement.

Mr. RAM is working in bike manufacturing company as a SCM consultant. which manufacture the BIKES based on customer specific requirements ( Engine characteristics / Bike Model….)

During the sales order creation process, he wants to provide the customer specific characteristics about finished product and also based upon the stock and planning situation, he has to provide the accurate & reliable order-promising dates **( generating the procurement proposals when the available quantity of requested sales order is insufficient )** . During this process Mr. Ram has to consider the sales & transportation capacities to protect the company business priorities & profitability goals. To support this business requirement he decided to work with aATP( PAL + SBC ) scenario. let’s see the following steps, how aATP will solve the Ram’s business requirement.

Below master data setup is maintained for the Finished product **CUSTOM\_BIKE** for more details about how to activate the  ATP check for (Supply Creation) kindly go through my previous blog [SBC Activation](https://blogs.sap.com/2023/01/31/supply-creation-based-confirmation-sbc-in-sap-s-4hana-aatp/)

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.2.png)

Figure2: Master Data details for CUSTOM\_BIKE Finished product

Before going through the scenario let’s quickly have look into how PAL will support this requirement .

**Product Allocations** provides the mechanism to restrict the confirmation of orders with certain order characteristics like e.g. dedicated customers or regions & variant configuration characteristics . This could prevent supply shortage situations caused by a single high volume order to consume significant stocks and thus leaving the other customers orders either down the line or unconfirmed

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.3.png)

Figure 3: Product Allocation Sequence

In below Figure 4 we can see that based on different PAL characteristics, the PAL sequence would restrict the Supply Creation process while considering the Sales & Capacity Allocation quota.

Before the Supply Creation process the Sales Allocation quota provides what we want to deliver in specified Bucket(Month/Week/Day ) based on PAL object configuration.

After Supply Creation process  the Capacity Allocation quota finally decides how much quantity going to be delivered for the requested delivery date and generating the delivery proposals.

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.4.png)

Figure:4 PAL characteristics & sequence with Incoming sales order

Let’s say on 28.02.2023 Mr. Ram got below requirement based on the following details, that he wants to provide the order promising dates while considering the companies business priorities and profitability goals.

**Requested Customer:** “ATP\_CUST01”

**Requested product:** “CUSTOM\_BIKEE” in **plant** 0001 with **quantity** 30 and with following custom configurations **Engine Type:** “Diesel engine **Engine ratio:**  1.6 engine rod ratio

**Requested date:** 28.02.2023.

Now lets see how the aATP(SBC+PAL) scenario process the above details based on below product allocation configuration.

Product Allocation Sequence --- which is having Sales Sequence group ( consumption- Backward-2 months & forward-5 months ) & Capacity Sequence group ( consumption- Backward-0 months & forward-5 months )

we can see the sales & capacity allocation object with Quota maintained in the month bucket based on Sales and transportation capacities

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.5.png)

Figure 5:Product Allocation Sequence master data details

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.6.png)

Figure 6: sales order details with customer and quantity details

Below we can see during the sales order creation process the system allowing user to enter the customer specific characteristics

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.7.png)

Figure 7: classic variant configuration screen for the requested sales order item during sales order creation process.

based on the given details the “Review Availability Check Results” RACR screen providing the confirmation quantities & proposal dates  as we can see in below Figure 8.

If we want to know the more details about how the above delivery proposals got generated we can navigate inside RACR screen requirement details .

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.8.png)

Figure 8 : RACR Screen with different delivery proposals

Below Figure 9 we can see the detailed flow of ATP check from requested delivery date & quantity to the output confirmation dates and quantities

Based on the requested delivery date 24.02.2023 & quantity 30 EA there are multiple checks (Sales PAL --> PAC/SC --> CapaPAL) that are processing the requested quantity for the sales order item for more details  kindly refer Figure 3 & Figure 9  .

![](/legacyfs/online/storage/blog_attachments/2023/03/FIG_2.10.png)

Figure 9: RACR Screen ATP Check intermediate results

below icons represents the different chec...