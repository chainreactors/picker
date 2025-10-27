---
title: REST API Integration for SAP Analytics Cloud – Gantt Chart Widget bidirectional example
url: https://blogs.sap.com/2023/07/29/rest-api-integration-for-sap-analytics-cloud-gantt-chart-widget-bidirectional-example/
source: SAP Blogs
date: 2023-07-30
fetch_date: 2025-10-04T11:52:35.100038
---

# REST API Integration for SAP Analytics Cloud – Gantt Chart Widget bidirectional example

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* REST API Integration for SAP Analytics Cloud - Gan...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163822&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [REST API Integration for SAP Analytics Cloud - Gantt Chart Widget bidirectional example](/t5/technology-blog-posts-by-members/rest-api-integration-for-sap-analytics-cloud-gantt-chart-widget/ba-p/13572174)

![planifyit01](https://avatars.profile.sap.com/2/e/id2eff90286945d69df30abf9b17f5fb2fbb2c569209341cd2785a7e2268ddb9c8_small.jpeg "planifyit01")

[planifyit01](https://community.sap.com/t5/user/viewprofilepage/user-id/142638)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163822)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163822)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572174)

‎2023 Jul 29
9:32 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163822/tab/all-users "Click here to see who gave kudos to this post.")

3,746

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)

View products (4)

![](https://static.wixstatic.com/media/15aea9_fbae00bfe5634253bd38c61fc72239a4~mv2.gif)

Hello everyone, welcome back to our blog series on transforming SAP Analytics Cloud (SAC) with custom widgets. In this blog post, we will extend our previous Gantt Chart widget by integrating it with SAC's API. This will allow us to update our project schedules directly from the widget and have the changes persist in our SAC model.

Before we dive in, make sure you've read our previous blog post on creating a Gantt Chart widget for SAC. This blog post will build upon the concepts and code introduced there.

Our previous blogs can be found here:

1. Transforming SAC with Custom Widgets (Part 1) – [link](https://blogs.sap.com/2023/05/24/transforming-sac-with-custom-widgets-part-1/)

2. Transforming SAC with Custom Widgets (Part 2 – Gamify)  – [link](https://blogs.sap.com/2023/05/29/transforming-sac-with-custom-widgets-part-2-gamify/)

3. Building a Customizable Calculator Widget for SAC – Styling and Builder Panel – [link](https://blogs.sap.com/2023/06/12/building-a-customizable-calculator-widget-for-sac-styling-and-builder-panel/)

4. Transforming SAC with Custom Widgets (Part 4 – Custom Widgets Data Binding)– [link](https://blogs.sap.com/2023/06/22/transforming-sac-with-custom-widgets-part-4-custom-widgets-data-binding/)

5. Gantt Chart Widget with Data Binding for SAP Analytics Cloud– [link](https://blogs.sap.com/2023/07/18/gantt-chart-widget-with-data-binding-for-sap-analytics-cloud/)

**Summary of Previous Blog:**

In our previous blog, we discussed the creation of a custom Gantt Chart widget in SAP Analytics Cloud (SAC) with data binding functionality.This approach provided a robust way to visualize data in SAC, but it also meant that the data had to exist(either via import or via planning) in SAC before it could be used in the Gantt Chart widget.We are now introducing a significant enhancement to this process. With the new API, data can be directly created within the Gantt Chart widget itself and then pushed into the SAC model.

**Our Goal**

Our goal is to extend our Gantt Chart widget with the ability to update our SAC model directly from the widget. This means that when we add tasks in the Gantt chart via the Widget, these changes will be stored in our SAC model. This will make our widget a more powerful tool for managing project schedules.

![](https://static.wixstatic.com/media/15aea9_e0c874acad494c389ecbbc33587773f0~mv2.gif)

**What is SAC's REST API?**

SAP Analytics Cloud (SAC) provides a RESTful API that allows third-party applications to interact with data stored on an SAC tenant. For example, you can create, read, update, and delete data in your SAC models, manage users and teams, and interact with the Content Network.The API is designed to be flexible and powerful, allowing you to automate and customize your SAC workflows.

To use the API, you need to have a tenant URL and an SAP Analytics Cloud user. You also need to configure OAuth to work with your application before you can use the REST API.

### API Endpoints

The SAC API provides several endpoints that allow you to interact with different aspects of your SAC tenant. Here are some examples:

* api/v1/dataexport: Allows you to extract a list of models and metadata on your tenant, or retrieve information about a specific model.

* api/v1/dataimport: Allows you to import fact and master data to SAC.

and so on.

**Authentication**

Before you can use the SAC REST APIs, you need to set up authentication.

To authenticate your application, you need to create an OAuth client in your SAC tenant. Your application will then be able to authenticate against the system’s OAuth service and obtain authorization to authenticate against the API.

For more information on the configuration and functionalities, see the [SAP Analytics Cloud REST API](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/3ccfab3348dd407db089accb66cff9a2.html) or the [API Developer Guide](https://help.sap.com/doc/9825c700f68e489ca5634a3da101a94c/release/en-US/ca804ae1c3874053a1e140e7c9cea019.pdf)

**Overview of Developed Objects: GanttChartWidgetAPI.js, GanttChartWidgetAPI.json, and SACAPI\_DataImport.js**

![](https://static.wixstatic.com/media/15aea9_546c1af332454a2cb7299cf1255663e3~mv2.png/v1/fill/w_740,h_230,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/15aea9_546c1af332454a2cb7299cf1255663e3~mv2.png)

In the context of SAP Analytics Cloud (SAC), the three developed objects, namely **`GanttChartWidgetAPI.js`, `GanttChartWidgetAPI.json`, and `SACAPI\_DataImport.js`,** play crucial roles in data manipulation, visualization, and integration. These files are interconnected and work together to provide a seamless user experience. Here's a brief overview of each file and how they relate to each other:

*GanttChartWidgetAPI.js and GanttChartWidgetAPI.json*

**`GanttChartWidgetAPI.js`** is a JavaScript file that contains the l...