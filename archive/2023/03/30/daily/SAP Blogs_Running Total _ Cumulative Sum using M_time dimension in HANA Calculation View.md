---
title: Running Total / Cumulative Sum using M_time dimension in HANA Calculation View
url: https://blogs.sap.com/2023/03/29/running-total-cumulative-sum-using-m_time-dimension-in-hana-calculation-view/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:48.396180
---

# Running Total / Cumulative Sum using M_time dimension in HANA Calculation View

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Running Total / Cumulative Sum using M\_time dimens...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161851&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Running Total / Cumulative Sum using M\_time dimension in HANA Calculation View](/t5/technology-blog-posts-by-members/running-total-cumulative-sum-using-m-time-dimension-in-hana-calculation/ba-p/13560214)

![Dhanasekar_C](https://avatars.profile.sap.com/6/d/id6d63904ba647dd6911d266d5c070a3208d3ad8ae2ca8e41950f9b6d301f4d94c_small.jpeg "Dhanasekar_C")

[Dhanasekar\_C](https://community.sap.com/t5/user/viewprofilepage/user-id/847331)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161851)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161851)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560214)

‎2023 Mar 29
11:03 PM

0
Kudos

2,704

* SAP Managed Tags
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

View products (1)

## Introduction

Usually, In Running total, we aggregate the total measure/assets which means from the start date to till date. There are multiple ways to achieve a running total. In this blog, we are going to work on using the M\_time dimension in the Graphical Calculation view (HANA STUDIO).

## Content

A time dimension is a hierarchical structure whose members represent different timescales, including years, semesters, quarters, months, weeks, days, and so on. A time dimension is useful for time-based analysis and reporting since it offers various levels of granularity and time levels.

Here we have taken VBAK where sales order header details will be stored.

* Select the required fields and get the input as a year.

* Create a calculated column 'C\_year' where we separate the year from the respective field.

```
  leftstr( "ERDAT" ,4) // C_year
```

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-26-182736.png)

* Create another calculated column 'dummy' where we hardcode the value it can be any value, here I have used ‘A’ as a hardcode value for 'dummy', then have a filter for 'C\_year' which must be less than or equal to the input year(ip\_year). **![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-140820.png)**

and in Parallel, add the 'dummy' calculated column as same as before for M\_time dimension with the same value and add a range to the 'year'. Here in this system data is available only from 2016 so created a filter from 2016 to the input year (starting year [2016] is optional).

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-140933.png)

Then add the projection using inner join for the dummy field to have an all combination of years.

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-180652.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-141347.png)

Then have a filter calculated year less than or equal to the year from the M\_time dimension.

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-141610.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-141522.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-141646.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-132826.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-27-141841-1.png)

## Conclusion

Similarly, using the M\_time dimension, we can get the Running Total for month-wise and week-wise also. Hope this blog will be useful for a better understanding of the concept of running total using the M\_time dimension.

* [cumulative sum](/t5/tag/cumulative%20sum/tg-p/board-id/technology-blog-members)
* [M\_time dimension](/t5/tag/M_time%20dimension/tg-p/board-id/technology-blog-members)
* [M\_time dimension in HANA Calculation View](/t5/tag/M_time%20dimension%20in%20HANA%20Calculation%20View/tg-p/board-id/technology-blog-members)
* [running total](/t5/tag/running%20total/tg-p/board-id/technology-blog-members)
* [Running Total Cumulative Sum using M\_time dimension in HANA Calculation View](/t5/tag/Running%20Total%20Cumulative%20Sum%20using%20M_time%20dimension%20in%20HANA%20Calculation%20View/tg-p/board-id/technology-blog-members)
* [running total graphical cv](/t5/tag/running%20total%20graphical%20cv/tg-p/board-id/technology-blog-members)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Frunning-total-cumulative-sum-using-m-time-dimension-in-hana-calculation%2Fba-p%2F13560214%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Calculation View Features of 2025 QRC3](/t5/technology-blog-posts-by-sap/calculation-view-features-of-2025-qrc3/ba-p/14192411)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [🚀 The Universal Journal is Calling: Master the Evolution to S/4HANA Intelligence](/t5/technology-blog-posts-by-members/the-universal-journal-is-calling-master-the-evolution-to-s-4hana/ba-p/14229512)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [Optimizing SAP Analytics Cloud – Best Practices and Performance](/t5/technology-blog-posts-by-sap/optimizing-sap-analytics-cloud-best-practices-and-performance/ba-p/14229397)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [What’s New in SAP HANA Cloud – September 2025](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-hana-cloud-september-2025/ba-p/14228564)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avata...