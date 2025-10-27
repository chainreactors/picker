---
title: SAP Data Services Real time Jobs – Overview and Best Practices
url: https://blogs.sap.com/2023/02/16/sap-data-services-real-time-jobs-overview-and-best-practices/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:52:09.095083
---

# SAP Data Services Real time Jobs – Overview and Best Practices

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Data Services Real time Jobs - Overview and Be...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161581&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Data Services Real time Jobs - Overview and Best Practices](/t5/technology-blog-posts-by-sap/sap-data-services-real-time-jobs-overview-and-best-practices/ba-p/13561221)

![karansawant](https://avatars.profile.sap.com/5/1/id5198a1ddde98b24bb89ecc379f1f9cbfae7ddacc4d39434d48802b67aed16cf6_small.jpeg "karansawant")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[karansawant](https://community.sap.com/t5/user/viewprofilepage/user-id/123128)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161581)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161581)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561221)

‎2023 Feb 16
11:49 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161581/tab/all-users "Click here to see who gave kudos to this post.")

6,311

* SAP Managed Tags
* [Support Services](https://community.sap.com/t5/c-khhcw49343/Support%2520Services/pd-p/564272146051092002342823452713708)
* [SAP Data Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Services/pd-p/01200314690800000395)

* [SAP Data Services

  SAP Data Services](/t5/c-khhcw49343/SAP%2BData%2BServices/pd-p/01200314690800000395)
* [Support Services

  Services and Support](/t5/c-khhcw49343/Support%2BServices/pd-p/564272146051092002342823452713708)

View products (2)

**Purpose:**

The motivation behind this blog is to give an overview about the best practices when it comes to real time job processing within Data Services. For Batch Jobs, a numerous amount of performance tuning metrics, best practices are readily available and can be implemented with the references, whereas here real-time job optimization best practices have been jotted down based on real-world experience and researching various SAP resources.

Before we get into the actual best practices, tips and tricks let’s have a brief look into the working, components, Job design, models etc. of SAP Data Services Real-time Jobs.

## **Real-time Jobs:**

SAP Data Services can receive messages from ERP systems or Web applications and then can respond in no time with the data from a data cache or any other application

The Processing of data in a real time job can require the usage of a data cache. Either the real-time job can add additional data to the message coming from a data cache or the real-time job can load the message data to the data cache.

### **Role of an Access server in Real-time Jobs:**

The time a real-time job receives a message, it’s the Access Server which routes the message to a waiting process which then performs a set of operations with respect to the message type.

When the real-time job sends back a response, again the Access Server sends back a reply to the upstream application

Please refer to the following diagram for getting a better understanding on working of Data Services Real-time Jobs

![](/legacyfs/online/storage/blog_attachments/2023/02/9-11.png)

Real-time Job working

### **Real time Job Design:**

A real-time Job may contain a single data flow, multiple data flows, work-flows, scripts, conditionals, while-loops etc.

Both single and multiple data flows can contain the following objects:

* **A single real-time source and target:** XML message (required).

* **Sources and targets**: Files, XML files, and tables, including SAP tables and template tables.

* Transforms and queries.

In multiple data flows one additional objects can be included:

* **Memory tables:** Which can be used as staging tables to move data to the subsequent data flow in the job.

Additionally, **IDOCS** can also be used to create real time jobs.

### **Real time Jobs Models:**

**Single Data Flow model:**

As the name suggests with this model, we can create a real-time job using a singular data flow. It only includes a single message source and a single message target.

![](/legacyfs/online/storage/blog_attachments/2023/02/6-17.png)

Single Data Flow model

**Multiple data flow model**

The multiple data flow model enables you to create a real-time job using more than one data flows in real-time processing.

![](/legacyfs/online/storage/blog_attachments/2023/02/7-13.png)

Multiple Data Flow model

By using multiple data flows, the data in every message is processed completely in an initial data flow before it goes to processing when the subsequent data flows starts.

For example, if the data has 10 items, all 10 should be passing through the first data flow to either a staging table or a memory table before it gets passed to the subsequent data flow. This will allows you to have more control and enable you to collect all the data at any point of time.

**Now, you might ask why Real-time instead of Batch Job processing?**

1. **You need a response back to the source system when data is moved to the data warehouse for carrying out next steps depending upon business use cases**

2. **There is no fixed allotted time when jobs can be scheduled as per the incoming data in 3rd Party applications**

3. **You don’t want to wait for an internal trigger or for scheduling a job and want to execute the job faster (depending upon the amount of data) as it is only waiting for a response from the dedicated access server**

Now let's look into some of the best practices with real-time jobs:

# SAP Data Services Real-time Job Best Practices:

## **1.Usage of Memory Datastore for real time jobs**

Memory datastores are advantageous for processing real-time jobs that handle small amounts of data as they allow for instant access to the data.

Memory tables serve as blueprints for temporarily storing intermediate data. They cache data from hierarchical data files and relational database tables. SAP Data Services stores this cached data in memory, ensuring immediate access without the need to access the original source data.

The repository stores memory table schemas in a memory datastore, which differs from a typical database datastore that connects to an adapter, database, or an application.

**Advantages of Memory Datastore:**

* By caching intermediate data and allowing data flows to access it from the cache instead of the remote database, memory tables can enhance job performance, especially for jobs with multiple data flows. It's recommended to use memory tables when dealing with small amounts of data to achieve the best performance.

* In addition to enhancing job performance, memory tables also improve function performance in transforms. Functions such as Lookup\_Ext that don't require database operations can access data from memory directly, eliminating the need to read it from a remote database.

## **2. Utilizing separate Job servers for real-time and Batch jobs**

Whenever a web-service request is made it is forwarded to the Data Services Web service Layer with the help of HTTP/SOAP ...