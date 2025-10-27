---
title: Optimizing Stories Performance and Fixing common errors – People Analytics Report Stories – Master Blog
url: https://blogs.sap.com/2022/12/11/optimizing-stories-performance-and-fixing-common-errors-people-analytics-report-stories-master-blog/
source: SAP Blogs
date: 2022-12-12
fetch_date: 2025-10-04T01:14:56.847046
---

# Optimizing Stories Performance and Fixing common errors – People Analytics Report Stories – Master Blog

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Optimizing Stories Performance and Fixing common e...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5684&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Optimizing Stories Performance and Fixing common errors - People Analytics Report Stories - Master Blog](/t5/human-capital-management-blog-posts-by-sap/optimizing-stories-performance-and-fixing-common-errors-people-analytics/ba-p/13548659)

![uditchandna](https://avatars.profile.sap.com/c/7/idc73c6adeb42eaec010a2290a456b59b3d79daff35fecd1feb9946ae0e0a61609_small.jpeg "uditchandna")

[uditchandna](https://community.sap.com/t5/user/viewprofilepage/user-id/26170)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5684)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5684)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548659)

‎2022 Dec 11
7:13 PM

[6
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5684/tab/all-users "Click here to see who gave kudos to this post.")

3,808

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)

View products (2)

With this guide, we wish to address how Report Designers can review their stories created in SuccessFactors People Analytics Report Stories to address Performance Issues that they may have faced. While we cover a good amount of ways to prevent Performance issues by providing design time guidelines in IDP but it is also important to review our stories from a diagnostic lens on what factors could have caused Performance issues

The following Master Blog would provide a diagnostic framework and an ongoing collection of individual blogs optimizing various areas of Report Stories for necessary Performance improvement. At the same time, we would also use the same to address some of the use cases which may be ideally suited for other People's Analytics tools and not just Report Stories

We would keep updating the content as and when we publish newer content on the same. Do check out the Master Blog for all the updated content

Please refer to the following guidance framework for debugging and optimizing Performance as necessary based on issues that are like the symptoms and have underlying causes that need to be reviewed

**New Blogs in the series - Released on 12 Dec 2022**

* [Apply Selection for Filters](https://blogs.sap.com/2022/12/09/apply-selection-for-filters-stories-in-people-analytics/)

* [How to import the HAR file](https://blogs.sap.com/2022/12/12/how-to-import-har-file/)

* [Configuring Custom MDF objects for reportability using Story Reports](https://blogs.sap.com/2022/12/12/configuring-custom-mdf-objects-for-reportability-using-story-reports./)

**New Blogs in the series - Released on 4 Jan 2023**

* [Export Widget data set in Excel](https://blogs.sap.com/2023/01/04/extract-complete-data-set-in-excel/)

|
 **Issues/Symptoms** |
 **Causes to Review** |
 **Details** |

|
 General Story Slowness |
 Too many widgets in the story |
 The IDP defines the ideal weight-based approach (tested by SAC) to the number of widgets one should have in the story to avoid. Refer to the IDP or [SAC Best Practice Document](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/fbe339efda1241b5a3f46cf17f54cdff.html) defining the weight-based approach for the number of widgets |

|
  |
 Bloated Data Model |
 The data model defined in the query designer should not be bloated or have an unnecessary number of widgets. The report designer should add only columns and object schemas on the need basis and functional design of the story report |

|
  |
 Too Many Data Sources |
 Some report designers try to bypass the suggested 120-column limit in the data source by introducing multiple data sources and linking them which in turn can lead to further performance deterioration |

|
  |
 Too Much Data Blending |
 While there are scenarios that require data blending, some report designers try to put so much information into a single page leading to unnecessary data blending which can cause problems |

|
  |
 Nesting too many Calculated Columns |
 Nesting calculated columns can lead to performance issues as building calculated columns over other calculated columns mean sequential processing leading to a longer time to render. In some scenarios wherever feasible, it is better to build calculated columns directly over source columns rather than building intermediate calculated columns |

|
  |
 Too many Self Joins |
 Some reports require multiple joins to the same object in the query designer. Some report designers use this as a mechanism as a prerequisite to show the transposition of values at the widget in the story  (row level value now being column headers).    This can be achieved by using the cross tab at the story level and still having single schema objects at the query designer layer    We will be adding a detailed blog on the same |

|
  |
 Wrong Use Case- Data Dump and SQL Analytics |
 Some use cases like dumping data to excel or complex window function-based SQL Aggregates are best suited for Workforce Analytics or other SAP tools like SAC Planning. Consult with your CSM and Partner on the same    For the partial export use case of Table Widget data export (for limited data volume), you can refer to the following [blog](https://blogs.sap.com/2023/01/04/extract-complete-data-set-in-excel/) here. [Note: Report Stories is not a Data Extraction Tool]    Alternatively, there is also a scheduling facility for similar export use cases. More details to follow |

|
 Slowness in working with filters |
 Improper Use of Filters |
 There are multiple scenarios with improper use of filters that can cause issues. A few of them to review are as below. We will define some of them below    1) Not using scope filters for providing matrix level filters i.e manager level/ HR level data access    2) Not using schema object level filters before joining 2 schema objects. This is critical to avoid data explosion at the time of data fetched for the query    3) Not using filters on story widgets    4) Using the same filters at multiple places    5) Not using bookmarks features where one needs to work a group of filters with specific values and store those as bookmarks    We will add other blogs on the Filter usage soon |

|
  |
 [Apply Selection for Filters](https://blogs.sap.com/2022/12/09/apply-selection-for-filters-stories-in-people-analytics/) |
 Not using the “A...