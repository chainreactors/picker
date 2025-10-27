---
title: Display Snapshot Monitor Data
url: https://blogs.sap.com/2023/05/11/display-snapshot-monitor-data/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:35.167129
---

# Display Snapshot Monitor Data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Display Snapshot Monitor Data

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158823&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Display Snapshot Monitor Data](/t5/technology-blog-posts-by-sap/display-snapshot-monitor-data/ba-p/13552925)

![christoph_weyd](https://avatars.profile.sap.com/9/a/id9a8d85d0f6eabecf6049618aad50983895674416bb9dd6c84dfa652ef720eb68_small.jpeg "christoph_weyd")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[christoph\_weyd](https://community.sap.com/t5/user/viewprofilepage/user-id/258399)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158823)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158823)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552925)

‎2023 May 11
7:25 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158823/tab/all-users "Click here to see who gave kudos to this post.")

11,736

* SAP Managed Tags
* [SAP NetWeaver Application Server](https://community.sap.com/t5/c-khhcw49343/SAP%2520NetWeaver%2520Application%2520Server/pd-p/01200615320800000352)

* [SAP NetWeaver Application Server

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BNetWeaver%2BApplication%2BServer/pd-p/01200615320800000352)

View products (1)

With ST-PI Support Package 20 we have introduced a new transaction which allows to generate graphics to display the snapshot monitoring data collected by transaction /SDF/MON or /SDF/SMON.

*see also SAP note [3210905 - Display Snapshot Monitor Data](https://me.sap.com/notes/3210905)*

![](/legacyfs/online/storage/blog_attachments/2023/05/SDFMON_DISPLAY_Overview-1.png)

The new program /SDF/SMON\_DISPLAY will open an external modal window to display the data in a simple graphic using the external JavaScript charting library plotly.js (see <https://plot.ly/javascript/> - (C)opyright 2012-2019, Plotly, Inc.).

**The new transaction is compatible with SAPGUI, WebGUI and JavaGUI.**

### Prerequisites

In order to use the new transaction **/SDF/SMON\_DISPLAY** (or report /SDF/SMON\_DISPLAY) the following prerequisites must be fulfilled:

+ The snapshot monitor /SDF/MON or /SDF/SMON must be scheduled.

+ A SAPGUI version of release 7.70 or later is recommended with Edge based on chromium enabled. (*See SAPGUI Options > Interaction Design > Control Settings*)

+ *Additionally **you must provide the URL to a plotly compatible library***. Minimum version of the plotly Javascript library is v1.58.5 (basic bundle, minimized version recommended). You find detailed information about the available libraries at: <https://github.com/plotly/plotly.js/#load-via-script-tag>. The links to the latest plotly basic bundle can found at <https://github.com/plotly/plotly.js/blob/master/dist/README.md#plotlyjs-basic>.
  ***Disclaimer:****SAP is unable to guarantee that the libraries downloaded from external sources are safe to use. Theoretically such external download locations could be compromised.
  If you do not trust an externally hosted library, you can download a library version of your choice, test this library and then host this library on a trusted server and use the URL to this trusted location. (we recommend using the minimized versions like plotly-basic-x.xx.x.min.js - more versions are available at [https://cdnjs.com/libraries/plotly.js)](https://cdnjs.com/libraries/plotly.js%29).*You must maintain the URL to the plotly library in table /SDF/PLOTLYCONF for ID = PLOTLY\_LIBRARY. (SE11 > Table: /SDF/PLOTLYCONF >Utilities > Table Content > Create Entries).

  ![christoph_weyd_0-1706715213673.png](/t5/image/serverpage/image-id/57646i3A115B0DC6D091C5/image-size/medium?v=v2&px=400 "christoph_weyd_0-1706715213673.png")

  **Alternatively, you can add parameter /SDF/PLOTLY = cdn.plot.ly/plotly-basic-2.26.0.min.js in your user parameters (transaction SU3).**

  ![christoph_weyd_0-1755008375905.png](/t5/image/serverpage/image-id/299955i8F39A407233C11F8/image-dimensions/568x88?v=v2 "christoph_weyd_0-1755008375905.png")

+ If you choose an external library location the front end must have internet/network connection to access and download this library.
+ As alternative you can host the plotly library on any of your SAP ABAP application servers as described in [https://help.sap.com/doc/saphelp\_nw73ehp1/7.31.19/en-US/48/3e1b4e252f72d0e10000000a42189c/content.ht...](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/48/3e1b4e252f72d0e10000000a42189c/content.htm)
  You use profile parameter *icm/HTTP/file\_access\_0 = PREFIX=/doc/, DOCROOT=/tmp/documents* to point to an application server directory where you host the plotly.js file and then you can use URL [http://<SERVER:PORT>/<PREFIX>/plotly.js](http://vmsap:8080/doc/plotly.js)

**New Version**A new version which is available via [SAP note 3530270 - Improvements /SDF/SMON\_DISPLAY](https://me.sap.com/notes/3530270) is adding improved graphic options:

* **Server Comparison Chart**
  ![christoph_weyd_3-1740679924151.png](/t5/image/serverpage/image-id/231350i15C73C5F8990749B/image-size/medium?v=v2&px=400 "christoph_weyd_3-1740679924151.png")
* **Server Time Series**
  ![christoph_weyd_4-1740679969669.png](/t5/image/serverpage/image-id/231351iDD4766562CD236C2/image-size/medium?v=v2&px=400 "christoph_weyd_4-1740679969669.png")
* **Server Time Series stacked**
  ![christoph_weyd_5-1740680018475.png](/t5/image/serverpage/image-id/231353iEF24724A3ED724EE/image-size/medium?v=v2&px=400 "christoph_weyd_5-1740680018475.png")

**Program Parameters**

**Server**

Application Server (*leave empty for all servers*)

**Date/Time**

Date and Time of the snapshot. extended monitoring data from /SDF/SMON will be automatically de-clustered if required.![](/legacyfs/online/storage/blog_attachments/2023/05/DateTime.png)

**Last n minutes**

Only select and display the last n minutes of data for the current day. If this option is selected, the input fields Date/Time are disabled and calculated automatically with each refresh.![](/legacyfs/online/storage/blog_attachments/2023/05/Last-n.png)

**Round Time to n seconds**

The timestamps from SDFMON will be rounded to the next multiple of the specified number of seconds (*max. rounding to 3600 seconds*)![](/legacyfs/online/storage/blog_attachments/2023/05/Round_Time-1.png)

**Data Source**

- Monitoring Data (*Table /SDF/MON\_HEADER*)
- Extended Monitoring (*Table /SDF/SMON\_HEADER*)

![](/legacyfs/online/storage/blog_attachments/2023/05/Data-Source-2.png)

**Measurements**

Up to three different measurements can be specified.![](/legacyfs/online/storage/blog_attachments/2023/05/Measurements-2.png)

If the data is rounded to n seconds or if multiple application servers are selected one can specify how the data is aggregated - the following options are available:

* AVG Average
* SUM Total
* MAX Maximum Value
* MIN Minimum Value
* CNT Number of values (count)

![](/legacyfs/online/storage/blog_attachments/2023/05/Aggregation-1....