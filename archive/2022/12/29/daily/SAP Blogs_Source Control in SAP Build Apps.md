---
title: Source Control in SAP Build Apps
url: https://blogs.sap.com/2022/12/28/source-control-in-sap-build-apps/
source: SAP Blogs
date: 2022-12-29
fetch_date: 2025-10-04T02:39:39.658426
---

# Source Control in SAP Build Apps

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Source Control in SAP Build Apps

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161048&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Source Control in SAP Build Apps](/t5/technology-blog-posts-by-sap/source-control-in-sap-build-apps/ba-p/13559460)

![kleventcov](https://avatars.profile.sap.com/f/6/idf632f5b6ce90af03a4fe7edb3f8d53f203fda5c36a124a99a70a75020c680cc3_small.jpeg "kleventcov")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[kleventcov](https://community.sap.com/t5/user/viewprofilepage/user-id/40495)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161048)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161048)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559460)

‎2022 Dec 28
12:42 PM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161048/tab/all-users "Click here to see who gave kudos to this post.")

2,221

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (3)

## ![](/legacyfs/online/storage/blog_attachments/2022/12/bannerSC.png)

## Introduction

If you are a developer, you are probably familiar with the concept of source control. Yet, for those who are new to the area, source control is a crucial tool that allows engineers to track changes to their projects over time. Furthermore, it enables seamless collaboration on projects, implements the ability to track changes, and undo them as needed.

Including source control in your development workflow has several advantages. Here are a few examples:

* Collaboration: It can be difficult to work on a project with other developers without a unified change history. Source control allows you to have a single point of truth when developing as a team.

* Organization: Your project may expand and become complex as it develops. Source control allows you to keep version backups that can be enabled at any point in the future.

I will dive deeper into the advantages of source control and how to start utilizing it in your own projects in this blog.

## History

SAP Build Apps keeps track of all the development changes in the History tab, found in the top right corner. It allows you to get an overview of recent modifications, and more importantly, rollback to them.

In the image below, you can find an example of a History entry. The oldest entry marks the point of creating a data resources called "On-Device". Afterward, a page called "Page 2" was created. The last two entries represent a change in the UI canvas and Logic canvas.

Every change is accompanied by a page identifier in the beginning. Thus, an entry titled 'Page 2 logic, Page 2 UI' shall be interpreted as User Interface modification on a page named 'Page 2'.

![](/legacyfs/online/storage/blog_attachments/2022/12/HistorySC-1.png)

Visual cloud functions are also enabled with the History feature. Read more about this [here](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/f69e8f2623074db08bcc3b6711966771.html).

## Project Sharing

Apart from having the ability to rollback to previous versions, source control enables you to share the development with others. In the SAP Build Lobby, you can use the three-dot menu to manage members of your project, or simply click on the Members list column.

![](https://help.sap.com/doc/431746e4c663458aa68d9754b237bfc6/Latest/en-US/loioee8cb2e3b6fd49a995c247c98708d709_HiRes.png)

There are three user roles available:

* **Viewer**: Read-only actions - Inspecting the app and history.

* **Developer**: Edit, deploy, release - Makes changes to the application

* **Administrator**: Complete access, including editing, sharing, and deleting a project - Full source control of the project.

Read more about project sharing [here](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/3cd678467c8a4292940f79fb9060f829.html).

## Export - Import

Export - Import enables source accessibility for your project. By simply exporting your app in SAP Build Lobby, you can transfer the source file between BTP subaccounts or simply share it with your colleagues.

Upon receiving an export file, they can seemingly import it via Lobby:

![](https://help.sap.com/doc/431746e4c663458aa68d9754b237bfc6/Latest/en-US/loio31e20595706744acb7e66eb86c78a220_LowRes.png)

Export - import becomes particularly handy in case your project needs to go through several stages of testing and quality assurance. Developers can export their applications and share them with the quality engineers, allowing both to separate their workflows without intervening with each other.

Read more about export - import [here](https://help.sap.com/docs/BUILD_APPS/431746e4c663458aa68d9754b237bfc6/bd06db488f5c4c3ca0d4086f6c921f1e.html).

## Replace

The newest Source Control feature that can be found in SAP Build Apps is 'Replace':

![](/legacyfs/online/storage/blog_attachments/2022/12/ReplaceButtonSC.png)

Replace allows you to override all content of an application with a provided backup file. Backup files can be generated using the 'Export' button, above.

![](/legacyfs/online/storage/blog_attachments/2022/12/ReplaceViewSC.png)

This feature is incredibly useful for making application fall back points. Simply export your app and rename the file to have a distinct version and/or timestamp. With that, you can always replace the content of any app with the saved version.

## Conclusion

I hope I was able to highlight the benefits of using source control in your development workflow. From enabling easy collaboration and organization to providing a history of changes and the ability to roll back if necessary, source control is an essential tool for any development team. I strongly recommend checking out the new 'Replace' functionality, that is useful for making large-scale changes to the project.

Whether you're working on a small project or a large one, source control can help improve your workflow and ensure the success of your projects.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/featur...