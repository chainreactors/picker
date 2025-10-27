---
title: Extending SAP Business Network for Logistics to estimate Green House Gas Emissions
url: https://blogs.sap.com/2023/05/06/extending-sap-business-network-for-logistics-to-estimate-green-house-gas-emissions/
source: SAP Blogs
date: 2023-05-07
fetch_date: 2025-10-04T11:38:01.806138
---

# Extending SAP Business Network for Logistics to estimate Green House Gas Emissions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Extending SAP Business Network for Logistics to es...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4745&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extending SAP Business Network for Logistics to estimate Green House Gas Emissions](/t5/supply-chain-management-blog-posts-by-sap/extending-sap-business-network-for-logistics-to-estimate-green-house-gas/ba-p/13548263)

![harsh_satsangi](https://avatars.profile.sap.com/e/0/ide0eaa7a5b03e9b9c7bb10ea0c09e94fbeda24b9f7a9f40e65ea9aa763c163bd2_small.jpeg "harsh_satsangi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[harsh\_satsangi](https://community.sap.com/t5/user/viewprofilepage/user-id/194356)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4745)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4745)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548263)

‎2023 May 06
10:30 PM

[7
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4745/tab/all-users "Click here to see who gave kudos to this post.")

1,296

* SAP Managed Tags
* [SAP Business Network for Logistics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Logistics/pd-p/73554900100800001025)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Network for Logistics

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BLogistics/pd-p/73554900100800001025)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

Climate change is the greatest challenge of our time, with rising temperatures and ecosystem degradation threatening life on Earth as we know it. We need a global, collaborative and inclusive approach to action on climate and nature in order to help restore our planet and protect our future. Several studies have indicated that Green House Gas emission is one of the leading causes of Climate change. The report below from a Government Agency is the US corroborates the facts that roughly 40% of Energy related emissions of CO2 comes from the transportation sector.

![](/legacyfs/online/storage/blog_attachments/2023/05/1-20.png)

Transportation related Green House Gas emission

Source: [https://www.cbo.gov/publication/58861#:~:text=Transportation%20is%20the%20largest%20source,greenhous...](https://www.cbo.gov/publication/58861#:~:text=Transportation%20is%20the%20largest%20source,greenhouse%20gas%20emissions%20from%20transportation).

SAP Business Network powers transparency, resiliency, and sustainability by Connecting people, processes, and systems across multiple enterprises to digitize transactions and create transparent, resilient, and sustainable supply chains.

SAP has the largest and most comprehensive business network, trusted by millions of companies around the world. With the power of SAP Business Network organization can drive  sustainability, Strive for zero waste by incorporating resilience and circularity in your supply chain and Access to diverse partners can expand your supply base and help you act with carbon efficiency in mind, so people can trust in your sustainable practices.

SAP Business Network for Logistics provides Collaboration between the shippers and carriers to optimize logistics processes, increase on-time deliveries, and mitigate supply risk. This includes Streamline freight collaboration,  Connect with logistics service providers, Gain insight into goods in transit & Track shipments enriched by data with Evaluate the impact of deviations. With the power of SAP Business Network for Logistics - Global Track and Trace companies achieve insight to action for order fulfillment and goods in transit by connecting physical movement with information flow improves situational awareness beyond milestone reporting, enabling exception detection, revealing actionable insights, and breaking down company silos.

With the Power of SAP Business technology Platform SAP customers are able to extend SAP Business Networks to introduce new and innovative capabilities through SAP's partner ecosystem.

One such capability recently introduced by our partner - Nihilent is iMission (<https://store.sap.com/dcp/en/product/display-0000061317_live_v1>). iMission estimates overall GHG emissions on shipments & freight orders and integrated with SAP Business Network for Logistics.

On the screenshot below you can see a typical Shipment document which originates in our customers SAP S/4HANA Logistics or Transportation Management system. The shipment or the freight document already contains critical information about the transportation like the Weight, Volume, distance , route as well as the mode of transportation. Using these critical data elements iMission is able to estimate the emissions for this shipment.

For example if we have a road freight order containing several orders going from the port of Hamburg to a plant in the south of Germany, the iMission application captures this information from an Open API from SAP BN4L and calculates the GHG emission which is then returned to the network and shown directly on the Shipment document.

The Logistics manager can directly access the GHG emissions on SAP BUsiness Network for Logistics against each freight document.

![](/legacyfs/online/storage/blog_attachments/2023/05/2-8.png)

Shipment / Freight Order on SAP Business Network

![](/legacyfs/online/storage/blog_attachments/2023/05/3-12.png)

Emission Calculation on Shipment / Freight Order

In addition to this iMission also provides a Dashboard to provide a consolidated view of GHG emissions across the different modes of transportation , across the carrier base and shipment lanes.

![](/legacyfs/online/storage/blog_attachments/2023/05/4-7.png)

SAP Analytics Cloud Dashboard : Aggregate Emissions reporting

**I**f you are interested to know more about SAP Business Network for Logistics and how it can help you optimize your logistics and achieve sustainability goals, do not hesitate to reach out to your SAP Account representatives.

Labels

* [Technology Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/technology%20updates)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-sap%2Fextending-sap-business-network-for-logistics-to-estimate-green-house-gas%2Fba-p%2F13548263%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Material & Quality ...