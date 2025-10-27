---
title: SAP ALM Analytics: SAP Cloud ALM Test Executions Dashboards
url: https://blogs.sap.com/2023/01/16/sap-alm-analytics-sap-cloud-alm-test-executions-dashboards/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:34.762971
---

# SAP ALM Analytics: SAP Cloud ALM Test Executions Dashboards

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP ALM Analytics: SAP Cloud ALM Test Executions D...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155821&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP ALM Analytics: SAP Cloud ALM Test Executions Dashboards](/t5/technology-blog-posts-by-sap/sap-alm-analytics-sap-cloud-alm-test-executions-dashboards/ba-p/13544368)

![Xavier](https://avatars.profile.sap.com/1/d/id1d30004849474879083050b873da5cdcebb5cc9543001f3dbdc54d08c8d12d41_small.jpeg "Xavier")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Xavier](https://community.sap.com/t5/user/viewprofilepage/user-id/4449)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155821)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155821)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544368)

‎2023 Jan 16
3:33 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155821/tab/all-users "Click here to see who gave kudos to this post.")

960

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

## Goal of this blog post

In this blog, we will create a simple **panel** displaying analytics for **Test Executions** entities managed by SAP Cloud ALM with the [SAP ALM Grafana plugin](https://github.com/SAP/alm-plug-in-for-grafana).

This plug-in lets you extend your analytics solutions for application life-cycle management. This plugin is based on the **SAP ALM analytics API**. The main concepts of the SAP ALM Analytics API can be found in this [blog](https://blogs.sap.com/2022/10/05/sap-alm-analytics-api/).

## **Pre-requisites**

* You have created a service key to your SAP Cloud ALM tenants (check this [blog](https://blogs.sap.com/2021/08/12/sap-cloud-alm-extend-with-api-get-started-with-sap-cloud-alm-api/)).

* You should configure a Grafana data source connected to your SAP Cloud ALM tenant.

* You have configured at least one project in your SAP Cloud ALM tenant. (check the [SAP support portal](https://support.sap.com/en/alm/sap-cloud-alm/implementation.html))

## **ALM Tests Execution Data Provider**

The ALM Tests Execution data provider supports the following dimension:

|
 **Dimensions** |
 **Description** |
 **Filter** |

|
 project |
 project of the test execution |
 yes |

|
 projectName |
 Project Name |
  |

|
 scope |
 scope ID |
 yes |

|
 scopeName |
 Scope of the test execution |
  |

|
 status |
 test execution Status |
 yes |

|
 type |
 type of the test |
 yes |

|
 testcaseID |
 ID of the test case |
 yes |

|
 testcaseName |
 Name of the test case |
  |

|
 total |
 counter (**Measures**) |
  |

## **Query**

From your Grafana instance, create a query for each project to be displayed in your dashboard:

* Add a Panel

* Select your SAP Cloud ALM “Data source”.

* Select the “*Table*” format.

* Select the data provider: “*ALM Test Executions*”

* Select the name of your project.

* Select the name of your project scope

* Select the following dimensions:

  + status

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-1-10.png)

## Visualisation

Select the "Pie Chart" visualisation with the following settings:

* **Query** **transformation**: Select the "Rename by regex" transformation to remove the measure name of the time-series legend.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-2-10.png)

* **Query Options**:

  + Select “**6M**” as relative time option in the “Query Options” panel.

## Result

The result will show a time series chart displaying the progress over weeks for test executions status for a given project, scope combination managed in your SAP Cloud ALM instance.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-2-9.png)

In the next blog, we will create a panel displaying [Health Monitoring](https://blogs.sap.com/2023/01/31/sap-alm-analytics-sap-cloud-alm-health-monitoring-dashboards/) analytics.

Thanks for reading.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-alm-analytics-sap-cloud-alm-test-executions-dashboards%2Fba-p%2F13544368%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Full-Page Fit vs. Scrollable Dashboards in SAC which one is better?](/t5/technology-blog-posts-by-members/full-page-fit-vs-scrollable-dashboards-in-sac-which-one-is-better/ba-p/14187381)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Choosing the Right SAP Analytics Tool: Features, Benefits, and Strategy](/t5/technology-blog-posts-by-sap/choosing-the-right-sap-analytics-tool-features-benefits-and-strategy/ba-p/14230016)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [🚀 The Universal Journal is Calling: Master the Evolution to S/4HANA Intelligence](/t5/technology-blog-posts-by-members/the-universal-journal-is-calling-master-the-evolution-to-s-4hana/ba-p/14229512)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") jeet\_kapase](/t5/user/viewprofilepage/user-id/16635...