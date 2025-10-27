---
title: Business Service Management in SAP Cloud ALM
url: https://blogs.sap.com/2023/05/01/business-service-management-in-sap-cloud-alm/
source: SAP Blogs
date: 2023-05-02
fetch_date: 2025-10-04T11:39:00.955154
---

# Business Service Management in SAP Cloud ALM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Business Service Management in SAP Cloud ALM

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162698&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Business Service Management in SAP Cloud ALM](/t5/technology-blog-posts-by-members/business-service-management-in-sap-cloud-alm/ba-p/13565335)

![Nilabh_](https://avatars.profile.sap.com/c/2/idc2091ea36ed9bbeafd6af0747a19a69e1a8172f446a049fb753d2f446abe1d8a_small.jpeg "Nilabh_")

[Nilabh\_](https://community.sap.com/t5/user/viewprofilepage/user-id/547183)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162698)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162698)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565335)

‎2023 May 01
3:46 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162698/tab/all-users "Click here to see who gave kudos to this post.")

41,047

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (2)

## Introduction:

As we know that SAP has come up with a cloud based ALM solution called SAP Cloud ALM. So, the SLA management of the business services and technical systems being one of the key feature for many customers. As many of the customers want a close observation and monitoring regarding the availability of their business services and availability. In most of the cases, service providers have an agreement regarding the availability of these business services and availability of the systems with their customers.

For this specific requirement, the functionality in SAP Solution Manager was called Service Availability Management. To know more about it, you can go through my previous blog regarding service availability management [Service Availability Management (SAM)](https://blogs.sap.com/2022/06/16/service-availability-management-in-sap-solution-manager-7.2/).

SAP Cloud ALM has come up with a better and advanced feature for the same purpose and is called Business Service Management.

**What is a Business Service?**

A business service can be used to abstract the technical names of cloud services or technical systems to a name which can be understood by business users. Each business service has a name and additional description. it contains a relationship to multiple cloud services or technical systems.

e.g. Hire to Retire, Lead to Cash, etc.

Business service is treated as a collection of cloud services and systems in SAP Cloud ALM.

**What is Business Service Management?**

Business Service Management is used to manage all the business services, systems, its availability and the SLA management, it's reporting and managing all its maintenance activities across the landscape.

It is basically a monitoring and reporting tool which can be used for the analytics parts as well.

SAP Basis/SAP SOLMAN/SAP Cloud ALM team are responsible for maintaining the availability of the systems across the landscape, hence a tool like business service management becomes important for them, and in this digital innovation age, where we are dealing with huge amount of data, hence the business services availability has become more critical than ever before.

It can be used for service providers in a way to present the data for the availability quarterly wise, yearly wise and monthly wise. Unlike Service availability in SAP SOLMAN 7.2, here in business service management, we can export the availability report in PDF form as well.

**What Business Service Management in SAP Cloud ALM offers?**

* Import of events triggered by SAP (maintenance, disruptions, degradation, communication events) including outbound API

* Automatic Triggering of alerts, notifications, operation flows, tickets, tasks, …

* Disruption/degradation events from monitoring to business service management

* Maintenance events from business service management to monitoring

* Maintenance and execution of customer specific events (single and reoccurring events)

* Service Level Agreement Management via Business Service Management

* Calculation and Consolidation (C & C) of availability against the service level agreement of business services and technical systems

* Embedded Service Level Reporting Dashboard

* Definition of service level objectives at business services level

* Define own events on cloud services and technical systems. This is especially useful for your on-premises systems, which are not covered by SAP in the Cloud Availability Center, as they are operated by the customer. Here you can define e.g., planned maintenances or downtimes for your own systems and communicate this to your end users.

* Provide an overview of the current status of all business services to the business users. This allows the users to see if any business functionality is currently affected by a downtime or if a planned maintenance will affect the business functionality in the near future.

* Show the service levels of your business services. You can summarize the service level of each business service on a monthly, quarterly or yearly view.

**Status Overview in Business Service Management:**

![](/legacyfs/online/storage/blog_attachments/2023/05/BSM-Status-Overview.png)

The home page displays the current overall status of each business service. The overall status is inherited from the services/systems which are assigned to the business service. Additionally, the following information is displayed:

* The date and time of the next planned maintenance

* The current duration of a disruption or degradation

* The remaining time for an ongoing maintenance

* The current service level quality

* Detail information about the business service and its current event

**Event Calendar in Business Service Management:**

![](/legacyfs/online/storage/blog_attachments/2023/05/BSM-Event-Calendar.png)

In the event calendar you can see all events of which were detected for a business service.

There are 2 views for the event calendar:

* The global event calendar shows all events for all business services in scope

* By clicking on the business service name in the global event calendar, you can display the
  business service specific event calendar. Here you can see the events for the selected business service and for all contained services and systems.

When you click on an event in the calendar, you can see the event details like:

* Event name, type, start/end time, duration, description.

* The action log with all changes that have been performed on the event (e.g.detection, update,resolution)

* Detail information about the affected services or systems

![](/legacyfs/o...