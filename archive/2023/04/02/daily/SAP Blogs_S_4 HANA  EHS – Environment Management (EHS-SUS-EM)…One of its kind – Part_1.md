---
title: S/4 HANA  EHS – Environment Management (EHS-SUS-EM)…One of its kind – Part:1
url: https://blogs.sap.com/2023/04/01/s-4-hana-ehs-environment-management-ehs-sus-em...one-of-its-kind-part1/
source: SAP Blogs
date: 2023-04-02
fetch_date: 2025-10-04T11:26:59.026905
---

# S/4 HANA  EHS – Environment Management (EHS-SUS-EM)…One of its kind – Part:1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* SAP S/4HANA EHS : Environment Management (Emissio...

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1510&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA EHS : Environment Management (Emissions Management) – Part:1 (Master Data Entities)](/t5/product-lifecycle-management-blog-posts-by-members/sap-s-4hana-ehs-environment-management-emissions-management-part-1-master/ba-p/13563682)

![Pardhasaradhi_Reddy_Chelikam](https://avatars.profile.sap.com/0/1/id01c0bd52ae25965202ba095352fa54575c9fb9d2b45cad6c887977ba00b19dfc_small.jpeg "Pardhasaradhi_Reddy_Chelikam")

[Pardhasaradhi\_Reddy\_Chelikam](https://community.sap.com/t5/user/viewprofilepage/user-id/44949)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1510)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1510)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563682)

‎2023 Apr 01
7:32 AM

[9
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1510/tab/all-users "Click here to see who gave kudos to this post.")

4,297

* SAP Managed Tags
* [SAP Environment, Health, and Safety Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Environment%252C%2520Health%252C%2520and%2520Safety%2520Management/pd-p/01200615320800000062)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [SAP Environment, Health, and Safety Management

  SAP Environment, Health, and Safety Management](/t5/c-khhcw49343/SAP%2BEnvironment%25252C%2BHealth%25252C%2Band%2BSafety%2BManagement/pd-p/01200615320800000062)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (2)

As part of Emissions management process in environment Management application component, before we perform any activities, related to environmental compliance, we must prepare the master data.

In this blog, I would like to outline the SAP Environment Management application master data entities that need to be prepared as prerequisites.

**What is Master Data:**

Master data is all the data that is mission-critical to the running of a business. It is typically just a small percentage of all business data, but it is some of the most complex and valuable data in an organization.

**Master Data Entities in SAP EHS-Environment Management:**

+ Manage locations and the location structure.

+ Manage listed substances.

+ Manage physical/chemical properties

+ Sampling methods.

![](/legacyfs/online/storage/blog_attachments/2023/03/Emissions-management-master-data-screen.png)

+ **Manage Locations:**

In environment management, locations are used to define the emission sources. In this process, a location structure must be created in the system. Without a single location, the process cannot be triggered.

We can either create locations directly in SAP EHS-Environment Management application and structure them or can import from back end system,S4 HANA Asset Management.

For instance, I go with import option. I have created a few locations, listed below, in my backend S4 HANA system.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-50.png)

I have also created a few functional locations and tagged each one of them to a desired "Location".![](/legacyfs/online/storage/blog_attachments/2023/03/Picture19-6.png)

Use App. "Manage Locations" to create or import locations from S4 HANA backend system.

![](/legacyfs/online/storage/blog_attachments/2023/03/1a.png)![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-35.png)

use option  "Import from PM",

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-31.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-33.png)

we can import both equipment and functional locations. For instance, I go with functional locations.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-29.png)

If we provide superior Functional Location, system pulls all the relevant sub-Functional Locations, however it is subjected to the way the hierarchy is maintained in S4 HANA Asset Management.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-21.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-16.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-19.png)

Use the value help to assign the "Location Type" to each of the imported technical objects.![](/legacyfs/online/storage/blog_attachments/2023/03/Picture13-13.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture14-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture15-10.png)

Once the location type has assigned to technical object, click on "Import"![](/legacyfs/online/storage/blog_attachments/2023/03/Picture16-9.png)

system copies all the Functional Locations, which are under superior Functional Location to Environment Management application from S4 HANA Asset Management.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture17-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/2-52.png)

Now, assign person(s) responsible for each of the locations. In the emissions management process, the assignment of environmental manager, and environmental technician or production operator at a location level is required to carry out the process.

The assignment of Environmental manager is required to manage compliance activities.

The assignment of Environmental technician or production operator is required to enable receipt of all notifications from the data collection.

Let us assign person responsible and desired roles to each location as shown below.![](/legacyfs/online/storage/blog_attachments/2023/03/1-79.png)

and assign the "Location Classifiers" as shown below![](/legacyfs/online/storage/blog_attachments/2023/03/2-53.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/4-37.png)

**Mini Note:** Location Classifier is a textual object that is used to categorize locations and can be assigned to compliance requirements to specify their applicability.

For each location, properties with environmental aspect can be defined to capture different parameters, for example, valve count, emission factor and so forth.

I have chosen, valve count and number of material handling equipment in carbon plant-01 to use them in the compliance scenario. Within the calculation definition, location properties can be used as input data sources to calculate emissions

![](/legacyfs/online/storage/blog_attachments/2023/03/Property-location-4.png)

Post assignment of persons responsible and environmental details, set the location status as "Active" to use it for complian...