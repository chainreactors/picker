---
title: Capacity Planning (Leveling) and Evaluation in S4HANA – Step by Step Guide
url: https://blogs.sap.com/2023/02/18/capacity-planning-leveling-and-evaluation-in-s4hana-step-by-step-guide/
source: SAP Blogs
date: 2023-02-19
fetch_date: 2025-10-04T07:29:47.571938
---

# Capacity Planning (Leveling) and Evaluation in S4HANA – Step by Step Guide

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Capacity Planning (Leveling) and Evaluation in S4H...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67189&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Capacity Planning (Leveling) and Evaluation in S4HANA - Step by Step Guide](/t5/enterprise-resource-planning-blog-posts-by-members/capacity-planning-leveling-and-evaluation-in-s4hana-step-by-step-guide/ba-p/13552256)

![RaghavanKathamuthu](https://avatars.profile.sap.com/e/c/idec1218e9fc1f14973ed92ad10f63cc2714062e17d3c033925faa528388406f2a_small.jpeg "RaghavanKathamuthu")

[RaghavanKathamuthu](https://community.sap.com/t5/user/viewprofilepage/user-id/17050)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67189)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67189)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552256)

‎2023 Feb 18
2:37 PM

[17
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67189/tab/all-users "Click here to see who gave kudos to this post.")

20,802

* SAP Managed Tags
* [MAN (Manufacturing)](https://community.sap.com/t5/c-khhcw49343/MAN%2520%28Manufacturing%29/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [SCM APO Production Planning and Detailed Scheduling (PP/DS)](https://community.sap.com/t5/c-khhcw49343/SCM%2520APO%2520Production%2520Planning%2520and%2520Detailed%2520Scheduling%2520%28PP%252FDS%29/pd-p/535959991487463189008370055922387)

* [MAN (Manufacturing)

  Software Product Function](/t5/c-khhcw49343/MAN%2B%252528Manufacturing%252529/pd-p/9aaa6d7b-e017-4ddc-805d-9bbd02a6c46d)
* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [SCM APO Production Planning and Detailed Scheduling (PP/DS)

  Software Product Function](/t5/c-khhcw49343/SCM%2BAPO%2BProduction%2BPlanning%2Band%2BDetailed%2BScheduling%2B%252528PP%25252FDS%252529/pd-p/535959991487463189008370055922387)

View products (3)

**Introduction**
In this blog we will see the capacity leveling and evaluation. **Capacity evaluation** is just a monitor to see weather all the resource/ work centers are available or not. **Capacity leveling** is moving the orders from one date to other if the capacity is not available or overloaded.

Before that why we need capacity apps in PP?

In APO all the materials will be planned by considering all the operation time and work centers as **finite capacity** in MRP itself. So all production orders will be created by considering the capacity accurately (Work hours, Break time, shift time, relationship time, inter operation time, Splits). Here we are in no need of Capacity planning.

But in PP all the  materials are planned by considering all the operation time and work centers as **infinite capacity** in MRP. so the system will not consider the capacity accurately. So the production orders will be created without considering the capacity. The operation times are considered only per order per material. For a material all orders will be created on same day. Since we need to do capacity leveling again in PP system.

That's why we are using APO for Planning (MRP) and PP for execution (Confirmation, GI, GR).

**Finite Capacity** - Molding machine which can handle certain amount of product on a day

**Infinite capacity** - Cooling silo which can cool enormous amount of air on a day

**Main Part -** Master data

Created materials and BOM as usual. Resource / Work center - MOULD with 24 working hrs. per day

![](/legacyfs/online/storage/blog_attachments/2023/02/WC.png)

Note : I missed to mention the active version. But its mandatory for Mange work center capacity app.

Capacity Formulas to be maintained.

![RaghavanKathamuthu_0-1726086975073.png](/t5/image/serverpage/image-id/165349iAA1BBEA4285B2FC7/image-dimensions/603x276?v=v2 "RaghavanKathamuthu_0-1726086975073.png")

Routing - Here I mentioned 24 hrs. for making 1 magazine.

![](/legacyfs/online/storage/blog_attachments/2023/02/Routing.png)

As per the above master data we can manufacture only one magazine per day as the machine MOULD can work 24 hrs. a day. Creating one production order for 1 quantity.

![](/legacyfs/online/storage/blog_attachments/2023/02/prd-ord-1.png)

I am using forward scheduling and starting on 20.02.2023. As per above statement it take 1 day to produce one magazine and the production gets ended by 20.02.2023.

**Capacity Evaluation -** We will see the app manage work center capacity app

At first maintain the area of responsibility in app settings. Otherwise work center will not be visible in app. Here we could see one production order on date 20.02.2023. The color is amber as the capacity is fully utilized. If its red means overload and green means under load.

![](/legacyfs/online/storage/blog_attachments/2023/02/app-set.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/AOR-1.png)

Now I am creating another order on same day 20.03.2023

![](/legacyfs/online/storage/blog_attachments/2023/02/prd-ord-2.png)

You may expect the new order should start by next date 21.02.2023, since we have capacity check in production order screen and we already have one order on 20.02.2023.

But PP system will not schedule the orders by considering the capacity by itself. If the order needs to schedule to next day you need to go to capacity planning table for evaluating the capacity condition and to put the schedule start data on next available capacity date.

![](/legacyfs/online/storage/blog_attachments/2023/02/cap-p-tab.png)

But this will also not be possible in FIORI if you are using grand chart capacity evaluation profile. Side by side you can use Monitor work center schedule apps for understanding it. Here also assign the area of responsibility in app settings.

It will not be possible to do the scheduling one by one. So we have an app called Manage work center capacity to see all the capacity overloads.

Now save the production order and go to Manage work center capacity app.

![](/legacyfs/online/storage/blog_attachments/2023/02/overload.png)As two orders scheduled on same day the evaluation app shows overload. Now capacity evaluation is done. i.e. we have realized that there are some overload in work center. Now we have to reduce the overload. So we have to either delete or reschedule the production order.

Also you can use the Monitor work center schedules app to get the detailed view.

![](/legacyfs/online/storage/blog_attachments/2023/02/sche1.png)Here you can see two orders scheduled on same day. (Click arrow mark near work center to see the no of orders on same work center)

**Capacity Leveling -**To reduce the overload we need to use schedule production app

To see the data in schedule production app we need to mention bottleneck work center (work ...