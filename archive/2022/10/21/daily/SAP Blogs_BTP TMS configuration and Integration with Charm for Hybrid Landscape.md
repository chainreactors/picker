---
title: BTP TMS configuration and Integration with Charm for Hybrid Landscape
url: https://blogs.sap.com/2022/10/20/btp-tms-configuration-and-integration-with-charm-for-hybrid-landscape/
source: SAP Blogs
date: 2022-10-21
fetch_date: 2025-10-03T20:29:20.214366
---

# BTP TMS configuration and Integration with Charm for Hybrid Landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* BTP TMS configuration and Integration with Charm f...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159923&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BTP TMS configuration and Integration with Charm for Hybrid Landscape](/t5/technology-blog-posts-by-members/btp-tms-configuration-and-integration-with-charm-for-hybrid-landscape/ba-p/13548931)

![shivamkumar074](https://avatars.profile.sap.com/4/7/id4719667a34d67bc23396ed1d11e430d2ae035bd589220a76806d3136b0742bed_small.jpeg "shivamkumar074")

[shivamkumar074](https://community.sap.com/t5/user/viewprofilepage/user-id/39463)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159923)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159923)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548931)

‎2022 Oct 20
7:35 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159923/tab/all-users "Click here to see who gave kudos to this post.")

7,824

* SAP Managed Tags
* [SAP Cloud Transport Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Transport%2520Management/pd-p/73554900100800001901)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Cloud Transport Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BTransport%2BManagement/pd-p/73554900100800001901)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

**Overview**

We will discuss configuration of SAP BTP Transport Management Service (TMS) with various BTP services.  Additionally, we’ll discuss integration of SAP TMS with ChaRM, which provides a one-stop shop to manage all transports created from various services on BTP.

**Initial Setup for SAP Transport Management Service**

To setup the SAP TMS instance, we will need to perform the below activities.

* [Configuring Entitlements for Cloud Transport Management](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/13894bed9e2d4b25aa34d03d002707f9.html)

* [Subscribing to Cloud Transport Management](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/7fe10fc1baae444e9315579786d623b9.html)

* [Setting Up Role Collections](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/eb134e02d2074918bcc5af34f50fb19f.html)

* [Creating a Service Instance and a Service Key](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/f44956035ce54684b1dbb9e4d23c37d2.html)

Detailed steps to perform each of these activities are available here at [Setup TMS Instance](https://help.sap.com/docs/TRANSPORT_MANAGEMENT_SERVICE/7f7160ec0d8546c6b3eab72fb5ad6fd8/8d9490792ed14f1bbf8a6ac08a6bca64.html).

**Configure Landscape**

Before we can use SAP TMS to transport applications or other developments created in various services between different subaccounts, we must configure the landscape.

To configure the landscape, we’ below steps:

* Create Transport Destinations.

* Create Transport Nodes

* Create Transport Routes

* Create Destinations from BTP applications to SAP TMS.

To perform these steps, we can either use the inbuilt landscape wizard or manually configure the individual entities. For this blog, we will use the landscape wizard.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-53.png)

Before proceeding to the next configuration, we will be creating **Transport Destinations** in BTP cockpit Connectivity à Destinations. Destinations contain the address of the target end point as well as the user credentials of the platform user that we need for the destination.

We must point this to deploy the service of development space.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-39.png)

Similarly, we will be creating a destination pointing to the Test and Prod tenant.

Next, we’ll proceed to the Landscape Wizard and will define the following:

* **Transport Nodes:** In Cloud Transport Management, transport nodes represent the source and target end points of a deployment process, such as a Cloud Foundry subaccount. Transports take place between transport nodes. This can be a free text, but since we’re going to integrate these nodes with Charm, we’ll keep these names at a maximum of three characters as per SAP’s recommendation.

* **Allow Upload**: This should be checked only for the node in which we want files to be directly loaded to the node.

* **Forward Mode**: This value is set to **Auto**. When the import of a transport request is started, the request is automatically forwarded to the target transport nodes according to the transport routes defined for the node where the import started. If we want to manually forward transport requests for this node, set **Forward Mode** to **Manual**.

* **Destinations**: We must point nodes to the end point destination we created in the previous step.

        ![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-22.png)

**Transport Routes**: In SAP Cloud Transport Management, transport routes are used to connect transport nodes.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture4-24.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture5-15.png)

This concludes the initial configuration of TMS service.

Next, we’ll discuss the steps to integrate TMS to CPI service to import artifacts from one tenant to another.

**Integration of TMS with CPI**

We need to create destinations in our SAP BTP subaccount to transport integration packages from a source tenant to the target tenant.

The following two destinations must be created:

* ContentAssemblyService

* CloudIntegration

Please note the destinations should be the same and are case sensitive, so create the destinations as per the step mentioned in [SAP help Doc](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/94057be5cf784617b104eaeab20e4fba.html).

Once created, we will navigate to CPI tenant and change Transport Mode to “Transport Management Service” and click on Check Configuration to check the status of integration. We should get a successful integration message as per below screenshot.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture6-16.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture7-12.png)

**Integration of TMS with Charm**

There are different steps to configure in Solution Manager and BTP TMS for this integration.

**Solution Manager:**

* Create RFC connections to Transport Management: Below RFCs need to be created in solution manager system to connect with the TMS instance.

1. RFC destination for SAP Cloud platform TMS authentication - CLOUD\_TMS\_AUTHENTICATION

1. RFC connection for the SAP Cloud Platform TMS REST APIs - CLOUD\_TMS\_API

* Create e...