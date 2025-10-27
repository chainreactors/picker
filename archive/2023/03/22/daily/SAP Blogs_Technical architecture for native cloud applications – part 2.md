---
title: Technical architecture for native cloud applications – part 2
url: https://blogs.sap.com/2023/03/21/technical-architecture-for-native-cloud-applications-part-2/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:15:02.183008
---

# Technical architecture for native cloud applications – part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Technical architecture for native cloud applicatio...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158360&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Technical architecture for native cloud applications – part 2](/t5/technology-blog-posts-by-sap/technical-architecture-for-native-cloud-applications-part-2/ba-p/13551751)

![i038615](https://avatars.profile.sap.com/d/8/idd8696b129158bc69c58baefdf1562c92e5c7291f0046072884c7a00fa5def250_small.jpeg "i038615")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[i038615](https://community.sap.com/t5/user/viewprofilepage/user-id/70960)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158360)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158360)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551751)

‎2023 Mar 21
6:27 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158360/tab/all-users "Click here to see who gave kudos to this post.")

3,605

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (2)

This is the 2nd part of the 4 blog posts about the technical architecture of native cloud applications:

* [Part 1 – Software architecture trends](https://blogs.sap.com/2023/03/15/technical-architecture-for-native-cloud-applications-part-1/)

* [Part 2 – How to build a scalable application - From 1 to 10K users (this blog post)](https://blogs.sap.com/2023/03/21/technical-architecture-for-native-cloud-applications-part-2/)

* P[art 3 – How to build a scalable application - From 10K to 100.000K users](https://blogs.sap.com/2023/05/11/technical-architecture-for-native-cloud-applications-part-3/)

* Part 4 – How to build a scalable application - Up to Million users

In the previous blog post we performed a very short review of the different software architecture trends. This post will detail how to build a scalable, reliable, and performant large-scale application step-by-step. Starting with a basic architecture, we'll apply patterns to scale it up to millions of users and we will explain how these patterns are also used by SAP to develop our own applications.

## How to build a scalable application - From 1 to 10K users

There is a well-known maxim in software engineering ***"Premature optimization is the root of all evil"*** , it means that trying to optimize code before it's necessary can lead to wasted time and effort, and may even make the code more complex and harder to maintain.

### Version 1.0 - A simple monolithic application

Starting with a monolithic application is a valid approach for building simple applications with a small user base. Deploying a monolith on a hyperscaler can provide immediate benefits such as scalability, high availability, and reduced maintenance costs.

There are plenty of famous examples of huge applications that started as very simple and tiny monoliths, probably one of the most well know example is the [origins of Google](https://en.wikipedia.org/wiki/History_of_Google) and their first server made of Legos but also many of the SAP SaaS applications like Concur started as a simple monolith.

In this initial monolithic phase, the front-end layer, application layer, and database layer all run on the same server.

![](/legacyfs/online/storage/blog_attachments/2023/03/1-monolith-2.jpg)

### Version 1.1 - Split the different layers (3-Tier architecture)

Let’s say you want to scale up to 1000 users... A simple approach would be to split the different layers of ourmonolith into different VMs or containers moving towards a 3-tier architecture.

This will allow you to scale vertically  (a.k.a scale-up) each layer independently and allocate resources where they are needed most, while keeping costs under control. For a startup company using open source software maybe it’s not so relevant but for enterprise software, this is particularly important since it is often licensed by cores, and dedicating too many cores can result in overspending.

Hyperscalers offer various types of virtual machines (VMs) based on your computing requirements, such as general purpose, compute-optimized, memory-optimized, and storage-optimized. This allows you to tailor your resource allocation even further for each layer of your application.

At this early stage, relational databases still offer several advantages and are a sufficient solution compared to other more specialized database types like hierarchical, key-value or document databases (also known as NoSQL - Not Only SQL). While these specialized databases have their own advantages, they may not provide the flexibility required for the current needs of the application.

This is particularly important for enterprise software, such as an ERP, where leveraging the ACID principles of relational databases is crucial to ensuring data consistency.

![](/legacyfs/online/storage/blog_attachments/2023/03/3-RDBMS.jpg)

### Version 1.2 - Vertical vs Horizontal scalability

Merely scaling up the different layers will not suffice as current hardware performance does not scale linearly. Moreover, application servers typically cannot take advantage of extremely large servers/VMs, and the majority of applications will offer better performance/price ratios on smaller VMs or commodity Intel/AMD 2-socket servers

In this case, a scale-out approach for the application layer is the next step, which involves adding more VMs or containers instead of increasing the size of the existing ones.

A desirable collateral effect of additional application servers is that it improves the reliability of your application by eliminating a Single Point of Failure (SPOF). However, this improvement comes at a cost. You will need a Load Balancer to distribute the workload among multiple application servers.

There are mainly three types of load balancers, depending on the OSI Network level they filter (Layer 3, Layer 4 or Layer 7). At this stage, we need an Application Load Balancer (Layer 7) to route all the application traffic (HTTP) and act as a reverse proxy.

Some popular choices for Application Load Balancers are Azure FrontDoor, Amazon Elastic LB, NGINX, and SAP WebDispatcher (which we usually use at SAP).

![](/legacyfs/online/storage/blog_attachments/2023/03/4.-Load-Balancer.jpg)

Scale-out and Load Balancing

###

### Version 2.0 - Stateless vs Stateful

if you are still looking for scalability, the first critical decision yo will need to take as an architect is which type of application you are going to desig...