---
title: Manage Workforce App – Deep Dive for IAM Experts (Part 1)
url: https://blogs.sap.com/2022/11/13/manage-workforce-app-deep-dive-for-iam-experts-part-1/
source: SAP Blogs
date: 2022-11-14
fetch_date: 2025-10-03T22:40:46.484295
---

# Manage Workforce App – Deep Dive for IAM Experts (Part 1)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Manage Workforce App - Deep Dive for IAM Experts (...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51006&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Manage Workforce App - Deep Dive for IAM Experts (Part 1)](/t5/enterprise-resource-planning-blog-posts-by-sap/manage-workforce-app-deep-dive-for-iam-experts-part-1/ba-p/13554810)

![anandkapadia](https://avatars.profile.sap.com/4/8/id48d5d5e36748ad95415b09b62715f5653493db8c677bd80eebf523087134a2df_small.jpeg "anandkapadia")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[anandkapadia](https://community.sap.com/t5/user/viewprofilepage/user-id/37089)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51006)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51006)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554810)

‎2022 Nov 13
6:36 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51006/tab/all-users "Click here to see who gave kudos to this post.")

2,359

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Human Resources](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Human%2520Resources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Human Resources

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BHuman%2BResources/pd-p/a8945cb2-dac7-490c-a6b6-7d8629f65668)

View products (2)

Please note this blog post is featured in [SAP S/4HANA Cloud Identity Access Management – Your Knowledge Base](https://blogs.sap.com/2022/07/29/sap-s-4hana-cloud-identity-access-management-your-knowledge-base/)

# Introduction

With the 2208 release of SAP S/4HANA Cloud, we have released the Manage Workforce app. This new app allows you to locally create and update workers (employees and contingent workers), including work agreements, and change employment situations in your SAP S/4HANA Cloud system. With the new app we have significantly improved the process of creating workforce-related data in the SAP S/4HANA Cloud system, i.e. from a CSV file to a simplified UI-based approach.

The key features of the app are

* creating workers directly in the app.

* editing personal or employment details.

* creating work agreements and assigning company codes, cost centers, and so on.

* changing employment situations: global assignment, concurrent employment, or transfers

* CSV upload of Business Users & Workers for mass upload

In addition, the app supports the following technical features and options:

* Navigate to the **Maintain Business Users** app, to assign a business user and business roles to your worker.

* Navigate to the **Business Partner** app, to enter business partner details of each worker, such as private address or bank account.

* Navigate to the **Fact Sheet** object page, to view worker-related information, such as project or payment details.

In this blog post, we want to do a deep dive into the Manage Workforce app from an IAM perspective. We will analyse what are the prerequisites to access the Manage Workforce app. In addition, we will see how to create a business user after having already created a worker in the system.

In part 2, we will see what are the restriction possibilities within the Manage Workforce app and in what ways you can design your business processes by combining the Manage Workforce app with other apps.

# Accessing the Manage Workforce App

So let's start with the basic question: **how can you access the Manage Workforce app?**

* The Manage Workforce app is part of the business catalog **Master Data - Manage Workforce (SAP\_BUM\_BC\_MNG\_WORKFORCE\_PC)**. So in order to access this app, you have to make sure that this business catalog is assigned to your business role.

* The business catalog is **not** linked to any scope item nor any scenario in SAP Central Business Configuration, i.e. the business catalog is available to all SAP S/4HANA Cloud customers. But in order to see the business catalog in your SAP S/4HANA Cloud system, you need to complete the [**Scope and Organizational Structure**](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/b0d4e53b7a9c4a21a482bf030d847faa/3a6e514ee9624939afc6f3a686145262.html?locale=en-US) phase in your SAP Central Business Configuration project and deploy the scope to your SAP S/4HANA Cloud system.

* This business catalog is assigned to the Business Role Templates Administrator (SAP\_BR\_ADMINISTRATOR) and Administrator - HR Info (SAP\_BR\_ADMINISTRATOR\_HRINFO).

* For troubleshooting also check SAP Note 3262756 - Manage Workforce is not available in SAP S/4HANA Cloud system.

> Please note SAP recommends that you use Business Roles based on Business Role Templates only for testing and exploring purposes (e.g. Fit-to-Standard workshops and testing of new functionality). It is strongly recommended to create business roles from scratch based on the identified workplaces for your Productive system.

![](/legacyfs/online/storage/blog_attachments/2022/10/BC_Apps-2.png)

# From Worker to Business Users

In this example, I will show you how to create an employee (John Doe) without any work agreement. After creating the employee master, we will then create the corresponding business user.

This scenario could be relevant if you want to simply create a business user and do not need to involve the business user in any business transaction within the SAP S/4HANA Cloud system.

## Creating the Employee in the Manage Workforce App

1. Launch the **Manage Workforce** app

2. Click on **Create**![](/legacyfs/online/storage/blog_attachments/2022/11/Create-Workforce.png)

3. Enter the **Personal Information** on header level (minimum requirements)

   * First Name

   * Last Name

   * Worker ID (enter here the employee number which you get from your HR system)

   * Email![](/legacyfs/online/storage/blog_attachments/2022/11/Header-1.png)

4. Select the right **Worker Type**

   * Employee (BUP003) or

   * Contingent Worker (BBP005) including the supplier in the field "Is Contingent Worker of"

5. Confirm the worker data by clicking on the **Create** button

## Creating the Business User

Please note for creating the business user, you need to have the business catalog **Identity and Access Management - User Management (SAP\_CORE\_BC\_IAM\_UM)** assigned to your business role. This business catalog is part of the business role template **Administrator (SAP\_BR\_ADMINISTRATOR)**.

After having created the worker, you can now create the b...