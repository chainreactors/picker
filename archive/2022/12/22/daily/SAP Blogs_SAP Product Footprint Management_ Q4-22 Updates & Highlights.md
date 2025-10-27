---
title: SAP Product Footprint Management: Q4-22 Updates & Highlights
url: https://blogs.sap.com/2022/12/21/sap-product-footprint-management-q4-22-updates-highlights/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:15.587886
---

# SAP Product Footprint Management: Q4-22 Updates & Highlights

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Product Footprint Management: Q4-22 Updates & ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158117&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Product Footprint Management: Q4-22 Updates & Highlights](/t5/technology-blog-posts-by-sap/sap-product-footprint-management-q4-22-updates-highlights/ba-p/13551093)

![NicoWottke](https://avatars.profile.sap.com/c/2/idc26d5127ded5e5c3d5613d483ccd89ff129def4dee279595e8e5643bece1ec4d_small.jpeg "NicoWottke")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[NicoWottke](https://community.sap.com/t5/user/viewprofilepage/user-id/123570)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158117)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158117)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551093)

‎2022 Dec 21
2:47 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158117/tab/all-users "Click here to see who gave kudos to this post.")

5,588

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Sustainability](https://community.sap.com/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Sustainability

  Topic](/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

To wrap up the year 2022, I prepared another blog post to highlight the major new features and functions in SAP Product Footprint Management this quarter, and to also look back on our achievements in the past year. In this edition I will cover:

* [Product Updates](#Product-Updates) (Transport Footprints, Manage Data App, Calculation Details)

* [Recap: Looking back on 2022](#Recap-2022)

* [Outlook: Looking forward to 2023](#Outlook-2023)

* [Free SAP Learning Journey](#Learning-Journey)

* [Additional Information & Updates](#Additional-Information&Updates)

## **Product Updates**

The biggest product update and highlight that we added into SAP Product Footprint Management in this quarter was the calculation of **Freight Transport Footprints**, providing value chain emissions related to GHG Protocol Scope 3.4 (upstream transportation) and Scope 3.9 (downstream transportation), as well as Scope 1 (Direct emissions related to company-owned vehicles). The Freight Transportation capabilities are integrated into SAP Product Footprint Management as additional stand-alone apps for calculating the transport emissions for all your inbound and outbound transports. The apps are delivered with preconfigured content, including network data like seaports, airports, rail barge terminals, as well vehicle data and emissions factors from the Global Logistics Emission Council (GLEC). Additionally, built-in analytics options enable visualizations of the calculated transports according to own-defined KPIs and provide insights on the resulting footprints of the vehicles and routes used. In the next days, we further plan to release visualizations on maps, showing all transport routes on a world map. For an overview on the new apps and deep dive into their features and benefits, have a look into my previous blog post [Calculating Transport Footprints with SAP Product Footprint Management](https://blogs.sap.com/2022/11/04/calculating-transport-footprints-with-sap-product-footprint-management/).

![](/legacyfs/online/storage/blog_attachments/2022/12/ViewTransportData.png)

View Transport Data App

One of the new applications that was introduced together with the Freight Transport capabilities is the **Manage Data App**. This app doesn't only enable you to view and configure transport-related data but also displays data that was replicated from the connected SAP ERP source system for calculating the footprints for purchased and manufactured products.

![](/legacyfs/online/storage/blog_attachments/2022/12/ManageDataApp.png)

Manage Data App

The entities that can be viewed include master data (such as plants and products), transactional data (such as physical goods movement and actual inventory), as well as cost estimate entities data. This functionality provides you additional transparency on the system data that is used for the footprint calculation, a further drill-down into its characteristics and date of its last import is possible as well. In the next weeks, we also plan to enable the upload of flat files directly into this app. This will complement the existing integration with SAP S/4HANA and Push APIs and will provide much more possibilities for leveraging business data for calculating footprints.

![](/legacyfs/online/storage/blog_attachments/2022/12/CostEstimates.png)

Manage Data App - Cost Estimates

To further enhance the usability of our solution we **improved and simplified the calculation details** section in the Monitor Footprints application. This section, visible when drilling down from the footprint results page, now combines and shows the inflows and outflows from/ to all sources/ targets as well as the previous inventory and current inventory in a single table. This change not only improves the user interface but further illustrates and clarifies how the overall footprint results are calculated and which data points were used.

![](/legacyfs/online/storage/blog_attachments/2022/12/CalculationDetails.png)

Monitor Footprints App - Footprint Calculation Details

## **Recap: Looking Back on 2022**

As we're wrapping up the year, I would like to use this opportunity to look back and reflect on where we are today with SAP Product Footprint Management and reflect on what we all achieved in 2022. For doing so, let me once again pull up our famous metro line picture, illustrating the product’s capabilities along the footprint journey:

![](/legacyfs/online/storage/blog_attachments/2022/12/PFM_Capabilities.png)

SAP Product Footprint Management – Capabilities as of Dec-22 (Labs Preview – Subject to Change)

When it comes to **Data Acquisition**, one of SAP Product Footprint Management’s key benefits is leveraging master data and transactional data that is existing already in SAP’s business systems. Since the product launch, we're providing an out-of-the box integration with SAP ...