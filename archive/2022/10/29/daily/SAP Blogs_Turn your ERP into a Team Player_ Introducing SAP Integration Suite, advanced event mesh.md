---
title: Turn your ERP into a Team Player: Introducing SAP Integration Suite, advanced event mesh
url: https://blogs.sap.com/2022/10/28/turn-your-erp-into-a-team-player-introducing-sap-integration-suite-advanced-event-mesh/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:18.991466
---

# Turn your ERP into a Team Player: Introducing SAP Integration Suite, advanced event mesh

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Turn your ERP into a Team Player: Introducing SAP ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/149135&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Turn your ERP into a Team Player: Introducing SAP Integration Suite, advanced event mesh](/t5/technology-blog-posts-by-sap/turn-your-erp-into-a-team-player-introducing-sap-integration-suite-advanced/ba-p/13525239)

![KStrothmann](https://avatars.profile.sap.com/f/a/idfabdcda21db6287c6f12ffae7e13fe5e0ddfd236eab7fd9829b68cb07bbd18c6_small.jpeg "KStrothmann")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[KStrothmann](https://community.sap.com/t5/user/viewprofilepage/user-id/7039)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=149135)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/149135)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13525239)

‎2022 Oct 28
7:19 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/149135/tab/all-users "Click here to see who gave kudos to this post.")

7,916

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP TechEd](https://community.sap.com/t5/c-khhcw49343/SAP%2520TechEd/pd-p/755421404636447943131706525840948)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP TechEd

  Event](/t5/c-khhcw49343/SAP%2BTechEd/pd-p/755421404636447943131706525840948)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

## How team sports explain Event-Driven Architecture

Have you experienced these moments when you hear a single sentence - and this sentence sums up things better than anything you could have come up with? That moment in respect to event-driven architecture took place on Tuesday for me.

I had been presenting to an American Fortune 500 customer on SAP Integration Suite, advanced event mesh and I had come up with this new slide wrapping up the advantages of event-driven architecture, comparing an EDA to team sports.

![](/legacyfs/online/storage/blog_attachments/2022/09/Soccer-5.jpg)

This comparison is in the end quite obvious since soccer players for example act loosely coupled while always knowing what is going on around them (situational awareness is the buzzword here) and ideally notifying each other in real time about their plans and actions.

In order to win, players need to act as a team. And in order to act as a team, they need situational awareness. You can replace soccer with your favourite team sport here - ice hockey, basketball, football, rugby. You pick. It's the same story. It is about situational awareness and teamwork. Talent wins games, teamwork wins championships.

Now transfer this to your SAP landscape - wouldn't it be great if your SAP S/4HANA system could inform your SAP Business Technology Platform and your SAP ECC system in real time of changes that are important? Of significant changes? Or even beyond your SAP landscape, if your SAP S/4HANA system would inform your Microsoft Teams of significant changes in real time.

My customer did this transfer in almost real time and worded it close to perfect: **I want my ERP to be a team player!**

I simply love this sentence. It sums things up so well.

Let's make the next step: what do you need for that? In order to turn your ERP into a team player, you need an event-enabled backend, suitable event consumers and you need the appropriate infrastructure to transport and distribute your events: an event broker or event mesh.

So far SAP Event Mesh has been SAP's single offering in this space. Lately, beginning of August 2022 to be exact, we have added SAP Integration Suite, advanced event mesh to our portfolio. Advanced Event Mesh complements SAP Event Mesh for more demanding scenarios and offers a highly sophisticated feature set perfectly suited for the SAP Event-Driven Ecosystem and beyond.

## SAP Integration Suite, advanced event mesh

SAP Integration Suite, advanced event mesh is a fully managed event streaming and management service that enables enterprise-wide and enterprise-grade event-driven architecture.

### What is Advanced Event Mesh?

* Advanced Event Mesh is a distributed mesh of event brokers that can be deployed across environments, both in the cloud and on-premise

* It offers a full purpose set of eventing services covering all relevant use cases

* AEM supports event streaming, event management and event monitoring

* Brokers fully scale as required and come in T-shirt sizes to perfectly fit different needs

![](/legacyfs/online/storage/blog_attachments/2022/10/AEM.png)

Advanced Event Mesh Cockpit

### What features and benefits does AEM offer?

* AEM offers enterprise-grade performance, reliability, security and governance.

* It scales to very large use cases – and very means very very very in this case. On the other hand, you can start small, if needed, as well.

* SAP Integration Suite, advanced event mesh offers deployment options across different hyperscalers and in private cloud environments. All it takes is a Kubernetes environment.

* AEM can be configured to form a distributed mesh of event brokers. Events can flow across the mesh to be consumed where desired.

* It includes a sophisticated toolset to address tasks like cluster management, mesh management and monitoring/tracing.

* SAP Integration Suite integrates with SAP backends via different options

### SAP Integration Suite, advanced event mesh in ten short statements

![](/legacyfs/online/storage/blog_attachments/2022/10/10-19.png)

SAP Integration Suite, advanced event mesh

1. is a general purpose, multi-site EDA platform and portal

2. allows for SAP to SAP, SAP to Everything and Everything to Everything scenarios

3. supports distributed networks of event brokers deployed in different clouds and on-premises

4. can be deployed in your cloud of choice or in your on premises K8S

5. provides sophisticated authentication and security features like Kerberos, OAuth or TLS

6. offers fine-grained filtering options

7. allows for real-time monitoring, capacity insights and di...