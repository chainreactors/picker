---
title: Event Driven Integration with SAP S/4 HANA Cloud using SAP Event Mesh and SAP Integration Suite
url: https://blogs.sap.com/2022/10/26/event-driven-integration-with-sap-s-4-hana-cloud-using-sap-event-mesh-and-sap-integration-suite/
source: SAP Blogs
date: 2022-10-27
fetch_date: 2025-10-03T21:00:28.984406
---

# Event Driven Integration with SAP S/4 HANA Cloud using SAP Event Mesh and SAP Integration Suite

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Event Driven Integration with SAP S/4 HANA Cloud u...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/156876&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Event Driven Integration with SAP S/4 HANA Cloud using SAP Event Mesh and SAP Integration Suite](/t5/technology-blog-posts-by-members/event-driven-integration-with-sap-s-4-hana-cloud-using-sap-event-mesh-and/ba-p/13529204)

![Dipan_Ghosh](https://avatars.profile.sap.com/e/5/ide54552f442bcb55689f0bf128f5492279a9d627525a217e20a5467cef2b75ea7_small.jpeg "Dipan_Ghosh")

[Dipan\_Ghosh](https://community.sap.com/t5/user/viewprofilepage/user-id/15933)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=156876)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/156876)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13529204)

‎2022 Oct 26
9:23 PM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/156876/tab/all-users "Click here to see who gave kudos to this post.")

18,737

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

# **Introduction:**

In the current world, an organization wants to get the notification of every event and act on them in real-time, because Business is a series of events. Event-Driven architecture helps us to communicate with different systems in real time when an event is notified.

In Event Driven Architecture, when a change happens within an enterprise system, it triggers an event without knowing what happens after, leaving it to the event router, which means the producer and consumer of the event always remain decoupled. Unlike traditional architecture, it speeds up scalability and agility in business processes.

SAP Event Mesh is a cloud-based capability that allows applications to communicate through asynchronous events. SAP Event Mesh Uses standard and Open messaging protocols like AMQP, MQTT, and Webhook to provide notifications of business events.

This blog details how we can implement event-driven integrations using SAP BTP's Event Mesh.

## **Use Case:**

**Sending real-time Product master/ Material Master information from S/4 HANA Public cloud to Salesforce.**

**Use Case Architecture:**

![](/legacyfs/online/storage/blog_attachments/2022/10/Architecture.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Architecture-3-1.png)

Our Customer requirement was If any new Product is created in S/4 HANA or any changes are made on the Product Master, it must be replicated in salesforce in real-time. When Product Master data is created or updated in S/4 HANA, it is notified in real-time via the events published by S/4 HANA towards SAP Event Mesh. In turn, SAP Event Mesh routes these events to SAP Cloud Integration. SAP Cloud Integration fetches the required details from SAP S/4 by calling suitable APIs and sends them to Salesforce.

In this blog. I will explain the followings.

1. How to configure SAP Event Mesh to connect with SAP Integration Suite.

2. Implementing Event-Driven integration to integrate S/4 Hana Public Cloud with Salesforce using the SAP integration Suite.

## **Prerequisites:**

1. Set up Integration Suite. This is necessary to create an Integration flow in SAP Cloud Integration. Please follow the step-by-step process in this [Link.](https://developers.sap.com/tutorials/cp-starter-isuite-onboard-subscribe.html)

2. S/4 HANA Public Cloud and Salesforce system details.

## **Step-by-Step Process:**

### Configure Event Mesh:

1. Go to BTP Global account -> System Landscape -> Add System.![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-pic-1.png)

2. Copy Registration Token![](/legacyfs/online/storage/blog_attachments/2022/08/BLog-pic-2.png)

3. Go to S/4 HANA -> Maintain Extensions on SAP BTP -> add new extension. Once the status is enabled, the system is registered.![](/legacyfs/online/storage/blog_attachments/2022/10/add-extesnion-in-SAP-BTP.png)

4. Go to Entitlements -> Entry Assignments -> Add SAP S/4 HANA Cloud Extensibility and Event Mesh.![](/legacyfs/online/storage/blog_attachments/2022/10/3_Blog.png)

5. Go to SAP BTP Subaccount -> Create an instance for SAP S/4 HANA Cloud Extensibility.![](/legacyfs/online/storage/blog_attachments/2022/10/4-3.png)

6. Once the instance is created successfully, Go to S/4 HANA Cloud -> search Apps -> Enterprise Event Enablement - Configure Channel Binding. Here you can see a channel is created. This will be used to publish the events from S/4 HANA. ![](/legacyfs/online/storage/blog_attachments/2022/10/Step-7-1.png)

7. Go to SAP BTP Subaccount -> Create a Subscription for SAP Event Mesh.![](/legacyfs/online/storage/blog_attachments/2022/10/6-21.png)

8. Go to SAP BTP Subaccount -> Create an Instance of SAP Event Mesh. Configure the parameter to subscribe to events.

9. ![](/legacyfs/online/storage/blog_attachments/2022/10/9.png)Go to S/4 HANA Cloud -> Maintain Event Channel Binding -> Create Outbound Topics

10. ![](/legacyfs/online/storage/blog_attachments/2022/10/8-2.png)​Go to Event Mesh-> Message Client. You can find both the update and change events published in the message client. This Message client will Publish the S/4HANA events.![](/legacyfs/online/storage/blog_attachments/2022/10/S4-Queue.png)

11. Go to Event Mesh -> Message Client -> you can find the newly created Message Client which is created in step 8. This Will be used to subscribe to the events. In the rules section, you can see this instance has **"subscribe"** permission (JSON parameters have to be configured in step 8).![](/legacyfs/online/storage/blog_attachments/2022/10/Rules.png)

12. Create a Queue and Subscribe to the Topics.![](/legacyfs/online/storage/blog_attachments/2022/10/1...