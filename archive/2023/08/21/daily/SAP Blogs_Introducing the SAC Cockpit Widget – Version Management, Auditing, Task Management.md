---
title: Introducing the SAC Cockpit Widget – Version Management, Auditing, Task Management
url: https://blogs.sap.com/2023/08/20/introducing-the-sac-cockpit-widget-version-management-auditing-task-management/
source: SAP Blogs
date: 2023-08-21
fetch_date: 2025-10-04T11:59:37.680797
---

# Introducing the SAC Cockpit Widget – Version Management, Auditing, Task Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Introducing the SAC Cockpit Widget - Version Manag...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165496&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Introducing the SAC Cockpit Widget - Version Management, Auditing, Task Management](/t5/technology-blog-posts-by-members/introducing-the-sac-cockpit-widget-version-management-auditing-task/ba-p/13580816)

![planifyit01](https://avatars.profile.sap.com/2/e/id2eff90286945d69df30abf9b17f5fb2fbb2c569209341cd2785a7e2268ddb9c8_small.jpeg "planifyit01")

[planifyit01](https://community.sap.com/t5/user/viewprofilepage/user-id/142638)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165496)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165496)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580816)

‎2023 Aug 20
8:17 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/165496/tab/all-users "Click here to see who gave kudos to this post.")

1,926

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)

View products (2)

We're excited to introduce a new open-source project: the SAC Cockpit Widget. This widget aims to bridge the gap between the functionalities that SAP Analytics Cloud (SAC) currently offers and the ones that users have been craving for. With this widget, you'll be able to manage versions, audit changes, schedule tasks, and much more. All this out of the box by simply downloading this widget and inserting your SAC and model information

![](https://static.wixstatic.com/media/15aea9_eef5972d138c440aaa66dee9d113d478~mv2.gif)

But before we dive in, make sure you've read our previous blog post:

1. Transforming SAC with Custom Widgets (Part 1) – [link](https://blogs.sap.com/2023/05/24/transforming-sac-with-custom-widgets-part-1/)

2. Transforming SAC with Custom Widgets (Part 2 – Gamify)  – [link](https://blogs.sap.com/2023/05/29/transforming-sac-with-custom-widgets-part-2-gamify/)

3. Building a Customizable Calculator Widget for SAC – Styling and Builder Panel – [link](https://blogs.sap.com/2023/06/12/building-a-customizable-calculator-widget-for-sac-styling-and-builder-panel/)

4. Transforming SAC with Custom Widgets (Part 4 – Custom Widgets Data Binding)– [link](https://blogs.sap.com/2023/06/22/transforming-sac-with-custom-widgets-part-4-custom-widgets-data-binding/)

5. Gantt Chart Widget with Data Binding for SAP Analytics Cloud– [link](https://blogs.sap.com/2023/07/18/gantt-chart-widget-with-data-binding-for-sap-analytics-cloud/)

6. REST API Integration for SAP Analytics Cloud – Gantt Chart Widget bidirectional - [link](https://blogs.sap.com/2023/07/29/rest-api-integration-for-sap-analytics-cloud-gantt-chart-widget-bidirectional-example/)

**Our Goal**

SAP Analytics Cloud is a powerful tool, but like any software, it has its limitations.

The SAC Cockpit Widget is a custom-built tool designed to enhance the capabilities of SAC. Initially, it will focus on version publishing and deleting, but the goal is to evolve it weekly, adding features like data locking, auditing, calendar task management, and more.For our initial release, we're focusing on version publishing and deleting.

At its core, the SAC Cockpit Widget is designed to provide planner-administrators with a seamless interface to manage different versions of their data. This is achieved through a combination of buttons, pop-ups, and feedback messages.

**The Code Structure:**

Before we go into the code, let's understand the structure. We have:

1. Main JS Code (**SACCockpitWidget.js**): This is the heart of our widget. It defines the appearance and behavior.

2. Builder Panel JS Code (**builder-panel.js**): This is the control panel for our widget, allowing users to customize its properties.

3. JSON Configuration (**SAC\_Cockpit.json**![:disappointed_face:](/html/@9F6FEF67A50DA1F0439248EFABEDFCE9/emoticons/1f61e.png ":disappointed_face:") This file defines the widget's properties, methods, events, and data bindings.

Let's break down the main components of our widget:

**1. Functionality**

***Managing Public Versions***

Public versions are finalized datasets that are available for wider consumption. They have passed all necessary reviews and are deemed accurate and reliable.

![](https://static.wixstatic.com/media/15aea9_b3b239bf0bdf4d75a8e0669e4ee192ea~mv2.png/v1/fill/w_592,h_143,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/15aea9_b3b239bf0bdf4d75a8e0669e4ee192ea~mv2.png)

Structure of the table:

- JSON Location: /versions?tenant=2

- Publish: A button to republish or update the public version.

- Delete: A button to remove the public version.

- ID: A unique identifier for the version.

- Is In Public Edit Mode: A flag indicating if this version is currently being edited.

- Is Shared: A flag indicating if this version is shared with other entities or users.

- Owner: The individual or entity responsible for this version.

- Category: The category or classification of this version.

- Description: A brief description or notes about this version.

- Source Version ID: The ID of the version from which this one was derived, if applicable.

- Creation Time: Timestamp indicating when this version was created.

- Copying Supported: A flag indicating if this version supports copying.

- Planning Supported: A flag indicating if planning operations are supported on this version.

- Currency Conversion Setting: Information about currency conversion, if applicable.

- Has Planning Area: A flag indicating if this version has a designated planning area.

- Workflow State: The current state of the version in the workflow process.

- Is Suspended For Input Schedule: A flag indicating if this version is currently suspended and not accepting inputs.

- Is Writeback Enabled: A flag indicating if writeback operations are enabled on this version.

***Managing Privat Versions***

Private versions are typically drafts or versions of data that are not yet ready for public consumption. They might be in the process of review, or they could be experimental versions that are being tested.

![](https://static.wixstatic.com/media/15aea9_a5cfc32f67f14b509cf22beac5f8d637~mv2.png/v1/fill/w_592,h_170,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/15aea9_a5cfc32f67f14b509cf22beac5f8d637~mv2.png)

Structure of the table:

- JSON location: /foreign-versions?tenant=7

- Publish: A button to move the private version to the public table.

- Delete: A ...