---
title: Design Patterns for Microservices
url: https://blogs.sap.com/2023/02/16/design-patterns-for-microservices/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:52:03.077134
---

# Design Patterns for Microservices

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Design Patterns for Microservices

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157714&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Design Patterns for Microservices](/t5/technology-blog-posts-by-sap/design-patterns-for-microservices/ba-p/13550122)

![former_member123446](https://avatars.profile.sap.com/former_member_small.jpeg "former_member123446")

![Employee](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Employee")
[former\_member123446](https://community.sap.com/t5/user/viewprofilepage/user-id/123446)

Employee

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157714)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157714)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550122)

‎2023 Feb 16
11:56 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157714/tab/all-users "Click here to see who gave kudos to this post.")

4,936

## Microservices Design Patterns:

* Aggregator

* API Gateway

* Chained or Chain of Responsibility

* Asynchronous Messaging

* Database or Shared Data

* Event Sourcing

* Branch

* Command Query Responsibility Segregator

* Circuit Breaker

* Decomposition

Microservice architecture has become the de facto choice for modern application development. Though it solves certain problems, it is not a silver bullet. It has several drawbacks and when using this architecture, there are numerous issues that must be addressed. This brings about the need to learn common patterns in these problems and solve them with reusable solutions. Thus, design patterns for microservices need to be discussed. Before we dive into the design patterns, we need to understand what principles microservice architecture has been built:

1. Scalability

2. Availability

3. Resiliency

4. Independent, autonomous

5. Decentralized governance

6. Failure isolation

7. Auto-Provisioning

8. Continuous delivery through DevOps

Applying all these principles brings several challenges and issues. Let's discuss those problems and their solutions.

## 1. Decomposition Patterns

### a. Decompose by Business Capability

#### **Problem**

Microservices is all about making services loosely coupled, applying the single responsibility principle. However, breaking an application into smaller pieces has to be done logically. How do we decompose an application into small services?

#### **Solution**

One strategy is to decompose by business capability. A business capability is something that a business does in order to generate value. The set of capabilities for a given business depends on the type of business. For example, the capabilities of an insurance company typically include sales, marketing, underwriting, claims processing, billing, compliance, etc. Each business capability can be thought of as a service, except it’s business-oriented rather than technical.

### b. Decompose by Subdomain

#### **Problem**

Decomposing an application using business capabilities might be a good start, but you will come across so-called "God Classes" which will not be easy to decompose. These classes will be common among multiple services. For example, the Order class will be used in Order Management, Order Taking, Order Delivery, etc. How do we decompose them?

#### **Solution**

For the "God Classes" issue, DDD (Domain-Driven Design) comes to the rescue. It uses subdomains and bounded context concepts to solve this problem. DDD breaks the whole domain model created for the enterprise into subdomains. Each subdomain will have a model, and the scope of that model will be called the bounded context. Each microservice will be developed around the bounded context.

**Note**: Identifying subdomains is not an easy task. It requires an understanding of the business. Like business capabilities, subdomains are identified by analyzing the business and its organizational structure and identifying the different areas of expertise.

### c. Strangler Pattern

#### **Problem**

So far, the design patterns we talked about were decomposing applications for greenfield, but 80% of the work we do is with brownfield applications, which are big, monolithic applications. Applying all the above design patterns to them will be difficult because breaking them into smaller pieces at the same time it's being used live is a big task.

#### **Solution**

The Strangler pattern comes to the rescue. The Strangler pattern is based on an analogy to a vine that strangles a tree that it’s wrapped around. This solution works well with web applications, where a call goes back and forth, and for each URI call, a service can be broken into different domains and hosted as separate services. The idea is to do it one domain at a time. This creates two separate applications that live side by side in the same URI space. Eventually, the newly refactored application “strangles” or replaces the original application until finally, you can shut off the monolithic application.

## 2. Integration Patterns

### a. API Gateway Pattern

#### **Problem**

When an application is broken down into smaller microservices, there are a few concerns that need to be addressed:

1. How to call multiple microservices abstracting producer information.

2. On different channels (like desktop, mobile, and tablets), apps need different data to respond to the same backend service, as the UI might differ.

3. Different consumers might need a different format for the responses from reusable microservices. Who will do the data transformation or field manipulation?

4. How to handle different types of Protocols some of which might not be supported by producer microservice.

#### **Solution**

![API gateway example](https://dz2cdn1.dzone.com/storage/temp/16147304-api-gateway-example.jpg)

An API Gateway helps to address many concerns raised by microservice implementation, not limited to the ones above.

1. An API Gateway is the single point of entry for any microservice call.

2. It can work as a proxy service to route a request to the concerned microservice, abstracting the producer details.

3. It can fan out a request to multiple services and aggregate the results to send back to the consumer.

4. One-size-fits-all APIs cannot solve all the consumer's requirements; this solution can create a fine-grained API for each specific type of client.

5. It can also convert the protocol request (e.g. AMQP) to another protocol (e.g. HTTP) and vice versa so that the producer and consumer can handle it.

6. It can also offload the authentication/authorization responsibility of the microservice.

### b. Aggregator Pattern

#### **Problem**

We have talked about resolving the aggregating data problem in the API Gateway Pattern. However, we will talk about it here holistically. When breaking the business functionality into several smaller logical pieces of code, it becomes necessary to think about how to collaborate the data returned by each service. This responsibility cannot be left to the consumer, as then it might need ...