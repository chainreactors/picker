---
title: The Advent of SAP Cloud SDK for JavaScript Version 3
url: https://blogs.sap.com/2022/12/12/the-advent-of-sap-cloud-sdk-for-javascript-version-3/
source: SAP Blogs
date: 2022-12-13
fetch_date: 2025-10-04T01:17:56.182652
---

# The Advent of SAP Cloud SDK for JavaScript Version 3

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud SDK for JavaScript Version 3 is in the m...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157166&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud SDK for JavaScript Version 3 is in the making](/t5/technology-blog-posts-by-sap/sap-cloud-sdk-for-javascript-version-3-is-in-the-making/ba-p/13548574)

![marika_marszalkowski](https://avatars.profile.sap.com/e/4/ide406e74380efab6f13d39af273e3136ee3ae7296acbc6ea57e5dea8aa5af5552_small.jpeg "marika_marszalkowski")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[marika\_marszalkowski](https://community.sap.com/t5/user/viewprofilepage/user-id/282898)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157166)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157166)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548574)

‎2022 Dec 12
9:41 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157166/tab/all-users "Click here to see who gave kudos to this post.")

1,051

* SAP Managed Tags
* [SAP Cloud SDK](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520SDK/pd-p/73555000100800000895)

* [SAP Cloud SDK

  SAP Cloud SDK](/t5/c-khhcw49343/SAP%2BCloud%2BSDK/pd-p/73555000100800000895)

View products (1)

SAP Cloud SDK for JavaScript version 3 is in the making. Check out what's new and share your feedback upfront.

**Update**: Version 3 was released in the mean time. For details, check the [release blog post](https://blogs.sap.com/2023/03/02/sap-cloud-sdk-version-3/).

*View this announcement on [GitHub](https://github.com/SAP/cloud-sdk-js/discussions/3197).*

## What's New?

### Improved OData Generator

We are discontinuing the shipment of pregenerated clients (often called Virtual Data Model, VDM). Instead, you can generate your own clients with the SAP Cloud SDK OData generator.
We are improving the API, default behavior and performance of the OData generator, to make it even more convenient for you to generate a client for the service you need.

### Middlewares

We will introduce a new concept: middlewares. With middlewares you will be able to add your own logic before request execution - similar to web application frameworks like Express or NestJS.
For example, you could send additional requests or change the payload before sending the actual request.
Another common case for middlewares is [resilience](https://github.com/SAP/cloud-sdk-js/discussions/3197#resilience), e.g. if you want to protect your system with a circuit breaker. With middlewares, you will be able to cancel request execution based on statistics from previous requests.

### Resilience

Finally, resilience for your target system is integrated in the SAP Cloud SDK. You will be able to use the SAP Cloud SDK's default configuration for circuit breakers, retries and timeouts, or implement your own.
For more details on middlewares and resilience, refer to our [architecture decision record](https://github.com/SAP/cloud-sdk-js/blob/main/knowledge-base/adr/0031-resilience-options.md).

### Sending E-Mails

We recently released experimental functionality to send e-mails against SAP BTP destinations of type "MAIL".
In version 3 we will make it available for productive use.
You can find more details in the [mail documentation](https://sap.github.io/cloud-sdk/docs/js/features/mail-client).

### Housekeeping

We want to keep our API clean and simple to use. Therefore we will remove most of the deprecated functionality from the API.

Node 18 is the current long term support (LTS) version. Previous node versions will reach their end of life within the next year (see [node.js release schedule](https://github.com/nodejs/Release#release-schedule)). Therefore, all SAP Cloud SDK for JavaScript libraries will switch to node 18 as the minimum supported node version.

## Should I Upgrade?

Absolutely!
We will provide a comprehensive upgrade guide to make it as easy for you as possible.
**Only if you upgrade, will you be able to benefit from security updates and new features.**
Also, we try to keep our breaking changes as small as possible. If you update with every version, you only have to deal with a minimal set of changes.

## When?

The release is scheduled for Q1 2023. Stay tuned!

Feel free to give feedback on the scope, current state or the SDK in general and start a new [discussion](https://github.com/SAP/cloud-sdk-js/discussions) or comment here.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-cloud-sdk-for-javascript-version-3-is-in-the-making%2Fba-p%2F13548574%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  5 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Build a Code-based Agent using SAP AI Core with Next.js and the Vercel AI SDK](/t5/technology-blog-posts-by-sap/build-a-code-based-agent-using-sap-ai-core-with-next-js-and-the-vercel-ai/ba-p/14230640)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [Top 10 SAP Cloud ALM News September 2025](/t5/technology-blog-posts-by-sap/top-10-sap-cloud-alm-news-september-2025/ba-p/14230396)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [The Ultimate Guide to SAP S/4HANA Master Data - Part 5](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-part-5/ba-p/14229426)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Friday

Top kudoed authors

| User | Count |
| --- | --- |
| [![Ria4](https://avatars.profile.sap.com/4/1/id41f53dcfce78ad1c94edcd3a60b4666df8e3aac18a25c618793ae5b110c6aee0_small.jpeg "Ria4")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") Ria4](/t5/user/viewprofilepage/user-id/1478971) | 14 |
| [![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jp...