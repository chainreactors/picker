---
title: Workload Fluctuations / Sizing and Optimal Number of Application Servers
url: https://blogs.sap.com/2023/02/26/workload-fluctuations-sizing-and-optimal-number-of-application-servers/
source: SAP Blogs
date: 2023-02-27
fetch_date: 2025-10-04T08:10:52.424033
---

# Workload Fluctuations / Sizing and Optimal Number of Application Servers

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Workload Fluctuations / Sizing and Optimal Number ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/168693&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Workload Fluctuations / Sizing and Optimal Number of Application Servers](/t5/technology-blog-posts-by-sap/workload-fluctuations-sizing-and-optimal-number-of-application-servers/ba-p/13554765)

![christoph_weyd](https://avatars.profile.sap.com/9/a/id9a8d85d0f6eabecf6049618aad50983895674416bb9dd6c84dfa652ef720eb68_small.jpeg "christoph_weyd")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[christoph\_weyd](https://community.sap.com/t5/user/viewprofilepage/user-id/258399)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=168693)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/168693)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554765)

‎2023 Feb 26
6:41 PM

[19
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/168693/tab/all-users "Click here to see who gave kudos to this post.")

5,137

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

## Introduction

Most SAP Systems are configured in a three-tier configuration with multiple application servers. For a given peak number of users/transactions and a resulting peak usage of system resources CPU/Memory/Work Processes a frequent question asked is how to configure the landscape; is it better to use only a few big application servers or rather many small servers.

![](/legacyfs/online/storage/blog_attachments/2023/02/Overview-1.png)

Although there are Pro's and Con's for larger/smaller number of servers one very important aspect which is very often neglected in this evaluation, is the impact of the various types of workload fluctuations on the overall system hardware requirements and stability of the system.

In this blog post we want to give a bit more insight on the different type of fluctuations and how those can impact the landscape design and sizing calculations.

## **Content**

+ **[Fluctuation Types](#toc-hId-569084898)**
+ **[Load Balancing Fluctuations](#toc-hId-372571393)**
+ **[Statistical Fluctuations](#toc-hId--609996132)**
+ **[Seasonal Fluctuations](#toc-hId--806509637)**
+ **[Daily Fluctuations](#toc-hId--655768785)**
+ **[Hourly Fluctuations](#toc-hId--852282290)**
+ **[Summary](#toc-hId--1048795795)**
+ **[Conclusions](#toc-hId--1441822805)**

## Fluctuation Types

We can group workload fluctuations into the following four areas:

+ Seasonal differences in the number/type of executed business transactions (e.g., increased number of transactions around Christmas, Black Friday...)
+ Daily workload patterns
+ Load balancing
+ Statistical fluctuations

The low frequency seasonal fluctuations are difficult to predict and depend often on macro-economic factors. Daily fluctuations however show very often a regular pattern which is stable over large time periods.

Fluctuations resulting from load balancing can somehow be influenced by the setup of logon groups, RFC server groups, batch server groups but at the same time a non-optimal setup can easily cause problems when some servers receive higher than desired workload.

The most ignored part of workload fluctuations however is resulting from the random behavior of the user interactions with the system itself, those fluctuations can only be described by statistical models or simulations which we explain further below.

## Load Balancing Fluctuations

To protect the system from hardware failures of individual servers and for scalability/cost reasons most customer use more than one SAP application server.

Load balancing will distribute the workload over these servers, but load balancing will introduce additional fluctuations which should be considered while sizing and designing the system. In order to get an estimation of those fluctuations we must know how many application servers will be used.

To avoid problems with load balancing the different logons groups should be either identical or distinct from each other, overlapping groups should be avoided.

In the below example the logon groups 1,2 are identical but distinct from group 3

![](/legacyfs/online/storage/blog_attachments/2023/02/LoadBalancing.Good_.png)

Below a bad configuration. Server 3 belongs to two logon groups and will receive the load of group 2 and Group 3. Compared to the servers 2,4,5 this server will likely receive higher load

![](/legacyfs/online/storage/blog_attachments/2023/02/LoadBalancing.Bad_.png)

**If a customer wants to separate users via logon groups from each other (*eg. dedicated servers for finance and logistics operations*) then the sizing and server layout should ideally be done separate too.**

Below a customer example. We see the main logon groups for end users and snapshots from SDFMON taken during peak business hours at 18:00 for consecutive days.

![](/legacyfs/online/storage/blog_attachments/2023/02/LoadBalancing.per-.ServerDay.png)

The differences between the different servers of the same logon group are much higher than one would expect if the logon balancing routine would create only statistical fluctuations.

The load balancing for “normal” users using the server with the best response time is assuming, that a user after the logon will start working and thus impacting/reducing the average response time on that server. The next user(s) would then be directed to another server. In real live many users will logon to the system in a relative short period of time (*start of business hours*). Many of those users however just logon, but they do not start working (*many users first read their emails, prepare a coffee…*). As result the average dialog response time of the fastest server remains unchanged for a longer period of time, thus attracting like a magnet much more users.

In most customer systems the user threshold parameter is not used, therefore we see typically fluctuations between the different servers of the same logon group which exceed the expected standard deviation by a factor of 2.5 to 4.5. Using the user threshold parameter can help distributing the number of users more evenly across the application server.

Goto SMLG, select a logon group and maintain user threshold value.

![](/legacyfs/online/storage/blog_attachments/2023/02/SMLG.User_.Threshold.png)

Using the user threshold parameter (*ideally set to around 60% of the peak logons per server*) can help to reduce the fluctuations as shown in the below example.

![](/legacyfs/online/storage/blog_attachments/2023/02/LoadBalancing.per-.ServerDay.Improved.png)

After setting the threshold parameter the imbalances between the servers significantly decreased from 30%-60% down to 12-15%.

to ...