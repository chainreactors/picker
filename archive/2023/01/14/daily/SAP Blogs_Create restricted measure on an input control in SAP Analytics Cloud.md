---
title: Create restricted measure on an input control in SAP Analytics Cloud
url: https://blogs.sap.com/2023/01/13/create-restricted-measure-on-an-input-control-in-sap-analytics-cloud/
source: SAP Blogs
date: 2023-01-14
fetch_date: 2025-10-04T03:52:46.640959
---

# Create restricted measure on an input control in SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Create restricted measure on an input control in S...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163100&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create restricted measure on an input control in SAP Analytics Cloud](/t5/technology-blog-posts-by-sap/create-restricted-measure-on-an-input-control-in-sap-analytics-cloud/ba-p/13566048)

![aneetta123](https://avatars.profile.sap.com/5/0/id5022d5f73b379b5f12014d5810ebd2994bde793eb7d09e58bafb556fabf3b08b_small.jpeg "aneetta123")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[aneetta123](https://community.sap.com/t5/user/viewprofilepage/user-id/44572)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163100)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163100)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566048)

‎2023 Jan 13
8:06 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163100/tab/all-users "Click here to see who gave kudos to this post.")

4,978

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

Overview:

In this blog, I will try to explain one of the use-cases in Sap Analytics Cloud.

 'How to create a restricted measure on a measure input control'.

First, let us try to understand the business scenario to be achieved.

Business Scenario:

The user has a requirement to create a trend chart to show current year sales data.

The chart should show Sales count trend and Sales Amount trend for the current year based on the selection of a measure input control

You can go through [SAP Analytic Cloud: Measure and Dimension Input Control](https://blogs.sap.com/2020/06/04/sap-analytic-cloud-measure-and-dimension-input-control/) to understand more about input controls in SAP Analytics Cloud

Solution:

To achieve the above mentioned business scenario we require the combination of two features in sap analytics cloud: Restricted measures and Cross calculation. The restricted measure would be used to restrict the Sales count and Sales Amount to current year data and the cross calculation would allow us to apply the restriction to both the measure (Sales count and Sales Amount).

Create a story, add a chart and follow the below steps to achieve the same

* Make the inserted chart a line trend chart![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-10-at-10.07.43-AM.png)

* Create a measure input control with the measures required for the dynamic selection

![](/legacyfs/online/storage/blog_attachments/2023/01/1-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/2-7.png)

           Rename the Measure input control created to 'Display As'.

* Add the input control created to the measure field of the trend chart

* Add a cross calculation to the chart
  ![](/legacyfs/online/storage/blog_attachments/2023/01/3-4.png)

Create a Cross Calculation restricted measure to restrict the data to current year sales.

In the selection context , select 'Measure Values' under Measure.

![](/legacyfs/online/storage/blog_attachments/2023/01/4-4.png)

The selection of measure values will enable the restricted measure to be controlled by the measure input control added in the chart and thereby achieving our requirement

* Further, add the dimension by which the data needs to be displayed(eg: quarter, month)

In the below screenshots you can see that the heading and the values on the trend chart changes based on the selection in the input control.

![](/legacyfs/online/storage/blog_attachments/2023/01/5-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/6-3.png)

To summarise, the above blog post will help to understand how to restrict the measures in an input control using cross calculation. This solution can be applied on other charts as well depending on the requirement.

I hope this blog will be useful for those who come across a similar scenario.

Thank you for taking time to go through the blog. Hope its been helpful. Please leave your valuable comments/likes/ratings below.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [cross calculation sac](/t5/tag/cross%20calculation%20sac/tg-p/board-id/technology-blog-sap)
* [restricted measure](/t5/tag/restricted%20measure/tg-p/board-id/technology-blog-sap)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fcreate-restricted-measure-on-an-input-control-in-sap-analytics-cloud%2Fba-p%2F13566048%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  8 hours ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  8 hours ago
* [What's New in SAP Analytics Cloud Modeling Extensions & Integration QRC4 2025 Release](/t5/technology-blog-posts-by-sap/what-s-new-in-sap-analytics-cloud-modeling-extensions-amp-integration-qrc4/ba-p/14208685)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Handling YTD and Previous Month Selection in SAC](/t5/technology-q-a/handling-ytd-and-previous-month-selection-in-sac/qaq-p/14231551)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-log...