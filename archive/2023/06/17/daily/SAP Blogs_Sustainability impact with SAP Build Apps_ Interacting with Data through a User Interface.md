---
title: Sustainability impact with SAP Build Apps: Interacting with Data through a User Interface
url: https://blogs.sap.com/2023/06/16/sustainability-impact-with-sap-build-apps-interacting-with-data-through-a-user-interface/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:11.190425
---

# Sustainability impact with SAP Build Apps: Interacting with Data through a User Interface

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Sustainability impact with SAP Build Apps: Interac...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162057&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Sustainability impact with SAP Build Apps: Interacting with Data through a User Interface](/t5/technology-blog-posts-by-sap/sustainability-impact-with-sap-build-apps-interacting-with-data-through-a/ba-p/13562509)

![szilo](https://avatars.profile.sap.com/e/7/ide76694b28c5cdcfc5cd9a72fd0a09f726ed89fc636a9d1b43ca6779f7c59570a_small.jpeg "szilo")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[szilo](https://community.sap.com/t5/user/viewprofilepage/user-id/177344)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162057)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162057)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562509)

‎2023 Jun 16
1:32 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162057/tab/all-users "Click here to see who gave kudos to this post.")

775

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

In the [previous blog post](https://blogs.sap.com/2023/06/13/a-low-code-no-code-journey-to-create-sustainability-impact-with-sap-build-apps/) we shared how we started our Low-Code/No-Code journey with SAP Build Apps. We gave you a sneak peek into our sustainable app, GreenLeenk that serves as our low-code/no-code playground to learn how to create a mobile application having no coding experience.

As GreenLeenk collects and showcases all restaurants in the user’s vicinity that make a conscious effort to run their business along sustainable guidelines and offer a “green” ambience for diners, we first started by implementing the restaurant related elements of the application. In this blog post, we will show you how we added and maintained the restaurants’ data on our app.

First you need to create the *UI fields for the data* (restaurants and website). Since these will be different every time a new user inputs their restaurant information, you set them up as your *Page variables* and dynamically define the *value* that these elements hold (name of the restaurant and the URL link). Once the *Page variables* hold the data that the users insert, you need to ensure that the data is updated in the backend table for each newly added restaurant. For this you first have to set up the *data resources* (restaurant and website fields), bind them to the backend with a *Button* and *record* their *properties* in the backend table. The process may seem complex at first glance but once you understand the app logic, it’s easy to accomplish: practically what you need to do is to create both the front and backend parts and bind them. Let’s see these steps in more details.

We kept the UI very simple. Do you remember SAP’s old slogan “Run simple!”? We still nurture this approach and we decided to ask the users to add only the name of the restaurant and its website. If our app is going to be developed further, we will implement more features like the possibility to call the restaurant or make a reservation directly from the app. However, we wanted to start our citizen developer journey with more simple challenges.

![](/legacyfs/online/storage/blog_attachments/2023/06/initial.jpg)

We found all the components we needed in the *Core* elements’ list. In case you don’t find the right building blocks, you can always browse the *Marketplace* or [create your own component](https://docs.appgyver.com/v1/docs/creating-and-editing-view-components) and make it available under the *By Me* tab.

![](/legacyfs/online/storage/blog_attachments/2023/06/core.jpg)

We started to build the UI by selecting the *Title* component and used the *Text* component for the subtitle part from the *Basic components* group.

On the left-hand side of the app you can pull different elements onto the UI canvas, the right-hand side of the UI composer lets you modify each component. We created the subtitle easily by adding the text under the *Content* part of the *Properties* tab.

![](/legacyfs/online/storage/blog_attachments/2023/06/title.jpg)

To display the restaurant’s name and the related website we used two *Input fields*. Quick tip: whenever you keep using the same element, it saves up a lot of time to use the *Duplicate* function then the same element can be placed on the canvas several times.

![](/legacyfs/online/storage/blog_attachments/2023/06/duplicate-component.jpg)

We divided the two components with *Containers* to create more space on the canvas. This was our own, first-time user, way of separating the different elements but once you read the AppGyver documentation, you learn to [modify the gaps](https://docs.appgyver.com/docs/style) to achieve the ideal spacing. However, we liked the flexibility of the app and we kept the containers on the canvas.

![](/legacyfs/online/storage/blog_attachments/2023/06/container.jpg)

Creating the UI part was rather quick. We found the *Page layout* field also handy because it allows you to review the whole structure of the UI. If you click on any of the elements, it highlights the component and brings you to it immediately and you can modify it according to your needs.

![](/legacyfs/online/storage/blog_attachments/2023/06/tree.jpg)

Once the UI part was ready, we had to connect the frontend with the backend table that we separately created. We chose the *Button* component to add and update the restaurants’ individual data to the backend table.

![](/legacyfs/online/storage/blog_attachments/2023/06/button-component.jpg)

To create the backend connection, you need to configure the REST API*.* To understand more about this, please see this blog on [Understanding REST APIs](https://blogs.sap.com/2022/08/18/what-are-rest-apis-in-sap-appgyver/).

Using the method highlighted in the blog above, we created a data entity called restaurants. We will now understand how to update the backend using the UI through the API.

First, we created two *P**age variables*: one for the restaurant’s name and one for restaurant’s website:

![](/legacyfs/online/storage/blog_attachments/2023/06/variables.jpg)

See this [blog](https://blogs.sap.com/2022/06/15/what-are-variables-i...