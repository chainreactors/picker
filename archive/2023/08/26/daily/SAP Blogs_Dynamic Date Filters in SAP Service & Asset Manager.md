---
title: Dynamic Date Filters in SAP Service & Asset Manager
url: https://blogs.sap.com/2023/08/25/dynamic-date-filters-in-sap-service-asset-manager/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T12:00:17.988897
---

# Dynamic Date Filters in SAP Service & Asset Manager

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Dynamic Date Filters in SAP Service & Asset Manage...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/55141&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Dynamic Date Filters in SAP Service & Asset Manager](/t5/enterprise-resource-planning-blog-posts-by-sap/dynamic-date-filters-in-sap-service-asset-manager/ba-p/13581559)

![RyanWeicker](https://avatars.profile.sap.com/8/2/id8285efbc987283f295990e2e5c3b1952e464513ae073336acc391998326939b0_small.jpeg "RyanWeicker")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[RyanWeicker](https://community.sap.com/t5/user/viewprofilepage/user-id/229191)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=55141)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/55141)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581559)

‎2023 Aug 25
8:51 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/55141/tab/all-users "Click here to see who gave kudos to this post.")

1,650

* SAP Managed Tags
* [Mobile Application Integration Framework](https://community.sap.com/t5/c-khhcw49343/Mobile%2520Application%2520Integration%2520Framework/pd-p/6baf0d27-c212-4154-85a9-71ed13c7b1ab)
* [SAP Service and Asset Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520and%2520Asset%2520Manager/pd-p/73555000100800000639)

* [SAP Service and Asset Manager

  Software Product](/t5/c-khhcw49343/SAP%2BService%2Band%2BAsset%2BManager/pd-p/73555000100800000639)
* [Mobile Application Integration Framework

  Software Product Function](/t5/c-khhcw49343/Mobile%2BApplication%2BIntegration%2BFramework/pd-p/6baf0d27-c212-4154-85a9-71ed13c7b1ab)

View products (2)

# Creating a Dynamic Date Filter for SAP Service & Asset Manager

A requirement during every SAP Service & Asset Manager project is to configure the data filters within the Mobile Application Integration Framework to determine what data is considered for synchronization to the mobile device. Many filter rule types are self explanatory - "User Profile Parameters" consider the parameter value maintained in SU3 while "Static Value in Range Table Format" allows you to explicitly declare filter values, while one, the "Filter Handler" is more complex.

A common requirement in projects is to **dynamically** filter data based on a date range. To do this, we leverage a powerful Filter Rule Type called a "Filter Handler" and specifically the "oMDO Filter Rule - Date Range" Handler. Through this handler, we can dynamically define start and end dates for a date range based on the date of synchronization. This blog will explain how to use this handler and provide an example calculation.

### Example - Using the "oMDO Filter Rule - Date Range" Handler

In our example, we wish to configure the "BASIC\_FINISH\_DATE" filter on the SAM2210\_WORK\_ORDER\_GENERIC oMDO to return all work orders whose BASIC\_FINISH\_DATE is **this week**.

To do this, navigate to the oMDO in transaction /SYCLO/CONFIGPANEL, we create a new Rule for the BASIC\_FINISH\_DATE of type "Filter Handler" and Handler "oMDO Filter Rule - Date Range". For the Input Parameter we use this: "CURRENT\_DATE=CURR\_WEEK\_FIRST\_DAY&FROM\_DATE\_OFFSET=0&TO\_DATE\_OFFSET=6"

If a synchronization is performed on Tuesday, August 22nd 2023, this rule will evaluate to a start date of 8/21/203 and an end date of 8/27/2023, thus giving us a date range of every date in this week.

![](/legacyfs/online/storage/blog_attachments/2023/08/2023-08-23_10-47-34.png)

A Screenshot of the WORK\_ORDER\_GENERIC oMDO

### Parameter Options for the "oMDO Filter Rule - Date Range" Handler

So how does this work?

The input parameter string provides the rule with the input to dynamically calculate the date range. The idea is to establish a starting date for the calculation through the use of the CURRENT\_DATE parameter, then determine the start and end of that range using the FROM\_DATE\_OFFSET and TO\_DATE\_OFFSET parameters which are integer values. The structure of the string is as follows:
"CURRENT\_DATE=<current\_date\_param\_value>&FROM\_DATE\_OFFSET=<integer>&TO\_DATE\_OFFSET=<integer>"

Note the exact syntax - the "=" between parameter name and value and the "&" between the three different parameters.

Because the CURRENT\_DATE is the basis for the calculation, is it required. FROM\_DATE\_OFFSET and TO\_DATE\_OFFSET are optional.

**Parameter: CURRENT\_DATE**

* Required (rule exits as blank if not provided)

* Determines the "CURRENT\_DATE" which is used as the basis for the date range calculation. Is calculated based on the possible parameter values described below

* Possible Values:

  + TODAY

  + CURR\_MONTH\_FIRST\_DAY

  + CURR\_MONTH\_LAST\_DAY

  + PREV\_MONTH\_FIRST\_DAY

  + PREV\_MONTH\_LAST\_DAY

  + CURR\_WEEK\_FIRST\_DAY

    - Note - the first day of the week is considered to be a MONDAY in SAP.

**Parameter: FROM\_DATE\_OFFSET**

* Optional

  + If not supplied, will return the CURRENT\_DATE resolved above

* Determines the start of the date range by subtracting the parameter value from the date resolved from parameter CURRENT\_DATE.

* Possible Values:

  + Must only contain a positive integer value

**Parameter: TO\_DATE\_OFFSET**

* Optional

  + If not supplied, will return the CURRENT\_DATE resolved above

* Determines the start of the date range by adding the parameter value from the date resolved from parameter CURRENT\_DATE.

* Possible Values:

  + Must only contain a positive integer value

Then to tie it all together - If we consider the example Input Parameter string above - "CURRENT\_DATE=CURR\_WEEK\_FIRST\_DAY&FROM\_DATE\_OFFSET=0&TO\_DATE\_OFFSET=6" the calculation would proceed as follows:

* First, the rule will determine the first day of the current week "CURR\_WEEK\_FIRST\_DAY". This will be calculated as 8/21/2023

* Second, the rule will subtract 0 (FROM\_DATE\_OFFSET) from that date to determine the start date of the range: 8/21/2023

* Finally, the rule will add 6 (TO\_DATE\_OFFSET) from that date to determine the end date of the range: 8/27/2028

**Technical Note -**if you want to see the logic in the backend, check ABAP class "/MFND/CL\_CORE\_DATE\_RANGE\_ORU" in SE24.

Hopefully this helps explain how to use this very useful Filter Handler!

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fdynamic-date-filters-in-sap-service-asset-manager%2Fba-p%2F13581559%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linke...