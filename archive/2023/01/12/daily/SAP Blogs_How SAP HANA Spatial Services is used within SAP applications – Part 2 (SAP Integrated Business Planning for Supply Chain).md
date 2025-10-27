---
title: How SAP HANA Spatial Services is used within SAP applications – Part 2 (SAP Integrated Business Planning for Supply Chain)
url: https://blogs.sap.com/2023/01/11/how-sap-hana-spatial-services-is-used-within-sap-applications-part-2-sap-integrated-business-planning-for-supply-chain/
source: SAP Blogs
date: 2023-01-12
fetch_date: 2025-10-04T03:39:19.267575
---

# How SAP HANA Spatial Services is used within SAP applications – Part 2 (SAP Integrated Business Planning for Supply Chain)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* How SAP HANA Spatial Services is used within SAP a...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4895&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How SAP HANA Spatial Services is used within SAP applications – Part 2 (SAP Integrated Business Planning for Supply Chain)](/t5/supply-chain-management-blog-posts-by-sap/how-sap-hana-spatial-services-is-used-within-sap-applications-part-2-sap/ba-p/13558180)

![shabana](https://avatars.profile.sap.com/4/2/id421f002983dabe4cec08cb24e3f4fec8c161b401c75c3909760056cb38973b1c_small.jpeg "shabana")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shabana](https://community.sap.com/t5/user/viewprofilepage/user-id/38259)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4895)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4895)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558180)

‎2023 Jan 11
9:00 PM

[6
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4895/tab/all-users "Click here to see who gave kudos to this post.")

1,259

* SAP Managed Tags
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

In this Part-2 of the SAP HANA spatial services (HSS) and its usage in SAP applications blog series, we will see how HSS is integrated and used with another SAP application – SAP Integrated Business Planning.

SAP Integrated Business Planning (SAP IBP) is a cloud-based solution and is powered by SAP HANA. It combines sales and operations planning (S&OP), forecasting and demand, response and supply, demand-driven replenishment, and inventory planning. It allows supply chain planning in real time and ensures business continuity in times of supply chain disruption. SAP IBP incorporates advanced machine learning algorithms for planning capabilities and provides tightly coordinated supply chain planning processes. It has native integration with SAP Supply Chain Control Tower and other solutions.

The integration scenario between SAP IBP and HSS is targeting customers of the IBP Cloud that would like to use the APIs offered by SAP HANA Spatial Services to render map tiles within the geographic visualizations of the IBP Control Tower Fiori Applications (ex. IBP Analytics, Dashboards, and Intelligent Visibility).

Let us now look at how this setup works.

**As prerequisites:**

1. The customer must own an IBP Cloud tenant.

2. The customer must have created a service instance of SAP HANA spatial services.

3. The customer must have generated a service key for their HSS service instance. Note: Once a customer has an HSS service key, they have access to all the APIs HSS offers.

4. The customer has generated the API Client ID, Client Secret and enabled access through the OAuth 2.0 Client credentials flow.

Note: For Steps 2 through step 4, refer to [this tutorial](https://developers.sap.com/tutorials/hana-spatial-services-apis.html) for detailed hands-on guidance.

Let us now consider that a business user (customer) would like to launch an IBP Control Tower Fiori application, and this application includes a geographic visualization (map view). The application will call the map configuration service to fetch the configuration of map providers maintained in the IBP system. Once the user has selected his choice of service provider, the IBP proxy service will fetch the map tile image through the HSS Mapping API. This result will be forwarded to the visualization control in the Fiori application. In case if the caching is turned on in the IBP tenant side, the image is directly fetched from the cache and no request is dispatched to the HSS Mapping API. After all this, the geographic visualization is rendered using the Geomap control from the visual business Fiori control library.

![](/legacyfs/online/storage/blog_attachments/2022/12/HSS_IBP-1.png)

Overview - SAP Integrated Business Planning for Supply Chain and SAP HANA spatial services in use

Here is a summary on how HSS is useful and beneficiary for SAP IBP (Supply Chain)

* Customers can add multiple instances of the same map provider, allowing them to view different variations of the same map.

* The HSS mapping API provides image tiles required for building a base map on the IBP’s Control Tower application offering end-to-end, real-time visibility across an organization’s entire network, including suppliers, manufacturers, and business partners.

* The customer has the liberty to choose from different service providers on the HSS side, like HERE (other 3rd party service providers for future integration are planned as well, please refer to the external [roadmap](https://roadmaps.sap.com/board?range=CURRENT-LAST&PRODUCT=73555000100800001421#Q4%202022)).

* The customer will be billed based on the [SAP BTP subscription model](https://discovery-center.cloud.sap/protected/index.html#/serviceCatalog/sap-hana-spatial-services?service_plan=lite&region=all&commercialModel=cloud&tab=service_plan) they choose, hence allowing them flexibility, lowering the TCO (Total Cost of Ownership) and providing a transparent and affordable billing process.

As next steps, understand in depth of how SAP HANA spatial services are integrated with Control Tower application in SAP Integrated Business Planning for Supply Chain by referring to this [help document](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/da797ae2bf6246d58abd417f24915d55/ba630fe4e1344fc1b08ad30f962066bc.html?state=production).

**References**

* Get in depth details on [HANA spatial services APIs](https://help.sap.com/docs/SAP_HANA_SPATIAL_SERVICES/c7837a0d78e24fb5b9f66a058ab9f730/e6e58ffc01664cc1af1becfa76fdb5a6.html)

* Learn more about [Intelligent Visibility](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/69b6fc590ae34727acd3b4c334f67757.html) under [SAP IBP for Supply Chain](https://www.sap.com/products/scm/integrated-business-planning.html)

* [Supply chain control towers: providing end-to-end visibility](https://www.sap.com/insights/supply-chain-control-tower.html)

Labels

* [Product Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/product%20updates)

* [SAP HANA spatial services](/t5/tag/SAP%20HANA%20spatial%20services/tg-p/board-id/scm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, registe...