---
title: SAP CPQ – Guide to eliminate Common Performance Issues
url: https://blogs.sap.com/2023/03/07/sap-cpq-guide-to-eliminate-common-performance-issues/
source: SAP Blogs
date: 2023-03-08
fetch_date: 2025-10-04T08:54:51.281043
---

# SAP CPQ – Guide to eliminate Common Performance Issues

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAP CPQ - Guide to eliminate Common Performance Is...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7689&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CPQ - Guide to eliminate Common Performance Issues](/t5/financial-management-blog-posts-by-sap/sap-cpq-guide-to-eliminate-common-performance-issues/ba-p/13540890)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7689)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7689)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13540890)

‎2023 Mar 07
9:19 PM

[1
Kudo](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7689/tab/all-users "Click here to see who gave kudos to this post.")

1,937

* SAP Managed Tags
* [SAP CPQ](https://community.sap.com/t5/c-khhcw49343/SAP%2520CPQ/pd-p/73555000100800001601)

* [SAP CPQ

  SAP Billing and Revenue Innovation Management](/t5/c-khhcw49343/SAP%2BCPQ/pd-p/73555000100800001601)

View products (1)

Hi All,

This guide provides comprehensive advice on how to eliminate common performance issues seen in your CPQ applications. It covers everything from understanding the common performance issues and determining the root cause, to implementing the necessary changes to improve performance and prevent future issues.

It also provides overview and some best practices to help you diagnose, troubleshoot, and resolve any performance issues that may arise. Additionally, this blog provides suggestions on how to monitor app performance, identify and address areas of improvement, and establish an efficient performance management system. With this blog, you can be sure to optimize your application performance and ensure a flawless Sales user experience.![](/legacyfs/online/storage/blog_attachments/2022/09/FccX_dtWQAoSBM2.jpg)

## 9 Tips & Tricks to solve Performance Issues

1. **Check system resources and configurations**: Check the system resources (CPU, memory, disk, etc.) to ensure that they are configured correctly and are sufficient for the application.

2. **Monitor for bottlenecks**: Monitor for performance bottlenecks, such as disk bottlenecks, network latency, memory contention, etc., and take corrective action.

3. **Optimize code and queries**: Optimize the code and sql queries to ensure that they are as efficient as possible.

4. **Utilize caching**: Utilize caching to store frequently-accessed data and reduce the load on the database.

5. **Utilize appropriate indexes**: Utilize appropriate indexes to improve sql query performance.

6. **Monitor application logs:** Monitor application logs to identify and resolve issues quickly.

7. **Tune SQL queries:** Tune SQL queries to ensure that they are as efficient as possible.

8. **Debugger** : Utilize a Developer Console: Utilize a console to Trace & identify code that is inefficient and can be optimized.

**9. Scripting :** Learn all the technical ways how to speed up your IronPython code by caching expensive function calls using the cache decorators  **Main Dashboard** for to find Script Performance, System Errors, Storage, Users License.
![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-07_22-03-22.png)Identify Script Performance to check if your scripts are running for long duration to optimize better.
![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-07_22-03-46.png)**Monitor Developer Console** for Tracing, Debugging and Performance tracking
![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-07_22-06-36.png)**Enable Data Deletion ( Auto Clean up )**![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-16_13-08-50.png)

---

## **Areas to look at it for finding the Issues**

* Storage Space
* Audit Trail workspace
* Poor writing IronPython scripts
* Scripts running for a long time
* Check the CTX Tags, which are looping many times.
* Custom table storing a huge data volume
* Incorrect Html/Javascript coding in Responsive templates
* Check Logs with frequent errors

![](/legacyfs/online/storage/blog_attachments/2022/10/FODGXacXMAEnTb0.jpg)

**API Response**

* Get the size of requests and responses (If you are working on API requests to get the data from applications).

* Never pull huge volume of data from your custom API, recommend to have pagination concept.

**Custom Table**

* Count the number of records into the database (you do not need to verify into all the tables, verify only the tables related to the service with the problem).
* Check if the table has indexed
* How long time take your service to finish when there are several users is accessible.

  [Tips for Speeding up Ironpython code](https://www.kdnuggets.com/how-to-speed-up-python-code-with-caching)

---

At this point, you should have all the enough information about what is happening, how it is happening, and where is it happening. Now, you have a general vision and you are ready to start to think about how to solve the problem in your application after reading this blog ![:slightly_smiling_face:](/html/@5D2D4274E851E17FD6B6AA8F470AA6B3/emoticons/1f642.png ":slightly_smiling_face:")

Labels

* [Technology Updates](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ffinancial-management-blog-posts-by-sap%2Fsap-cpq-guide-to-eliminate-common-performance-issues%2Fba-p%2F13540890%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC Tuesdays: Preventing Potential Fraud and Data Irregularities Across Ultra-High-Volume Operations](/t5/financial-management-blog-posts-by-sap/grc-tuesdays-preventing-potential-fraud-and-data-irregularities-across/ba-p/14205601)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  2 weeks ago
* [SAP PaPM Cloud Standard Model Data Import to SAP Analytics Cloud using RFA JS](/t5/financial-management-blog-posts-by-sap/sap-papm-cloud-standard-model-data-import-to-sap-analytics-cloud-using-rfa/ba-p/14222384)
  in [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)  2 weeks ago
* [Balance Validation accelerating the period closing by...