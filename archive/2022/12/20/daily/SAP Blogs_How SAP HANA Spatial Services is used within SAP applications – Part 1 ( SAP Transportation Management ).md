---
title: How SAP HANA Spatial Services is used within SAP applications – Part 1 ( SAP Transportation Management )
url: https://blogs.sap.com/2022/12/19/how-sap-hana-spatial-services-is-used-within-sap-applications-part-1-sap-transportation-management/
source: SAP Blogs
date: 2022-12-20
fetch_date: 2025-10-04T01:58:49.240398
---

# How SAP HANA Spatial Services is used within SAP applications – Part 1 ( SAP Transportation Management )

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* How SAP HANA Spatial Services is used within SAP a...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5086&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How SAP HANA Spatial Services is used within SAP applications - Part 1 ( SAP Transportation Management )](/t5/supply-chain-management-blog-posts-by-sap/how-sap-hana-spatial-services-is-used-within-sap-applications-part-1-sap/ba-p/13567853)

![shabana](https://avatars.profile.sap.com/4/2/id421f002983dabe4cec08cb24e3f4fec8c161b401c75c3909760056cb38973b1c_small.jpeg "shabana")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shabana](https://community.sap.com/t5/user/viewprofilepage/user-id/38259)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5086)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5086)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567853)

‎2022 Dec 19
5:55 PM

[9
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5086/tab/all-users "Click here to see who gave kudos to this post.")

3,575

* SAP Managed Tags
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

SAP HANA spatial services (HSS) provide a set of services running on SAP Business Technology Platform (SAP BTP). These services focus on providing simple access through a unified interface to geocoding, mapping, and routing functionalities integrated from third-party service providers. With SAP HANA spatial services, you can benefit from pre-configured integration scenarios. You are also able to run SAP HANA spatial services with third-party or custom applications.

In part 1 of this blog series, we will see how SAP HANA spatial services is used within SAP Transportation Management’s context which is an SAP application.

![](/legacyfs/online/storage/blog_attachments/2022/12/HSS_TM.png)

SAP HANA spatial services and integration with SAP application overview

SAP Transportation Management (SAP TM) is an SAP application that streamlines comprehensive processes for goods movement across various transportation modes, which helps improve operational efficiency and reduce costs. It helps you enhance service levels for businesses that need better logistics visibility, hence allowing them to gain reliability and on-time delivery. SAP TM helps you meet these needs by providing the ability to manage transportation demand, consolidate orders, monitor, and track shipments, and maximize the return on transportation spend.

Further we will now briefly look at how HSS is used within SAP TM and the value add of using them together.

![](/legacyfs/online/storage/blog_attachments/2022/12/HSS_TM_Map.png)

Overview - SAP Transportation Management and SAP HANA spatial services in use

SAP HANA spatial services aids SAP TM customers in improving transportation efficiency and visibility by adding the benefits of geographical services. HSS also helps leverage geographical services for efficient and effective decision-making in transportation businesses by

* Providing transparency on durations, distances, and costs.

* Making it easier for transportation planning to reduce costs and CO2 footprint, deliver on time and to maximize fleet utilization

* Providing visibility on real-time truck positions and planned routes to monitor transportation execution and to adapt the plan

Here is how the spatially powered SAP HANA Spatial Services solution is used by SAP TM customers

* TM users can increase the geographic visibility of their transportation systems by leveraging the HSS Mapping API to visualize the transport execution on maps (consuming mapping tiles from a third-party service provider).

* TM users can dynamically generate optimized routing proposals for orders based on business rules using the HSS Routing API that further avoids extra freight costs and thus delivers better customer service.

* Transportation routes can be efficiently calculated between multiple start and destination points using HSS Matrix Routing APIs. These start and destination point addresses are in turn into longitudinal and latitudinal values and can be viewed on a map via the HSS Geocoding API.

To sum up, below is how SAP TM users are benefitted by using HSS

* HSS helps in easier and better handling of SAP TM related data such as matrix routing and geocoding results.

* Since HSS is already integrated with SAP TM, customers benefit from having to spend less time and effort procuring their own services from independent service providers. Consequently, the development and maintenance of the integration will require less additional effort, which will lower the implementation's overall effort and expense.

* HSS allows flexible choice of contracted providers like HERE and Esri currently and many other 3rd party location service providers in the future (planned on the external [Roadmap](https://roadmaps.sap.com/board?range=CURRENT-LAST&PRODUCT=73555000100800001421#Q4%202022))

* HSS adapts transparent transaction-based billing via Cloud Platform Enterprise Agreement (CPEA, SAP Cloud Platform’s pay-per-use model) hence enabling customers to choose a billing model as per their requirements.

Get started today on how to do the initial setup for SAP HANA spatial services by following this [developer tutorial](https://developers.sap.com/tutorials/hana-spatial-services-apis.html) put together by my PM (Product Manager) colleague daniel.vanleeuwen . For in detailed explanation of HSS and the Rest APIs please refer to this [help portal document](https://help.sap.com/docs/SAP_HANA_SPATIAL_SERVICES/c7837a0d78e24fb5b9f66a058ab9f730/e6e58ffc01664cc1af1becfa76fdb5a6.html).

In the next blog, we will see how SAP HANA spatial services is used within SAP’s another application - SAP IBP (Integrated Business Planning).

**References**

* Learn more about [SAP Transportation Management](https://www.sap.com/products/scm/transportation-logistics.html)

* [Demo video](https://www.youtube.com/watch?v=CovUpcLWMUA) showing use of HSS within SAP TM application

* Refer to the next part of this blog series [here](https://blogs.sap.com/2023/01/11/how-sap-hana-spatial-services-is-used-within-sap-applications-part-2-sap-integrated-business-planning-for-supply-chain/)

Labels

* [Product Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/product%20updates)

* [SAP HANA spatial services](/t5/tag/SAP%20HANA%20spatial%20...