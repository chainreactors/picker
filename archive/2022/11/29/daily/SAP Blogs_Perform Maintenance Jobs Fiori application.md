---
title: Perform Maintenance Jobs Fiori application
url: https://blogs.sap.com/2022/11/28/perform-maintenance-jobs-fiori-application/
source: SAP Blogs
date: 2022-11-29
fetch_date: 2025-10-03T23:58:57.004809
---

# Perform Maintenance Jobs Fiori application

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Perform Maintenance Jobs Fiori application

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51159&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Perform Maintenance Jobs Fiori application](/t5/enterprise-resource-planning-blog-posts-by-sap/perform-maintenance-jobs-fiori-application/ba-p/13555743)

![VikasGupta_ASM](https://avatars.profile.sap.com/0/e/id0e0dd32c7b6d562dfe2698455a16f22bfc03fb1d502e34e36652a90da1c2cbad_small.jpeg "VikasGupta_ASM")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[VikasGupta\_ASM](https://community.sap.com/t5/user/viewprofilepage/user-id/375553)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51159)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51159)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555743)

‎2022 Nov 28
7:12 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51159/tab/all-users "Click here to see who gave kudos to this post.")

13,279

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Asset Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Asset%2520Management/pd-p/a6cdc8a5-6d3b-485f-9ece-cbea17de666b)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)

* [SAP S/4HANA Cloud Public Edition Asset Management

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BAsset%2BManagement/pd-p/a6cdc8a5-6d3b-485f-9ece-cbea17de666b)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)

View products (2)

## **Overview**

During execution of the maintenance work, the maintenance technician requires different information which helps him/her in performing the jobs. This starts from understanding the job details, having access to descriptions, documents, manuals etc. During or after the execution of the job, the technician needs to record the efforts spent on the jobs, he/she might need to perform goods movements or record measurement data. Once work is done, the maintenance technician can enter data about the underlying failure so that it can be used for the later analysis.

Here in this blog, I would like to draw your attention to the new Perform Maintenance Jobs Fiori app(F5104A) , which is the one stop shop solution for maintenance technicians to perform most of the activities needed for their day-to-day maintenance jobs.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture13-5.png)

The initial app was delivered with SAP S/4HANA Cloud 2105 and with SAP S/4HANA 2021 releases and has been enhanced with multiple capabilities in the recent releases. The blog explains the scope of the app as of SAP S/4HANA Cloud 2208 release.

This app is a successor app for Display Job List and Confirm Jobs apps which are been deprecated from S/4HANA Cloud 2208 release onwards.

You can use the following link to access the details of this app from Fiori Apps library <https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F5104A')/S32> The link gives you information on the technical catalog and business role necessary to access the app.

***In the context of the app the term job refers to a maintenance order operation or sub-operation which is ‘ready to be executed’ by the assigned work center / person responsible. A job is ‘ready to be executed’ when it has been dispatched for execution for the orders that follows the phase model-based approach or once the order is released when the order does not follow phase model-based approach.***

### **Prerequisites for using Perform maintenance jobs app:**

For maintenance orders that follow the best practice phase model approach related jobs will be available in the list once the underlying maintenance order operations are being dispatched from the ‘Scheduling’ phase to the ’Execution’ phase. Please refer to the following picture depicting the phases of the Reactive Maintenance process, which is one of the best practice scenarios which follows the phase model. For more information on phase model, you can refer: [SAP Help documentation for Maintenance Process Phases](https://help.sap.com/viewer/2dfa044a255f49e89a3050daf3c61c11/LATEST/en-US/57372b93c62943718032b05fe5551733.html)

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture15-6.png)

***The list will also include jobs related to maintenance orders not following the phase model. For such jobs, it should have been released. For such jobs, subphase details will not be available. This is supported from SAP S/4HANA 2022 releases onwards.***

## **Perform Maintenance** **Jobs App**

As maintenance technician when you login and see the Perform Maintenance Jobs tile, it shows the count of jobs that are still open and to be executed by maintenance technician and his/her team. Once the application is launched, by default you see the list of outstanding Jobs.

App has following capabilities:

+ Identify outstanding jobs that need to be performed.

+ Self-assign jobs that are yet to be assigned.

+ Quick confirmation of the jobs from the list page.

+ Assess all information required to perform a job along with the reference documents linked to the order, operation, equipment, or functional location levels.

+ Record the progress of the work being performed and view confirmation data.

+ Record malfunction information.

+ Issue and return planned goods.

+ Issue goods that were not added previously into the order.

+ Save measurement for an object associated at order header, job, object list etc.

+ Upload and attach documents to operation or to order header.

###

### **List page**

The list of available filters allows the maintenance technician to plan his/her jobs better which need to be executed during the day, week and so on. It is possible to fine tune the list page to suit his/her needs and even set them as screen variants. A few important filters include ‘Responsibility,’ ‘Subphase,’ ‘Technical object,’ ‘Order’ etc.

In the standard variant, these jobs are sorted according to the Latest Scheduled Finish field in descending order so that the jobs that are nearing their scheduled finish time appear at the top. The jobs that are not yet assigned can be viewed (or accessed) by selecting any one of the values from the Responsibilities filter such as ‘Mine and to be assigned in my team’ or ‘To be assigned in my team.’

You can use any of the following values of the Responsibilities filter:

+ **All Jobs:** This filter shows all the jobs that are available for execution.

+ **Mine and My team's:** This filter shows all the operations that belong to your team and are already assigned to you or any other team member. It excludes all the operations that are yet to be assigned to anyone from...