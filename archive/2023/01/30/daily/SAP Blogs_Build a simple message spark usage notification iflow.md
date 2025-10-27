---
title: Build a simple message spark usage notification iflow
url: https://blogs.sap.com/2023/01/29/build-a-simple-message-spark-usage-notification-iflow/
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:18.359827
---

# Build a simple message spark usage notification iflow

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Build a simple message spike usage notification if...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160077&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Build a simple message spike usage notification iflow](/t5/technology-blog-posts-by-sap/build-a-simple-message-spike-usage-notification-iflow/ba-p/13556484)

![AlexDong](https://avatars.profile.sap.com/3/c/id3c83fee5ba461d26603cb976b78e6ecabe86c28805cc4244f856dab70bc6118b_small.jpeg "AlexDong")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AlexDong](https://community.sap.com/t5/user/viewprofilepage/user-id/41983)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160077)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160077)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556484)

‎2023 Jan 29
9:58 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160077/tab/all-users "Click here to see who gave kudos to this post.")

1,737

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Alert Notification service for SAP BTP](https://community.sap.com/t5/c-khhcw49343/SAP%2520Alert%2520Notification%2520service%2520for%2520SAP%2520BTP/pd-p/73555000100800001401)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Alert Notification service for SAP BTP

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BAlert%2BNotification%2Bservice%2Bfor%2BSAP%2BBTP/pd-p/73555000100800001401)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

## Background

We know that one of the biggest advantages for SAP Integration Suite is the monitor functionality. You can monitory different KPI figures like how many messages completed in the past 12 hours or how many messages failed in the past hour, as the following screenshot shows.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-16.51.54.png)

However, sometimes we don't want to check manually every day to see if something goes wrong with messages. We want to have some notification mechanism that when e.g. message counts go beyond some threshold then we will receive a email notification. And SAP Alert Notificaiton Service can help here.

The IFlow will look like this.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-16.47.42.png)

## Prerequisites

1. You have basic knowlege on SAP Integration Suite

2. You already have SAP Integation Suite instance

3. You already have entitlements on SAP Alert Notification Service

## Steps

First of all we need to have some API which can show the message status during the last 12 hours for instance. Fortunately SAP has already given such kind of API called [Message Processing Logs](https://api.sap.com/api/MessageProcessingLogs/resource).

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-16.59.40.png)

The first one will give all message details given the filter condition e.g. you can set `Status eq 'FAILED'` which returns message processing logs with status 'FAILED'. Let's try the third simple one, which you can leverage to return the message count given the filter information.

You can test this API via postman very conveniently.

* API host is your SAP Integration Suite runtime address, which you must be very familiar if you are a integration developer.

* API path is /api/v1/MessageProcessingLogs/$count

* API filter is $filter=LogEnd gt datetime'2023-01-28T20:17:57' and LogEnd le datetime'2023-01-29T08:17:57'. Of course the start time and end time should be dynamic and we need to set it up within this Iflow.

* API payload is just the message count number e.g. 96 here.

* API authorization is the same as the one used for other iflows e.g. the OAuth2 client id and secret

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-17.04.20.png)

We also need to have SAP Alert Notification Service (ANS) running so that if the message count within last 12 hours have exceeded the threshold we specified, we will get an email. SAP ANS is not complicated and you can search in SAP community for information like how to create instance and how to set it up and finally how to test it. E.g. here is a nice [blog post](https://blogs.sap.com/2022/02/01/connect-sap-platform-integration-with-alert-notification-service-cloud-foundry/) telling how to set it up in Cloud Foundry environment. Regarding the cost and price, you can refer to [Discovery Center](https://discovery-center.cloud.sap/serviceCatalog/alert-notification?region=all&tab=service_plan). Once you have SAP ANS instance ready, you can fill in the email subject and payload and send it to SAP ANS and then SAP ANS sent email to the person specified in SAP ANS.

Here is the event condition I set.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-17.22.30.png)

Now we have the API endpoint for Message Logs and SAP ANS for sending out notification emails.

Let's start to compose the Integration Flow, starting with a timer, which will trigger this IFlow every 12 hours.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-17.25.32-1.png)

I also put a content modifier named "Initialize" which is pertty simple, so that you can specify the message threshold. If the message count within the 12 hours exceeds this threshold, then we trigger the notification, otherwise we do nothing. This is an externalized parameter and you can configure it each time you want to change it to some new value.

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-29-at-17.28.57.png)

The next step we need to calculate the time range for last 12 hours via a groovy script. Here is the code I used. And we need to consume the two properties called "CURRENT\_TIME\_FRAME\_START" and "CURRENT\_TIME\_FRAME\_END" for the Message Logs API endpoint filter. You can also see we set 12 hours for "MAX\_TIME\_FRAME\_SIZE\_MS".

```
import com.sap.gateway.ip.core.customdev.util.Message

import groovy.transform.Field

import java.text.ParseException

import java.text.SimpleDateFormat

@Field final String TIME_ZONE = "UTC"

@Field final String TIME_FORMAT = "yyyy-MM-dd'T'HH:mm:ss"

@Field final SimpleDateFormat DATE_FORMATTER = new SimpleDateFormat(TIME_FORMAT)

@Field final String LOG_PROPERTY_KEY = 'Log'

@Field final String LAST_TIME_FRAME_END_HEADER_NAME = "LAST_TIME_FRAME_END"

@Field final String CURRENT_TIME_FRAME_END_HEADER_NAME = "CURRENT_TIME_FRAME_END"

@Field final String CURRENT_TIME_FRAME_S...