---
title: SAP BTP Service Applicability Assessment
url: https://blogs.sap.com/2022/10/24/sap-btp-service-applicability-assessment/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:28.725152
---

# SAP BTP Service Applicability Assessment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BTP Service Applicability Assessment

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159191&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP Service Applicability Assessment](/t5/technology-blog-posts-by-sap/sap-btp-service-applicability-assessment/ba-p/13554002)

![huijiezhang](https://avatars.profile.sap.com/3/9/id39babb8c67e0ffe9a3f499eef977b595378e964040145bef234df3e9c5d5f032_small.jpeg "huijiezhang")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[huijiezhang](https://community.sap.com/t5/user/viewprofilepage/user-id/7593)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159191)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159191)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554002)

‎2022 Oct 24
9:53 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159191/tab/all-users "Click here to see who gave kudos to this post.")

2,068

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [Cloud](https://community.sap.com/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud

  Topic](/t5/c-khhcw49343/Cloud/pd-p/431932400353955532628433796433200)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

Many SAP customers initially subscribe to SAP BTP for one or two services that they need for the projects in scope. As the discovery and design phases unveil, and also as more BTP services are rolled out onto the platform, customers may find out that more BTP services can be leveraged in their project implementations. This blog post illustrates some common criterions involved in assessing the applicability of a BTP service for customer’s adoptions.

**Where to find the service that I need**

While the SAP BTP introduction site (<https://www.sap.com/sea/products/technology-platform.html>) gives an overview of SAP BTP and its benefits to businesses, the site is too general for people who are looking for a BTP service that can help them to solve a technical or business problem. I found that the SAP Discovery Center (<https://discovery-center.cloud.sap/serviceCatalog?provider=all&regions=all>) is very helpful. On this site, you can search services in various ways and the returned results are normally very relevant.

Once the service is found, pay attention to the tag at the top of the card.

![](/legacyfs/online/storage/blog_attachments/2022/10/ServicesFound.png)

Services Found

If it indicates “RETIRING SOON”, it should not be positioned as part of your solution.

Service details can be found by clicking on the service card. On the overview page, the service document can be found on the Resources section:

![](/legacyfs/online/storage/blog_attachments/2022/10/Service-Document.png)

Link to Service Document

**Functionality Match**

Yes of course. The service has to have the features needed. In cases where integration to the service is required, the service has to have APIs or events for external systems to connect to.

All these details can be found in the service document mentioned in the previous section.

**On Premises, Self-Managed vs. SaaS**

Sometimes, a company has the option of installing a freeware or a cheaper solution that also fits its need and manage it by self. While this the short-term approach may reduce project cost temporarily, more companies are inclined to use the SaaS services in BTP. Security, maintenance, availability and scalability are all concerns with self-managed services and addressing which may end up with higher costs than using BTP services.

**Regional Availability**

Although an SAP BTP is available in multiple regions across the world, not all BTP services are available in all country’s regions. Due to each country’s legislations and the company’s contracts with its business partners, some may require that the BTP service be in the region that is inside the country. For example, some requires that any data that contains personal information must be stored and even processed within the country.

Thus when looking at the service at the Discovery Center afore mentioned, pay attention to the regional availabilities on the Pricing tab:

![](/legacyfs/online/storage/blog_attachments/2022/10/Service-Regions.png)

Service Available Regions

Regional Availability also affects your landscape creation and/or even your design. The service must be under a subaccount in its available region.  As very few things can be shared across subaccounts, if two services are needed and there happens to be no region that has both of these two services, then two subaccounts are to be created, and resource sharing or communication between the two subaccounts are to be considered.

**Performance**

This is where SaaS is superior to on premise. For all the services in SAP BTP, their performances do not vary by environment type. Typically we create different subaccounts for different types of environments, Development, QA or Production environments are just different subaccounts and the services perform the same under these different subaccounts.  Based on our experience, the services performances are typically steady with reasonable concurrencies. Well, that’s the nature of SaaS isn’t it.

**Security**

Security assessment is always part of the analysis when selecting a service to use. In this respect, SAP With SAP BTP services have the following characteristics:

* For the Featured services, users need to have access to the subaccount and granted the proper Role Collections

* All services are accessed via HTTPS TLS 1.2

* All APIs provided by the services are guarded by OAuth 2.0 at least

* All data persisted by the services are encrypted (Encryption at Rest)

* All services are guarded by the hyperscaler’s infrastructure’s security layer. For example, on AWS, services are guarded by AWS Shield.

* SAP Cloud Connector can be used to secure integration between SAP BTP services and applications or services outside of SAP BTP

Other aspects of the security compliances of the BTP services can be found at the SAP Trust Center: <https://www.sap.com/about/trust-center/certification-compliance.html>

A service's security is a shared responsibility among service user, SAP and the selected hyperscaler (AWS, AZure, GCP or Alibaba). Here is a very helpful blog post:

[https://blogs.sap.com/2021/09/15/rise-with-sap-shared-security-responsibility-for-sap-cloud-services...](https://blogs.sap.com/2021/09/15/rise-with-sap-shared-secu...