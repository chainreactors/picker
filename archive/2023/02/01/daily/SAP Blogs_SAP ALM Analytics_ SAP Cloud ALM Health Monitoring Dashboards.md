---
title: SAP ALM Analytics: SAP Cloud ALM Health Monitoring Dashboards
url: https://blogs.sap.com/2023/01/31/sap-alm-analytics-sap-cloud-alm-health-monitoring-dashboards/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:19:51.852900
---

# SAP ALM Analytics: SAP Cloud ALM Health Monitoring Dashboards

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP ALM Analytics: SAP Cloud ALM Health Monitoring...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157560&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP ALM Analytics: SAP Cloud ALM Health Monitoring Dashboards](/t5/technology-blog-posts-by-sap/sap-alm-analytics-sap-cloud-alm-health-monitoring-dashboards/ba-p/13549729)

![Xavier](https://avatars.profile.sap.com/1/d/id1d30004849474879083050b873da5cdcebb5cc9543001f3dbdc54d08c8d12d41_small.jpeg "Xavier")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Xavier](https://community.sap.com/t5/user/viewprofilepage/user-id/4449)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157560)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157560)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549729)

‎2023 Jan 31
5:59 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157560/tab/all-users "Click here to see who gave kudos to this post.")

4,870

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

## Goal of this blog post

In this blog, we will create a simple **panel** displaying analytics for **Health Monitoring** data managed by SAP Cloud ALM with the [ALM Grafana plugin](https://github.com/SAP/alm-plug-in-for-grafana).

This plug-in lets you extend your analytics solutions for application life-cycle management. This plugin is based on the **SAP ALM analytics API**. The main concepts of the SAP ALM Analytics API can be found in this [blog](https://blogs.sap.com/2022/10/05/sap-alm-analytics-api/).

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-3-5.png)

##

## **Pre-requisites**

* You have created a service key to your SAP Cloud ALM tenants (check this [blog](https://blogs.sap.com/2021/08/12/sap-cloud-alm-extend-with-api-get-started-with-sap-cloud-alm-api/)).

* You should configure a Grafana data source connected to your SAP Cloud ALM tenant.

* You have configured at least one project in your SAP Cloud ALM tenant. (check the [SAP support portal](https://support.sap.com/en/alm/sap-cloud-alm/implementation.html))

## **ALM Health Monitoring Data Provider**

The SAP Cloud ALM Health Monitoring data provider supports the following dimension:

|
 **Dimensions** |
 **Description** |
 **Filter** |

|
 **serviceType** |
 Service type |
 yes |

|
 **serviceId** |
 Service id |
 yes |

|
 **serviceName** |
 Service name |
  |

|
 **metricId** |
 Metric Id |
 yes |

|
 **metricName** |
 Metric Name |
  |

|
 **metricLabel** |
 Metric Label |
 yes |

|
 **value** |
 value of the metric |
  |

|
 **limit** |
 Maximum value for the metric (**Measures**) |
  |

|
 **usage** |
 Used capacity from limit in % (**Measures**) |
  |

|
 **okStatus** |
 % of ok status (**Measures**) |
  |

|
 **warningStatus** |
 % of warning status (**Measures**) |
  |

|
 **criticalStatus** |
 % of critical status (**Measures**) |
  |

## **Query**

From your Grafana instance, create a query for each service type to be displayed in your dashboard:

* Add a Panel

* Select your SAP Cloud ALM “Data source”.

* Select the “*Time Series*” format.

* Select the data provider: “***ALM** **Health** **Monitoring***”

* Select your service type: (ex: "*SAP S/4 HANA Cloud*")

* Select the following dimensions:

  + ***ServiceName***

  + ***ServiceId***

  + ***ServiceType***

* Select the following metrics

  + ***okStatus***

## Visualisation

Select the "*Status History*" visualisation with the following settings:

* **Query** **transformation**: Select the "*Rename by RegExp*" transformation to extract the service name from the query legend as showed below:

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-1-6.png)

## Result

The result will show a table displaying the overall percentage of successful metrics per services.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-2-5.png)

## **Query**

From your Grafana instance, create a query for each service name to be displayed in your dashboard:

* Add a Panel

* Select your SAP Cloud ALM “Data source”.

* Select the “*Time Series*” format.

* Select the data provider: “***ALM** **Health** **Monitoring***”

* Select your service in the filters.

* Select the following dimensions:

  + *ServiceName*

  + *ServiceId*

  + *ServiceType*

  + **MetricName**

* Select the following metrics

  + ***okStatus***

## Visualisation

Select the "*Status History*" visualisation.

## Result

The result will show a table displaying the overall percentage of successful status for each metrics of the selected service.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-4-4.png)

In the next blog, we will create dashboards for [Real User](https://blogs.sap.com/2023/02/27/sap-alm-analytics-sap-cloud-alm-real-user-monitoring-dashboards/) Monitoring use-cases.

Thanks for reading.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-alm-analytics-sap-cloud-alm-health-monitoring-dashboards%2Fba-p%2F13549729%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  9 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Full-Page Fit vs. Scrollable Dashboards in SAC which one is better?](/t5/technology-blog-posts-by-members/full-page-fit-vs-scrollable-dashboards-in-sac-which-one-is-better/ba-p/14187381)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Choosing the Right SAP Analytics Tool: Features, Benefits, and Strategy](/t5/technology-blog-posts-by-sap/choosing-the-right-sap-analytics-tool-features-benefits-and-strategy/ba-p/14230016)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember...