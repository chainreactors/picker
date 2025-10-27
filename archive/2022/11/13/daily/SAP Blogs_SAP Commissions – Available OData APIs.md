---
title: SAP Commissions – Available OData APIs
url: https://blogs.sap.com/2022/11/12/sap-commissions-available-odata-apis/
source: SAP Blogs
date: 2022-11-13
fetch_date: 2025-10-03T22:37:51.559632
---

# SAP Commissions – Available OData APIs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions - Available OData APIs

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5330&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions - Available OData APIs](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-available-odata-apis/ba-p/13543637)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5330)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5330)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543637)

‎2022 Nov 12
5:25 PM

[4
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5330/tab/all-users "Click here to see who gave kudos to this post.")

1,060

* SAP Managed Tags
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (2)

Dear All,

This article is mainly for SAP Commissions users/customers/partners to know & understand available OData API endpoints for your development or building web applications out of it.

## Introduction

OData is the current default way to communicate with an SAP backend, be it for an (SAPUI5) frontend or any other integration scenario. The goal of this document is to get an Commissions developer up and running with understanding and implementing OData services in an SAP Commissions-based backend system.

OData services; background information and how to test them.

I’ll try to explain what OData is by using calls on existing OData services, and expanding those calls with more options. I’ll start using a tool in my IDE so we’ll need to get this learning as the first step.

Reference :<https://www.odata.org/>![](/legacyfs/online/storage/blog_attachments/2022/10/FOGtyjCVcAI4Sno.jpg)
**SAP Commissions OData API Documentation**

<https://{domain-name}/APIDocument/odata/index.html>

#### **Filtering Options**

Operator Description

|  |
| --- |
| Logical Operators |
| eq | matches exactly (default) |
| ne | not equal to |
| gt | greater than |
| ge | greater than or equal |
| lt | less than |
| le | less than or equal |
| null | Supported by eq and ne operator. |
| like | Supported by eq and ne operator with the wildcard \*. |
| Grouping Operators |
| () | Precedence grouping |

---

**To find SAP Commissions OData Metadata structure or edmx (Entity Data Model)**

![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-30-57.png)
**To find the records through entityname**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-25-45-1.png)
**To find the total records count through passing Entity name**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-22-40.png)
**To find the Entity records in particular Page(Return the first 15 results)**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-19-17.png)
**To find the records through filter method**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-35-56.png)

**To find the records using Filter with multiple fields**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-41-28.png)

**To find the find the records through field using Order by descending or ascending** ![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-49-44.png)
**To find the records using Wildcard search**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_21-00-24.png)

**To find the records using selected fields in result output.**![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-12_20-54-24.png)
**Refer Standard OData Schema and useful endpoints**

+ <https://www.odata.org/odata-services/>

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [OData](/t5/tag/OData/tg-p/board-id/hcm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fhuman-capital-management-blog-posts-by-sap%2Fsap-commissions-available-odata-apis%2Fba-p%2F13543637%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [New CQC Solution Optimization Service](/t5/human-capital-management-blog-posts-by-sap/new-cqc-solution-optimization-service/ba-p/14234135)
  in [Human Capital Management Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)  an hour ago
* [Automating Custom Performance Data Transfer to Employee Profiles](/t5/human-capital-management-blog-posts-by-members/automating-custom-performance-data-transfer-to-employee-profiles/ba-p/14217030)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  Monday
* [Need to send Date Created and Start Date via OData API](/t5/human-capital-management-q-a/need-to-send-date-created-and-start-date-via-odata-api/qaq-p/14222765)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2 weeks ago
* [country field from Candidate profile template to Employee profile field for internal Hiring-SAP RCM](/t5/human-capital-management-q-a/country-field-from-candidate-profile-template-to-employee-profile-field-for/qaq-p/14222502)
  in [Human Capital Management Q&A](/t5/human-capital-management-q-a/qa-p/hcm-questions)  2 weeks ago
* [Deprecation of API Basic Authentication & Configuring Open ID Connect](/t5/human-capital-management-blog-posts-by-members/deprecation-of-api-basic-authentication-amp-configuring-open-id-connect/ba-p/14215998)
  in [Human Capital Management Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![ThomasBilbaugh](https://avatars.profile.sap.com/e/0/ide0070e22003039d74134e36021e60621f3d8092be5f11f8ea807d3b320997975_small.jpeg "ThomasBilbaugh")  ![Product and Topic Expert](/html/@138D6F765B...