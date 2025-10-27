---
title: How to relocate an existing app running on your Kubernetes Cluster to Kyma on SAP Business Technology Platform
url: https://blogs.sap.com/2022/12/19/how-to-relocate-an-existing-app-running-on-your-kubernetes-cluster-to-kyma-on-sap-business-technology-platform/
source: SAP Blogs
date: 2022-12-20
fetch_date: 2025-10-04T01:58:55.026849
---

# How to relocate an existing app running on your Kubernetes Cluster to Kyma on SAP Business Technology Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to relocate an existing app running on your Ku...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158412&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to relocate an existing app running on your Kubernetes Cluster to Kyma on SAP Business Technology Platform](/t5/technology-blog-posts-by-sap/how-to-relocate-an-existing-app-running-on-your-kubernetes-cluster-to-kyma/ba-p/13551871)

![mangeshpise](https://avatars.profile.sap.com/3/c/id3cb00775f418fcc9e7a52a6b3ed81fe1dff09089a9df8d25937baeb7b95559e1_small.jpeg "mangeshpise")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mangeshpise](https://community.sap.com/t5/user/viewprofilepage/user-id/3250)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158412)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158412)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551871)

‎2022 Dec 19
4:58 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158412/tab/all-users "Click here to see who gave kudos to this post.")

1,642

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (1)

At its core, Kyma is an open-source project that was initially launched in July 2018 by SAP. The basic premise of this project was to provide an enterprise-grade developer experience (DX) on the Kubernetes platform so that they can build extensions to other enterprise applications. Kyma is a runtime that comes standard with building blocks comprised of tools such as Istio - which enables secure traffic management, Kubeless - the serverless framework, Prometheus & Grafana - providing observability via monitoring and alerting, Luigi - which provides a full- fledged Kyma UI for developers and administrators to manage the deployments and the platform itself, etc.

Where Kyma became powerful for SAP customers, is when SAP decided to provide it as a supported platform on the SAP Business Technology Platform (SAP BTP). Kyma sits next to Cloud Foundry runtime and the recently-announced ABAP Cloud runtime. All of these together provide a wide array of choices for developers to safely, reliably, and effortlessly extend business capabilities from large enterprise applications, such as SAP S/4HANA solutions, SAP Customer Experience solutions, SaaS solutions - such as SAP SuccessFactors, SAP Ariba, etc.

## The Challenge

In this blog post, we are going to put Kyma through a test. We are going to find out how easy it is to relocate an existing containerized application that runs on an existing Kubernetes cluster to the Kyma runtime on SAP BTP. But why this challenge?

Here’s why - many organizations have extended their business processes outside the core ERP platforms as a side-by-side application. That’s good, or at least, better than modifying the core itself! However, over a while, such extensions grow into a “thing of its own”. These side-by-side applications eventually need dedicated development teams, testing cycles, environment dependencies, cloud infrastructure requirements, etc. That increases the overall Total Cost of Ownership (TCO). So, how do we protect the core ERP by using a side-by-side architecture pattern, and yet keep the TCO to the minimum?

The answer is - by keeping the focus on the extension itself without having to spend additional time, money, and effort in managing the platform on which you build the extension. In other words, low-TCO extensions can be built by leveraging a platform like Kyma that -

1. enables developers to deploy their containerized applications on Kubernetes, and

2. which comes in-built with platform management services (read as, managed services provided by SAP as a part of SAP BTP).

Thus, within the scope of this blog post - developers should be able to relocate their existing side-by-side applications running on Kubernetes, without any re-factoring, re-architecting or re-platforming requirements. That’s what we will put Kyma to the test for in this blog post.

## The App in Question

The app in question which is currently running on a Kubernetes cluster, is a 3-tier application with MongoDB as the database, Microservices written in NodeJS, and the frontend UI written in AngularJS. The application is a demo eCommerce store that lists products on its landing page where a user can add items to a cart and eventually place an order. There is also a page to view all the orders placed by the users.

|
 ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-17-at-3.31.56-PM.png) |
 ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-17-at-3.32.15-PM.png) |

|
 Fig. 1. Demo app: Product Catalog and Orders | |

Let me describe the architecture layer by layer, in detail, below:

|
 ![](/legacyfs/online/storage/blog_attachments/2022/12/arch.001.png) |

|
 Fig. 2. Microservices Architecture |

### Microservices / Middleware

The NodeJS applications for providing product and order APIs are containerized using Docker images and are stored in the Docker Hub’s container registry (a place where all images are stored, versioned/tagged, and later retrieved to put to use).

For deploying these microservices on the Kubernetes platform as Pods (smallest deployable units that can be scaled into multiple replicas), the Docker images referred to above are pulled at deploy-time and instantiated to create a runtime application. Kubernetes Services are then built atop these Pods so they can load balance user requests between one or more Pod replicas.

However, do note that all these replicas and services run in Kubernetes’ internal cluster network. That means none of the Pods or Services can be accessed from your browser (or the internet) for now. This is where we add a Kubernetes object called Ingress. Ingress provides an externally available name and also serves as a proxy to rewrite URLs to point them to appropriate Services. For example, in our application, the API endpoints containing https://`api-endpoint/orders/` would route to Kubernetes Services connecting to the **Order** Pods, while those containing https://`api-endpoint/products/` would route to **Product** Pods.

### Database Layer

In this application, we decided to use the official docker image for MongoDB, called mongo. Hence, all we need is a Kubernetes deployment object to pull the mongo Docker image and configure it using environment variables that hold the initializing DB username and password (as provided in the Docker image documentation).

However, to support the secure storage and retrieval of the username and password, we leverage Kubernetes Secrets.

What about persistence? Since MongoDB would need some physical storage to persist user ...