---
title: Extensibility in the Development System of a 3-System Landscape
url: https://blogs.sap.com/2022/12/07/extensibility-in-the-development-system-of-a-3-system-landscape/
source: SAP Blogs
date: 2022-12-08
fetch_date: 2025-10-04T00:53:01.322033
---

# Extensibility in the Development System of a 3-System Landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Extensibility in the Development System of a 3-Sys...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53382&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extensibility in the Development System of a 3-System Landscape](/t5/enterprise-resource-planning-blog-posts-by-sap/extensibility-in-the-development-system-of-a-3-system-landscape/ba-p/13570453)

![Tayane](https://avatars.profile.sap.com/4/d/id4d2d58bc40b1d37b5ee1cb7b23f537eb72d39ac3b3946114f66c9b4b52cf47de_small.jpeg "Tayane")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Tayane](https://community.sap.com/t5/user/viewprofilepage/user-id/143549)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53382)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53382)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570453)

‎2022 Dec 07
6:50 PM

[12
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53382/tab/all-users "Click here to see who gave kudos to this post.")

5,369

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Extensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition Extensibility

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BExtensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

Hello Community!

In this blog post, I want to talk about Extensibility in 3-System Landscapes in a simplified way, so that you understand what each tenant is for and how to use it correctly for each feature.

Depending on your installation, your SAP S/4HANA Cloud system is based on a 2-System Landscape or on a 3-System Landscape.

It is very likely that you are already familiar with 2-System Landscape. It's based on a Quality and Production System.
The Quality System combines development, configuration and testing activities. In this system you can configure your content and create low-code custom developments using Key User Extensibility.
On the other hand, the Production System is where you'll transport the items from Quality System and where you'll work productively.

In 3-System Landscape, the configuration is a bit different. It consists of a Development System, Test System and Production System. The Development System is divided into two different tenants with specific purposes: The Customizing Tenant and the Development Tenant.
The development tenant and customizing tenant are technically clients in the development system.

It is quite common to get confused with both tenants, but each one has a specific function that I will show you below:

1. **Development Tenant**This tenant provides access to the SAP S/4HANA Cloud ABAP Environment. In this environment you can build your own custom developments based on lifecycle-stable SAP objects, this is called Developer Extensibilty.
   The Developer Extensibility is available only in a 3-System Landscape and includes: ABAP RESTful Application Programming model (RAP), Eclipse based IDE with debugger, troubleshooting and testing tool support and ABAP software lifecycle support.
   To get started as a Developer in ABAP Environment, you need to have the Business Role SAP\_BR\_DEVELOPER assigned to your user without restrictions. Please, check [SAP Help Portal | Getting Started as a Developer in the ABAP Environment](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6aa39f1ac05441e5a23f484f31e477e7/e3527dfa1c5a41f69d4e63691f174f0a.html?locale=en-US) for more information.

   *\*If the Business Role Template SAP\_BR\_DEVELOPER is not available in your system, it's because you didn't completed the steps for initial admin user in Development System and your CBC system is still in "Ready for initial deploy" status. Please, follow the documentation [SAP Help Portal | Development System - Steps for the Initial Admin User](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e8dd54fa4764420a3ea36934a4e025b.html?locale=en-US) and complete the prerequisites in your SAP S/4HANA Cloud Development System.*

   \*\*Development objects are called client-independent and are accessible in all clients. Hence, when you, as a developer, create development objects in the development tenant, these objects are available in the customizing tenant as well. For instance, when you create a new SAP Fiori app and assign this app to a business catalog in the development tenant, the app is also accessible in the customizing tenant.
2. **Customizing Tenant**This tenant allows you to configure your activities based on the reference content from SAP Central Business Configuration and to create low-code custom developments in Key User applications, this is called Key User Extensibility.
   The Key User Extensibility is based on applications and features that help you customize applications and their UIs, reports, email templates, and form templates. Using extensibility apps, you can create custom fields, data source extensions, and implementation descriptions for specific business contexts to enhance predelivered applications that are extensible in order to adapt them to your business needs. You can also create custom CDS views based on predelivered data sources. You can create custom business objects with UIs. You can also add custom logic to custom business objects. You can thus create your own applications based on custom business objects. You can use Custom Analytical Queries to create new queries or reuse predefined queries. You use fields from CDS views to create a query.

   To get started with Key User Extensibility, you first need to activate it in your system by following the steps below:
   1. Go to "Extensibility Settings" app
   2. Click on the swap button for "Key User Extensibility" to set it to "ON"

   \**Master data is called client-dependent and is only accessible in the respective client. Hence, when you, as an administrator, create a business role to a business user in the customizing tenant, this is only visible in the customizing tenant.

   \*\*That is only true for Partner Demo / Starter systems. In regular development systems, extensibility is on by default.*

You can check the following table to compare the Extensibility options that we discussed about:![](/legacyfs/online/storage/blog_attachments/2022/12/Extensibility.png)For more information, please check [SAP Help Portal | Extensibility](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/53...