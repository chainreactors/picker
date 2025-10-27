---
title: Developing a New Custom Data Source in SAP C4C
url: https://blogs.sap.com/2023/01/18/developing-a-new-custom-data-source-in-sap-c4c/
source: SAP Blogs
date: 2023-01-19
fetch_date: 2025-10-04T04:16:40.002455
---

# Developing a New Custom Data Source in SAP C4C

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Developing a New Custom Data Source in SAP C4C

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6313&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Developing a New Custom Data Source in SAP C4C](/t5/crm-and-cx-blog-posts-by-members/developing-a-new-custom-data-source-in-sap-c4c/ba-p/13561925)

![msalmani](https://avatars.profile.sap.com/e/0/ide01fadfb8b08f371a1fe9683c864e9265dbeb09bc3ec9c8e0948ed51685c31cc_small.jpeg "msalmani")

[msalmani](https://community.sap.com/t5/user/viewprofilepage/user-id/43930)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6313)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6313)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561925)

‎2023 Jan 18
8:55 PM

[2
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6313/tab/all-users "Click here to see who gave kudos to this post.")

4,694

* SAP Managed Tags
* [SAP Cloud Applications Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Applications%2520Studio/pd-p/67837800100800006741)
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)
* [SAP Service Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520Cloud/pd-p/73555000100700000801)
* [C4C Analytics](https://community.sap.com/t5/c-khhcw49343/C4C%2520Analytics/pd-p/511689111249479074500962158147418)
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)
* [C4C Service](https://community.sap.com/t5/c-khhcw49343/C4C%2520Service/pd-p/569449780209093647095570245113309)

* [SAP Cloud Applications Studio

  SAP Cloud Applications Studio](/t5/c-khhcw49343/SAP%2BCloud%2BApplications%2BStudio/pd-p/67837800100800006741)
* [C4C Analytics

  Software Product Function](/t5/c-khhcw49343/C4C%2BAnalytics/pd-p/511689111249479074500962158147418)
* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)
* [C4C Service

  Software Product Function](/t5/c-khhcw49343/C4C%2BService/pd-p/569449780209093647095570245113309)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)
* [SAP Service Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BService%2BCloud/pd-p/73555000100700000801)

View products (6)

# 1. Introduction

In this blog, you will learn how to develop a new custom data source in SAP C4C. This data source can be used further for developing a new report, key figure or a new custom KPI. It means, developing a data source gives us more flexibility to develop more helpful analytical dashboards and reports.

# 2. Data Source Types

Based on what SAP explained [here](https://help.sap.com/docs/SAP_CLOUD_FOR_CUSTOMER/66e9a9081a7b40e38c8604d6617d0311/b1a76330cbd74ff5b987d48ab1a00d68.html), two types of custom data sources could be created in C4C:

* **Combined Data Sources**: this type combines at least two data sources which are expected to have same set of characteristics and different key figures to have all of the key figures in one place. However, in some cases you may create a combined data sources for gathering different characteristics which are not available purely in one single data source.

* **Joined Data Sources**: this type can be used when at least two different data sources have same characteristics and different key figures and joining them will set all these characteristics beside each other. It is possible to have more than one join. In C4C you can create two types of joined data sources:

  + **Inner Join**: In this case, only records will be joined which exist in all of the selected data sources.

  + **Left Outer Join**: In this case records inside the data source selected as anchor will be considered as source and the additional characteristics of the records in other data sources with the same characteristics will be added to it.

# 3. Developing a New Custom Data Source

To develop a new custom data source, you should at first access "Business Analytics - Design Data Sources" through SAP C4C main manu:

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-1-2.jpg)

Image 01: Accessing Data Source Work Center

As the next step, you can clock "New" and then select desired data source type which can be Joined or Combined as explained in previous section:

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-2-2.jpg)

Image 02: Selecting Desired Data Source Type

## 3.1. Developing a Joined Data Source

If you select "Joined Data Source" in Image 02, you can create a joined data source after which you see following screen. Here you can enter Name and Description of the data source and determine desired Join Type. In this example, you want to create a Joined Data Source with type Inner Join.

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Joined-01-2.jpg)

Image 03: Creating a Joined Data Source - Step 01

As you see above, as the next step you should add standard Data Sources by pressing "Add Data Source", after which you can select desired data sources and required characteristics as following:

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Joined-02.jpg)

Image 04: Creating a Joined Data Source - Step 02

After adding all desired data sources and selecting required characteristics, you can see that C4C identifies possible characteristics for joining records, however, you can remove them or add new joins.

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Joined-03.jpg)

Image 05: Creating a Joined Data Source - Step 03

As the final step, you can save and close it, afterwards you can run it by selecting the data source and pressing "Preview":

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Joined-04.jpg)

Image 06: Preview a Joined Data Source

If you run it, you can see how corresponding records will be joined. On the right side, you can determine which characteristics and key figures could be visible:

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Joined-05-1.jpg)

Image 07: Run a Joined Data Source

## 3.2. Developing a Combined Data Source

If you select "Combined Data Source' in Image 02, you can create a combined data source after which you see following screen. Here you can enter Name and Description of the data source.

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Combined-01.jpg)

Image 08: Creating a Combined Data Source - Step 01

As you see above, as the next step you should add standard Data Sources by pressing "Add Data Source", after which you can select desired data sources and required characteristics as following:

![](/legacyfs/online/storage/blog_attachments/2023/01/C4C-Combined-02-1.jpg)

Image 09: Creating a Combined Data Source - Step 02

After adding all desired data sources and selecting required characteristics, you can see that C4C identify possible characteristics for mapping records, however, you can remove them or add other ...