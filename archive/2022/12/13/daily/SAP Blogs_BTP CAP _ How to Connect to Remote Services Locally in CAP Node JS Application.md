---
title: BTP CAP : How to Connect to Remote Services Locally in CAP Node JS Application
url: https://blogs.sap.com/2022/12/12/btp-cap-how-to-connect-to-remote-services-locally-in-cap-node-js-application/
source: SAP Blogs
date: 2022-12-13
fetch_date: 2025-10-04T01:18:05.755063
---

# BTP CAP : How to Connect to Remote Services Locally in CAP Node JS Application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* BTP CAP : How to Connect to Remote Services Locall...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157690&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BTP CAP : How to Connect to Remote Services Locally in CAP Application](/t5/technology-blog-posts-by-sap/btp-cap-how-to-connect-to-remote-services-locally-in-cap-application/ba-p/13550070)

![showkath_naseem](https://avatars.profile.sap.com/b/3/idb31430339dce394fae56e5099a002a181ef4cf21068545b19463517d3280ac9b_small.jpeg "showkath_naseem")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[showkath\_naseem](https://community.sap.com/t5/user/viewprofilepage/user-id/1529)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157690)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157690)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550070)

‎2022 Dec 12
6:35 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157690/tab/all-users "Click here to see who gave kudos to this post.")

17,674

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

# Introduction

In this blog post, we will learn How to Connect to Cloud Services From CAP Application Locally

Though our SAP [CAP Official Document](https://cap.cloud.sap/docs/advanced/hybrid-testing) is clearly explained [hybrid-testing](https://cap.cloud.sap/docs/advanced/hybrid-testing), I would like to illustrate with an use-case  “Connect to Northwind Cloud Service Locally in CAP Node JS Application using Function Import”

In General  Service can be from any external remote system or SAP System like S/4 HANA

For Example Business Partner OData service in SAP S/4HANA

Reference :  [Connect to Remote Services from Local](https://cap.cloud.sap/docs/guides/using-services?q=cds+bind#connect-to-remote-services-from-local)

I assume you already aware how to integrate any Remote Service on BTP

* If it is Cloud Service for example (S/4 HANA Cloud ) then you need to use BTP Destination service

* If it is On Premise System which requires VPN to connect to then you need to use BTP BTP Connectivity service & SAP Cloud Connector

Reference : [CAP BTP Connection - Destination](https://cap.cloud.sap/docs/guides/using-services?q=cds+bind#connect-and-deploy)

## **Target Audience**

Developers

## Prerequisites

I assume you already configured required services for CAP APP

[Destination](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/34010ace6ac84574a4ad02f5055d3597.html?locale=en-US)

[Authorization and Trust Management Service XSUAA  Service](https://help.sap.com/docs/CP_AUTHORIZ_TRUST_MNG?locale=en-US)

![](/legacyfs/online/storage/blog_attachments/2022/12/1-BTP-DestinationInstance-Key.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Northwind-Destination.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/2-BTP-Auth-Instance-Key.png)

#### **Sample Source Code**

Below is sample CAP Node JS Source code to connect to BTP Destination
> this.on("getRemoteNWData", async req => {
>
>
>
> letresponse;
>
>
>
> constcpqservice = awaitcds.connect.to('ext\_northwind')
>
>
>
> try {
>
>
>
>
> LOG.info("start demo Northwind connecting")
>
>
>
> response = awaitcpqservice.send({
>
>
>
> query:'GET /v2/northwind/northwind.svc/Products',
>
>
>
> headers: {
>
>
>
> 'Content-Type':'application/json'
>
>
>
> }
>
>
>
> })
>
>
>
> LOG.info("end Northwind connection ")
>
>
>
> returnresponse;
>
>
>
> } catch (error) {
>
>
>
> req.error(500, error.message)
>
>
>
> }
>
>
>
> });

...

I hope you know further code & how to prepare CAP Application to communicate to BTP cloud services

###

### **Scenario :  Use Local Application Destinations (Non BTP)**

For Testing ,If you don’t want to use SAP BTP destinations, you can also define destinations, which means the URL, authentication type, and additional configuration properties, in your application configuration or code.

As of now only Basic Type authentication Destination works with Local CAP Destination

Refer : <https://cap.cloud.sap/docs/guides/using-services?q=destination#app-defined-destinations>

###

### **Scenario : On-Premise Connectivity**

Few. SAP systems are located within a company's internal network ,Example : S/4HANA On-Premise  , SAP ERP (CRM) ... . They are not exposed to the internet. The SAP Cloud SDK provides helpful features to allow connecting to on-premise systems.

Reference : <https://sap.github.io/cloud-sdk/docs/js/features/connectivity/on-premise>

###

### **Consuming Services in CAP APP**

[Consuming Services](https://cap.cloud.sap/docs/guides/using-services)

<https://cap.cloud.sap/docs/node.js/cds-connect>

<https://cap.cloud.sap/docs/node.js/cds-serve>

> You can easily test your CAP application using a local database and mock ups. But at some point, you’re going to want to test with **real cloud services**. Of course, you can also deploy your application to the cloud & test but if you want to connect to Real Service locally before deploying to the cloud then you may want to run some ad-hoc tests,CAP Provides below options

# Approach 1

* Create default-env.json

* Copy VCAP\_SERVICES Values from BTP Environment Variable of your application

* run **cds watch** from terminal

![](/legacyfs/online/storage/blog_attachments/2022/12/1-Default-env.png)

**Note** :

<https://cap.cloud.sap/docs/node.js/cds-env?q=default-env.json#in-default-envjson>

Recently The use of *default-env.json* is deprecated

![](/legacyfs/online/storage/blog_attachments/2022/12/default-env-json-deprecated.png)

# Approach 2 [Hybrid Testing]

A new approach to bi...