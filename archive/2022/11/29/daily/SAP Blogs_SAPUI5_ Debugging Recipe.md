---
title: SAPUI5: Debugging Recipe
url: https://blogs.sap.com/2022/11/28/sapui5-debugging-recipe/
source: SAP Blogs
date: 2022-11-29
fetch_date: 2025-10-03T23:58:29.649095
---

# SAPUI5: Debugging Recipe

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAPUI5: Debugging Recipe

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161662&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAPUI5: Debugging Recipe](/t5/technology-blog-posts-by-members/sapui5-debugging-recipe/ba-p/13559463)

![Syed](https://avatars.profile.sap.com/0/a/id0a8030f4c67191f2a9b5ea6e452f375934f2473d040349ef919e0ec5db84dd68_small.jpeg "Syed")

[Syed](https://community.sap.com/t5/user/viewprofilepage/user-id/970)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161662)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161662)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559463)

‎2022 Nov 28
11:33 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161662/tab/all-users "Click here to see who gave kudos to this post.")

4,976

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

Hello SAP Community,

## **Introduction:**

This is **Syed Baba Tajuddin Hussaini** with a new blog post on SAPUI5.

The blog post you are viewing at this moment provides the following helpful information for newbies:

1. **How to identify the "view name" and the "UI element"?**

2. **When the button is clicked, which function is called, and its location?**

## **Let's get straight to the point:**

1. ### How to identify the "view name" and the "UI element"?

* Add [Fiori Doctor](https://chrome.google.com/webstore/detail/fiori-doctor/abmocanmemghgbcegmmdgpefgfjbkglf) Plugin to Google Chrome or Microsoft Edge.![](/legacyfs/online/storage/blog_attachments/2022/11/FioriDoctor.png)

* Click on the Fiori Doctor Plugin Icon to start:

![](/legacyfs/online/storage/blog_attachments/2022/11/FioriDoctorLogo.png)

To know the view name of a page and control. Switch on the following buttons.![](/legacyfs/online/storage/blog_attachments/2022/11/FioriDoctorOptions.png)

 We can see in the below image the plugin shows the namespace, project name, and view name.

        ![](/legacyfs/online/storage/blog_attachments/2022/11/ViewName.png)

* If we hover over any UI element. The Fiori Doctor Plugin shows the UI element name. For instance, we will hover over the web component button the plugin shows the class name as shown below.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/FioriDoctorButton.png)

* The Fiori Doctor plugin enables us to instantly identify the view name, UI element name, clear the cache, and know the SAPUI5 version of the application, etc.

  ### **2. When the button is clicked, which function is called, and its location?**

* A very useful tool is provided by the SAPUI5 framework called UI5 Diagnostics.

* We will be using a UI5 Diagnostic tool for debugging.

* Make sure that the SAPUI5 application you would like to debug is open / loaded in your web browser.

* Once the application is loaded.

* You can open the Technical Information Dialog by pressing Ctrl + Shift + Alt + S.

* Another way to open is by pressing Ctrl + Shift + Alt + P.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/TechnicalInformationDialog.png)

* Click on "Open DIagnostics".

* UI5 Diagnostics window will get opened.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/UI5Diagnostics-1.png)

* Expand Debugging.

* Click on the "Select Class" drop-down list. Here, the list of classes appears. As per Fiori Doctor, we will select the web component button class as shown in one of the above images "sap.ui.webc.main.Button" in other cases if it is a normal button select the class as "sap.m.button".

  ![](/legacyfs/online/storage/blog_attachments/2022/11/sap.ui_.webc_.main_.Button.png)

* Once you select the required class.

* Click on Add Class.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/selectMethod.png)

* Click on the "Select Method" drop-down list. Here, the list of methods appears.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/SelectMethod1.png)

* We will select a method called "fireClick".

  ![](/legacyfs/online/storage/blog_attachments/2022/11/fireClick.png)

* In this example, we have used the SAPUI5 web component button. Hence, we selected the method "fireClick".

* However, if the class of the button is "sap.m.button" then select the method as "firePress".

* Once we select the required method.

* Go to your application which is opened/loaded in the browser.

* Right-click on the application and click "Inspect" or press F12 to open the console.

* Make sure your UI5 diagnostic window is opened/running.

* Now, click on the button from your application you want to know about.

* Once, you click on the button, the debugger will get triggered.

* Go to the Console tab.

* Clear Console.

* Type this.mEventRegistry in Console and press Enter.

  ![](/legacyfs/online/storage/blog_attachments/2022/11/this.mEventRegistry.png)

* Click to expand it.

* Once you expand.

* You can see the function name and function location.

* In this case, the function name is "handleClick" and the function location is "View1.controller.js".

  ![](/legacyfs/online/storage/blog_attachments/2022/11/functionName-and-Location.png)

## Conclusion:

In this blog post, we have seen that if we would like to know the namespace, project name, view name, UI element name, and SAPUI5 version of the SAPUI5-based application we can make use of the amazing plugin Fiori Doctor to save time and get the instant required details. Also, we have seen how to identify the function name and where the function is located upon clicking on the button.

Happy learning!

Thank you!

**Syed Baba Tajuddin Hussaini**

* [fiori debugging](/t5/tag/fiori%20debugging/tg-p/board-id/technology-blog-members)
* [SAPUI5](/t5/tag/SAPUI5/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsapui5-debugging-recipe%2Fba-p%2F13559463%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Running a SAPUI5 App from a Previous Commit Without Affecting Remote Repository](/t5/technology-blog-posts-by-members/running-a-sapui5-app-from-a-previous-commit-without-affecting-remote/ba-p/14139276)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Jul 02
* [Building an Agentic AI System with Model Context ...