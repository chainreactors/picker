---
title: Add useful Extensions to Dev spaces in SAP Business Application Studio
url: https://blogs.sap.com/2022/11/13/add-useful-extensions-to-dev-spaces-in-sap-business-application-studio/
source: SAP Blogs
date: 2022-11-14
fetch_date: 2025-10-03T22:40:59.377987
---

# Add useful Extensions to Dev spaces in SAP Business Application Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Add useful Extensions to Dev spaces in SAP Busines...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164308&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Add useful Extensions to Dev spaces in SAP Business Application Studio](/t5/technology-blog-posts-by-sap/add-useful-extensions-to-dev-spaces-in-sap-business-application-studio/ba-p/13569731)

![showkath_naseem](https://avatars.profile.sap.com/b/3/idb31430339dce394fae56e5099a002a181ef4cf21068545b19463517d3280ac9b_small.jpeg "showkath_naseem")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[showkath\_naseem](https://community.sap.com/t5/user/viewprofilepage/user-id/1529)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164308)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164308)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569731)

‎2022 Nov 13
9:28 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164308/tab/all-users "Click here to see who gave kudos to this post.")

2,080

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (2)

# Introduction

As explained in [Capire documentation](https://cap.cloud.sap/docs/about/features) you can efficiently and rapidly build enterprise ready cloud services & business applications in a full-stack development approach and extend S/4HANA  with your own choice of Tools using **your comfortable IDE/Code Editors** such as [SAP Business Application Studio](https://cap.cloud.sap/docs/tools#bastudio)  or [Visual Studio Code](https://cap.cloud.sap/docs/tools#vscode) or [Eclipse](https://cap.cloud.sap/docs/java/getting-started#eclipse)  based on either JavaScript/Node.js/Express.js or Java Spring Boot in a platform-agnostic mode

**CAP has Dedicated tools support** provided in [SAP Business Application Studio](https://cap.cloud.sap/docs/tools#bastudio), [Visual Studio Code](https://cap.cloud.sap/docs/tools#vscode) , [Eclipse](https://cap.cloud.sap/docs/java/getting-started#eclipse).

For a preconfigured development environment, use [*SAP Business Application Studio*](https://blogs.sap.com/2020/09/28/sap-business-application-studio/) which comes with all of the required tools preinstalled. **i.e**you no need to install most of tools if you are going to use [*SAP Business Application Studio*](https://blogs.sap.com/2020/09/28/sap-business-application-studio/)

On the other hand  CAP certainly gives *opinionated* guidance, we do so without sacrificing openness and flexibility. At the end of the day, **you stay in control** of which tools or technologies to choose or which architecture patterns to follow ,still keeping the door wide open for custom choice

The purpose of this article is to share tricks , useful extensions you can install in your **comfortable IDE/code Editors** [SAP Business Application Studio](https://cap.cloud.sap/docs/tools#bastudio) or [Visual Studio Code](https://cap.cloud.sap/docs/tools#vscode) or [Eclipse](https://cap.cloud.sap/docs/java/getting-started#eclipse)

you can try to install below extensions in [SAP Business Application Studio](https://cap.cloud.sap/docs/tools#bastudio) or  [Visual Studio Code](https://cap.cloud.sap/docs/tools#vscode) or [Eclipse](https://cap.cloud.sap/docs/java/getting-started#eclipse) just to **speed up** the **development** & **boost** your **productivity**

# Useful extensions to Initialize  Data in CAP Application

As you might know  SAP [CAP](https://www.consolvis.de/en/blog/what-is-the-sap-cloud-application-programming-model/)has option to initialize local data for your BTP applications in CSV file for local testing of Services, Fiori APPS .You can read about [How to Initialize data in CAP Application](https://cap.cloud.sap/docs/guides/databases#providing-initial-data)

A CSV file representing a whole table  & must be named as db\_name.table\_name.csvGo to your “db” folder and create a subfolder called “csvs or “data”, and inside create a CSV file.. The name of file name pattern *<namespace>-<model\_name>.csv*

As shown below by default you need to enter values for columns with semicolon-separated

![](/legacyfs/online/storage/blog_attachments/2022/11/1-csv-before-extension1.png)

However this will be hard to edit csv file ,modify data if CSV contains too many columns ,chance are there for mistakes

## **Extension 1**

You can install this extension in SAP Business Application Studio as shown below

* Open you Dev Space in SAP Business Application Studio

* Select Extensions options & search for “csv” as shown below

* Click in install

That’s it .  Extension installation is so easy feature in our SAP Business Application Studio. You no need to restart Dev Space

Congratulations! , ***You have*** successfully ***installed***  extension in SAP Business Application Studio

This extensions allows you to edit csv files with an excel like table UI

![](/legacyfs/online/storage/blog_attachments/2022/11/2-Install-Extensions.png)

**Now to open CSV file , you can right click & choose “Edit CSV”**

![](/legacyfs/online/storage/blog_attachments/2022/11/4-Edit-CSV-2.png)

With this option your csv files displayed as below in table format , so that you can easily manage data just like in Excel

![](/legacyfs/online/storage/blog_attachments/2022/11/4-Edit-CSV-3-Table.png)

## **Extension 2**

[CDS CSV Generator](https://marketplace.visualstudio.com/items?itemName=ozgurkadir.cds-csv-generator) is a tool to create initial CSV data files for [SAP Cloud Application Programming Model](https://cap.cloud.sap/docs/) applications

#

# Uninstall Extension Procedure

Any time if you don’t need any extension in Business Application Studio & you decided to uninstall

Procedure to uninstall extension is
> > You can go to Extensions View

          > Select desired Extension you want to uninstall

          > Click on Uninstall button

> For example

![](/legacyfs/online/storage/blog_attachments/2022/11/5-Uninstall.png)

**SAP Business Application Studio DISCLAIMER**

SAP provides you with a mechanism to access third party sites to view and download open-source, 3rd party or its own tools, libraries, or software components (“Extensions”) to dev spaces in SAP Business Application Studio. Using this mechanism, you can view and install VS Code Extensions from the VSX Open Regi...