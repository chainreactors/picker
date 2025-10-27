---
title: Scheduling RMS Flows in Data Intelligence via the Internal API
url: https://blogs.sap.com/2022/11/11/scheduling-rms-flows-in-data-intelligence-via-the-internal-api/
source: SAP Blogs
date: 2022-11-12
fetch_date: 2025-10-03T22:31:28.617151
---

# Scheduling RMS Flows in Data Intelligence via the Internal API

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Scheduling RMS Flows in Data Intelligence via the ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163865&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Scheduling RMS Flows in Data Intelligence via the Internal API](/t5/technology-blog-posts-by-sap/scheduling-rms-flows-in-data-intelligence-via-the-internal-api/ba-p/13568252)

![Ian_Henry](https://avatars.profile.sap.com/d/5/idd5d9ebe93280684040ce03bad285fdd3a428e8b2473250904ce90745807cab83_small.jpeg "Ian_Henry")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ian\_Henry](https://community.sap.com/t5/user/viewprofilepage/user-id/239)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163865)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163865)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568252)

‎2022 Nov 11
10:00 AM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163865/tab/all-users "Click here to see who gave kudos to this post.")

5,682

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

The DI (Data Intelligence) RMS (Replication Management Service) provides initial loads or initial  and delta, sometimes a scheduled delta is preferred.

In this blog post I will describe how we can achieve a scheduled delta with an RMS Flow and/or RMS Tasks. At the time of writing (November 2022) the Data Intelligence scheduler doesn’t allow that, which why this blog exists.

1. Identify the Internal API Calls

2. Additional API Calls Identified

3. Data Intelligence pipeline for scheduling

## 1. Identify the Internal API Calls

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-10-at-14.00.12.png)

Figure 1.1 RMS Flows vs RMS Tasks

For clarity Figure 1.1 shows the relationship of RMS Flows to RMS Tasks, one flow can contain multiple tasks.

The [official public DI API](https://api.sap.com/package/SAPDataIntelligenceCloud/rest) does not cover the RMS (Replication Management Service), this requires using the internal (unsupported) API, this has worked flawlessly in my testing. In fact most actions within Data Intelligence use internal APIs and that includes the management of RMS Flows and the RMS Tasks.

To understand the RMS internal API, check the browser developer tools and inspect the API calls.
Here, the GET calls are mainly used to populate the UI and the PUT stop and start the flows or tasks.

![](/legacyfs/online/storage/blog_attachments/2022/11/Developer_Tools.png)

Figure 1.2: Developer Tools, Network trace

The requirement I have is to stop and start an entire RMS Flow. This is performed by the PUT calls, using the query parameter requestType. The flow name makes up the last part of the URL The resulting API call is below.

```
https://vsystem.ingress.{{Tenant}}.dhaas-live.shoot.live.k8s-hana.ondemand.com/app/rms/api/dt/v1/rep...
```

requestType paramers

Stop - SUSPEND\_ALL\_ACTIVE\_TASKS

Start - RUN\_OR\_RESUME\_ALL\_INACTIVE\_TASKS

As described in the [Pubic Data Intelligence API](https://help.sap.com/docs/SAP_DATA_INTELLIGENCE/ca509b7635484070a655738be408da63/8039c62f7d3740bca72ccc63cca175bd.html?locale=en-US&q=x-requested-with), to use a Data Intelligence PUT API call you need to use the header as below.

```
x-requested-with: Fetch
```

Initial testing was done with Postman to confirm the API behaviour.

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-Validation.png)

Figure 1.3: Postman to Validate API Calls

## 2. Additional API Calls Identified

Here are some additional API calls that were identified and could be useful to enhance the workflow and/or capture some statistics as to the performance of the replication process. These are not necessary for the the scheduling process, more for reference.

GET all flow statuses
source, target, status, change date, user
/app/rms/api/dt/v1/replicationflows/

GET specified flow details and tasks
source, target, connection, container, output format, load type
/app/rms/api/dt/v1/replicationflows/{{flowname}}

GET specified flow configuration
Priority, max connections source and target
/app/rms/api/dt/v1/replicationflows/{{flowname}}/configuration

GET (Monitor) specified flow
source, target, connection, container, output format, status, duration
/app/rms/api/dt/v1/replicationflowMonitors?name={{flowname}}

GET (Monitor) tasks in specified flow
/app/rms/api/dt/v1/replicationflows/{{flowname}}/taskMonitors
Source, target, priority, load type, status, number of records, number of partitions, duration, bytes sent

GET Status of last flow (PUT) action
Status, time of change
/app/rms/api/dt/v1/replicationflows/{{flowname}}/changerequeststatus

PUT start specified flow
/app/rms/api/dt/v1/replicationflows/{{flowname}}?requestType=RUN\_OR\_RESUME\_ALL\_INACTIVE\_TASKS

PUT stop specified flow
/app/rms/api/dt/v1/replicationflows/{{flowname}}?requestType=SUSPEND\_ALL\_ACTIVE\_TASKS

PUT start specified task(s) within flow
/app/rms/api/dt/v1/replicationflows/{{flowname}}?requestType=RUN\_OR\_RESUME\_SELECTIVE\_INACTIVE\_TASKS
In the request body you need to specify the task name, the name is the name as shown from the “Get specified flow details and tasks” API call

PUT stop specified task(s) within flow
/app/rms/api/dt/v1/replicationflows/{{flowname}}?requestType=SUSPEND\_SELECTIVE\_ACTIVE\_TASKS
In the request body you need to specify the task name, the name is the name as shown from the “Get specified flow details and tasks” API call

## 3. Data Intelligence pipeline for scheduling

To be able to schedule these actions I have created a simple pipeline to call these APIs and log the output of the call. The pipeline, which triggers the RMS flow can then be scheduled to run at the required times.

Using the Data Intelligence connection management provides a secure place to store the credentials.

![](/legacyfs/online/storage/blog_attachments/2022/11/Open-API-Connection-1.png)

Figure 3.1: Open API Connection

We can then use this connecti...