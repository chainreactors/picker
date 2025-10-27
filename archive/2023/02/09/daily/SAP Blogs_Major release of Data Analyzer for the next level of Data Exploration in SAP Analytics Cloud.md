---
title: Major release of Data Analyzer for the next level of Data Exploration in SAP Analytics Cloud
url: https://blogs.sap.com/2023/02/08/major-release-of-data-analyzer-for-the-next-level-of-data-exploration-in-sap-analytics-cloud/
source: SAP Blogs
date: 2023-02-09
fetch_date: 2025-10-04T06:07:15.906167
---

# Major release of Data Analyzer for the next level of Data Exploration in SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Major release of Data Analyzer for the next level ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162917&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Major release of Data Analyzer for the next level of Data Exploration in SAP Analytics Cloud](/t5/technology-blog-posts-by-sap/major-release-of-data-analyzer-for-the-next-level-of-data-exploration-in/ba-p/13565385)

![bettina_denonville](https://avatars.profile.sap.com/7/0/id7058a9dcbbae1d302c037d94a04add723cecc4bf05ad636a22ba798510dc1dac_small.jpeg "bettina_denonville")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[bettina\_denonville](https://community.sap.com/t5/user/viewprofilepage/user-id/840379)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162917)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162917)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565385)

‎2023 Feb 08
7:52 PM

[40
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162917/tab/all-users "Click here to see who gave kudos to this post.")

10,938

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

**It has been quiet around Data Analyzer in the past months. This is due to the major release in QRC Q1 2023 with significant updates. In this blog we show you all upcoming improvements, just enjoy and find out the big step we made on the road to first class data exploration!**

We continue to execute towards our vision of one **standalone** exploration experience for **ad hoc analysis**. In SAP Analytics Cloud we provide different experiences for different use cases and personas. The “Analyze” capabilities play a central role since they are used either as a powerful standalone analysis tool or tightly coupled within the use cases of our other capabilities.

![](/legacyfs/online/storage/blog_attachments/2023/02/ask_analyze_build.png)

With the QRC Q1 2023 release we will ship a big set of enhanced functionalities, an improved user experience and an optimized architecture focused on performance.

Taking Data Analyzer to the next level would not have been possible without the tremendous input we got from you – our customers and partners. Many of these enhancements were driven by requests coming from you via our influence portal.

But now let’s dive into the new features for Q1 2023.

## Improved Table

We have introduced “**Lazy Loading**” on the Data Analyzer table. While showing up to 50 columns, we have removed the row limit. The number of visible rows is estimated on the screen size and when scrolling, a new backend request is issued to retrieve new data. This improves the perceived performance and enables smooth scrolling through large datasets.

Dimensions and Measures can now be rearranged using **Drag and Drop** within the table directly.

![](/legacyfs/online/storage/blog_attachments/2023/02/lazy_drill.gif)

With the **Adaptive Table Layout,** we have adjusted the automatic sizing of the table to fit the number of columns.

![](/legacyfs/online/storage/blog_attachments/2023/02/table_size.png)

By showing **ID and Description** in two separate columns, passing the **default line break** from BW queries and the **extended display options for the ID** (non-compounded key display, etc.) we improve the usage of BW based data sources.

![](/legacyfs/online/storage/blog_attachments/2023/02/compound.png)

The **position of totals** and **parent nodes for hierarchies** can now be arranged independently.

![](/legacyfs/online/storage/blog_attachments/2023/02/Totals_nodes.png)

We support additional drill level capabilities for Universal Display Hierarchies and **Compact Display**. You can now use the Expand to Dimension option on hierarchy header and on each hierarchy node level.

![](/legacyfs/online/storage/blog_attachments/2023/02/expand.png)

## Improved Filter

For the Filters we are now using one central place for all filters, the well-known **Filter Bar**, giving the same experience as within stories. There are no widget filters anymore and all selected filters, no matter if in the context menu of the table or the member selector, are placed and displayed in this central place. Additionally, the default filters of a BW query are shown here.

![](/legacyfs/online/storage/blog_attachments/2023/02/filterbar.png)

With the new **Dimension Member Dialog,** you can display and search by attributes, select all member with one click and copy paste filter values! This harmonizes the member selector of the filter and the variable prompt.

![](/legacyfs/online/storage/blog_attachments/2023/02/member.png)

## Enhanced Context Menu

In our enhanced context menu, you now can directly **Filter by a certain Member** irrespective of the drilled position in the table or open the member selector dialog for this Dimension. This also works out of the box for members of a second structure in a BW query.

![](/legacyfs/online/storage/blog_attachments/2023/02/filter.gif)

Data Analyzer now **Freezes Headers** by default. If you want to change it, you can use the context menu to do so.

![](/legacyfs/online/storage/blog_attachments/2023/02/freeze.png)

The context menu on **Display Attributes** now allows to change the options for showing ID and Description.

![](/legacyfs/online/storage/blog_attachments/2023/02/display-2.png)

## Improved Builder Panel

We revamped the **Builder Panel**. You can now easily add and remove **display attributes** to the table as they are now listed in the available object list. You can arrange these attributes also by drag and drop directly.

![](/legacyfs/online/storage/blog_attachments/2023/02/builder.gif)

Welcome BW **2-structure queries** to Data Analyzer! Our improved workflow allows adding and removing members of the second structure to the table as well as reordering by drag and drop. All directly in the Builder Panel. By the way – this was one of the most requested features for our old story explorer experience. Check.

![](/legacyfs/online/storage/blog_attachments/2023/02/2structure.png)

But we did not forget HANA Live - **Order your measures** of a HANA view by drag and drop is now supported with the new Builder Panel in Data Analyzer.

## Story Integration

As I have mentioned in the beginning of this blog – tight integration of our Analysis capabilities is important and gives the end user the ability to look behind the curtain and understand the data behind the charts. As Data Analyzer will **replace the Story Explorer** for the Optimized Story Experience, we are integrating it tightly into our story workflows. Providing the ability to **jump to** the Data Analyzer from a table widget by concurrently passing the existing table state (such as filters, variables, and current drill-down actions) is a big step towards ...