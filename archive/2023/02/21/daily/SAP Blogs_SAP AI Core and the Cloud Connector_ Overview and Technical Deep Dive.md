---
title: SAP AI Core and the Cloud Connector: Overview and Technical Deep Dive
url: https://blogs.sap.com/2023/02/20/sap-ai-core-and-the-cloud-connector-overview-and-technical-deep-dive/
source: SAP Blogs
date: 2023-02-21
fetch_date: 2025-10-04T07:37:07.538474
---

# SAP AI Core and the Cloud Connector: Overview and Technical Deep Dive

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP AI Core and the Cloud Connector: Overview and ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158395&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP AI Core and the Cloud Connector: Overview and Technical Deep Dive](/t5/technology-blog-posts-by-sap/sap-ai-core-and-the-cloud-connector-overview-and-technical-deep-dive/ba-p/13551849)

![ceylino92](https://avatars.profile.sap.com/e/2/ide229176a682e033d0e231768a122cf895c9047849eea31a88cb2891eb1c32e39_small.jpeg "ceylino92")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[ceylino92](https://community.sap.com/t5/user/viewprofilepage/user-id/46590)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158395)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158395)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551849)

‎2023 Feb 20
9:17 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158395/tab/all-users "Click here to see who gave kudos to this post.")

7,127

* SAP Managed Tags
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Core/pd-p/73554900100800003641)
* [SAP AI Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Launchpad/pd-p/73555000100800003283)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Core

  SAP Business AI](/t5/c-khhcw49343/SAP%2BAI%2BCore/pd-p/73554900100800003641)
* [SAP AI Launchpad

  SAP Business AI](/t5/c-khhcw49343/SAP%2BAI%2BLaunchpad/pd-p/73555000100800003283)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

View products (4)

# **Cloud Connector Demo**

## **Abstract**

This blog will demonstrate how you can setup an easy integration between your on-premise systems and cloud services like SAP AI Core, using the Cloud Connector. Using the cloud, you stay future-proof and up-to-date and can run resource-heavy AI workloads in the cloud at lower costs without any upfront investment.

## **Overview**

If you are not familiar with SAP AI Core and SAP AI Launchpad yet, here is a quick intro:

[SAP AI Core](https://help.sap.com/docs/AI_CORE) is SAP’s runtime for heavy-load AI. It allows you to train and deploy your AI models cost-efficiently at scale. Make your choice from a broad range of storage, CPU and GPU service plans and benefit from auto scaling and accelerated performance with GPU support.

[SAP AI Launchpad](https://help.sap.com/docs/AI_LAUNCHPAD) is the central application to access and manage your AI use cases. Connect to multiple runtimes, such as SAP AI Core, and streamline the AI lifecycle management of your use cases. Leverage SAP AI Launchpad to monitor your models and continuously improve their performance.

Both services enable customers to realize the full potential of deploying and managing their AI use cases. To provide better integration with on-premise systems, SAP AI Core enables users to access data from SAP HANA systems for training and serving using the Cloud Connector.

![](/legacyfs/online/storage/blog_attachments/2023/01/BTP_-CC_AICore.png)

This diagram shows Connectivity Service is part of SAP BTP which offers SAP AI Launchpad and SAP AI Core as services on the left. On the right, we have the SAP HANA as our on premise system which has Cloud Connector set up which can communicate with the Connectivity Service and open a secure tunnel to bypass the firewall.

## **What is Connectivity Service?**

The Connectivity Service provides two components to access on-premise systems:

* Cloud Connector which serves as a link between SAP BTP applications and on-premise systems (hosted on the on-premise application side)

* Connectivity Proxy which is a Kubernetes component that connects workloads running on a Kubernetes cluster to on-premise systems that are exposed via the Cloud Connector (hosted on the Kubernetes cluster side)

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-02-20-at-12.59.16-AM.png)

This diagram shows how the Connectivity Service, Connectivity Proxy and Cloud Connector are connected to each other.

## **Why is this important?**

Communication between SAP AI Core which is hosted on a Kubernetes cluster and an on-premise system is not permitted as there is a firewall which blocks any transfer of data. This is a problem because this makes accessing data from an on-premise system such as the SAP HANA database and using it for training or testing purposes on SAP AI Core service impossible. Connectivity Service allows data from an on-premise system to be accessible by a cloud service such as SAP AI Core. This is done by opening a secure tunnel between the two.

## **What is the purpose of this demo?**

This demo outlines how through the use of Cloud Connector, executions and deployments on SAP AI Core can use data and services of on-premise systems that are otherwise publicly inaccessible.

Connectivity Proxy already handles the creation of auth secrets, making it simple to directly use client\_id, client\_secret and token\_service\_url that are provided by the Connectivity Proxy instance. Together, these keys can be used to create the jwt token that is needed to connect SAP AI Core to Cloud Connector.

### **TLDR:**

Prerequisites to running this demo:

* subscribe to an SAP AI Core instance on SAP BTP

* create a Connectivity Proxy instance and service key on SAP BTP

* set up an on-premise network

* have Cloud Connector deployed on the on-premise network

## **Demo Setup Instructions**

1. Set up Cloud Connector on the on-premise system by deploying the Dockerfile: <https://github.com/nzamani/sap-cloud-connector-docker/blob/master/Dockerfile>

2. Have some service running on the on-premise system like a application or database such as SAP HANA (in our case, we have a simple hello world REST service running)

3. Have a Connectivity Proxy instance running on SAP BTP, create Connectivity Proxy Secrets json here, which will include client\_id, client\_secret and token\_service\_url (will be used in the AI Core workflow template to create a jwt token)

4. Already have an SAP AI Core instance deployed and running on the Kubernetes side

5. Connect Cloud Connector to SAP BTP subaccount for SAP AI Core

   1. You can refer to the Cloud Connector Setup instructions here: [https://help.sap.com/docs/CP\_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e7d4927dbb571014af7ef6ebd...](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e7d4927dbb571014af7ef6ebd6cc3511.html)

6. Now you are ready to run the demo.[ipynb](https://github.com/SAP-samples/ai-core-sa...