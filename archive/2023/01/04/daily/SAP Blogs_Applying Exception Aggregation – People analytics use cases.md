---
title: Applying Exception Aggregation – People analytics use cases
url: https://blogs.sap.com/2023/01/03/applying-exception-aggregation-people-analytics-use-cases/
source: SAP Blogs
date: 2023-01-04
fetch_date: 2025-10-04T02:59:28.323260
---

# Applying Exception Aggregation – People analytics use cases

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Applying Exception Aggregation – People analytics ...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5917&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Applying Exception Aggregation – People analytics use cases](/t5/human-capital-management-blog-posts-by-sap/applying-exception-aggregation-people-analytics-use-cases/ba-p/13555380)

![FrankErle](https://avatars.profile.sap.com/f/0/idf0bf4e070daf90f85ad172c43c079990d4b6ad8d5d2105bfe4c87816b8c9ab2e_small.jpeg "FrankErle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[FrankErle](https://community.sap.com/t5/user/viewprofilepage/user-id/17855)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5917)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5917)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555380)

‎2023 Jan 03
6:44 PM

[10
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5917/tab/all-users "Click here to see who gave kudos to this post.")

3,643

* SAP Managed Tags
* [SAP SuccessFactors Workforce Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Workforce%2520Analytics/pd-p/67837800100800006335)

* [SAP SuccessFactors Workforce Analytics

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BWorkforce%2BAnalytics/pd-p/67837800100800006335)

View products (1)

### Summary

A SuccessFactors report designer/admin/author can easily notice the advantage of Story, especially when it comes to aggregating data. It is an enhanced function compared to Canvas or Table report. After a data model is built in Query designer, in Story, summarizing data is easier in Story, for example, headcounts, total compensation, or count of requisitions. Story provides multiple types of calculation and ‘Aggregation’ type conveniently calculates unique counts based on selected aggregation dimensions.
However, there are multiple situation where straight forward aggregation capabilities are not sufficient anymore but so-call "Exception Aggregation" is need. This blog post provides some further insights how to use this particular aggregation type.

### Introduction

There’s an exception aggregation using ‘Aggregation’ calculation type to ensure the calculation with multiple rows of user ID data are accurately aggregated. The use case is when you want to accumulate any measure on a parent object which has a 1:N relationship to children objects. “Exception Aggregation” is so-to-speak the “Measure-counterpart” of the ‘operation’ and “Count Dimension” which is applied for a distinct count of dimensions.

### Use case 1: Total FTE

The use case will become clear with the help of following example: Anchor of the query is job Info – which also has the FTE of the employee. What should be accumulated – and other objects with 1:N cardinality are joined (in the concrete case it’s the “Direct Report JobInfo”). See the example below, simply summing up FTE will not work (i.e. it would give “13” for the 13 records) since 2 of the 6 employees have direct reports (User “Awan” has 4 direct reports and user “Tchin” has 3 direct reports). To consider the FTE of users “Awan” and “Tchin” just once, a trick was applied (=”Exception Aggregation”) by creating 2 calculated story measures as indicated here:

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_1.png)

*Example how to create the two calculated measures to get the correct number of FTE*

Please note that, the same result can be achieved by changing aggregation type of FTE in query. When the data semantic type is ‘Measure’, the default aggregation type is NONE. Change the type to Max/Min to only pick 1 value per user ID.

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_2.png)

After the query is set, create a calculated column (Aggregation) in Story. Below is an aggregation calculation then the result will be same as the first approach.

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_3.png)

### Use case 2: Average days of requisition age

Recruiting data with application data result in multiple rows of data unavoidably due to the relationship between requisition and applications. A requisition has multiple applications (unless no candidate is interested) and this will cause multiple rows per same requisitions. Since the age definition is an age of requisition, the average should be an average per requisition.

To calculate average age per requisition, exception aggregation is required. Otherwise, it will end up summing all ages listed by applications, not by requisitions. This means, to average the data, we need to define the correct data sum and correct count to divide the sum. Since each requisitions have applications data, the sum of age will be an inflated number. Exception aggregation can overcome this.

Step 1: First step is in query designer, set ‘Age’ field to be measure and aggregation type ‘Max’ to ensure it is only picking up one value per requisition:

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_4.png)

Step 2: Save the query and in Story, create a calculated column to sum ages of requisitions. This will only add one age value per requisition:

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_5.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_6.png)

Step 3: Create another calculated column to average the requisition age as below. Notice the measure is not age, but the sum of requisition age ‘Requisition Age Sum’, which is calculated in Step 2.

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_7.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_8.png)

For example, we have 3 requisitions, 2844, 2845, and 2861. Requisition 2844 has 1 application data, 2845 is null, and 2861 has 12 applications. Each requisition has age of 215, 215 and 32 days respectively. Requisition age sum is 462 days, not adding all values which is 814  (= 215 + 215 + 14 x 32) days due to the repetition from application for requisition 2861. And we’re seeing a correct average of requisition which is 462 divided by 3, that is 154 days.

![](/legacyfs/online/storage/blog_attachments/2022/12/Exception_Aggregation_9.png)

Labels

* [Product Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/product%20updates)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fapplying-ex...