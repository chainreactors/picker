---
title: Sustainability impact with SAP Build Apps: Simplified user management and authentication
url: https://blogs.sap.com/2023/07/14/sustainability-impact-with-sap-build-apps-simplified-user-management-and-authentication/
source: SAP Blogs
date: 2023-07-15
fetch_date: 2025-10-04T11:52:45.042289
---

# Sustainability impact with SAP Build Apps: Simplified user management and authentication

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Sustainability impact with SAP Build Apps: Simplif...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161131&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Sustainability impact with SAP Build Apps: Simplified user management and authentication](/t5/technology-blog-posts-by-sap/sustainability-impact-with-sap-build-apps-simplified-user-management-and/ba-p/13559889)

![szilo](https://avatars.profile.sap.com/e/7/ide76694b28c5cdcfc5cd9a72fd0a09f726ed89fc636a9d1b43ca6779f7c59570a_small.jpeg "szilo")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[szilo](https://community.sap.com/t5/user/viewprofilepage/user-id/177344)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161131)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161131)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559889)

‎2023 Jul 14
9:45 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161131/tab/all-users "Click here to see who gave kudos to this post.")

699

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

We have arrived at the last chapter of our citizen developer journey. Through the [previous blog posts](https://blogs.sap.com/2023/07/07/sustainability-impact-with-sap-build-apps%E2%80%AFdevelop-rate-and-share-your-green-experience/) we introduced you to our GreenLeenk application. We showed you how we built the prototype of an application using SAP Build Apps that gathers all sustainable restaurants in the app user’s location. In this closing blog post we have still a lot to share about how we developed user management to create a user-friendly and simple access both for first time users and those whole already joined the GreenLeenk community.

First time app users have three options to access GreenLeenk based on which we developed the user management pages. They can **sign up** as a permanent user, which means they would get directed to a **Login** page next time, or they can opt to explore the application **as a Guest**.

The **initial Landing page** contains these three options along with a short welcome message and an image.

![](/legacyfs/online/storage/blog_attachments/2023/07/landing-page.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/landing-sign-up.jpg)

The **sign-up page** holds a welcome message and the basic user data like name, email address and password. For each of these elements we used a separate *Container* with an *Input field* in it.

To ensure better user experience, we also incorporated a *Find my location* functionality to the page.

![](/legacyfs/online/storage/blog_attachments/2023/07/signup-landing.jpg)

Majority of our login was handled by Xano’s authentication API. More information on this can be found in their [official documentation](https://docs.xano.com/building-features/authentication-sign-up-and-log-in/authentication). We configured our REST API in Build Apps as per Xano’s guidance:

![](/legacyfs/online/storage/blog_attachments/2023/07/configure-rest-base.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/07/signup-create-record.jpg)

It is important to note that the *authToken* will act as your unique identifier in Build Aps. That is, the *authToken* will be used to remember that you are the one logged in. Remember to create an app variable to hold this information:

![](/legacyfs/online/storage/blog_attachments/2023/07/app-variables.jpg)

Behind the Sign-up *Button* we created logic to make the sign in work. Firstly, we added a *Create record* component and linked it to our Signup API:

![](/legacyfs/online/storage/blog_attachments/2023/07/signup-button-logic.jpg)

We then set the *authToken app variable* to the value of the return value we get from the API call:

![](/legacyfs/online/storage/blog_attachments/2023/07/Signup.jpg)

If the user has already signed up, next time he would directly see the **Login page** and fill out the Username and Password fields that have been built the same way as before. We used *Container* components to hold the data of the respective *Input fields*.

![](/legacyfs/online/storage/blog_attachments/2023/07/login.jpg)

Now for the login, first we have to configure our API as we did for the Sign-up part:

![](/legacyfs/online/storage/blog_attachments/2023/07/configure-login.jpg)

With the following schema:

![](/legacyfs/online/storage/blog_attachments/2023/07/create-record-login.jpg)

The Xano API will ensure that the login details are correct and handle the authentication. All that’s left for you to do is to create a data record using the login API and set your *authToken* app variable as we did with sign on:

![](/legacyfs/online/storage/blog_attachments/2023/07/variable-logic.jpg)We also created a user variable and set the values as per the response schema of the API to ease our developments, but this is optional.

If you use GreenLeenk **as a Guest**, you would be able to perform basic functions, like adding restaurants, or viewing restaurants but you will not be able to interact with the app in anyway that would require data for your user to be maintained.

Since our developments, some upgrades have been done within Build Apps and BTP authentication is now available. For more information on this, see this [youtube video.](https://www.youtube.com/watch?v=DxeNG_S9Nw0)

On this page the Welcome message automatically populates the name of the registered user to give a personal touch to the app. This has been achieved by a simple *Container* holding a *Title* field and a variable *Text* field. Then we offered to choose from three path to follow: users can quickly review which are the Top restaurants that gained recognition due to their green efforts and visit any of them. Alternatively, they can search within the GreenLeenk database according to their liking. From this page they can jump onto the site where they can add a newly discovered environmentally conscious place.

With this we have reached the goal of our project. We created the prototype of a small application with SAP Build Apps. The app is working as expected: you can register for it or use it as a Guest user. You can browse in its database and add new sustainable restaurants to it. We still have ide...