---
title: Integrate Qualtrics Surveys directly with SAP Emarsys Engagement Platform
url: https://blogs.sap.com/2023/06/07/integrate-qualtrics-surveys-directly-with-sap-emarsys-engagement-platform/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:18.358467
---

# Integrate Qualtrics Surveys directly with SAP Emarsys Engagement Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Integrate Qualtrics Surveys directly with SAP Emar...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158648&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrate Qualtrics Surveys directly with SAP Emarsys Engagement Platform](/t5/technology-blog-posts-by-sap/integrate-qualtrics-surveys-directly-with-sap-emarsys-engagement-platform/ba-p/13552484)

![carsten_heuer1](https://avatars.profile.sap.com/f/3/idf30967c37c3a387226faad6e8975871d8c05ba1e04094fc73cb54fb5121060f5_small.jpeg "carsten_heuer1")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[carsten\_heuer1](https://community.sap.com/t5/user/viewprofilepage/user-id/281076)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158648)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158648)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552484)

‎2023 Jun 07
10:59 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158648/tab/all-users "Click here to see who gave kudos to this post.")

2,818

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Marketing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Marketing/pd-p/01200615320800003850)
* [Qualtrics CoreXM](https://community.sap.com/t5/c-khhcw49343/Qualtrics%2520CoreXM/pd-p/cd2c430f-9140-4b41-9310-89b9391b0524)
* [SAP Emarsys](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys/pd-p/73554900100800003661)

* [SAP Marketing

  SAP Marketing](/t5/c-khhcw49343/SAP%2BMarketing/pd-p/01200615320800003850)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Qualtrics CoreXM

  Software Product](/t5/c-khhcw49343/Qualtrics%2BCoreXM/pd-p/cd2c430f-9140-4b41-9310-89b9391b0524)
* [SAP Emarsys

  Software Product](/t5/c-khhcw49343/SAP%2BEmarsys/pd-p/73554900100800003661)

View products (4)

# Introduction

Are you using SAP Emarsys Engagement Platform and Qualtrics XM in your organisation? Combine the advantages of both solutions and receive personal experience feedback!

Learn here, how to integrate SAP Emarsys with Qualtrics directly by using SAP Integration Suite and standard extensibility features. SAP Emarsys is an engagement platform best suited for omnichannel and highly personalized marketing use cases. A frequently used marketing scenario is to interact with customers by sending out any kind of surveys to collect experience feedback for different purposes. Qualtrics XM is an experience management platform and among other surveys can be created, run, and evaluated. With SAP Emarsys an email campaign with an embedded personalized link to a Qualtrics survey is send out to customers and the survey response data are pushed back from Qualtrics to SAP Emarsys custom fields for further marketing activities like segmentation or automation program triggering.

This blogpost outlines the process flow and uses standard capabilities of SAP Emarsys, SAP Integration Suite on SAP Business Technology Platform (SAP BTP) and Qualtrics XM. My thank goes to rafael.creutz for configuring and setting up all described technical steps and the great collaboration and support. His documentation on step-by-step technical details together with the used Integration Flow (iFlow) as a template for free download are located on [SAP Business Accelerator Hub](https://api.sap.com/allcommunity) as Community Content (consider the disclaimer for any use of these content assets). There is no guarantee or support for any information or code in this blog post. Please test any content that you may want to use yourself.

# Table of Content

* [Use Case](#UseCase)

* [Process Flow – Overview](#ProcessFlow)

* [Integration Scenario – Detailed Steps](#IntegrationScenario)

* [Recommendations](#Recommendations)

* [Summary](#Summary)

* [Related Articles](#Articles)

# Use Case

Surveys are a great activity in marketing to engage with your customers and let them express their perception on your brand, get an understanding if they are happy with the usage of a recently bought product, or any other kind of customer feedback. This can reactivate inactive customers, increase retention, and help to collect useful additional data to better understand the needs of your customers.

To illustrate our integration scenario of SAP Emarsys and Qualtrics, we will use a Brand Survey scenario to measure the brand perception with a NPS score. For this, an Email campaign is sent from SAP Emarsys to customers with an embedded personalized link targeting to the brand survey in Qualtrics. The customer receives the Email, clicks the link to the survey and completes the survey. The survey responses are stored in Qualtrics. The customers response to the question on Brand NPS is replicated from Qualtrics to a custom field at SAP Emarsys. The individual Brand NPS score value can be used in SAP Emarsys segmentation to identify brand promoters and brand detractors for further follow-up activities.

# Process Flow – Overview

The above use case can be realized by a direct integration of SAP Emarsys and Qualtrics, which is done in two parts.

## Part I – Launch personalized Email campaign with individual survey links

1. For each customer of a segment a personalized link to the Qualtrics survey is generated by Qualtrics triggered from an SAP Emarsys automation program (Webhook node). This is done via API calls from SAP Emarsys to Qualtrics member by member for the given segment. SAP Integration Suite is used for authentication, field mapping and some logical steps.

2. On Qualtrics side an individual survey link is generated and replicated from Qualtrics to SAP Emarsys as payload of an external event.

3. The external event launches the trigger Email campaign on Emarsys side per customer.

4. The personalization service of SAP Emarsys ensures that the personalized survey link is inserted to the corresponding token during email launch. The Email goes out to the customer.

![](/legacyfs/online/storage/blog_attachments/2023/06/Demo_Flow_Part1a.png)

Process Diagram – Part I

## Part II – Push survey response data from Qualtrics to SAP Emarsys

1. The customer receives the Email with the personalized survey link.

2. By clicking on the personalized survey link in the Email the customer navigates to the survey on the Qualtrics platform, enters some answers and completes the survey.

3. With the completion of the survey a Qualtrics survey workflow is started which calls a second iFlow to handle SAP Emarsys authentication and storing the NPS score to the corresponding custom field at SAP Emarsys.

4. Depending on the individual NPS score value the customer is assigned to the Brand Promoter or Brand Detractor segment.

![](/legacyfs/online/storage/blog_attachments/2023/06/Demo_Flow_Part2a.png)

Process Diagram – Part II

Every process step is described in more detail in the next chapter.

# Integration Scenario – ...