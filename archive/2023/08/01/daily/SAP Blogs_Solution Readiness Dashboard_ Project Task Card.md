---
title: Solution Readiness Dashboard: Project Task Card
url: https://blogs.sap.com/2023/07/31/solution-readiness-dashboard-project-task-card/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T16:59:50.689060
---

# Solution Readiness Dashboard: Project Task Card

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Solution Readiness Dashboard: Project Task Card

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164114&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Solution Readiness Dashboard: Project Task Card](/t5/technology-blog-posts-by-sap/solution-readiness-dashboard-project-task-card/ba-p/13569086)

![Ravinakn](https://avatars.profile.sap.com/0/b/id0b9d2d3f2674768e2eeb70762d7d765a605cad77175b4b5a11d015cf3c6e3009_small.jpeg "Ravinakn")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ravinakn](https://community.sap.com/t5/user/viewprofilepage/user-id/5278)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164114)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164114)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569086)

‎2023 Jul 31
10:34 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164114/tab/all-users "Click here to see who gave kudos to this post.")

867

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (2)

## **Introduction**

This blog is part of the blogs series for the new "Solution Readiness Dashboard" delivered as part of Focused Build SP12 delivery. This blog focuses on the overview page and Detail page of the Project Task card.

## **Pre-requisite**

Please go through the first blog of the series :[Solution Readiness Dashboard – Initial set up and Pre-requisites](https://blogs.sap.com/2023/07/25/solution-readiness-dashboard-initial-set-up-and-pre-requisites/)

## **Overview Page:**

This card shows the total number of project task according to their statuses. The project task data is extracted from Project Management App.

![](/legacyfs/online/storage/blog_attachments/2023/06/PR_Task_Overview_page.jpg)

Project Task : Overview Page

## **Chart Legend:**

Depicts the statuses of the Project Task. Sequence of the color in the chart is constant.

## **Days until Next Q-gate:**

The data point in the header of chart  indicates the number of days until next quality gate. Tasks which are not in "Released status" are considered for calculation.

Data displayed in the card is categorized under 3 statuses. These statuses are decided based on the Task end date.

1. To Be Done

2. Overdue

3. Completed

**To Be Done :**
If the end date is lower than current date, Task is classified under this status.

**Overdue:**
If the end date is greater than current date, Task is said to be overdue.

**Completed:**
If the status of the task is completed, then it comes under completed status.

## **Detail Page:**

This detail page is build based on Fiori Analytical List Page. Navigation to detail page can be done from the header of the card which would display below page. Project name in the detail page is carried forward from the overview page.

![](/legacyfs/online/storage/blog_attachments/2023/06/Project_task_detail_page.jpg)

Project Task Detail Page

## **Variant Management and Save as tile**

Refer the [blog](https://blogs.sap.com/?p=1623941&preview=true&preview_id=1623941) for more information on how to save variant and save as Tile.

## **Filters:**

The filter bar provides filter options on Main/Single project , Build project, Wave, Task and Task type. By default below filter fields are displayed on the detail Page.

![](/legacyfs/online/storage/blog_attachments/2023/06/PR_Filter_default.jpg)

Project Task Detail Page : Default Filters

## **Task Type Filter:**

Task type value help consists of task types which are maintained in the below customizing.
*SAP Solution Manager-->Focused Build-->Project Management Configuration-->Focused Build Projects - Task Type Visibility*

## **Adapt Filters:**

It shows the additional filters which can be to filter bar.

![](/legacyfs/online/storage/blog_attachments/2023/06/Additional_Filters.jpg)

Project Task: Additional Filters

## **Chart:**

Chart is plotted using "Number of Task" as measure and "Task Status" as dimension. The chart used here is "Stacked Bar Chart" by default. However it can be changed in the chart settings as follows.

![](/legacyfs/online/storage/blog_attachments/2023/06/Detail_Page_chart.jpg)

Project Task : Stacked Bar Chart

![](/legacyfs/online/storage/blog_attachments/2023/06/Stacked_Bar_Chart.jpg)

Project Task : Chart Types

## **View Settings for the chart:**

In this settings, measures and dimension can be changed and based on the settings chart will be modified.

![](/legacyfs/online/storage/blog_attachments/2023/07/Project_task_view_settings_chart.jpg)

View Settings for Chart

## **Table:**

It displays the values based on the filters applied in the Filter bar.

![](/legacyfs/online/storage/blog_attachments/2023/06/Project_Task_Table-1.jpg)

Project Task : Table

The first column in the table is Task which is associated with link and on click of link would lead to Project Management App. More information about the task can be found on project management app.

## View Settings for the Table:

By using this option, columns seen in the table can be controlled.

![](/legacyfs/online/storage/blog_attachments/2023/07/Project_task_view_settings.jpg)

Project Task :View Settings

## **Export to Excel:**

Project Tasks can be exported to excel sheet to analyze further. This icon will be loaded as soon as table loads with values.

![](/legacyfs/online/storage/blog_attachments/2023/07/Issue_Export_to_spreadsheet.jpg)

*Project Task :Export to Excel*

## Important Links and Resources

* [Focused Build SP12 Released.](https://blogs.sap.com/2023/07/03/support-package-12-of-focused-build-has-been-released/)

* [Understanding the New “Solution Readiness Dashboard”](https://blogs.sap.com/2023/07/25/understanding-the-new-solution-readiness-dashboard/)

* [Usage Rights](https://support.sap.com/en/alm/usage-rights.html)

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [focused build](/t5/tag/focused%20build/tg-p/board-id/technology-blog-sap)
* [R2D in focused Build](/t5/tag/R2D%20in%20focused%20Build/tg-p/board-id/technology-blog-sap)
* [Solution Readiness Dashboard](/t5/tag/Solution%20Readiness%20Dashboard/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/provi...