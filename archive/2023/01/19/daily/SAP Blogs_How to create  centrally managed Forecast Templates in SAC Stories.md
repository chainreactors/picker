---
title: How to create  centrally managed Forecast Templates in SAC Stories
url: https://blogs.sap.com/2023/01/18/how-to-create-centrally-managed-forecast-templates-in-sac-stories/
source: SAP Blogs
date: 2023-01-19
fetch_date: 2025-10-04T04:16:47.933957
---

# How to create  centrally managed Forecast Templates in SAC Stories

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to create centrally managed Forecast Template...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163472&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to create centrally managed Forecast Templates in SAC Stories](/t5/technology-blog-posts-by-members/how-to-create-centrally-managed-forecast-templates-in-sac-stories/ba-p/13570092)

![N1kh1l](https://avatars.profile.sap.com/7/d/id7d44752df87eb970a04cfb3208c829f693c4d329f6a76523b37770e363773b06_small.jpeg "N1kh1l")

[N1kh1l](https://community.sap.com/t5/user/viewprofilepage/user-id/124370)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163472)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163472)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570092)

‎2023 Jan 18
8:47 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163472/tab/all-users "Click here to see who gave kudos to this post.")

7,675

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)

View products (2)

In this blog post we will learn how to create  centrally managed/maintained dynamic Forecast Layout templates to support planning and analysis process in SAC stories.

**Business Scenario:**

Financial forecasting is a crucial aspect of any business or financial planning. It involves predicting future financial performance based on past performance and current trends. By creating accurate financial forecasts, businesses and individuals can make informed decisions about future investments, expenses, and revenue streams.

A rolling forecast is a financial forecasting method that involves regularly updating a forecast as new data (Actuals) becomes available. This type of forecasting is particularly useful for businesses that operate in rapidly changing environments.

Forecast can have varied granularity like Monthly/Quarterly/Annual etc. and they allow businesses to continuously update their financial forecasts and adjust their plans accordingly, in order to stay on track and meet their goals.

A sample Forecast layout looks like below.

![](/legacyfs/online/storage/blog_attachments/2023/01/Sample-Forecast-1.jpg)

**Forecast Layout in SAC Stories:**

If you are using a planning Model, SAC offers a forecast layout to be chosen in table widget in stories. In the builder panel one can select the forecast layout option as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/01/SAC-Table-Forecast.png)

The builder panel offers a host of option to customize the layout as per the needs.

![](/legacyfs/online/storage/blog_attachments/2023/01/Forecast-Configuration.png)

|
 Layout fields |
 Information |

|
 Look back on |
 Select the version to use for looking back. |

|
 Look ahead on |
 Select the version for forecasting or looking ahead. |

|
 Cut-over date |
 Options for cut-over date:    * Today: The current date; this is the default choice.  * Specific Date: In Select member for <Time>, select the date.   You can also set a dynamic time filter.  * Last Booked (Actuals): This means the latest date of data entered for the Actuals version. |

Timeframe: options include the following:

|
 Type: Forecast |
 Granularity:    * Quarter  * Month |

|
 Look back additional: number of intervals |
 * Year  * Quarter  * Month |

|
 Look ahead additional: number of intervals |
 * Year  * Quarter  * Month |

**Derive the Forecast version and the cutoff dates from attributes of version and thus creating  centrally managed Forecast Templates**

Above section highlights the options to choose the Forecast version and cutoff dates for Actual. But sometimes business needs require us to maintain the Forecast versions and cutoff dates centrally especially if we have more than one Forecast layout and do not want to update all the stories due to change in forecast cycle.

In below steps I will show you how we can achieve a dynamic Forecast template using some attributes in Version dimension and use of FIND() formula.

In SAC All the three layout configuration option namely **Look Back on**, **Look Ahead on** and **Cutover date** offer to select the **Calculation Input Control** option. This option allows us to add the dynamic character to all these 3 variables.

In below example I will use the Calculation Input Control option to derive my Forecast Version (Look Ahead on ) and the cutoff Date by reading the attributes of my version dimension.

The version Dimension will be configured as below. We add two attributes Forecast\_Version and Cutoff\_Date to our version dimension.

![](/legacyfs/online/storage/blog_attachments/2023/01/Version-Config.png)

Now that our Version attributes are done we create our Forecast layout in SAC stories.

I will select the SAC table widget and choose the Forecast Layout option. On the Forecast layout configuration I select **Calculation Input Control** for both Look back on and Cutoff Dates. The granularity for Forecast has been set to Months.

In both the calculation input control option we choose the formula option to determine the variables.

![](/legacyfs/online/storage/blog_attachments/2023/01/calc-input-control.png)

Formula to derive the version as below.

![](/legacyfs/online/storage/blog_attachments/2023/01/ForecastVersion.png)

```
FIND('X', [d/Version].[p/Forecast_Version], [d/Version].[p/ID])
```

Formula to derive the cutoff dates for Actuals

![](/legacyfs/online/storage/blog_attachments/2023/01/CutoffDates.png)

```
FIND([@ForecastVersion],[d/Version].[p/ID],[d/Version].[p/Cutoff_Date])
```

**Output:**

Now that we are done with the configuration steps, lets see the template in Action.

With Cutoff Date set as 202203 (March 2022) in Version dimension and Forecast marked as X for selected version.

![](/legacyfs/online/storage/blog_attachments/2023/01/cutoff1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Forecast1.png)

With Cutoff Date set as 202206 (June 2022) in Version dimension

![](/legacyfs/online/storage/blog_attachments/2023/01/cutoff2.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Forecast2.png)

**Points to Note:**

* Use of Calculation Input Control is currently not supported in Optimized Design mode for the stories.

* The above steps can be extended to also derive more than one Forecast version with different cutoff dates. (Exciting possibilities)

**Summary:**

The above steps outlines the process to create centrally managed dynamic Forecast layouts to be used in the planning...