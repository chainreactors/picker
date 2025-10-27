---
title: SAP Integration Suite, advanced event mesh:  Using SAP SuccessFactors solutions as an Event Source
url: https://blogs.sap.com/2022/12/23/sap-integration-suite-advanced-event-mesh-using-sap-successfactors-solutions-as-an-event-source/
source: SAP Blogs
date: 2022-12-24
fetch_date: 2025-10-04T02:25:12.147595
---

# SAP Integration Suite, advanced event mesh:  Using SAP SuccessFactors solutions as an Event Source

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Integration Suite, advanced event mesh: Using...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160668&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Integration Suite, advanced event mesh: Using SAP SuccessFactors solutions as an Event Source](/t5/technology-blog-posts-by-sap/sap-integration-suite-advanced-event-mesh-using-sap-successfactors/ba-p/13558143)

![KStrothmann](https://avatars.profile.sap.com/f/a/idfabdcda21db6287c6f12ffae7e13fe5e0ddfd236eab7fd9829b68cb07bbd18c6_small.jpeg "KStrothmann")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[KStrothmann](https://community.sap.com/t5/user/viewprofilepage/user-id/7039)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160668)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160668)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558143)

‎2022 Dec 23
6:20 PM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160668/tab/all-users "Click here to see who gave kudos to this post.")

8,162

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

SAP SuccessFactors solutions are cloud-based HCM software applications that support core HR and payroll, talent management, HR analytics and workforce planning, and employee experience management. SuccessFactors solutions are used by over 235+ million users in more than 200 countries and territories around the world.

![](/legacyfs/online/storage/blog_attachments/2022/12/SuccessFactors.png)

## SAP SuccessFactors Intelligent Services Events

SuccessFactors already comes with Intelligent Services events that allow to simplify HR workflows with the capabilities of these HTTP-based events. As a result, a number of SAP-built events are already available in SAP SuccessFactors that can be adjusted to specific use cases and needs and therefore used in event-driven business cases around SuccessFactors.

Intelligent Services Events include for example:

* Employee Hire - a new worker is created with a specified start date

* Change in Manager - published after a job information change for an employee that has been assigned to a new manager

* Change in Employee Location - a worker has moved to a new location

A list of all available Intelligent Services Events can be found in the SAP SuccessFactors solutions documentation [here](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/e85fac4e6a3b4884b6451d4208cdb778/e7382856e8704b2f9bb288f90fe77b1f.html).

## SAP Event Mesh as an event broker for SuccessFactors

A few years ago my colleague Sai Harish Balantrapu has written an excellent blog on using SAP Event Mesh as an event broker for SuccessFactors. You can find this blog [here](https://blogs.sap.com/2019/01/17/sap-cloud-platform-enterprise-messaging-as-an-eventbus-for-successfactors/).

We will take the approach this blog has described and adjust it for usage with our new offering SAP Integration Suite, advanced event mesh. In the end the approach remains the same, with just a few adjustments that are needed.

A lot of ground we are covering here has been described in the original blog. I was wondering whether it would make sense to just describe the differences, in the end decided to give you the full picture here to make it as easy as possible to follow.

Again, Kudos to Sai Harish for all the groundwork!

## SAP Integration Suite, advanced Event Mesh

SAP Integration Suite, advanced event mesh is a fully managed event streaming and management service that enables enterprise-wide and enterprise-grade event-driven architecture. Advanced Event Mesh is a distributed mesh of event brokers that can be deployed across environments, both in the cloud and on-premise It offers a full purpose set of eventing services covering all relevant use cases AEM supports event streaming, event management and event monitoring Brokers fully scale as required and come in T-shirt sizes to perfectly fit different needs

![](/legacyfs/online/storage/blog_attachments/2022/12/AEM.png)

## High Level Overview of our Approach

On the SuccessFactors side we will create an integration in the Integration Center. The destination for this integration is going to be REST and we will choose JSON format for the event. We will add selected fields to the event. Then we will have to create the destination settings. We will use basic authentication and REST. The information for the destination we will have to look up in Advanced Event Mesh, so keep it open in parallel.

![](/legacyfs/online/storage/blog_attachments/2022/12/SF29-1.png)

There is a very important step that we, most likely and depending on your individual settings, have to take before: we have to change the ports we use. The standard settings for SAP SuccessFactors ports don't fit the standard settings for Advanced Event Mesh ports. So either we have to open up our AEM standard ports in SuccessFactors, or we can just adjust the ports on the Advanced Event Mesh side. Here we will just adjust the AEM port settings since this is very straightforward.

## Preparation on the Advanced Event Mesh side

Go to the **Cluster Manager** and select your Event Broker

Click on **Manage**

Click on **Advanced Options**

![](/legacyfs/online/storage/blog_attachments/2022/12/AEM1.png)

Scroll down to **Port Configuration**

Expand **Public Endpoint**

![](/legacyfs/online/storage/blog_attachments/2022/12/AEM2-1.png)

Check on the value for **Secured REST Host**. AEM standard settings here would be 9443 which is typically blocked by SAP SuccessFactors. By standard the **Secured Web Messaging Host** is set to port 443 in AEM.

If you would like to adju...