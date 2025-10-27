---
title: SAP Build Apps + SAP Mobile Start
url: https://blogs.sap.com/2023/06/16/sap-build-apps-sap-mobile-start/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:46:55.617093
---

# SAP Build Apps + SAP Mobile Start

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Build Apps + SAP Mobile Start

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162071&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Build Apps + SAP Mobile Start](/t5/technology-blog-posts-by-sap/sap-build-apps-sap-mobile-start/ba-p/13562632)

![MarcHuber](https://avatars.profile.sap.com/b/f/idbf68913d04e2bd22420dcb52e4327b500252006467dd795a8b0c429a1cd35e6d_small.jpeg "MarcHuber")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MarcHuber](https://community.sap.com/t5/user/viewprofilepage/user-id/13080)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162071)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162071)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562632)

‎2023 Jun 16
3:21 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162071/tab/all-users "Click here to see who gave kudos to this post.")

6,723

* SAP Managed Tags
* [SAP Mobile Start](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Start/pd-p/73554900100800003452)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)

* [SAP Mobile Start

  Software Product](/t5/c-khhcw49343/SAP%2BMobile%2BStart/pd-p/73554900100800003452)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (3)

Motivation:

In this blog you will learn how to display a responsive SAP Build Apps web application on your mobile phone with SAP Mobile Start.

SAP Build Apps empowers anyone to develop applications in a visual way by drag&drop of components.

SAP Mobile Start allows users to access native or web-responsive (such as SAPUI5) business apps, data, and information from SAP Build Work Zone, standard edition. Users can easily access content, apps, and tasks in one place so that they can stay informed and carry out all their tasks no matter where they are.

Prerequisites

* SAP Build Work Zone, standard edition

* SAP Build Apps

* SAP Mobile Start app on your mobile phone

Getting started:

First of all you need to create a SAP Build Apps application. For example my Sales Order App.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-33.png)

You need to build and deploy the application that end-users can access the app. In the “Launch” Navigation open the Build Service.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-23.png)

Build your project as MTAR. This will take about 15 minutes.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-26.png)

You can refresh the page and see the status of the current build process. After the build is completed, you can deploy the app to your BTP account. Select “Deploy MTA”.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-20.png)

Authorize BTP Deployments with your user, select HTML5 Application Repository where you want to upload your app. The deployment can take several minutes and looks like this:

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-13.png)

After the successful deployment you can see the link to your deployed application:

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-17.png)

Now all steps are completed in SAP Build Apps and we go to your Work Zone, standard edition account. Go to your BTP subaccount where you have deployed your app, go to Instances and Subscriptions in the left menu and select “SAP build Work Zone, standard edition”.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture7-16.png)

Now you can create a new Site in Work Zone.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture8-15.png)

Ensure that SAP Mobile Start is enabled:

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture9-13.png)

Close the Site Editor and open the Channel Manager to update the content. This will make the deployed app visible in the Content Manager.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture10-11.png)

After the update is done, select Content Manager in the Menu on the left side, select Content Explorer und Select HTML5 Apps

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture11-10.png)

Search for your SAP Build Apps Application and add it to your content.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture12-8.png)

Afterwards you should see your app in “My Content”.

*Optional:* If you have built an app with approval workflows in SAP Build Process Automation, you can also enable the “My Inbox” in the Content Explorer, that it will also appear in SAP Mobile Start.

Next step is to create a new Group where you can register the application.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture13-9.png)

Provide a Title and assign the apps to the group. Press Save afterwards.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture14-9.png)

Last step is to define the user right. In my case the role “Everyone” should be able to access to application. I open the Everyone role. You could also create new roles, if needed.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture15-6.png)

Press Edit and assign the apps to the role. Afterwards save.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture16-5.png)

That’s it. Let’s jump to the app.

I installed the SAP Mobile Start app from the app store.

After opening the SAP Mobile Start app the first time, accept the End User License Agreement. Press on the “Get Started”. Now you need the scan the QR Code to connects SAP Mobile Start with your Work Zone site. You can find the QR Code in your Work Zone Site. You can open the site from the Site Directory.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture17-5.png)

In the top right corner select your Settings.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture18-4.png)

Select SAP Mobile Start Application and select “Register” afterwards.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture19-5.png)

Scan the QR-Code and press continue. Afterwards you have to login with your user on your mobile phone.

Next step is to Create a Passcode in SAP mobile Start, additionally I activated the Biometric Authentication. Now you should see your app in SAP Mobile Start.

Final result

![](/legacyfs/online/storage/blog_attachments/2023/06/Untitled-Project.gif)

If you have any issue, you can find additional information how to set-up SAP Mobile start here: [https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/sett...](https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition/setting-up-sap-mobile-st...