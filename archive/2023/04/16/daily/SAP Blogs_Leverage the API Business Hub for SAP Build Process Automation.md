---
title: Leverage the API Business Hub for SAP Build Process Automation
url: https://blogs.sap.com/2023/04/15/leverage-the-api-business-hub-for-sap-build-process-automation/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:30.460866
---

# Leverage the API Business Hub for SAP Build Process Automation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Leverage the API Business Hub for SAP Build Proces...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159060&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Leverage the API Business Hub for SAP Build Process Automation](/t5/technology-blog-posts-by-sap/leverage-the-api-business-hub-for-sap-build-process-automation/ba-p/13553468)

![Manuel_Namyslo](https://avatars.profile.sap.com/6/4/id64b93c0a8d79faa663a13b18709e5ce5fceaae61502c9763a1fceab63c1054fc_small.jpeg "Manuel_Namyslo")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Manuel\_Namyslo](https://community.sap.com/t5/user/viewprofilepage/user-id/97167)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159060)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159060)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553468)

‎2023 Apr 15
4:11 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159060/tab/all-users "Click here to see who gave kudos to this post.")

3,672

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (7)

##

## **Intelligent Processes are Integrated Processes**

If you are already building advanced workflows in SAP Build Process Automation you are probably familiar with SAP Business Technology Platform and its comprehensive integration services. Those components a key for our Low-Code/No-Code portfolio to deliver truly integrated processes and automate in a more secure and standardized fashion. It can also be used as a complimentary tool next to SAP Build to re-use prebuilt integration content, establish central API Governance and to utilize more advanced technologies such as eventing or iPaaS solutions in the cloud.

In today’s blog I want to highlight why you should consider the API Business Hub and how this component can help you during process development.

More and more companies rely on modern interfaces, especially REST APIs, in order to build integrations or applications. The proliferation of REST APIs makes the documentation and testing of APIs absolutely necessary. This is where the API Business Hub comes into play as a central catalog of SAP and selected partner *APIs* for application developers to search, discover, test and consume these APIs to build extensions or integrations using SAP Business Technology Platform. The API Business Hub also comes with a sandbox environment where you can test and review listed APIs. Logged-in users can experience this API without having an account or license for a specific API.

**Here are some advantages of using the sandbox environment:**

* Homogeneous API Sandbox approach for the consumer

* One API Key per user to test and experience the APIs in SAP API Business Hub

* SAP community user can test and experience APIs without an account/subscription.

* When user test an API with Sandbox, implicitly user’s API key is passed to authenticate/authorize user for API call.

Note: In API Business Hub, all sandbox APIs are protected by API Key which is generated per user.

This blog-post is ideal for process-developers that want to get a simplified backend-access which ought to be used for Proof-of-Concepts, Hackathons or testing purposes.

## **How to use the API Business Hub for integrated processes**

APIs across SAP solutions are heterogenous in terms of protocols, documentation and access mechanisms. Application and Integration Developers on SAP Build do not easily know the available APIs in various SAP systems (on-premise/cloud). This increases the total cost of Low-Code/No-Code development. Additionally, it is hard to easily test APIs and build quick prototypes as developers may spend quite some time to get access to systems/tenants.

Based on a use-case for purchase order management I want to show you how to leverage the API Business Hub inside SAP Build Process Automation. The goal of this scenario is to generate a purchase order approval workflow to change the purchasing organization of a purchase order that is documented inside SAP S/4 HANA. It is very critical to retrieve PO-related information directly from S/4 HANA and therefore we will utilize BTP Destinations and [Actions-Projects](https://help.sap.com/docs/build-process-automation/sap-build-process-automation/create-actions-project?locale=en-US&q=actions) in SAP Build Process Automation. Please keep in mind that it is a very simplified scenario to keep it as generic as possible. The same procedure can also be used for other backend systems as well.

First you need to login to the [API Business Hub](https://api.sap.com/). If you don’t already have a user you need to create one to access the sandbox environment and to retrieve the API key which is protecting the connection in a very simplified way. Inside the API Business Hub you can basically select any Rest-API that would be relevant for your scenario, but you need to make sure that the API also comes with a sandbox. I recommend using APIs from S/4 HANA Cloud because they are very well documented and have a sandbox system attached to it. In my example I went for the purchase order API to retrieve PO-related data based on the given purchase order ID. By clicking on the *Try Out* button you are automatically being forwarded to the sandbox environment where you can start ...