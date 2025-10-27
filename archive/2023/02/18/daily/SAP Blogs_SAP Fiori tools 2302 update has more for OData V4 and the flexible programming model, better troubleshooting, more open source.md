---
title: SAP Fiori tools 2302 update has more for OData V4 and the flexible programming model, better troubleshooting, more open source
url: https://blogs.sap.com/2023/02/17/sap-fiori-tools-2302-update-has-more-for-odata-v4-and-the-flexible-programming-model-better-troubleshooting-more-open-source/
source: SAP Blogs
date: 2023-02-18
fetch_date: 2025-10-04T07:22:21.548423
---

# SAP Fiori tools 2302 update has more for OData V4 and the flexible programming model, better troubleshooting, more open source

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori tools 2302 update has more for OData V4 ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158089&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori tools 2302 update has more for OData V4 and the flexible programming model, better troubleshooting, more open source](/t5/technology-blog-posts-by-sap/sap-fiori-tools-2302-update-has-more-for-odata-v4-and-the-flexible/ba-p/13551009)

![tashley](https://avatars.profile.sap.com/6/9/id696e13ca1929f051a85e82971844abe727fa277e8bd4cffcec0e8a424dab26af_small.jpeg "tashley")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[tashley](https://community.sap.com/t5/user/viewprofilepage/user-id/316392)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158089)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158089)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551009)

‎2023 Feb 17
5:21 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158089/tab/all-users "Click here to see who gave kudos to this post.")

4,179

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori tools](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520tools/pd-p/73555000100800002345)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Fiori tools

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Btools/pd-p/73555000100800002345)

View products (4)

The SAP Fiori tools team continues to deliver capabilities to simplify the SAP Fiori development experience. With the SAP Fiori tools 2302 update, we have focused on making annotations  easier, expanding support for flexible programming model and OData V4, and releasing more open source modules that can be reused by the community. In this post, I’ll focus on some of the new functionality.

## Making annotations easier for SAP Fiori elements OData V4 apps

We hear your feedback that annotations can sometimes be a challenge when developing SAP Fiori elements applications. We received positive comments that we are moving in the right direction with the annotation code completion, Guided Development, and annotation support in the Page Editor (OData V4 only). Hence, we continue to build upon the foundation. I am pleased to announce the availability of code completion to reference annotations used in building blocks. You will find the latest features in the [UI5 Language Assistant](https://marketplace.visualstudio.com/items?itemName=SAPOSS.vscode-ui5-language-assistant)  extension version 4.0.3. If you had installed SAP Fiori tools via the extension pack in Visual Studio Code, you should already see the extension installed (manual update maybe required if you do not have auto update on). The UI5 Language Assistant is also included in the SAP Fiori and Full Stack Cloud Application dev spaces in SAP Business Application Studio.

![](/legacyfs/online/storage/blog_attachments/2023/02/2302_UI-l-a_noPreview.gif)

Code Completion for annotations referenced in flexible programming model building blocks

Page Editor now supports annotations needed to add analytical features to your OData V4 apps (with an analytics-enabled service). You can add analytical charts and visual filter to the list report page. As we try to get the new capabilities to the hands of our customers as quickly as we can, you can expect to see further enhancements to support more use cases.

![](/legacyfs/online/storage/blog_attachments/2023/02/2302_VisualFilter.png)

Page Editor adds support for visual filters for OData V4 apps

###

###

## “Grow As you Go” approach to managing project artifacts

Consistent with our goal to make SAP Fiori development simpler, we want to make management of the project artifacts easier. Currently, when the project is generated, the start scripts are already included in the `package.json`, based on the selection during project generation. It is often a challenge for users to know what configuration needs to be done in what artifact if they want to add a new one post project generation.

We made the management of project artifacts modular so you can easily add or update the artifacts when you need it. To do that, we have added a new module [@sap-ux/create](https://github.com/SAP/open-ux-tools/tree/main/packages/create) in the [open-ux-tools](https://github.com/SAP/open-ux-tools) repo.  You can trigger the command from the Application Info page for your project, or type “**npm init [@Sisn](/t5/user/viewprofilepage/user-id/1387241)-ux**” at a terminal. This module is already being used in SAP Fiori tools to add/update mockserver config. We plan to add support for other configurations such as deployment or FLP  configurations in the near future.

![](/legacyfs/online/storage/blog_attachments/2023/02/2302-grow-as-you-go-1.png)

New open source module to manage project configuration files

###

###

## Integrated Troubleshooting Experience

In my [last blog on the 2211 update](https://blogs.sap.com/2022/11/02/sap-fiori-tools-2211-update-includes-typescript-support-easier-troubleshooting-flexible-programming-model-support-and-more/), I talked about how you can make use of the [Guided Answers extension by SAP](https://marketplace.visualstudio.com/items?itemName=SAPOSS.sap-guided-answers-extension) for troubleshooting. We are making this even easier by integrating the Guided Answers extension into the development experience using SAP Fiori tools. At the time when you encounter an error while using SAP Fiori tools, we are now providing you a direct link to the answer in Guided Answers for some of the most common problems such as destination errors encountered in SAP Business Application Studio during project generation. While the messages shown to you is slightly different between VSC and SAP Business Application Studio, they both link to Guided Answer content. We hope this enables you to get past the problems quickly so you can focus on your development tasks.

![](/legacyfs/online/storage/blog_attachments/2023/02/Invalid_SSL_VSCode_GA.png)

Direct Link to Guided Answer when error is encountered for faster troubleshooting

![](/legacyfs/online/storage/blog_attachments/2023/02/Invalid_Destination_GA.png)

Troubleshoot destination problems in BAS with Guided Answer

##

###

## Guides made sim...