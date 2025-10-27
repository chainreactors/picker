---
title: SAP HANA Monitoring with RybaFish: custom KPIs
url: https://blogs.sap.com/2023/03/21/sap-hana-monitoring-with-rybafish-custom-kpis/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:15:05.705393
---

# SAP HANA Monitoring with RybaFish: custom KPIs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP HANA Monitoring with RybaFish: custom KPIs

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160703&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP HANA Monitoring with RybaFish: custom KPIs](/t5/technology-blog-posts-by-members/sap-hana-monitoring-with-rybafish-custom-kpis/ba-p/13554016)

![rybafish](https://avatars.profile.sap.com/b/a/idbacaa362a9809557fbbb60f1410460fcbeb5136ba70969732c0a16ed0a3d06af_small.jpeg "rybafish")

[rybafish](https://community.sap.com/t5/user/viewprofilepage/user-id/125151)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160703)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160703)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554016)

‎2023 Mar 21
5:23 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160703/tab/all-users "Click here to see who gave kudos to this post.")

1,079

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

Hello, HANA community.

Today I want to draw your attention to the visual aspect of information presentation.

The human brain is incredibly good at getting and interpreting visual information. We spent years in our high schools and universities analyzing graphs of functions and getting common with this form of information. A huge part of those charts has time on the X-axis, in this case, we have the value dependency on time. One extreme example of this approach is the so-called "black box" or flight recorder read-outs used in aircraft accident investigation.

![](/legacyfs/online/storage/blog_attachments/2023/02/blackbox-1.png)

Simplified sketch of a flight recorder readout

The key feature of black box red-outs is multiple charts on the same timeline. Values can be in different units of measure, which might be confusing in the beginning, because you cannot directly compare different metrics. But having things on the same chart makes it possible to see how different indicators correlate and you can get a multi-dimensional picture of the processes of the multifactor system.

People have been using those charts for decades to analyze the behavior of such a complex system as modern aircraft, so why don't we use the same approach for the database analysis? And in my experience, it makes nothing but sense: you can get a real quick impression of the system behavior just by having a quick glance at such a chart.

## Okay, now to SAP HANA

Luckily, SAP HANA already contains such a "flight recorder". A lot of useful telemetry is collected by the nameserver and put into nameserver\_history.trc file. This information is also available from m\_load\_history\* views. And this data can be visualized for interpretation, which gives us easy access to the insides of the database behavior.

Standard nameserver telemetry includes such KPIs as memory usage, CPU utilization, disk and network activity, transactions, locks, and many, *many* more: it is ~50 (!) of them available for each SAP HANA service. This already gives quite detailed information on the database's health. But the nameserver is limited to this decent yet fixed set of KPIs chosen by SAP engineers to be carefully collected every 10 seconds by every SAP HANA instance in the observable universe.

In some situations, we can benefit from having additional information on the screen based on other data sources like monitoring views, statistics service tables, or even business tables. And this can be done with custom KPIs.

There are three types of custom KPIs in [RybaFish](https://blogs.sap.com/tag/rybafish/): Regular, Gantt, and Multiline.

### Regular KPIs

Regular custom KPIs have the same principle as the standard ones: a measurement is done every moment in time. Unlike standard ones, regular custom KPIs are based on an alternative source of data (not m\_load\_history\* views). There is a blog post with a step-by-step implementation of custom KPI to [monitor SAP HANA table size](https://blogs.sap.com/2022/08/12/monitoring-table-size-in-sap-hana/).

### Gantt Chart

Thanks to Henry Gantt, we have a common way to visualize processes on timelines. And this could be an extremely informative way to show activities in such a noisy system as a corporate database.

Unlike the standard KPIs like memory usage or CPU consumption, processes have start and end times. Examples of processes are: delta merges, savepoints, abap jobs, internal threads, etc. But the most used one is the expensive statements.

Most of the activities in the database have a corresponding statement, and with proper trace configuration, the ones generating excessive resource consumption will be recorded in the expensive statements trace. What is recorded - can be visualized.

![](/legacyfs/online/storage/blog_attachments/2023/02/ss01.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/ss01_l.png)

In this case, we see three users (DATALOAD, RIP\_THE, TESTER) were executing statements in this timespan. It is very clear that statements  executed by RYP\_THE user are perfectly aligned with increased memory and CPU consumption. So, we know the user, the exact impact, and, if required, also the statement itself: in the application Gantt bars are clickable and you can see actual statement text.

This technique covers at least 80-85% of unusual activities in the database, and it is very convenient when you can get access to this information with just a mouse click.

### Multiline

In some cases, the information has an additional "dimension" coming from the data source itself. This characteristic can be used in visualization to get additional information on the chart.

For instance, let's have a look at aggregated host\_heap\_memory data. There is a "component" column that provides additional information on memory allocation purposes:

```
select server_timestamp, component, sum(exclusive_size_in_use)

from _sys_statistics.host_heap_allocators

where port = 30003

group by server_timestamp, component

order by server_timestamp desc, component;
```

![](/legacyfs/online/storage/blog_attachments/2023/02/ss05_table.png)

Having this visualized, we will see the heap memory distribution between different components (row-store not included):

![](/legacyfs/online/storage/blog_attachments/2023/02/ss02_.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/ss02_l.png)

Now it is obvious that increased memory consumption is related to the "System" and "Column Store" components. What is also interesting: after each statement execution the System component drops to its baseline, but the Column Store component usually stays on a bit higher level, compared to the start of the statement execution. This already reveals a lot about this activity, but there is even more we can get from the very same diagram.

If we zoom in on the "Suspicious execution" after 07:30, we...