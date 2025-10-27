---
title: SAP Fiori for SAP S/4HANA – Developing a Custom Fiori Launchpad Plugin with SAP Business Application Studio and Embedded Steampunk in SAP S/4HANA
url: https://blogs.sap.com/2023/01/03/sap-fiori-for-sap-s-4hana-developing-a-custom-fiori-launchpad-plugin-with-sap-business-application-studio-and-embedded-steampunk-in-sap-s-4hana/
source: SAP Blogs
date: 2023-01-04
fetch_date: 2025-10-04T02:59:33.339856
---

# SAP Fiori for SAP S/4HANA – Developing a Custom Fiori Launchpad Plugin with SAP Business Application Studio and Embedded Steampunk in SAP S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori for SAP S/4HANA – Developing a Custom Fi...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161943&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori for SAP S/4HANA – Developing a Custom Fiori Launchpad Plugin with SAP Business Application Studio and Embedded Steampunk in SAP S/4HANA](/t5/technology-blog-posts-by-sap/sap-fiori-for-sap-s-4hana-developing-a-custom-fiori-launchpad-plugin-with/ba-p/13562179)

![Jorge_Baltazar](https://avatars.profile.sap.com/0/0/id0033ed3df4c7c8a848830f06b06c9d16a9d63385d33cb754729cf5d13c1cabd3_small.jpeg "Jorge_Baltazar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Jorge\_Baltazar](https://community.sap.com/t5/user/viewprofilepage/user-id/17062)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161943)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161943)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562179)

‎2023 Jan 03
5:54 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161943/tab/all-users "Click here to see who gave kudos to this post.")

8,569

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)

View products (4)

***Update - Feb 2023 - Content is now available in the SAP-samples github repository***

Providing your end-users with the best possible User Experience at work while using SAP solutions is still one of the pillars of SAP Fiori.

In the past, we provided some options on how to create an SAP Fiori Launchpad plugin with SAP WebIDE and SAP S/4HANA versions 1511 to 1909. However, as time goes by tools and technologies change, and as a side question many people still wonder how to create an SAP Fiori Launchpad Plugin while using SAP Business Application Studio, additionally, there's multiple discussions on the Clean-Core concept and how to use it going forward to newer versions of SAP S/4HANA.

Considering these requests (using BAS to create a plugin, and giving an example on how to use clean core concept), from the SAP S/4HANA RIG we are providing an update to our previous blog: [SAP Fiori for SAP S/4HANA – Developing a Custom Fiori Launchpad Plugin](https://blogs.sap.com/2019/03/19/fiori-for-s4hana-developing-a-custom-fiori-launchpad-plugin/) through a new exercise which would guide you through the development of an SAP Fiori Launchpad Plugin and a custom HTTP Service with Embedded Steampunk in SAP S/4HANA 2022.

But before we jump into the details, let's answer some questions that you might have:

### What is the use case for creating a plug-in in for the SAP Fiori Launchpad?

Overall, there might be some user requirements which cannot be provided via an application, for example: a new button in the Launchpad header to navigate to an external/third party site, a new settings option for a custom app in the user settings menu, adding a tool area to the Launchpad Shell to display a customized menu or the use case in our exercise which is providing a customized text in the Launchpad Shell Header for the user to identify which system and client they have logged on.

![](/legacyfs/online/storage/blog_attachments/2023/01/overview.png)

Custom Shell Header Title through plugin

### How can you create an SAP Fiori Launchpad Plugin?

Nowadays, the recommended tool to create any SAP Fiori object is SAP Business Application Studio, with this tool you would create your custom plugin by using the standard SAPUI5 freestyle - SAPUI5 application generators and editing the generated project to create a component instead of an application. Same procedure can be run in VS Code.

While creating your plugin keep in mind the [Plugin Development Guidelines](https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/1b305d3e6b864e32a9464a13f3076b8b.html?version=202210.000) and two main points:

1. Custom code in your plugin should be as simple as possible (otherwise it will affect the total load time of the Fiori Launchpad)

2. There is no guarantee from the launchpad at which point in time a plug-in is initialized so your implementation should handle situations where required resources might not be ready yet, or certain processing has already been executed.

![](/legacyfs/online/storage/blog_attachments/2023/01/step63.png)

Creating a plugin with standard generators

### Why would plugins use the clean core concept?

As mentioned above you really need your plugin to be as simple as possible, hence you might want to push all business logic to the backend. This could be achieved by traditional OData or CDS development, but it could also be a good approach to achieve this by creating backend enabled HTTP services to be consumed by the plugin.

For testing purposes and as a starting point for you to learn about clean-core development we propose the following architecture for a sample custom plugin:

![](/legacyfs/online/storage/blog_attachments/2023/01/dev_arch.png)

Clean Core - Plugin Development Architecture

Considering this architecture what you will be doing is:

1. You will start by creating an upgrade stable object. In this case through a custom function module based only on standard function modules and BAPIs to provide the required information from the system. This custom function module would act as a wrapper for standard objects.

2. Your custom function module will then be consumed by a custom HTTP Service. This service will contain a small footprint easing the maintenance effort and will be created on top of the Embedded Steampunk "engine" meaning at this layer you will be using cloud-like ABAP code which is also upgrade stable and even gives you options at a later point to decouple the code in this layer and relocate to other solutions like SAP ABAP Cloud Environment on BTP.

3. A custom Fiori Plugin created on SAP Business Application Studio. In this object you will implement custom code to call the custom HTTP service, manipulate data from the response (if needed) and publish information in the SAP Fiori Launchpad.

### What's next?

Having answered some of the basic questions, it mi...