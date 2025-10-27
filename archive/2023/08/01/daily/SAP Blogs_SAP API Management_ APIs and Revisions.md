---
title: SAP API Management: APIs and Revisions
url: https://blogs.sap.com/2023/07/31/sap-api-management-apis-and-revisions/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T17:00:04.014198
---

# SAP API Management: APIs and Revisions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP API Management: APIs and Revisions

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164096&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP API Management: APIs and Revisions](/t5/technology-blog-posts-by-sap/sap-api-management-apis-and-revisions/ba-p/13568943)

![ashutosh_kumar_singh02](https://avatars.profile.sap.com/1/1/id11d45ec50d9c296c4eefb4c13ce6a8ec90874f9cbe45900c7685bcfc679120bd_small.jpeg "ashutosh_kumar_singh02")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ashutosh\_kumar\_singh02](https://community.sap.com/t5/user/viewprofilepage/user-id/453525)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164096)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164096)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568943)

‎2023 Jul 31
9:29 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164096/tab/all-users "Click here to see who gave kudos to this post.")

3,961

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

**Introduction**

As an API proxy developer, you might have wondered how to track the incremental changes you’ve made to an API proxy and then view the deployed copy of the API proxy without causing any disruption to the deployed API in API portal.

Most of the time, these changes are compatible and incremental in nature. For example, adding a property or adding a new resource or attaching a policy to the API proxy.

Well, with API Revisions you can easily achieve the above and much more. You can increase your productivity, by performing the following tasks conveniently:

* + Preserve the incremental changes.

  + Refer to its older state.

  + Revert/restore the API to its older state.

  + Develop an API proxy without impacting the deployed state.

In this blog, we will explore the importance of API Revision and how it helps an API developer to make changes to an API proxy in a controlled and safe manner. Also, note that this feature is available both on SAP Integration Suite and SAP API Management.

**API Proxy and Revisions**

You create Revisions when there are changes that don't break the existing consumption flows. You can refer to the older state of the proxy preserved during API proxy development. You can access the past changes made to the API proxy, and even restore the API to any of its previous states.

A few salient features of API revisions:

* + Revisions will let an API owner make small changes to the API proxy and even restore the API to any of its previous states.

  + Revisions are immutable. Therefore, you can’t make changes to the revisions directly. You need to create a draft out of a revision to work on it.

  + Revision is a design time concept, that allows multiple revisions of an API proxy to co-exist. Only one revision can be deployable or executable.

  + Revision helps in tracking past changes and facilitates API development paradigm.

**How it Works**

When you create and save an API proxy, a draft gets created. You can deploy the draft and still continue to work on it. Once you’ve made the changes and tested it, you can also save this draft as a revision. The draft ceases to exist when a revision is created out of it.

Every edit on Revision creates a draft. You can revert from any of the previous revisions, the revert action creates a new Revision out of it.

An API Proxy gets created in a draft state. The draft is a working copy where the changes are allowed to be made and can also be deployed. Once the changes are made and tested, a Revision can be created from that draft. Draft ceases to exist when revision is created out of it. To capture the incremental changes, the API proxy developer can again create a draft from the latest saved revision.

![](/legacyfs/online/storage/blog_attachments/2023/07/Revisions.png)

Please refer to the step-by-step tutorial on revisions [here](https://developers.sap.com/tutorials/api-mgmt-revisioning.html).

**Import and Transport**

Every time you import or transport an API proxy, a new revision of the API gets created which can be deployed. This helps in traceability and lifecycle management. In both cases, the revision name is auto-generated.

**Summary**

* Capture small and incremental changes of an API proxy via revisions

* Create multiple revisions iteratively.

* Refer or Revert to any of the created revisions.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [api management](/t5/tag/api%20management/tg-p/board-id/technology-blog-sap)
* [api proxy](/t5/tag/api%20proxy/tg-p/board-id/technology-blog-sap)
* [API Proxy Revision](/t5/tag/API%20Proxy%20Revision/tg-p/board-id/technology-blog-sap)
* [APIManagementCapability](/t5/tag/APIManagementCapability/tg-p/board-id/technology-blog-sap)
* [IntegrationSuiteAPIM](/t5/tag/IntegrationSuiteAPIM/tg-p/board-id/technology-blog-sap)
* [sap btp](/t5/tag/sap%20btp/tg-p/board-id/technology-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-api-management-apis-and-revisions%2Fba-p%2F13568943%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday
* [What’s new in Mobile development kit client 25.9](/t5/technology-blog-posts-by-sap/what-s-new-in-mobile-development-kit-client-25-9/ba-p/14227370)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Thursday
* [Building SaaS Products on SAP BTP](/t5/technology-blog-posts-by-members/building-saas-products-on-sap-btp/ba-p/14231929)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Tuesday
* [Q3 2025 Quarterly Release Highlights: SAP BTP Security and Identity & Access Management](/t5/technology-blog-posts-...