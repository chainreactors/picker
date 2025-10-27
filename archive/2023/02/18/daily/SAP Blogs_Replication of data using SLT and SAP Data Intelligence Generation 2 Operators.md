---
title: Replication of data using SLT and SAP Data Intelligence Generation 2 Operators
url: https://blogs.sap.com/2023/02/17/replication-of-data-using-slt-and-sap-data-intelligence-generation-2-operators/
source: SAP Blogs
date: 2023-02-18
fetch_date: 2025-10-04T07:22:25.155513
---

# Replication of data using SLT and SAP Data Intelligence Generation 2 Operators

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Replication of data using SLT and SAP Data Intelli...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157834&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Replication of data using SLT and SAP Data Intelligence Generation 2 Operators](/t5/technology-blog-posts-by-sap/replication-of-data-using-slt-and-sap-data-intelligence-generation-2/ba-p/13550502)

![pranchal](https://avatars.profile.sap.com/d/9/idd936d10f747ad6dd299e635e492e91d27204be116624453d5a992f6ef49637b8_small.jpeg "pranchal")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[pranchal](https://community.sap.com/t5/user/viewprofilepage/user-id/817395)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157834)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157834)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550502)

‎2023 Feb 17
4:52 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157834/tab/all-users "Click here to see who gave kudos to this post.")

8,857

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [SAP Landscape Transformation replication server](https://community.sap.com/t5/c-khhcw49343/SAP%2520Landscape%2520Transformation%2520replication%2520server/pd-p/67838200100800005841)

* [SAP Landscape Transformation replication server

  SAP Landscape Transformation](/t5/c-khhcw49343/SAP%2BLandscape%2BTransformation%2Breplication%2Bserver/pd-p/67838200100800005841)
* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)

View products (2)

## Introduction

SAP Landscape Transformation Replication Server (SLT) is a product that allows users to replicate data between systems. While there are a lot of blogs out there covering SLT in general, I will focus on how SLT can be used with SAP Data Intelligence (DI) for replication.

SAP Data Intelligence is a product that is used to organize a heterogenous data system landscape from SAP systems and third-party systems. It is the main tool that I work with on the Data Management Team in Ireland. Within DI you have the option to build pipelines using Generation 1 Operators or Generation 2 Operators.

If you are using Generation 1 Operators, please have a look at this excellent blog by Martin Boeckling ([https://blogs.sap.com/2021/07/20/replication-and-filtering-of-data-by-using-slt-and-sap-data-intelli...](https://blogs.sap.com/2021/07/20/replication-and-filtering-of-data-by-using-slt-and-sap-data-intelligence/)).

In this blog, I will give you a step-by-step walkthrough of how you can build a pipeline in DI to replicate data from an SLT table and store it in any target using Generation 2 Operators.

## Prerequisites

To follow this blog, you will need a SLT system (either a standalone DMIS system or a SLT version on an SAP S/4HANA system) and a DI system (on-prem or cloud) with an ABAP connection to the SLT system you wish to use. This SAP Note (<https://launchpad.support.sap.com/#/notes/2835207>) contains details of how to connect the two systems.

## SLT

### Create your configuration

In order to connect a SLT system to a DI system you must create a configuration within SLT using the SLT cockpit which can be accessed with the LTRC transaction. By clicking the paper icon (in the red square below), you can create the configuration in the pop-up window that follows.

![](/legacyfs/online/storage/blog_attachments/2023/02/1_SLT_cockpit.png)

SLT Paper Icon

Follow this blog ([https://blogs.sap.com/2019/10/29/abap-integration-replicating-tables-into-sap-data-hub-via-sap-lt-re...](https://blogs.sap.com/2019/10/29/abap-integration-replicating-tables-into-sap-data-hub-via-sap-lt-replication-server/)) to create the connection. At the end be sure to check you have configured everything correctly in the review screen. If everything is as necessary, click create to create the configuration.

![](/legacyfs/online/storage/blog_attachments/2023/02/2_SLT_Create.png)

SLT Create Button

Once the configuration has been created, you can access an overview and any current replications related to it using the glasses icon.

![](/legacyfs/online/storage/blog_attachments/2023/02/3_DEMO_Config.png)

SLT Replication Details

### Table replication

For this blog, we will use the SFLIGHT table to demonstrate this replication scenario. The table appears as follows within SLT:

![](/legacyfs/online/storage/blog_attachments/2023/02/4_SFLIGHT.png)

SFLIGHT Table

## SAP Data Intelligence

### Integrate SLT configuration within SAP Data Intelligence

Now that we have our SLT Configuration made, let’s look at building the replication pipeline in DI. For this, we are required to use the Modeler tile from the Launchpad. In order to use this tile and to be able to view the replication results, we must have the following policies assigned to the user we wish to use: app.datahub-app-data.fullAccess, sap.dh.member, sap.dh.developer. (<https://launchpad.support.sap.com/#/notes/2981615>)

![](/legacyfs/online/storage/blog_attachments/2023/02/5_Launchpad.png)

Data Intelligence Launchpad

We will now connect to the SLT system, replicate the data to a file in DI and view the results.

### Build your pipeline

For this, we will use the Read Data from SAP System Operator which can be accessed from the “Operators” tab on the left, under the ABAP category. By right clicking the operator and selecting the view documentation option, you can read the details of the operator and its parameters.

![](/legacyfs/online/storage/blog_attachments/2023/02/6_Read_Data.png)

Read Data from SAP System Operator

Now to configure the operator. To do this you can either right click and choose the open configuration option or you can use the shortcut that appears when you select the operator.

![](/legacyfs/online/storage/blog_attachments/2023/02/7_Open_Config.png)

Open Configuration of Operator

This will open the configuration panel where we must specify the ABAP connection to be used to connect to out SLT system and choose the version of operator we wish to use.

![](/legacyfs/online/storage/blog_attachments/2023/02/8_ABAP_Connection.png)

ABAP Connection for SLT

![](/legacyfs/online/storage/blog_attachments/2023/02/9_Specify_Version.png)

Specify Operator Version

Once this has been specified, we will be able to see additional fields in the configuration panel. Namely, Object Name and Transfer Mode. When specifying the Object Name, we will need to select the Mass Transfer ID we previously created and once we select that, we can search for the SFLIGHT table within it.

![](/legacyfs/online/storage/blog_attachments/2023/02/10_Select_Table.png)

Selecting the Table

Next, we must specify the Transfer Mode we wish to use for our pipeline. Here we have three options: Initial Load, Delta Load and Replication. These determine ...