---
title: Status Handling in Opportunities
url: https://blogs.sap.com/2022/12/30/status-handling-in-opportunities/
source: SAP Blogs
date: 2022-12-31
fetch_date: 2025-10-04T02:47:31.347621
---

# Status Handling in Opportunities

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* Status Handling in Opportunities

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/12605&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Status Handling in Opportunities](/t5/crm-and-cx-blog-posts-by-sap/status-handling-in-opportunities/ba-p/13536162)

![marcus_echter](https://avatars.profile.sap.com/c/6/idc6b650ae5b25e2f1764335e0e42a054c92d5203e167a5f57e7eaec20821b7b87_small.jpeg "marcus_echter")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[marcus\_echter](https://community.sap.com/t5/user/viewprofilepage/user-id/192478)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=12605)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/12605)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13536162)

‎2022 Dec 30
5:38 PM

[9
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/12605/tab/all-users "Click here to see who gave kudos to this post.")

3,392

* SAP Managed Tags
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)
* [SAP Cloud for Customer core applications](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520for%2520Customer%2520core%2520applications/pd-p/67837800100800004276)
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)

* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)
* [SAP Cloud for Customer core applications

  SAP Cloud for Customer](/t5/c-khhcw49343/SAP%2BCloud%2Bfor%2BCustomer%2Bcore%2Bapplications/pd-p/67837800100800004276)

View products (3)

When dealing with opportunities, status management is an important way to keep track of your deal progress. SAP Cloud for Customer (C4C) offers 2 approaches to handling statuses in opportunities - standard and custom status handling. This blog provides insights into both approaches.

## Standard Status Handling

C4C comes with a predefined status schema with fixed status values and transitions. The status values are the following:

* Open

* In Process

* Stopped

* Won

* Lost

These status values are pre-defined and cannot be changed or extended. The following status transitions are possible:

* Open -> In Process / Won / Lost

* In Process -> Open / Won / Lost / Stopped

* Won -> In Process

* Lost -> In Process

* Stopped -> In Process / Won / Lost

These status transitions are fixed as well and can only be performed via dedicated actions (e.g. "Set as In Process", "Set as Lost" etc.). Please note that the standard status field on the opportunity header cannot be directly edited.

![](/legacyfs/online/storage/blog_attachments/2022/12/status-2.jpg)

Standard statuses and transitions in opportunities

In addition to the status a reason can be maintained as to why a certain status has been set, e.g. "Lost to Competition" for the lost status. These reasons can be maintained via finetuning option "Opportunities-Reasons" and assigned to the respective status via option "Opportunities-Assignment of Reasons". The system comes with various pre-configured reasons and a key user can maintain custom reasons starting with "Z\*". As a best practice it is recommended to maintain reasons at least for lost and won opportunities in order to analyze success and failure of deal conversions.

![](/legacyfs/online/storage/blog_attachments/2022/12/reasons.jpg)

Reason why a status has been set

Once an opportunity has been set to won or lost, the fields "Probability", "Weighted Value" and "Close Date" are updated accordingly.

## Custom Status Handling

Another option of handling oppy statuses is via a custom status scheme. This is the preferred method in case a customer wants to use tailored deal statuses and transitions. A custom status schema can be defined for a certain document type via finetuning option "Opportunities-Maintain Custom Status". If no custom status schema exists for the selected document type, the system will default to the standard status schema as described above. Each value within a custom status schema needs to start with "Z\*" and should be assigned to a corresponding standard lifecycle status. Via this assignment the system derives possible status transitions, assigned reasons and field value updates as mentioned above.

![](/legacyfs/online/storage/blog_attachments/2022/12/custom_status.jpg)

Custom status schema maintenance

After configuring these options the sales rep can visualize and adjust the custom status via a dedicated field “Custom Status”. Possible Status transitions are honored as this field only shows values which can be reached from the current custom status. It should be emphasized that status transitions are directly maintained within the field “Custom Status” as opposed to executing an action in the standard status handling option. Neither the standard actions for status transitions nor the standard status field on opportunity header are available for a document type with a configured custom status schema.

![](/legacyfs/online/storage/blog_attachments/2022/12/custom_status_usage.jpg)

Custom status selection

This summarizes the different options for opportunity status handling in C4C.

Labels

* [Product Updates](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap/label-name/product%20updates)

* [custom\_status](/t5/tag/custom_status/tg-p/board-id/crm-blog-sap)
* [deal](/t5/tag/deal/tg-p/board-id/crm-blog-sap)
* [opportunity](/t5/tag/opportunity/tg-p/board-id/crm-blog-sap)
* [opportunity\_status](/t5/tag/opportunity_status/tg-p/board-id/crm-blog-sap)
* [Status](/t5/tag/Status/tg-p/board-id/crm-blog-sap)
* [status\_handling](/t5/tag/status_handling/tg-p/board-id/crm-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-sap%2Fstatus-handling-in-opportunities%2Fba-p%2F13536162%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [AI-Powered Dispute Management with SAP Enterprise Service Management (ESM) and S/4HANA Cloud](/t5/crm-and-cx-blog-posts-by-members/ai-powered-dispute-management-with-sap-enterprise-service-management-esm/ba-p/14231169)
  in [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)  yesterday
* [Data Transfer Tool](/t5/crm-and-cx-blog-posts-by-sap/data-transfer-tool/ba-p/14228496)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  Tuesday
* [Leveraging Asynchronous Request-Reply Pattern for Order Management Fou...