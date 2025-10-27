---
title: Do More With Less. Performance Analysis for Hardware Optimization in SAP Systems.
url: https://blogs.sap.com/2022/12/16/do-more-with-less.-performance-analysis-for-hardware-optimization-in-sap-systems./
source: SAP Blogs
date: 2022-12-17
fetch_date: 2025-10-04T01:46:15.015356
---

# Do More With Less. Performance Analysis for Hardware Optimization in SAP Systems.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Do More With Less. Performance Analysis for Hardwa...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68302&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Do More With Less. Performance Analysis for Hardware Optimization in SAP Systems.](/t5/enterprise-resource-planning-blog-posts-by-members/do-more-with-less-performance-analysis-for-hardware-optimization-in-sap/ba-p/13566214)

![andrew_varney](https://avatars.profile.sap.com/8/5/id857d22d962f7ec4116805d17331062cba9cdc9f61945d1b8761c882ea041b8cb_small.jpeg "andrew_varney")

[andrew\_varney](https://community.sap.com/t5/user/viewprofilepage/user-id/392855)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68302)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68302)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566214)

‎2022 Dec 16
6:22 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68302/tab/all-users "Click here to see who gave kudos to this post.")

1,374

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Sustainability](https://community.sap.com/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Sustainability

  Topic](/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)

View products (4)

## Introduction

SAP Performance is a broad topic. In this blog I'm going to explain a simple approach to reduce hardware utilization. This means identifying ways to reduce physical CPU, Memory, Disk, Database, Network load, etc. There are many great tools to help with this. Today I'll be using an app called Lensera. This one has a simple user interface and does a lot of the data-intensive work for you.

There are many reasons to look at improving system performance. For example:

* lowering infrastructure costs

* better sustainability

* improving user experience

* increased stability

## Where to start

Whether you're running your SAP systems in your own data centres or on your cloud infrastructure, at some point you will probably start to reach the physical limits of the servers. You may hear "We are running low on CPU" or "The memory is almost at 100%". Rather than upgrading the hardware or upsizing the VM, it's possible that some analysis and application changes can solve the problem.

Let's look at 3 examples of high usage: CPU, Memory, and Database Time - and pinpoint the root causes.

### High memory usage

The screenshot below is the default view when the app starts. It's showing the total Memory (RAM) usage across all SAP Application Servers. In this case there is one S/4HANA server, and one S/4HANA Gateway server. The Lensera application will group together as many SAP systems as you configure, or you can look at them individually.

This chart is showing the total memory usage of the 2 systems over a 7-day period. You can clearly see most of the memory is used during the 5 business days of the week.

![](/legacyfs/online/storage/blog_attachments/2022/12/Memory.png)

7 Day Memory Usage

Let's find out what caused one of the peaks. By zooming in and highlighting the area on the main chart, we can see each of the processes that ran during that time. In this example, transaction PFCG was being used heavily at that time, accounting for 56.6% of the memory used. Transaction PFCG is used to configure user roles in SAP.

![](/legacyfs/online/storage/blog_attachments/2022/12/Memory-Selection-2.png)

Peak Memory Selected

### High CPU Usage

From the menu, switch over to the CPU Metric. Again, most of the CPU is being used during business hours.

![](/legacyfs/online/storage/blog_attachments/2022/12/CPU.png)

7 Day CPU Usage

Zoom in and highlight the peak period. The top 15 CPU consuming processes are instantly shown below the chart. In this example, the Fiori Launchpad OData Page Builder service consumed 23.7% of the CPU during the selected period. The Page Builder service is required to run the Fiori Launchpad.

![](/legacyfs/online/storage/blog_attachments/2022/12/CPU-Selection.png)

Peak CPU Selected

### High Database Usage

There are a whole range of factors that affect the performance of the database. We will just look reducing Database load by finding the processes that spent the most time making database requests.

Select the desired time range and switch over to the Database Response Time metric:

![](/legacyfs/online/storage/blog_attachments/2022/12/DB-Time.png)

8 Days Database Time

Drag the mouse over the chart to highlight the peak. In this example, 48.5% of the database time used during the peak was due to the Task Processing OData process. This is used by Fiori apps like My Inbox.

![](/legacyfs/online/storage/blog_attachments/2022/12/DB-Time-Selection.png)

Peak DB Time Selected

## Next Steps

Now you know which transaction, OData service, RFC, Batch Job etc is causing the peak load, it's time to fix it.

* Check how often its running. It may be using so many resources because it's been scheduled to run way too often

* Schedule the SAT trace tool to capture the process as its running. This will give a granular performance profile of the selected process.

#### For standard SAP processes

* Check the SAT trace to see if a customer enhancement been done. Use the trace information to see how that code can be improved.

* Check the SAP Support Portal for more information or a Note that may fix the problem

#### For custom 'Z' processes

* Check the SAT trace to see how the code can be improved.

## Conclusion

Performing this analysis and implementing some changes can be a more sustainable and cost effective solution when hardware capacity is running low. Because the process is very simple to run, it can also be done as part of the ongoing management of the systems. As well as reducing load on the server, it should also improve response times and as a result, the user experience.

If you are facing an issue like this, hopefully the resolution becomes a little easier.

Please share your feedback or thoughts in the comments below.

Check out some of the other great performance related information on the [SAP Community Pages](https://community.sap.com/search/?ct=blog&q=performance)

* [capacity](/t5/tag/capacity/tg-p/board-id/erp-blog-members)
* [cpu](/t5/tag/cpu/tg-p/board-id/erp-blog-members)
* [database](/t5/...