---
title: Event Driven Architecture with Event Mesh – Part-1
url: https://blogs.sap.com/2022/12/04/event-driven-architecture-with-event-mesh-part-1/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:30:58.148026
---

# Event Driven Architecture with Event Mesh – Part-1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Event Driven Architecture with Event Mesh - Part-1

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159497&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Event Driven Architecture with Event Mesh - Part-1](/t5/technology-blog-posts-by-sap/event-driven-architecture-with-event-mesh-part-1/ba-p/13555059)

![Avinash_Vaidya](https://avatars.profile.sap.com/6/f/id6f2d5310e825aaf89f8200d77951ac7bb99081af33cdae929f9121209606b899_small.jpeg "Avinash_Vaidya")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Avinash\_Vaidya](https://community.sap.com/t5/user/viewprofilepage/user-id/120687)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159497)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159497)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555059)

‎2022 Dec 04
3:25 AM

[21
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159497/tab/all-users "Click here to see who gave kudos to this post.")

13,942

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

## Introduction

This is the continuation of my previous [blog](https://blogs.sap.com/?p=1651088&preview=true), where I explained how to create entity relationships in CAP/CDS with a working example of a very useful scenario observed in enterprise applications.

In this blog, I will take the same use case further by enhancing and integrating it SAP Event Mesh.

### What is Event-Driven-Architecture (EDA) and Why we need it?

As enterprises grow in size, there arises a need to cater to varied software applications, systems and processes to perform daily tasks in an automated and optimized way. As number of software applications grow, organization must develop a communication strategy but without overhead on the systems and the underlying infrastructure. As systems evolve, point to point communication can become bottleneck in many scenarios. Decoupled/Asynchronous communication helps to improve the performance and scale the software landscape.

That is where the event-driven-architecture comes to the rescue.

I will highly recommend going through this 10 minutes [tutorial](https://developers.sap.com/tutorials/cp-enterprisemessaging-learn-messaging-concepts.html). to understand the basics of EDA.

A typical use case in an organization can be diagrammatically explained below

|
 ![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-27-at-4.02.15-PM-1.png) |

Figure-1

In the above diagram,

1. A change in S/4 HANA creates a data event.

2. Event is queued in Event Mesh.

3. Business application consumes the event from the queue to get data updates.

All this is event driven and helps to reduce the business applications to constantly poll or request for data irrespective of any change. Think about it from a large scale perspective and you will empathize the benefits.

### What is an Event and what are the types of events?

Event is a change in the state of the business entity in a software system.

**Types:**

1. **Notification Events** - In this type of event, source system triggers a notification which indicates data change and the target system which is interested in this change, will then invoke a API call to get the complete set of data from source system.

2. **Data Events** - In this type of event, source system publishes the complete data set of the business entity which has changed which is used by the target system.

Of course, there are some pros and cons of the above two approaches. One should take a calculated decision based of the use case to choose any one of the above event strategy.

For the scope of this blog, I am going to showcase a data event.

Now as we had a brief introduction about event driven architecture, purpose and types, let us dive into our hands on part of the blog.

Let us break down the tasks which I am going to perform.

1. Design thinking.

2. Create an event mesh instance on SAP BTP and create a queue.

3. Quick test with POSTMAN.

4. Integrate event mesh with CAP project and send payload.

Sounds cool right?

### Task-1: Design thinking

Take a look at a simple high level integration diagram.

|
 ![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-27-at-4.27.44-PM.png) |

*Figure-2*

I have divided the complete use case in 3 parts. We are going to perform parts A and B in this hands on.

**Part-A**: Integrating event mesh instance in CAP project.

**Part-B**: This is the pre-cursor for Part-A, where we will set up event mesh service on cloud and make it ready to be consumed by consumer (in this case it is the CAP project)

**Part-C**: I will enhance this project to create a consumer for the messages and that will be an API exposed from **Integration Suite**. Part-C is future scope. So, STAY TUNED for my next blog.

### Task-2: Create an event mesh instance on SAP BTP and create a queue

1. Login to your sub account.

2. Go to your dev space

3. On right hand side pane, select "Service Marketplace" under "Services"

   |
    ![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-01-at-7.46.36-AM.png) |

   *Figure-3*

4. Click "Create".

5. Add the below service descriptor with unique namespace, topic and queue rules.

   ```
   {

       "options": {

           "management": true,

           "messagingrest": true,

           "messaging": true

       },

       "rules": {

           "topicRules": {

               "publishFilter": [

                   "${namespace}/*"

               ],

               "subscribeFilter": [

                   "${namespace}/*"

               ]

           },

           "queueRules": {

               "publishFilter": [

                   "${namespace}/*"

               ],

               "subscribeFilter": [

                   "${namespace}/*"

               ]

           }

       },

       "version": "1.1.0",

       "emname": "taskmanager-events",

       "namespace": "sap/taskmanager-events/event-mesh"

   }​
   ```

6. This will create a message client with ***taskmanager-events*** as the inst...