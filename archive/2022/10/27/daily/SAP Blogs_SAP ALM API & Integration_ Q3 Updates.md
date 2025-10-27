---
title: SAP ALM API & Integration: Q3 Updates
url: https://blogs.sap.com/2022/10/26/sap-alm-api-integration-q3-updates/
source: SAP Blogs
date: 2022-10-27
fetch_date: 2025-10-03T21:00:35.265668
---

# SAP ALM API & Integration: Q3 Updates

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP ALM API & Integration: Q3 Updates

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155680&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP ALM API & Integration: Q3 Updates](/t5/technology-blog-posts-by-sap/sap-alm-api-integration-q3-updates/ba-p/13543890)

![Xavier](https://avatars.profile.sap.com/1/d/id1d30004849474879083050b873da5cdcebb5cc9543001f3dbdc54d08c8d12d41_small.jpeg "Xavier")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Xavier](https://community.sap.com/t5/user/viewprofilepage/user-id/4449)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155680)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155680)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543890)

‎2022 Oct 26
6:49 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155680/tab/all-users "Click here to see who gave kudos to this post.")

973

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP Focused Run](https://community.sap.com/t5/c-khhcw49343/SAP%2520Focused%2520Run/pd-p/73555000100800000451)
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [Focused Insights for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Insights%2520for%2520SAP%2520Solution%2520Manager/pd-p/0c9ec02c-46fe-498e-a301-66c5a13461e9)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SAP Focused Run

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BFocused%2BRun/pd-p/73555000100800000451)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [Focused Insights for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BInsights%2Bfor%2BSAP%2BSolution%2BManager/pd-p/0c9ec02c-46fe-498e-a301-66c5a13461e9)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (5)

## Goal of this blog series

With this series of blogs, we want to keep you informed on the latest news and what is important in the area of SAP ALM **APIs** and **integration** for **SAP Cloud ALM**, **SAP Focused Run** and **SAP Solution Manager**.

## ![](/legacyfs/online/storage/blog_attachments/2022/10/Intro.png)

#### Motivation

Today, ALM tool chain must connect different teams from different locations, platforms, solutions and tools relying on open source or proprietary technologies.

ALM requires the capabilities to **integrate** all ALM tools and the capacity to produce unified reporting and analytics for the entire life-cycle.

# Q3 Updates

## SAP Cloud ALM Tasks API

The [Tasks API](https://api.sap.com/api/CALM_TKM/overview) has been extended with the following attributes:

* **type**: News **Task types** supported with dedicated approval state values:

  + CALMTMPL: Template

  + CALMTASK: Task

  + CALMUS: User Story

  + CALMST, Sub-Task

  + CALMREQU: Request

  + CALMDEF: Defect

* **deliverables**: Create, update, read, and delete custom deliverables

* **workstreams**: Create, update, read, and delete work-streams.

* **startDate**: Set and read the start date of new and existing tasks.This allows you to control the manual duration of tasks by API.

## SAP Cloud ALM Analytics API

### Tasks analytics

* The [Tasks](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/5767f7721fe7422fbac995199fad07ee.html) data providers supports the following new dimension:

  + **Scope,**

  + **Type**,

  + **Processor**.

### Defects and Requirements Analytics

Two new analytics data providers for **Defects** and **Requirements** are available:

* **Defects**: Check the [help.sap.com](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/8ef2bf2f48db4e888d8a187df4a01bc4.html) API guide.

* **Requirements**: Check the [help.sap.com](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/bd271197f7cb4824ac7cfe30de4c8561.html) API guide.

Defects and requirements analytics APIs complement the following SAP Cloud ALM for Implementation analysis data providers already available: **Projects**, **Tasks** and **Test** **Executions**.

![](/legacyfs/online/storage/blog_attachments/2022/10/Requirements.png)

### Business Status Events Analytics

The Business Status Events Analytics is used to retrieve statistical information for status events managed by SAP Cloud ALM.

**Documentation**:

* [SAP API Hub](https://api.sap.com/api/CALM_ANALYTICS/overview)

* [help.sap.com](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/f97b4bc19c124280961f600f87a4316b.html)

You can generate SAP and custom events reports to monitor maintenance, degradation, and outage situations.

* **Status Events**: Check the [help.sap.com](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/f97b4bc19c124280961f600f87a4316b.html) API guide.

![](/legacyfs/online/storage/blog_attachments/2022/10/Status.png)

## SAP Cloud ALM Resource Changes API

The SAP Cloud ALM Resource Changes API is used to define a **web-hook** and create an event resources **subscription** specific to that web-hook.

The web-hook is implemented by third party applications interested in receiving resource change events from selected SAP Cloud ALM resources.

**Documentation**:

* [SAP API Hub](https://api.sap.com/api/CALM_RESOURCE_CHANGES/overview)

* [help.sap.com](https://help.sap.com/docs/CloudALM/fe419bfabbdc46dfbddbfd78b21483d5/64ccd91adb1e4a23bf654556cdb8affa.html)

**Supported Resource types**:

* EVENT-SITUATIONS

**Supported Event types**:

* EVENT-SITUATION.CREATED: Occurs whenever an event-situation is created.

* EVENT-SITUATION.UPDATED: Occurs whenever an event-situation is updated.

* EVENT-SITUATION.DELETED: Occurs whenever an event-situation is deleted.

* EVENT-SITUATION.PING: Occur to get latest event-situation data.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-alm-api-integration-q3-updates%2Fba-p%2F13543890%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related ...