---
title: SAP Business Technology Platform Audit Logs Command-line Interface (CLI) to automate downloads plus associated best practices and FAQs
url: https://blogs.sap.com/2023/02/23/sap-business-technology-platform-audit-logs-command-line-interface-cli-to-automate-downloads-plus-associated-best-practices-and-faqs/
source: SAP Blogs
date: 2023-02-24
fetch_date: 2025-10-04T07:58:10.105861
---

# SAP Business Technology Platform Audit Logs Command-line Interface (CLI) to automate downloads plus associated best practices and FAQs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Business Technology Platform Audit Logs Comman...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160110&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Business Technology Platform Audit Logs Command-line Interface (CLI) to automate downloads plus associated best practices and FAQs](/t5/technology-blog-posts-by-sap/sap-business-technology-platform-audit-logs-command-line-interface-cli-to/ba-p/13556631)

![Matthew_Shaw](https://avatars.profile.sap.com/0/1/id01d8ac7acc3476d360b2ff66e47d2f7b6c79bb17c0fc2116604af2de293d75cf_small.jpeg "Matthew_Shaw")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Matthew\_Shaw](https://community.sap.com/t5/user/viewprofilepage/user-id/70553)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160110)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160110)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556631)

‎2023 Feb 23
5:58 PM

[16
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160110/tab/all-users "Click here to see who gave kudos to this post.")

3,672

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

Having recently published an article and sample solution that downloads the [SAP Analytics Cloud Activities Log](https://blogs.sap.com/2023/01/18/sap-analytics-cloud-activities-log-command-line-interface-cli-to-automate-downloads-associated-best-practices/), I thought I'd make a few adjustments so to enable the same for the BTP Audit Logs.

So, that's what I've done and this sample solution is available now.

The BTP Audit Logs had an extra challenge which was to dynamically parse the JSON within the 'message' and turn each of the name/value pairs into a column of the generated .csv file. Whilst this solution doesn't load the data into a database, and so may fall short for some, I suspect the feature of turning the nested JSON in to columns will be of particular interest to many.![](/legacyfs/online/storage/blog_attachments/2023/02/nested-json-to-columns-scaled.jpg)

Nested JSON message is dynamically parsed and each name/value pair turned into a column

My solution uses nodejs and Postman. If you’re happy to use nodejs (which is available on the SAP BTP platform too) and the Postman libraries ‘newman’ then this sample solution is ideal.

## The benefits of this sample are:

* Command line interface

  + enabling automation

  + removing human effort and error

* Files created

  + by time period, rather than by size

  + which are truly complete without duplicates in different files

  + with a consistent time zone of your choice eliminating a missing or duplicate hour

  + in a way that enables 3rd party tools to easily read them

  + **with a column for each element of the nested JSON message allowing you to easily access any element within it**

* Design and error management

  + enabling a known result

## Adopt and consume

I’ve done my very best to remove as many barriers as I can, and it means you can immediately adopt and consume the Audit Log API

* All the thinking and best practices has been done for you

* No need to develop or write any code

* No need to understand how the API works

* No need to fathom various complexities

  + How to parse the nested JSON (and for NEO, how to extract JSON from the message)

  + daylight saving time zones, error handling, very rare API errors etc.

* Detailed step-by-step [user guide](https://dam.sap.com/mac/u/a/vfjnhzM.htm?rc=10&includeRelatedAssets=true) to get it all working within about 2 hours

* Shared best practices and known issues to ensure best possible success

My meticulous attention to detail should mean you are probably going to avoid a number of rare errors and you may even resolve some exceptionally rare issues with the manual download too! I hadn’t realised how complicated downloading a bunch of logs really was until I dived into the detail and thought about it for weeks on end!

You’ll find an article below on this solution, but I’ve also added in a load of other related topics. I’ve compiled a list of best practices covering many areas including, the sample script itself, the audit log in general, a bunch of FAQs, and for the developer an overview of how the solution actually works.

## Feedback is important

Administrators just like you would very much value feedback from other customers on this solution. Please find the time to post a comment to this blog if you adopt it and hit the like button!  As a suggestion, please use this template:

```
We have this number of audit logs: xx

We use this sample with this number of SAP BTP subaccounts: xx

We use the option(s): ‘all’, ‘lastfullmonth’, etc.

We use time zone hour/mins: xx hours / 0 mins

We use a scheduler to run this sample script: yes/now

We use the dynamically generated columns derived from the JSON: yes/no

We saved this much time using this sample, rather than developing it ourselves: xx weeks/days

We rate this sample out of 10 (1=low, 10=high): xx

Our feedback for improvement is: xx
```

Your feedback (and likes) will also help me determine if I should carry on investing my time to create such content.

Feel free to follow this blog for updates.

## Simple demo

A simple demo of the command-line interface is shown here. There are 12 other command-line argument options available.

![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-Audit-Log-demo-download.gif)

Downloading the audit logs. There are 12 other command-line options

![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-Audit-Log-demo-view-in-Excel.gif)

The .c*sv file generated as viewed in Microsoft Excel. A column is created for each value pair in the message JSON*

# Resources

|
 Latest article |
 [Version 1.0 – February 2023](#TOC)  Microsoft PowerPoint [Preview Slides](https://dam.sap.com/mac/u/a/qsQwiKE.htm?rc=10&includeRelatedAssets=true)  Microsoft PowerPoint [Download Slides](https://d.dam.sap.com/a/qsQwiKE) |

|
 [Installation and Configuration] user guide |...