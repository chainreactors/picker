---
title: Forecast Consumption for TS Supply Planning
url: https://blogs.sap.com/2023/04/01/forecast-consumption-for-ts-supply-planning/
source: SAP Blogs
date: 2023-04-02
fetch_date: 2025-10-04T11:26:49.372517
---

# Forecast Consumption for TS Supply Planning

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Forecast Consumption for TS Supply Planning

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4885&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Forecast Consumption for TS Supply Planning](/t5/supply-chain-management-blog-posts-by-members/forecast-consumption-for-ts-supply-planning/ba-p/13566439)

![kunalroy](https://avatars.profile.sap.com/d/9/idd9b4e35ee22ca8071ac7b33fda5fbf8efe652d43612216431b3dd8fe09c9c35c_small.jpeg "kunalroy")

[kunalroy](https://community.sap.com/t5/user/viewprofilepage/user-id/42239)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4885)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4885)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566439)

‎2023 Apr 01
9:13 AM

[7
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4885/tab/all-users "Click here to see who gave kudos to this post.")

3,974

* SAP Managed Tags
* [SAP Integrated Business Planning for demand](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520demand/pd-p/ef3d81c2-849e-4189-8aca-d26b9f4aa268)
* [SAP Integrated Business Planning for response and supply](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520response%2520and%2520supply/pd-p/ad3b7f3b-110d-4d49-9b0a-6ca8b89b1b04)
* [SAP Integrated Business Planning for sales and operations](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520sales%2520and%2520operations/pd-p/ff8b7b2c-f548-4d7c-bd78-eba4d1920785)
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)

* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Integrated Business Planning for demand

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bdemand/pd-p/ef3d81c2-849e-4189-8aca-d26b9f4aa268)
* [SAP Integrated Business Planning for response and supply

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bresponse%2Band%2Bsupply/pd-p/ad3b7f3b-110d-4d49-9b0a-6ca8b89b1b04)
* [SAP Integrated Business Planning for sales and operations

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bsales%2Band%2Boperations/pd-p/ff8b7b2c-f548-4d7c-bd78-eba4d1920785)

View products (4)

The theory of forecast consumption is explained [here](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/aa57378f6f184e7191f31a6afa62dc90.html). In this blog, I wanted to share examples to show the effect of configuration parameters through different scenarios. This blog only focuses on Forecast Consumption for TS Supply Planning. Forecast Consumption for Order Based Planning would be shared in a separate post. While most of the forecast consumption scenarios are easy to understand, the scenarios related to Forecast consumption direction- ***Backward from boundary end*** & ***Forward from boundary start*** could be confusing. I have attempted to explain those scenarios with a few examples as well.

## **Given:**

1. 8 Materials- FERT1 to FERT7.

2. 1 Location- LOC1

3. Forecast Consumption modes- 7 modes with different settings as shown below (Fig01).

4. Assignment of the modes to the Location Products in Location Product Master- FERT1 to 101, FERT2 to 102 and so on). Refer Fig02.

5. Here are the 4 key figures used in forecast consumption profile (I have copied & pasted their definitions from SAP [help](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/6b6f48f2887e4a358242b6a7352441a5.html))

   * **Input Forecast**: This key figure represents the forecast that is available for consumption by the incoming sales orders.

   * **Input Sales Order**: This key figure represents the sales order quantities that consume the input forecast.

   * **Output Open Forecast**: This key figure is filled by the forecast consumption algorithm and represents the open forecast. It is calculated by deducting the consumed forecast from the input forecast.

   * **Output Total Demand**: This key figure is filled by the forecast consumption algorithm and represents the total demand. It is calculated by adding the input sales order to the output open forecast.

6. Other settings in forecast consumption Profile settings (See Fig03):

   * Forecast Consumption Level: Location ID- Product ID

   * Time Boundary Level: **Quarter (this is the time boundary within which you want the forecast to be consumed).** It is only activated if the Boundary ID attribute in Forecast Consumption Model Master data has values other than **0** or **null**.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig-01.png)

Fig01: Forecast Consumption Mode Master Data settings.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig-02-1.png)

Fig02: Location Product Master Data Settings.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig03-1.png)

Fig03: Forecast Consumption Profile settings.

## **Scenarios**:

Please note that for all the 7 scenarios, I have considered data in monthly buckets for a 1-year horizon- Jan-23 to Dec-23. The “Input forecast" is 100 in every month and the "Input sales order" is 600 and 400 in the months of Mar-23 & Dec-23 respectively. There is no data in any other time buckets.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig04.png)

Fig04: Job template settings

### ***Scenario01:***

* Forecast Consumption Mode settings (as shown in figure 01)

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig05.png)

Fig05: Forecast consumption mode- Scenario 01

* Output for Forecast Consumption Run:

* + 600 first consumes 100 in the Mar bucket, then consumes 3 buckets forward and 2 buckets backward.

  + 400 first consumes 100 in Dec bucket, then consumes 3 months backward (as there is nothing to consume forward).

  + Boundary =0 means there is no boundary restriction and hence the “quarterly” boundary set in the forecast consumption profile is not applicable here.

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig06.png)

Fig06: Output- Scenario 01

### ***Scenario02:***

* Forecast Consumption Model Settings:

![](/legacyfs/online/storage/blog_attachments/2023/04/Fig07.png)

Fig07: Forecast consumption mode- Scenario 02

* Output for Forecast Consumption Run:

  + 600 first consumes 100 in the Mar bucket. Since there is a boundary restriction, it cannot consume anything outside of its current boundary (which is Quarter 1 - Jan to Mar).

  + 400 first consumes 100 in the Dec bucket. Since there is a boundary restriction, it cannot consume anything outside of its current boundary (which is Q4 -Oct to Dec).

  + Boundary =1 means the forecast consumption is limited ...