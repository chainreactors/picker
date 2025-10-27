---
title: Data Transfer for Cloud ALM for Service
url: https://blogs.sap.com/2022/12/21/data-transfer-for-cloud-alm-for-service/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:17.830508
---

# Data Transfer for Cloud ALM for Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Data Transfer for Cloud ALM for Service

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163713&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Data Transfer for Cloud ALM for Service](/t5/technology-blog-posts-by-sap/data-transfer-for-cloud-alm-for-service/ba-p/13567744)

![Ulrike_Hormann](https://avatars.profile.sap.com/e/0/ide03b7ea69d78bca62fc452e395b9e2b9a4e37585242ed6e44fcca7e82578747e_small.jpeg "Ulrike_Hormann")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Ulrike\_Hormann](https://community.sap.com/t5/user/viewprofilepage/user-id/72191)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163713)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163713)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567744)

‎2022 Dec 21
1:26 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163713/tab/all-users "Click here to see who gave kudos to this post.")

9,230

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

# Initial Situation

You want to understand the details about how data will be transferred between SAP and your Cloud ALM tenant.

# Why

Cloud ALM for Service is the single central collaboration platform for all service related activities. It allows customers and SAP to collaborate during the preparation, execution and follow up for all services that are delivered within SAP service contracts.

Collaboration requires the exchange of information. To achieve this, there are SAP internal applications that run on SAP internal tenants. This is where the SAP service consultants maintain their information relevant for a service delivery. Information from these SAP internal tenants is transferred to the customer's cloud ALM tenant where the customer maintains the service delivery relevant information.

![](/legacyfs/online/storage/blog_attachments/2022/12/ISDHub_2.png)

This data exchange is initially active, but can be deactivated via a customer incident on component SV-CLM-SD. For details, please see [SAP Note 3401303](https://me.sap.com/notes/3401303).

# Some clarifications up front

## Prerequisites

Data Transfer for Cloud ALM for Service only happens if the data transfer is active.

## What kind of data is transferred

Only data related to service deliveries for the customer number associated with your Cloud ALM tenant is transferred. This means:

* No data for other customer numbers is touched, meaning data meant for your Cloud ALM tenant is only transferred into your tenant and no other Cloud ALM tenant will receive your service information.

* Data from your Cloud ALM tenant is only transferred back to SAP, not to any other customer tenant.

* Only service related data is transferred (meaning data accessible via Cloud ALM for Service). Data from Cloud ALM for Implementation and Operation is not transferred

## What about the size of the data

Service information is persisted in your Cloud ALM tenant and allocates space there in the HANA DB. It thus contributes to the size of your Cloud ALM tenant. However, the information for the service deliveries themselves is typically very small. The objects that allocate a lot of space are screenshots and attachments. These are not stored in the HANA DB, but in a separate Document Management system and do NOT contribute to the size of your Cloud ALM tenant.

## What happens when the data transfer gets deactivated

As of that moment, the data transfer between SAP and your Cloud ALM tenant no longer happens. Data that has already been transferred does not get deleted. All service information becomes read-only. You can no longer change anything in Cloud ALM for Service and you cannot upload documents any longer.

# Service related Data Transfer

## SAP → Your Cloud ALM Tenant

SAP will sends the following information to your Cloud ALM tenant:

* List of scheduled service deliveries

  + Name and dates of the upcoming service deliveries

* Service Details per service delivery

  + Scope

  + Delivery Team

  + System information

  + Service status

* Preparation tasks that were created by SAP that you as a customer are supposed to work on

* Notes that were created by SAP that are relevant for you

  + might include meeting minutes

* Attachments that were created by SAP that are relevant for you

  + Physically, the attachments are stored in a DMS instance that is also accessible by customers. What is transferred is the link to these attachments and the entitlement to access them. The same is true for all pictures stored in issues / actions / preparation tasks / notes / service results.

* Service Results that were created and published by SAP

  + Service results that are still being worked on (status "Draft") are not replicated

* Issues and Actions that were created and published by SAP

  + Issues and actions that are still being worked on (status "Draft") are not replicated

You will get this information into your Cloud ALM tenant regardless of whether or not you actively use Cloud ALM for Service.

## Your Cloud ALM Tenant → SAP

SAP synchronizes the following information from your Cloud ALM tenant back to SAP:

* Preparation tasks

  + Status changes you have made for preparation tasks for a service

  + All comments you entered for preparation tasks for a service

  + If you assign a preparation task to a user, that assignment information is NOT replicated back to SAP.

  + *Please note that you can only change existing preparation tasks, but not create new tasks.*

* Notes

  + Notes that you have created for a service

  + Comments that you have provided for notes

* Attachments

  + documents that you have uploaded for a service

  + Physically, the attachments are stored in a DMS instance that is also accessible by SAP. What is transferred is the link to these attachments and the entitlement to access them.

* Issues and Actions

  + Changes that you have made to issues and actions

  + If you assign an issue or an action to a user, that assignment information is NOT replicated back to SAP.

All of this information requires active involvement from your side. If you do not change any information in Cloud ALM for Service of your tenant, no information is replicated back to SAP.

# Further Information

In case you want to try out Cloud ALM for Service, please check out the[Cloud ALM Demo](https://support.sap.com/en/alm/demo-systems/cloud-alm-demo-system.html) tenant.

For an overview about how to use Cloud ALM for Service, see the blog “[Service Delivery with Cloud ALM](https://blogs.sap.com/2022/05/06/service-delivery-with-cloud-alm/)“.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [SAP Cloud ALM for service](/t5/tag/SAP%20Cloud%20ALM%20for%20service/...