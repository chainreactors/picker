---
title: SAP Fiori tools 2306 update includes more on flexible programming model building blocks, TypeScript for CAP projects, and open source
url: https://blogs.sap.com/2023/06/28/sap-fiori-tools-2306-update-includes-more-on-flexible-programming-model-building-blocks-typescript-for-cap-projects-and-open-source/
source: SAP Blogs
date: 2023-06-29
fetch_date: 2025-10-04T11:47:37.339853
---

# SAP Fiori tools 2306 update includes more on flexible programming model building blocks, TypeScript for CAP projects, and open source

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Fiori tools 2306 update includes more on flexi...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164610&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori tools 2306 update includes more on flexible programming model building blocks, TypeScript for CAP projects, and open source](/t5/technology-blog-posts-by-sap/sap-fiori-tools-2306-update-includes-more-on-flexible-programming-model/ba-p/13570616)

![tashley](https://avatars.profile.sap.com/6/9/id696e13ca1929f051a85e82971844abe727fa277e8bd4cffcec0e8a424dab26af_small.jpeg "tashley")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[tashley](https://community.sap.com/t5/user/viewprofilepage/user-id/316392)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164610)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164610)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570616)

‎2023 Jun 28
10:25 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164610/tab/all-users "Click here to see who gave kudos to this post.")

3,780

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Fiori tools](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520tools/pd-p/73555000100800002345)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Fiori tools

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Btools/pd-p/73555000100800002345)

View products (5)

The SAP Fiori tools team continues to accelerate development and foster best practices for SAP Fiori apps. In the last few months, we have added support for **TypeScript in CAP projects** and introduced guides to help developers adopt TypeScript as a programming language for developing SAP Fiori apps. It is quick to add any **flexible programming model building block** with the code completion capabilities. We have made it even easier for you to make use of the most frequently used flexible programming model [building blocks using Page Editor](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/02172d2bb461469f83c18c834613232c.html#loio6d3ad83b9694475684d41f017bbccf20). On the open source front, we continue our journey to **move the code to open source** and make it reusable by the community. In parallel, we are also continuously delivering new capabilities to the open source extensions ([Guided Answers extension by SAP](https://github.com/SAP/guided-answers-extension) & [UI5 Language Assistant](https://github.com/SAP/ui5-language-assistant/)) based on the feedback from the community. In this update, I will give you a summary of these topics.

For those of you planning to attend [UI5con](https://openui5.org/ui5con/germany2023/index.html#agenda), we will cover these topics in the following sessions:

*Boost Your Productivity In Developing SAPUI5 apps With SAP Fiori Tools* (workshop)

*Develop SAP Fiori apps in TypeScript using SAP Fiori tools* (talk)

## TypeScript offers more flexibility

The mission of SAP Fiori tools is to simplify the developer’s experience and foster best practices. TypeScript leads to better coding quality and offers more flexibility. We had been adding end-to-end support around TypeScript to help to boost developer efficiency. You can now generate a new project with TypeScript enabled for all supported templates and OData versions using SAP Fiori tools, including CAP projects.

When generating a new project with Custom Template for flexible programming model, the controller for the default view is generated in TypeScript. For those of you who prefer the step-by-step approach to coding, two TypeScript guides (*Add a custom action to a page using extensions and Add a custom filter to the filter bar*) have been added to the collection of guides in Guided Development. When using Page Editor to add extensions such as custom column for OData V4 apps, the controller code is generated in TypeScript.

![](/legacyfs/online/storage/blog_attachments/2023/06/project-generation-typescript-1.jpg)

Controller code created in TypeScript

## Flexible programming model made easier

Building blocks are reusable artifacts that are offered in the SAP Fiori elements runtime to further accelerate your development. We have now made the experience even easier with the ability to add/maintain building blocks using Page Editor. When adding a building block, Page Editor starts a guide to walk you through the creation, and you can update the building blocks in the properties panel. Currently, you will see options for filterbar, chart, and table building blocks. You can expect that we will continue to add support for other building blocks. You can also maintain any blocks using code completion as I mentioned in my previous [update](https://blogs.sap.com/2023/02/17/sap-fiori-tools-2302-update-has-more-for-odata-v4-and-the-flexible-programming-model-better-troubleshooting-more-open-source/).

![](/legacyfs/online/storage/blog_attachments/2023/06/building_blocks_promo.gif)

Easily add/update building block using Page Editor

## Open Source journey continues

Open Source remains a key initiative for us. Our goal for open source is to bring transparency, promote reuse of code, and foster community collaboration. We added new modules for deployment tooling, project access, and all writers now support TypeScript. On the capabilities front, since the launch of [Guided Answers extension by SAP](https://github.com/SAP/guided-answers-extension/), we had been improving the quality of content of troubleshooting tips in Guided Answers, and incorporated it into the message text for most frequently encountered problems.

To make it easier to share and collaborate with other developers, we have introduced the shareable link feature allowing you to easily copy the shortcut link which you can pass to your colleagues to directly launch Visual Studio Code, open the Guided Answers extension, and navigate t...