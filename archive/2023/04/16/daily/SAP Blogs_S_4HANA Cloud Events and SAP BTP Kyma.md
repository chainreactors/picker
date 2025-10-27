---
title: S/4HANA Cloud Events and SAP BTP Kyma
url: https://blogs.sap.com/2023/04/15/s-4hana-cloud-events-and-sap-btp-kyma/
source: SAP Blogs
date: 2023-04-16
fetch_date: 2025-10-04T11:32:35.553859
---

# S/4HANA Cloud Events and SAP BTP Kyma

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* S/4HANA Cloud Events and SAP BTP Kyma

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164693&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA Cloud Events and SAP BTP Kyma](/t5/technology-blog-posts-by-sap/s-4hana-cloud-events-and-sap-btp-kyma/ba-p/13570748)

![Gunter](https://avatars.profile.sap.com/a/4/ida479f2e0596469f30f8f256760af4a49349a092dbda1284ed2860522f6ceccd8_small.jpeg "Gunter")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Gunter](https://community.sap.com/t5/user/viewprofilepage/user-id/727)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164693)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164693)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570748)

‎2023 Apr 15
5:53 AM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164693/tab/all-users "Click here to see who gave kudos to this post.")

2,484

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (3)

## ![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-15-135144.jpg)SAP Event Objects - What and Why?

Event-driven architecture is an approach to software design where the components of a system are designed to respond to events or messages in a decoupled manner. In this architecture, events are sent and received by the system's components, triggered by user actions, system events, or external factors.

This design allows for more flexibility, scalability, and responsiveness in system design, as well as improved handling of large volumes of data and traffic. Additionally, it can enable greater collaboration and innovation by allowing organizations to integrate different systems and technologies.

SAP developed event-frameworks for our line-of-business solutions. So in the very recent years a very impressive set of event objects became available for S/4HANA (Cloud and On-Premise) which you can find documented on the [API business hub](https://api.sap.com/). Events are sent following the [Cloud Events](https://github.com/cloudevents/spec) specification.

## What does this blog address?

This blog serves as a practical how-to guide for setting up SAP event objects, compiled from various sources of information and personal insights. The aim is to help you save time and effort in setting up your system by providing clear and concise steps for implementation. While not addressing a specific use case, this guide will explain the mechanics and setup of SAP event objects, so you can get started with this powerful tool and take full advantage of its capabilities.

By following this guide, you can benefit from SAP's event objects in many ways, including faster data processing, better integration with other systems, and improved system agility. Whether you're new to SAP or an experienced user, this guide can help you unlock the full potential of event-driven architecture in your business processes.

## Concept of external cloud events on SAP BTP Kyma

One of the most challenging aspects of working with SAP S/4HANA Cloud Events on SAP Event Mesh on SAP BTP Kyma is understanding how *external events* are processed. Initially, I was caught up in the paradigm of how Kyma and NATS eventing works, which turned out to be a different approach altogether.

To shed some light on the process, let's take a look at the image below, which illustrates the flow of event information from source to consumer.

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-14-194321.png)

Image 1: Event information flow from source to consumer.

While this is not a perfect technical explanation, the basic idea is that an event raised in S/4HANA Cloud goes through the event framework on S/4HANA Cloud and identifies a suitable scenario (in this case, 0092) where the event was previously set as an *outbound topic* through the Fiori *Enterprise Event Enablement* Application.

From there it travels to the BTP Event Mesh into the client that is generated by the S/4HANA Cloud Messaging extensibility service. There one can also see subscribed event (which was an *Outbound Topic* in S/4HANA Cloud) - however not set it. This can be seen a read-only client.

In the Event Mesh client, though an *Event Queue* is set up with a subscription to the event provided by the aforementioned client. Here all incoming external events are collected for consumption. In order to allow for that, a webhook is defined that points to a URL on the Kyma cluster secured through OAuth2 client-credentials.

Finally the event is received by the *API Rule* on Kyma and forwarded through the service to the program running in a pod's container. That can be a Kyma serverless function or any other container. Above image also shows how such a cloud event is structured with the information in between the data-section being business object or better: event object specific.

## Configure Event consumption from S/4HANA Cloud

Let's now do the same for events.

### A. Define and deploy the Event Mesh for S/4HANA Cloud

This event mesh instance is providing the extensibility for events to and from S/4HANA Cloud. Create a yaml file similar to below.

```
apiVersion: services.cloud.sap.com/v1

kind: ServiceInstance

metadata:

  name: s4hc-ext-em-service

  labels:

    app.kubernetes.io/name: s4hc-ext-service

  namespace: s4hc-extensibility

spec:

  externalName: ''

  serviceOfferingName: s4-hana-cloud

  servicePlanName: messaging

  parameters:

    systemName: S4HANA-CLOUD-APJREGION

    emClientId: apj0
```

It's important to have entitlement for the S/4HANA Cloud Extensibility for the plan messaging set (we did this before already if you followed all steps). The *systemName* is the same name with which we registered the S/4HANA Cloud tenant. The *emClientId* must be not more than 4 characters.

This service create takes a while (approx. 5mins) since it also creates an instance of the SAP Event Mesh in the BTP. Once you log in to the Event Mesh UI you should see the *emClientId* as a client like so:

![](/legacyfs/online/storage/blog_attachments/2023/04/スクリーンショット-2023-04-06-110400.jp...