---
title: Status search in SAP S4/HANA for Customer Management
url: https://blogs.sap.com/2023/07/27/status-search-in-sap-s4-hana-for-customer-management/
source: SAP Blogs
date: 2023-07-28
fetch_date: 2025-10-04T11:54:06.228504
---

# Status search in SAP S4/HANA for Customer Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* Status search in SAP S/4HANA for Customer Manageme...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6355&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Status search in SAP S/4HANA for Customer Management](/t5/crm-and-cx-blog-posts-by-members/status-search-in-sap-s-4hana-for-customer-management/ba-p/13568645)

![pjedrasiewicz](https://avatars.profile.sap.com/3/f/id3f1b644251e6d78b1cb23932644d1ecb55d00621d0b7b74535ba25e6f1f1dd1d_small.jpeg "pjedrasiewicz")

[pjedrasiewicz](https://community.sap.com/t5/user/viewprofilepage/user-id/153379)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6355)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6355)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568645)

‎2023 Jul 27
11:03 PM

0
Kudos

3,661

* SAP Managed Tags
* [SAP CRM on-demand solution](https://community.sap.com/t5/c-khhcw49343/SAP%2520CRM%2520on-demand%2520solution/pd-p/01200314690800000159)
* [SAP Customer Relationship Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Relationship%2520Management/pd-p/01200615320800000556)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [CRM Sales](https://community.sap.com/t5/c-khhcw49343/CRM%2520Sales/pd-p/637115821191636376336141602158512)
* [CRM Service](https://community.sap.com/t5/c-khhcw49343/CRM%2520Service/pd-p/336839465795980684603250734763165)
* [CRM WebClient UI](https://community.sap.com/t5/c-khhcw49343/CRM%2520WebClient%2520UI/pd-p/216479123645680540588211456657763)

* [SAP CRM on-demand solution

  SAP Customer Relationship Management](/t5/c-khhcw49343/SAP%2BCRM%2Bon-demand%2Bsolution/pd-p/01200314690800000159)
* [SAP Customer Relationship Management

  SAP Customer Relationship Management](/t5/c-khhcw49343/SAP%2BCustomer%2BRelationship%2BManagement/pd-p/01200615320800000556)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [CRM Sales

  Software Product Function](/t5/c-khhcw49343/CRM%2BSales/pd-p/637115821191636376336141602158512)
* [CRM Service

  Software Product Function](/t5/c-khhcw49343/CRM%2BService/pd-p/336839465795980684603250734763165)
* [CRM WebClient UI

  Software Product Function](/t5/c-khhcw49343/CRM%2BWebClient%2BUI/pd-p/216479123645680540588211456657763)

View products (6)

### The intention of this blog is to propose an end-to-end solution for search documents by status in SAP S/4HANA for Customer Management.

![](/legacyfs/online/storage/blog_attachments/2023/07/0-to-be.png)

Search Customer Management by custom Lifecycle Status

# Requirements

## Functional

Enable search by status on Opportunity and Service Request search screens in SAP S/4HANA for Customer Management.

Display status description on Opportunity and Service Request search result screens in SAP S/4HANA for Customer Management.

## Technical

Optimize performance of 1Order status search by avoiding joining on CRM\_JEST status table in S/4HANA CM.

# Audience

Functional and Technical consultants.

No coding skills are needed.

# How it was in CRM 7.0

Status search was available on Opportunity and Service Request screens as standard field STATUS\_COMMON which provided a concatenated combination of user status and status profile for all process types in the system. From a technical point of view, the search required either to JOIN on CRM\_JEST and CRMD\_ORDER\_INDEX tables or just using view CRMV\_INDEX\_JEST which considered the tables. The approach was correct and available almost out of the box but it had two side effects:

+ Status search dropdown could contain duplicates which were important for results. For example visible twice status 'Open' could belong to status profile ZOPPT1 status E0001 'Open' and status profile ZOPPT2 status E0002 'Open'. When a user selected the first 'Open' status then only documents having status profile ZOPPT1 were displayed. (of course, the workaround was to enable key display in all dropdowns across the system but not every user was happy about it).

+ Performance was not optimal because each status-related query ended with at least one SQL join with CRM\_JEST table.

# How it is in S/4HANA for Customer Management

The status search known from CRM 7.0 is no longer available. Field STATUS\_COMMON is still technically available but it is obsolete and the search engine is not working out of the box (see note <https://me.sap.com/notes/2768599>).

There is a new data model which gave up CRMD\_ORDER\_INDEX (and join on CRM\_JEST) for CRMS4D\_OPPT\_H and CRMS4D\_SERV\_H tables. Luckily, a new version of the system brought us a new possibility which is the so-called Lifecycle Status (see note <https://me.sap.com/notes/3074858>). Customization is available in tcode SM34 cluster view CRMS4VC\_STAT\_LC. Requires two steps:

+ Definition of the Status Lifecycle (4 characters length field),

+ Mapping Status Lifecycle values with Status Profile, User Status, and placeholder of the Status Lifecycle (corresponding field name in CRMS4D\_OPPT\_H or CRMS4D\_SERV\_H table where the new status will be saved). As a logical consequence, there can only be one Status Lifecycle at a time for one document.

The concept is well explained in the blog post: <https://blogs.sap.com/2018/03/08/one-order-status-component-in-s4hana-for-customer-management/>

# How could it be

Despite the fact that the above blog is amazing, some extra steps still must be performed to provide a fully working solution:

+ Customization of the Status Lifecycle mapping can be time-consuming due to the amount and complexity of status profiles for multiple process types. It would be nice to have an automatic or semi-automatic customization generator,

+ Lifecycle Status Description column on the Opportunity search results screen is only showing standard Lifecycle Statuses (A-F). In the case of custom status, the field under the column is blank.

# Proposed solution:

1. Use the below report to validate status profile customizing and to generate Status Lifecycle customizing by Status code (TXT04) or Status description (TXT30) of status profiles resolved from process types

![](/legacyfs/online/storage/blog_attachments/2023/07/1-status-profile.png)

1.1 Go to tcode SE38, create new report ZCRM\_GENERATE\_STATUS\_LIFECYCLE

![](/legacyfs/online/storage/blog_attachments/2023/07/2-se38-create.png)

1.2 Paste code from the code snippet, save and activate. NOTE: Report can only insert new entries in Status Lifecycle customizing, it has not update/delete statements.

![](/legacyfs/online/storage/blog_attachments/2023/07/3-se38-activate.png)

```
*&---------------------------------------------------------------------*

*& Report ZCRM_GENERATE_STATUS_LIFECYCLE

*&---------------------------------------------------------------------*

*& Report to validate status profile customization in TJ30T table

*& and generate Status Lifecycle based on status profiles resolved

*& from provided proc...