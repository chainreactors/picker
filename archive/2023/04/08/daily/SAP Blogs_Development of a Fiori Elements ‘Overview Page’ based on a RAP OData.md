---
title: Development of a Fiori Elements ‘Overview Page’ based on a RAP OData
url: https://blogs.sap.com/2023/04/07/development-of-a-fiori-elements-overview-page-based-on-a-rap-odata/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:08.120542
---

# Development of a Fiori Elements ‘Overview Page’ based on a RAP OData

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Development of a Fiori Elements 'Overview Page' ba...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163496&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Development of a Fiori Elements 'Overview Page' based on a RAP OData](/t5/technology-blog-posts-by-members/development-of-a-fiori-elements-overview-page-based-on-a-rap-odata/ba-p/13570146)

![Xaver](https://avatars.profile.sap.com/9/2/id92fb643205e47dc354d3ed42a8881f713559a9ae825b88ab1756235f5d9aae85_small.jpeg "Xaver")

[Xaver](https://community.sap.com/t5/user/viewprofilepage/user-id/164835)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163496)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163496)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570146)

‎2023 Apr 07
9:36 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163496/tab/all-users "Click here to see who gave kudos to this post.")

3,907

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

I was curious on how to best implement an Fiori Elements 'Overview Page' Layout based on an OData Service exposed by our SAP BTP, ABAP Environment. After a little "googling" I found several Articles, Blogs, or UI5 Extensions Guides about Overview Pages but no concrete Guide on what the necessary Steps are to create a executable App. Here are the steps I found with some trial and error on how to create a Fiori Elements Overview Page based on a RAP-based OData V2 Service.

**Necessary Technical Objects**

A Service Binding wich exposes an UI - V2 OData Service, **instead** of an UI - V4 OData which is used for List-Object Page Apps.

 *I wasn't able to get it running with UI - V4 Odata, maybe this isnt supported yet?*

**Steps**

1. I use the BAS Template Generator to select the Overview page Template.![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05-16_57_28-fiori-SAP-Business-Application-Studio-und-1-weitere-Seite-Geschaftlich-–-Mic.png)

2. I select my relevant System and OData V2 Service

3. ![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05-16_58_24-fiori-SAP-Business-Application-Studio-und-1-weitere-Seite-Geschaftlich-–-Mic.png)And which Entity is the MainEntity where the Filter will be applied on![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05-16_59_55-fiori-SAP-Business-Application-Studio-und-1-weitere-Seite-Geschaftlich-–-Mic.png)

4. and then let it generate.

5. This will return an empty Overview Page.![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05-17_11_08-Test-und-1-weitere-Seite-Geschaftlich-–-Microsoft​-Edge.png)

6. Using the Information shared in the UI5 SDK Article for [Fiori Elements Extension Overview Page](https://sapui5.hana.ondemand.com/#/topic/f194b411027e4402a0be0537fa7b803b) I was able to extend the manifest.json and add my first Table into the Overview Page.

```
"sap.ovp": {

    "globalFilterModel": "mainModel",

    "globalFilterEntityType": "<<<YourEntitySetHere>>>",

    "containerLayout": "resizable",

    "enableLiveFilter": true,

    "considerAnalyticalParameters": false,

    "cards": {

      "<<<YourCardName>>>": {

        "settings": {

          "addODataSelect": true,

          "entitySet": "<<<YourEntitySetHere>>>",

          "listFlavor": "standard",

          "listType": "extended",

          "showLineItemDetail": true,

          "sortBy": "<<<Field>>>",

          "sortOrder": "descending",

          "subTitle": "{{cardSubtitle}}",

          "title": "{{cardTitle}}",

          "defaultSpan": "auto"

        },

        "model": "mainModel",

        "template": "sap.ovp.cards.table"

      }

    },

    "disableErrorPage": false,

    "smartVariantRequired": true,

    "showBasicSearch": true,

    "refreshIntervalInMinutes": 5,

    "bHeaderExpanded": true
```

This is my current Endresult, defintly still a work in progress, but better than a blank Overview Page. ![:face_with_tongue:](/html/@0B5602356D2E1D4CD032611145E78D9C/emoticons/1f61b.png ":face_with_tongue:")

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-05-17_19_48-Overview-on-V2-und-2-weitere-Seiten-Geschaftlich-–-Microsoft​-Edge.png)

My Current Overview Page

Its definitely cool to finally have a visible result, but it took alot of trial and error specifically with the OData - V2 and then with what coding is relevant in the Manifest.json. I would appreciate similar to the RAP feature Showcase, also a detailed Showcase for the Overview Page and its possibilities.

Thanks for reading, I will try and keep updating if I try additional Tricks in my Overview Page. ![:slightly_smiling_face:](/html/@AB1AFF728742E596A69993DB64EECECF/emoticons/1f642.png ":slightly_smiling_face:") What have your experiences been with the Overview Page?

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fdevelopment-of-a-fiori-elements-overview-page-based-on-a-rap-odata%2Fba-p%2F13570146%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Optimizing Accessibility for Visual Impairment](/t5/technology-blog-posts-by-sap/optimizing-accessibility-for-visual-impairment/ba-p/14234652)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-memb...