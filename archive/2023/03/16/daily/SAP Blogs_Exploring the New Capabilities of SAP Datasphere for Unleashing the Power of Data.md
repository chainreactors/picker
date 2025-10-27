---
title: Exploring the New Capabilities of SAP Datasphere for Unleashing the Power of Data
url: https://blogs.sap.com/2023/03/15/exploring-the-new-capabilities-of-sap-datasphere-for-unleashing-the-power-of-data/
source: SAP Blogs
date: 2023-03-16
fetch_date: 2025-10-04T09:44:37.409046
---

# Exploring the New Capabilities of SAP Datasphere for Unleashing the Power of Data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Exploring the New Capabilities of SAP Datasphere f...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160140&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Exploring the New Capabilities of SAP Datasphere for Unleashing the Power of Data](/t5/technology-blog-posts-by-members/exploring-the-new-capabilities-of-sap-datasphere-for-unleashing-the-power/ba-p/13550671)

![carlosbasto](https://avatars.profile.sap.com/a/c/idacace38f7bda335722ec7261a3326a57d35c99d1b4f82af6e9b153cf2a58e5f0_small.jpeg "carlosbasto")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[carlosbasto](https://community.sap.com/t5/user/viewprofilepage/user-id/209738)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160140)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160140)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550671)

‎2023 Mar 15
5:27 PM

[24
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160140/tab/all-users "Click here to see who gave kudos to this post.")

10,849

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

## **Context and Introduction**

In today's fast-paced business world, making sense of data can be a daunting task. But don't worry, SAP has got your back with their latest innovation: SAP Datasphere. This technology is designed to make your life easier by seamlessly integrating, cataloging, modeling, and virtualizing data from various sources, including SAP and non-SAP systems.

In this article, we'll take a closer look at three exciting features of SAP Datasphere:

* Application and Data Integration

* Semantic Modeling

* Data Cataloging and Quality

… and explain how they can help businesses to unleash the power of data.

## **1. Application and Data Integration**

Integrating data can be a challenge, especially when it comes to bringing together SAP and non-SAP data. However, with SAP Datasphere, you can seamlessly integrate data from both sources.

SAP Datasphere can help you to reduce integration complexity and get an integrated view of information, regardless of where it's stored or how it was designed. This means you can spend less time worrying about the technical aspects of integration and more time using your data to make informed decisions for your business.

So why not get started on our exciting journey by creating a [Replication Flow](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/25e2bd7a70d44ac5b05e844f9e913471.html?locale=en-US&q=%22replication%22) today? The first step is to establish a connection to your source system. Once you've done that, you'll be well on your way to simplifying your data replication process and saving time and effort.

### **1.1.** **Gathering SAP HANA Cloud Information and Initial Setup**

In our example, we'll need to work with the SAP HANA Cloud Instance (HCD). And the best part? Getting everything you need is super easy! All you need to do is "Copy SQL Endpoint". This nifty feature will provide you the host and port information required to connect to SAP HANA Cloud.

![](/legacyfs/online/storage/blog_attachments/2023/03/1-34.png)

SAP HANA Cloud SQL Endpoint

The next piece of the puzzle is your user and password. Simply add these details to your connection settings in SAP Datasphere, and you're good to go!

![](/legacyfs/online/storage/blog_attachments/2023/03/2-20.png)

User Management

To start, click on "User Management" and create your user. If you already have one, you can use it, just like in my case. For this article, you only need access to your own schema, but you can manage the privileges as you desire.

![](/legacyfs/online/storage/blog_attachments/2023/03/3-23.png)

DEVELOPER user

Now, let's look at what you can use in SAP HANA Cloud:

![](/legacyfs/online/storage/blog_attachments/2023/03/4-15.png)

SAP HANA Database Explorer

Our scope will be comprised of three (3) tables as follows:

* **ACTUAL\_DEMAND:** This table contains all historical demand units. This is the actual data I have.

* **DEMAND\_CHANNEL:** This table contains all the demand channels descriptions.

* **DEMAND\_PREDICTIONS:** This table provides predictions for a horizon of 15 days (note that this table will be used only for replication part of this blog, it could be used in further analytics developments but the idea was to demonstrate that you may compose a strategy for long-term modeling from the replication capabilities we'll experiment here).

### **1.2.** **Creating SAP HANA Cloud Connection in SAP Datasphere**

Before we proceed, it's important to note that at the time of writing, replication flows are only able to copy certain [source objects](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/25e2bd7a70d44ac5b05e844f9e913471.html?locale=en-US). Please keep this in mind as you begin using this feature.

* CDS views (in ABAP-based SAP systems) that are enabled for extraction.

* Tables that have a unique key (primary key)

* Objects from ODP providers, such as extractors or SAP BW artifacts.

Now, let's move into SAP Datasphere and [Create a Connection](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/c2165842082c43fc85bad9f0c97572bb.html?locale=pt-BRstate=PRODUCTION) to the SAP HANA Cloud. Simply use the information you have and you're good to go!

![](/legacyfs/online/storage/blog_attachments/2023/03/5-16.png)

SAP Datasphere Connection

Here you just use the information you already got and that’s it. Pretty simple, hun?

### **1.3.** **Creating a Replication Flow in SAP Datasphere**

The next step is to create a Replication Flow for copying the data from those 3 tables into SAP Datasphere. To do this, go to the "Data Builder."

![](/legacyfs/online/storage/blog_attachments/2023/03/6-12.png)

Data Builder

Notice that I don’t have any file in my environment! We’ll see new artifacts very soon in there. But for now, you may click on “Replication Flow” and the following screen will show up:

![](/legacyfs/online/storage/blog_attachments/2023/03/7-12.png)

New Replication Flow

**Note:** If you cannot see the "Replication Flow," check if you have the "SAP Datasphere Integrator" role.

To choose the SAP HANA Cloud connection, click on "Select Source Connection."

![](/legacyfs/online/storage/blog_attachments/2023/03/8-7.png)

Select Source Connection

When you select it, you'll need to choose the Source Container.

![](/legacyfs/online/storage/blog_attachments/2023/03/9-8.png)

Select Container

Select your own schema "DEVELOPER," and finally, by clicking on "Add Source Objects," pick the tables you want.

![](/legacyfs/online/storage/blog_attachments/2023/03/10-10.png)

Select Source Objects

In the next s...