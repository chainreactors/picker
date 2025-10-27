---
title: How to use filters in SAP AppGyver
url: https://blogs.sap.com/2022/12/21/how-to-use-filters-in-sap-appgyver/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:02.503910
---

# How to use filters in SAP AppGyver

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to use filters in SAP AppGyver

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160697&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use filters in SAP AppGyver](/t5/technology-blog-posts-by-members/how-to-use-filters-in-sap-appgyver/ba-p/13554010)

![vikas_992001](https://avatars.profile.sap.com/f/d/idfdd0a879f46a97393c0ce597c2070d4f613c571fc63330f09be55b52b9f7e073_small.jpeg "vikas_992001")

[vikas\_992001](https://community.sap.com/t5/user/viewprofilepage/user-id/149885)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160697)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160697)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554010)

‎2022 Dec 21
7:04 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160697/tab/all-users "Click here to see who gave kudos to this post.")

3,500

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (2)

In this blog we will learn how we can filter our data in SAP AppGyver using Data entity. For this blog I will be using Northwind oData for my backend and how we can filter the data in our UI application.

# Introduction

[AppGyver](https://answers.sap.com/tags/6cfd8176-04ae-4548-8f38-158456e1a47a) is a low-code/no-code (LCNC) platform designed to streamline app development. AppGyver's core feature, has a drag-and-drop interface that allows users to add buttons and animations, create dropdown menus, import data, and build automated workflows. Think of it as an online editor where you can enter data to draw business processes or workflows within the app.

Working with SAP [AppGyver](https://answers.sap.com/tags/6cfd8176-04ae-4548-8f38-158456e1a47a), most of your time will be spent in the **app builder**.

It allows you to:

* Define your app's structure and navigation logic

* Build pixel-perfect user interfaces

* Create complex logic with visual programming

* Integrate with external data resources

* Bind data to your components to create dynamic views, and more.

I would recommend you too go through this link to get started with [AppGyver](https://answers.sap.com/tags/6cfd8176-04ae-4548-8f38-158456e1a47a).

<https://docs.appgyver.com/docs/home>

# Solution

To start with, we are going to create a **data entity** which will fetch our backend data. Click on create data entity and then click on oData integration.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-19-105142.png)

Enter the URL and verify it. Then select your entity and do a test run to verify the data. Save data resource.

![](/legacyfs/online/storage/blog_attachments/2022/12/oDataIntegration.png)

An entity will be created

![](/legacyfs/online/storage/blog_attachments/2022/12/Entity-1.png)

Now create a **Data variable** using the same property as defined in the screen shot and click on **save**. We will use this property to bind it with our list on the UI.

![](/legacyfs/online/storage/blog_attachments/2022/12/CreateDataVariabel.png)

Now we have to create a basic list to use this entity in our UI. So, we will create a **list item** by drag and drop. Now click on the list item and select repeat with.

![](/legacyfs/online/storage/blog_attachments/2022/12/ListItem.png)

Now click on **Data and Variables**and then click on the **D****ata** **variable** created and **save**.

![](/legacyfs/online/storage/blog_attachments/2022/12/RepeatWith.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/SelectDataVariable.png)

After binding the data to the list, the list item should look like in the below screen shot with repeated entries.

![](/legacyfs/online/storage/blog_attachments/2022/12/BindedEntity-1.png)

Now we have to bind our **Primary**and **Secondary label**. To bind click on the button ABC and then click on **Data item in repeat**.

![](/legacyfs/online/storage/blog_attachments/2022/12/ABC.png)

Select your field and save it.

![](/legacyfs/online/storage/blog_attachments/2022/12/DataItemField-1.png)

We can use formula too, here I am concatenating first name and Last name of Employee.

![](/legacyfs/online/storage/blog_attachments/2022/12/ConcatFirstLastName.png)

Now once binding is done for all fields, we can preview our data by downloading the SAP [AppGyver](https://answers.sap.com/tags/6cfd8176-04ae-4548-8f38-158456e1a47a) app from PlayStore/AppleStore and scanning the QR code. The QR code can be obtained by clicking on the **Launch** button in home screen. I am skipping this part for users. once we complete all the steps, we will be able to preview our app in mobile.

This is our expected output result.

![](/legacyfs/online/storage/blog_attachments/2022/12/MobileResult.png)

Now we are all set to use a filter in our list. To use the filter, we have to click on **repeat with** button, select formula and replace our query as mentioned below and click on **save**.

```
SELECT(data.EmployeesData, item.City == 'Seattle')
```

![](/legacyfs/online/storage/blog_attachments/2022/12/FilterQuery.png)

Once we save all our changes, we can see our preview again in mobile app, we will get the list of data which matches the city 'Seattle'.

![](/legacyfs/online/storage/blog_attachments/2022/12/FinalResultFilter.png)

For more informtaion you can check these links too.

[SAP Build Apps | SAP Community](https://community.sap.com/topics/build-apps)

[SAP Builders - SAP Community Groups](https://groups.community.sap.com/t5/sap-builders/gh-p/builders)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-use-filters-in-sap-appgyver%2Fba-p%2F13554010%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [RAP Using Custom Entity with load multiple data using Pagination and Preview using UI annotations](/t5/technology-q-a/rap-using-custom-entity-with-load-multiple-data-using-pagination-and/qaq-p/14233901)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  14 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/techno...