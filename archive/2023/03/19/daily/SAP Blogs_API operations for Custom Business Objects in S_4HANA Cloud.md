---
title: API operations for Custom Business Objects in S/4HANA Cloud
url: https://blogs.sap.com/2023/03/18/api-operations-for-custom-business-objects-in-s-4hana-cloud/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:09.973325
---

# API operations for Custom Business Objects in S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* API operations for Custom Business Objects in S/4H...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50745&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [API operations for Custom Business Objects in S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/api-operations-for-custom-business-objects-in-s-4hana-cloud/ba-p/13552628)

![varunvenkat](https://avatars.profile.sap.com/6/d/id6d9836d543f88d438477c8e54903aa6ba4a079c87ec08d808dc512a637a4c55f_small.jpeg "varunvenkat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[varunvenkat](https://community.sap.com/t5/user/viewprofilepage/user-id/83606)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50745)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50745)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552628)

‎2023 Mar 18
10:12 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50745/tab/all-users "Click here to see who gave kudos to this post.")

13,922

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Extensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Extensibility

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BExtensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)

View products (4)

In SAP S/4HANA Cloud, there are three fundamental possibilities available for the extensibility of the standard functionality that is available out-of-the-box. These possibilities are:

* In-App/Key User Extensibility

* Side-by-Side Extensibility

* Developer Extensibility/Embedded Steampunk

For a high-level understanding of these different options, please refer to the following [blog](https://blogs.sap.com/2022/09/27/extensibility-in-sap-s-4hana-cloud/) which offers a great overview on this topic.

In this blog post, we’ll be looking at a specific extensibility scenario available with In-app/Key user extensibility, namely the use of so-called [Custom Business Objects](https://developers.sap.com/group.abap-extensibiliy-cbo-cce-ccl.html) (CBO’s). With CBO’s, it is possible to create custom variations of standard business objects (for eg. Sales Orders or Purchase Orders) and enhance these objects with custom logic to fit the needs a specific customer requirement. Given this background, I would like to demonstrate in this blog how you can create a CBO and execute the standard API operations (GET, POST, DELETE) on this CBO. You can also enhance CBO’S with custom fields and custom logic using ABAP BADI’s, however in this blog, I’ll only be covering the execution of API operations.

**Create the new CBO**

The first step in the process is to create a new custom business object, on which we can test the API calls. For this, use the Fiori app “Custom Business Objects” and create a new CBO.

![](/legacyfs/online/storage/blog_attachments/2023/03/Create_CBO_screen.png)

Create CBO

**Add Nodes and Fields**

Once inside the CBO, activate the checkbox “User Interface” under the General Information tab. This will automatically generate a UI and back end service associated with your CBO.

![](/legacyfs/online/storage/blog_attachments/2023/03/CBO_Gen_info.png)

Generate UI for CBO

Next, under the Fields tab, add some fields that you want to use in your CBO and define at least one of these as a key field. In this demo, I’ll use a fictional scenario where I want my CBO to display a list of arbitrarily selected Sales Orders along with their respective delivery dates.

![](/legacyfs/online/storage/blog_attachments/2023/03/CBO_fields.png)

Add fields to the CBO

Once this is done, click Publish. After publishing, go back to the “General Information” tab and click on the *Go To Generated UI* link, which will have now been activated. Create a test entry on the UI, so that we have some test data for our GET request later on.

![](/legacyfs/online/storage/blog_attachments/2023/03/CBO_UI_entry.png)

CBO UI with test entry

**Create a custom comm. Scenario and a communication arrangement for the CBO**

Once the CBO has been created and published, the next step is to create a communication arrangement for it. To do this, use the Fiori app “Custom communication scenarios”. After creating a new custom comm. scenario, click on Add in the “Inbound Services” tab. Here, search for the identifier of the CBO created in the first step and add it as an inbound service. We can ignore the outbound services for now, as these are not pertinent for testing out API operations on our CBO. Save and publish the custom comm. Scenario.

![](/legacyfs/online/storage/blog_attachments/2023/03/custom_comm_scenario_inbound_service.png)

Custom comm. scenario with inbound service

The last step is to now create a communication arrangement for our custom comm. Scenario. Go to the “Communication Arrangements” app and create a new arrangement by selected the ID of the scenario created in the previous step. Select an appropriate comm. System and user for inbound communication and save the arrangement.

![](/legacyfs/online/storage/blog_attachments/2023/03/create_comm_arrangement_select_system_user.png)

Create comm. arrangement

With this, all the setup for running API operations on our CBO is complete. Let’s now get into the actual doing. We’ll be using Postman as a tool to test the API calls.

**GET data from our CBO**

* Copy the inbound service URL from the comm. Arrangement and use this as request URL in Postman.

* In the Authorization tab, select “Basic Auth” and enter the username and password of your communication user.

* Execute the request and you should see the following result

![](/legacyfs/online/storage/blog_attachments/2023/03/CBO_Get_screen1.png)

Get request to CBO root node

* In the response, we see that the CDS View of the communication arrangement shows our CBO as an existing entity. Append this value to the request URL and execute the result to see the actual results of the data from our CBO, which will look like this:

![](/legacyfs/online/storage/blog_attachments/2023/03...