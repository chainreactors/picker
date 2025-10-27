---
title: Using Generic Connector On SAP Customer Data Platform
url: https://blogs.sap.com/2022/12/07/using-generic-connector-on-sap-customer-data-platform/
source: SAP Blogs
date: 2022-12-08
fetch_date: 2025-10-04T00:52:43.076295
---

# Using Generic Connector On SAP Customer Data Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Using Generic Connector On SAP Customer Data Platf...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13362&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Generic Connector On SAP Customer Data Platform](/t5/crm-and-cx-blog-posts-by-sap/using-generic-connector-on-sap-customer-data-platform/ba-p/13570486)

![MayaraRegazio](https://avatars.profile.sap.com/d/5/idd5e514c1a78fa24918a0ed7d9091f6650b8458be006686f2193d08fb92af57ee_small.jpeg "MayaraRegazio")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MayaraRegazio](https://community.sap.com/t5/user/viewprofilepage/user-id/13116)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13362)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13362)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570486)

‎2022 Dec 07
10:07 PM

[3
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13362/tab/all-users "Click here to see who gave kudos to this post.")

3,575

* SAP Managed Tags
* [SAP Customer Data Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Data%2520Platform/pd-p/73554900100800002991)
* [SAP Customer Identity](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Identity/pd-p/73554900100800002464)
* [Customer Experience](https://community.sap.com/t5/c-khhcw49343/Customer%2520Experience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)

* [Customer Experience

  Topic](/t5/c-khhcw49343/Customer%2BExperience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)
* [SAP Customer Identity

  Software Product](/t5/c-khhcw49343/SAP%2BCustomer%2BIdentity/pd-p/73554900100800002464)
* [SAP Customer Data Platform

  Software Product](/t5/c-khhcw49343/SAP%2BCustomer%2BData%2BPlatform/pd-p/73554900100800002991)

View products (3)

SAP Customer Data Platform (CDP) has a vast number of connectors available for integration with different types of applications, as a source or destination of data. Despite of this, we may face some cases the client has applications that still do not have an OTB(Out-of-the-box) CDP connector, or the application version is not compatible with the current CDP connector.

During a CDP implantation, the current version of the client’s SAP CAR was not compatible with the was not compatible with the CDP connector. As the client was implementing CPI, I used a simple solution provided by CDP, the generic connector provided by CDP and CPI so that CDP could ingest the data from the source.

Below I am going to show the steps I followed to configure the generic connector and how I tested the API calls to the endpoint provided by the connector.

## How To Set Up The Generic Connector In CDP

As the application is being configured to send activity data to CDP, on the menu go to **Connect** then **Sources** and click on the button **Connect Application**.

The Application Library will prompt, choose the **Server Application** under custom applications category.

![](/legacyfs/online/storage/blog_attachments/2022/12/CustomSource.png)

A window prompts so you can define the name of the connector, the fields Description and Data Quality Rank are optional.

![](/legacyfs/online/storage/blog_attachments/2022/12/Generic-Connector.jpg)

After clicking on **Create** button, the new connector is available under **Sources**:

![](/legacyfs/online/storage/blog_attachments/2022/12/Generic-Connector2.jpg)

And the user key and secret key for the connector is generated, the combination of them is used to authenticate the application that makes the API calls to CDP. All requests are conducted over HTTPS when using user and secret keys to authenticate the API calls.

![](/legacyfs/online/storage/blog_attachments/2022/12/UserSecreKeys.png)

After the connector was ready, I created the event which was used to ingest the data of a specific activity into CDP. To do this, click on the button **Create New Event** in the connector area.

![](/legacyfs/online/storage/blog_attachments/2022/12/NewEvent.png)

### Creating The Event

To create a new event, a name and data type are required in the first step, **Settings**.

![](/legacyfs/online/storage/blog_attachments/2022/12/NewEventSettings-1.png)

In the step 2, **Model**, I created the schema of the activity that is be ingested, in this case Order activity. Every time you create a new event in a connector, you need to create the activity schema or create the schema from a JSON file.

![](/legacyfs/online/storage/blog_attachments/2022/12/Model.png)

On the step 3, **Mapping**, the **Model** fields were mapped with the customer identifier fields in Profile schema and Order activity schema as the data of this activity will be ingest through the event *PostEvent* created.

![](/legacyfs/online/storage/blog_attachments/2022/12/Mapping1.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Mapping2.png)

In the last step the event listener is generated for the event. It is endpoint that will be used by SAP CPI for integration.

![](/legacyfs/online/storage/blog_attachments/2022/12/Listener.png)

After this, the event was created and is enabled so it can be used:

![](/legacyfs/online/storage/blog_attachments/2022/12/Connector.png)

## Using CDP APIs To Test The Connector

I used the CDP APIs to simulate the integration of CPI and CDP using Postman. This helped on verifying the payload that need to be send to CDP and anticipated any issue that could occur during the integration and assist the CPI architect with the correct format of the JSON.

On Postman, I used the method POST and copied the URL provided in the event on the step 4, **Listener**. The URL indicates which CDP domain will be reached depending on where the Business Unit was created:

* For Business Units in EU: cdp.EU5-prod.gigya.com

* For Business Units in US: cdp.US5-prod.gigya.com

We can ingest one or multiple activities using the following CDP APIs:

* For one activity: /api/businessunits/{businessUnitId}/applications/{applicationId}/dataevents/{dataEventId}/event

* For multiple activities: /api/businessunits/{businessUnitId}/applications/{applicationId}/dataevents/{dataEventId}/events

For both CDP APIs you need to send, in the body of the API call, the payload with the data of one or multiple activities, respectively, observing the structure of fields and field types defined in the step 2, **Model**, of the event.

After the data ingestion, you can check the events processed in the connector status.

In this case, six events were processed indicating the integration with the CDP connector is working.

![](/legacyfs/online/storage/blog_attachments/2022/12/ConnectorAfterIngestion.png)

For more information about how to integrate CDP using API calls see the SAP Help Portal [Server Applications: API Integrations](https://help.sap.com/docs/SAP_CUSTOMER_DATA_PLATFORM/8438f051ded544d2ba1303e67fc5ff86/2e0cd2c354ff42979762cd99cae66391.html) and about the [CDP APIs](https://help.sap.com/docs/...