---
title: SAP ALM Analytics: SAP Cloud ALM Requirements Dashboards
url: https://blogs.sap.com/2023/01/16/sap-alm-analytics-sap-cloud-alm-requirements-dashboards/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:36.942703
---

# SAP ALM Analytics: SAP Cloud ALM Requirements Dashboards

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP ALM Analytics: SAP Cloud ALM Requirements Dash...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155822&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP ALM Analytics: SAP Cloud ALM Requirements Dashboards](/t5/technology-blog-posts-by-sap/sap-alm-analytics-sap-cloud-alm-requirements-dashboards/ba-p/13544387)

![Xavier](https://avatars.profile.sap.com/1/d/id1d30004849474879083050b873da5cdcebb5cc9543001f3dbdc54d08c8d12d41_small.jpeg "Xavier")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Xavier](https://community.sap.com/t5/user/viewprofilepage/user-id/4449)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155822)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155822)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544387)

‎2023 Jan 16
3:26 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155822/tab/all-users "Click here to see who gave kudos to this post.")

1,030

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

## Goal of this blog post

In this blog, we will create a simple **panel** displaying analytics for **Requirements** entities managed by SAP Cloud ALM with the [ALM Grafana plugin](https://github.com/SAP/alm-plug-in-for-grafana).

## **Pre-requisites**

* You have created a service key to your SAP Cloud ALM tenants (check this [blog](https://blogs.sap.com/2021/08/12/sap-cloud-alm-extend-with-api-get-started-with-sap-cloud-alm-api/)).

* You should configure a Grafana data source connected to your SAP Cloud ALM tenant.

* You have configured at least one project in your SAP Cloud ALM tenant. (check the [SAP support portal](https://support.sap.com/en/alm/sap-cloud-alm/implementation.html))

## **ALM Requirements Data Provider**

The SAP Cloud ALM Requirements data provider supports the following dimension:

|
 **Dimensions** |
 **Description** |
 **Filter** |

|
 name |
 Requirement Name |
  |

|
 GUID |
 Internal GUID of the requirement |
 yes |

|
 project |
 project of the requirement |
 yes |

|
 project name |
 Project Name |
  |

|
 scope |
 scope ID |
 yes |

|
 scope name |
 Scope of the requirement |
  |

|
 status |
 Requirement Status |
 yes |

|
 statusText |
 Text of the requirement status |
  |

|
 assignee |
 Assigned owner of the requirement |
 yes |

|
 priority |
 Priority of the requirement |
 yes |

|
 team |
 Team assigned to the requirement |
 yes |

|
 workstream |
 Work-stream attached to the requirement |
  |

|
 Role |
 Role of the Requirement |
 yes |

|
 Process |
 Solution process of the requirement |
  |

|
 counter |
 Requirement counter (**Measures**) |
  |

## **Query**

From your Grafana instance, create a query for each project to be displayed in your dashboard:

* Add a Panel

* Select your SAP Cloud ALM “*Data source*”.

* Select the “*Time Series*” format.

* Select the data provider: “*ALM Requirements*”

* Select the name of your project.

* Select the following dimensions:

  + scopeName

  + scope

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-1-9.png)

## Visualisation

Select the "Pie Chart" visualisation with the following settings:

* **Query** **transformation**: Select the "*Rename by regex*" transformation to remove the measure name of the time-series legend. (Note: As two dimensions were selected by the query, the name of the series correspond the combination the two dimensions).

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-2-8.png)

* **Query Options**:

  + Select “**now/d**” as relative time option in the “Query Options” panel to retrieve data of the "Today as of now" time period.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-3-11.png)

##

##

## Result

The result will show a pie-chart showing the scope distribution of requirements per scope for a given project.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture-4-5.png)

In the next blog, we will create a panel displaying [Test Executions](https://blogs.sap.com/2023/01/16/sap-alm-analytics-sap-cloud-alm-test-executions-dashboards/) analytics.

Thanks for reading.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-alm-analytics-sap-cloud-alm-requirements-dashboards%2Fba-p%2F13544387%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  8 hours ago
* [Top Reasons to Modernize with SAP HANA Cloud – Blog #5 in the Series](/t5/technology-blog-posts-by-sap/top-reasons-to-modernize-with-sap-hana-cloud-blog-5-in-the-series/ba-p/14206266)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Unlocking SAP Fiori and other business content on Mobile: A Practical Guide](/t5/technology-blog-posts-by-sap/unlocking-sap-fiori-and-other-business-content-on-mobile-a-practical-guide/ba-p/14230532)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Artificial Intelligence and SAP Master Data Governance](/t5/technology-blog-posts-by-sap/artificial-intelligence-and-sap-master-data-governance/ba-p/14152960)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Pr...