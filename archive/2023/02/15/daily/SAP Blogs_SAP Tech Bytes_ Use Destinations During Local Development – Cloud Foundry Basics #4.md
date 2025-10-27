---
title: SAP Tech Bytes: Use Destinations During Local Development – Cloud Foundry Basics #4
url: https://blogs.sap.com/2023/02/14/sap-tech-bytes-using-destinations-during-local-development-cloud-foundry-basics-4/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:37:22.674846
---

# SAP Tech Bytes: Use Destinations During Local Development – Cloud Foundry Basics #4

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Tech Bytes: Use Destinations During Local Deve...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/156939&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Tech Bytes: Use Destinations During Local Development - Cloud Foundry Basics #4](/t5/technology-blog-posts-by-sap/sap-tech-bytes-use-destinations-during-local-development-cloud-foundry/ba-p/13547863)

![nicoschoenteich](https://avatars.profile.sap.com/9/e/id9e344f0b44ebe008feb7d8f8fc61286cdabf9680afdc05e70d6e2d9fe7fb7822_small.jpeg "nicoschoenteich")

![Developer Advocate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Developer Advocate")
[nicoschoenteich](https://community.sap.com/t5/user/viewprofilepage/user-id/898)

Developer Advocate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=156939)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/156939)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13547863)

‎2023 Feb 14
5:03 PM

[26
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/156939/tab/all-users "Click here to see who gave kudos to this post.")

8,135

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (6)

*This SAP Tech Byte is about how to consume SAP BTP destinations during local development - covering both instance level and subaccount level destinations.*

**The source code for this blog post can be found at <https://github.com/SAP-samples/sap-tech-bytes/tree/cloud-foundry-basics/post4>.**

Building on top of the [previous blog post](https://blogs.sap.com/2022/08/03/sap-tech-bytes-consume-data-using-destinations-with-an-approuter-cloud-foundry-basics-3/) of this "Cloud Foundry Basics" series, where we learned how to consume data using destinations, we will learn how to use destinations during local development today. Imagine a scenario where you want to use real backend data to test and build your application using an existing SAP BTP (Cloud Foundry) destination, instead of mocking it all locally. This blog post will cover two variations of this scenarios:

1. In the first scenario we are using the standalone approuter we already created in the previous blog post alongside an **instance level destination.**

2. For the second scenario we are using the [SAP Fiori Tools - UI5 Tooling](https://www.npmjs.com/package/%40sap/ux-ui5-tooling) and the SAP Business Application Studio to consume a **subaccount level destination** locally.

The fundamental difference between those scenarios are the different types of destinations used. So before we get started, we need to make sure we have a good understanding of the difference between instance level and subaccount level destinations on SAP BTP.

Check out this [blog post](https://blogs.sap.com/2018/10/08/using-the-destination-service-in-the-cloud-foundry-environment/) for a general introduction to the Destination Service on SAP BTP, Cloud Foundry environment.

# Instance Level vs. Subaccount Level Destinations

In this blog post series so far we have created and consumed an instance level destination, meaning we created an instance of the Destination Service that lives in a Cloud Foundry space:

Such a destination instance can be bound to specific standalone applications ("application binding"), for example an approuter, making it possible to call the destination from within the application (see binding information in the screen shot above). In contrast to that, subaccount level destinations are created, as the name implies, on subaccount level and therefore don't live in a Cloud Foundry space:

Such a subaccount level destination cannot be bound to specific standalone applications (that do live in a Cloud Foundry space). Consumption of a subaccount level destination therefore differs and requires different tooling. More on that further down below.

# Consuming Instance Level Destinations Locally

For this first scenario we are using the standalone approuter we already created and deployed in the [previous blog posts](https://blogs.sap.com/2022/08/03/sap-tech-bytes-consume-data-using-destinations-with-an-approuter-cloud-foundry-basics-3/). When running in the cloud, we can see that the approuter is serving the backend data through the destination (via **/backend**![:disappointed_face:](/html/@51317F7935B06825B21C40F70A87A8E5/emoticons/1f61e.png ":disappointed_face:")

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture-19-1.png)

The approuter was bound to our instance level destination during deployment as we configured the "services" attribute in the **manifest.yaml** file:

```
---

applications:

- name: my-web-page

  ...

  services:

  ...

  - backendDestination
```

But what if we want to work on our UI5 application locally and need the backend data for that? If where to simply start our approuter locally (via **npm start**) we get an "unknown destination" error:

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture-09.png)

The fix for this is pretty straightforward, as long as we have previously deployed an app that is bound to the destination we want to call. We simply have to copy the environment variables from the deployed approuter into our local environment. Another option would be to create a service key and use its credentials. The local approuter can then connect to the destination in Cloud Foundry. The local environment variables can be set via a **default-env.json** file at root level of the approuter project. We can get the environment variables for our application via the SAP BTP cockpit (or alternatively via the **cf env m...