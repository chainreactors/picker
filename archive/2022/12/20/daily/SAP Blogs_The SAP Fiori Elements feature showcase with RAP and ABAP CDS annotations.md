---
title: The SAP Fiori Elements feature showcase with RAP and ABAP CDS annotations
url: https://blogs.sap.com/2022/12/19/the-sap-fiori-elements-feature-showcase-with-rap-and-abap-cds-annotations/
source: SAP Blogs
date: 2022-12-20
fetch_date: 2025-10-04T01:58:46.071849
---

# The SAP Fiori Elements feature showcase with RAP and ABAP CDS annotations

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* The SAP Fiori Elements feature showcase with RAP a...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158613&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The SAP Fiori Elements feature showcase with RAP and ABAP CDS annotations](/t5/technology-blog-posts-by-sap/the-sap-fiori-elements-feature-showcase-with-rap-and-abap-cds-annotations/ba-p/13552411)

![JessieCheah](https://avatars.profile.sap.com/d/d/iddd2c6d60341df2c8d497c995b9a01c1b8b901a02af484318d378b5f01d1f9596_small.jpeg "JessieCheah")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[JessieCheah](https://community.sap.com/t5/user/viewprofilepage/user-id/46342)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158613)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158613)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552411)

‎2022 Dec 19
7:07 PM

[79
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158613/tab/all-users "Click here to see who gave kudos to this post.")

39,470

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (3)

*Updated 6th January 2023. For all those who are more visually stimulated, I have updated the blog post with a video**posted on the SAP Developers YouTube channel on how to use the app.*

*Updated 23 February 2023. [Release 2302](https://blogs.sap.com/2023/02/23/the-sap-fiori-elements-feature-showcase-with-rap-and-abap-cds-whats-new-in-release-2302/)*

*Updated 20 September 2023. [Release 2308](https://blogs.sap.com/2023/09/20/the-sap-fiori-elements-feature-showcase-with-rap-whats-new-in-release-2308/)*

*Updated 20 May 2024. [Release 2402](https://community.sap.com/t5/technology-blogs-by-sap/sap-fiori-elements-feature-showcase-app-with-rap-for-release-2402-why-is-it/ba-p/13610549)*

### What it is, in a nutshell

Are you a newbie in the world of ABAP CDS, SAP Fiori Elements and CDS annotations? Or perhaps you are a seasoned developer but just can't seem to figure out how to implement a UI feature in your SAP Fiori application?

With the [SAP Fiori Elements Feature Showcase App for RAP](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase) you get a reference technical app that showcases the SAP Fiori Elements UI features which can be implemented using ABAP CDS annotations. The feature showcase app is developed using the ABAP RESTful Application Programming Model (RAP) for oData V4 and is transactional- and draft- enabled.

![](/legacyfs/online/storage/blog_attachments/2022/12/app-list.jpg)Feature Showcase App - List Report

 ![](/legacyfs/online/storage/blog_attachments/2022/12/app-objectpage.jpg)Feature Showcase App - Object Page

To use the feature showcase app, follow the instructions in the GitHub [README](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/blob/main/README.md) and start the service binding app preview. When you see a feature that you would like to implement, copy or take note of the search term (e.g., **#SearchTermExample**) and perform a search in the [Wiki guide](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide). You will be presented with

+ a short description of the feature,

+ code snippets and where to find them in the source code,

+ and in some cases, a link to the official RAP documentation for more information.

Check out the video below to see an example on how to use the app.

### Where can I run the app?

The feature showcase app is designed to be run on *SAP BTP**, ABAP Environment* and *SAP S/4HANA Cloud, ABAP Environment* systems, and also ABAP Platform systems like *SAP S/4HANA, on-premise edition* or *SAP S/4HANA Cloud, private edition*. Just choose the corresponding branch from the [GitHub repository](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase) and follow the instructions in the README.

If you don't have a system available, you could also try it out in the *SAP BTP ABAP Environment Trial*systems. Check out this [tutorial](https://developers.sap.com/tutorials/abap-environment-trial-onboarding.html) on how to get a trial user.

### Any subsequent releases?

Since SAP Fiori Elements and ABAP CDS annotations are still growing, we intend to include new features in the feature showcase app in releases corresponding to the SAP BTP, ABAP Environment (aka Steampunk) releases. So remember to watch/follow the feature showcase GitHub repository to get the newest releases. As an alternative, follow my profile here in SAP Community and don't forget to leave your comments and questions.

Also check out the [feature showcase app built with CAP CDS annotation](https://blogs.sap.com/2021/12/07/the-sap-fiori-elements-feature-showcase-with-cap-cds-annotations/)!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [abap cds annotations](/t5/tag/abap%20cds%20annotations/tg-p/board-id/technology-blog-sap)
* [feature showcase app](/t5/tag/feature%20showcase%20app/tg-p/board-id/technology-blog-sap)
* [odata v4](/t5/tag/odata%20v4/tg-p/board-id/technology-blog-sap)
* [RAP](/t5/tag/RAP/tg-p/board-id/technology-blog-sap)
* [ui annotations](/t5/tag/ui%20annotations/tg-p/board-id/technology-blog-sap)

13 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fthe-sap-fiori-elements-feature-showcase-with-rap-and-abap-cds-annotations%2Fba-p%2F13552411%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Goodbye Vibe-Coding: The Future of SAP Development with AI + Low-Code](/t5/technology-blog-posts-by-members/goodbye-vibe-coding-the-future-of-sap-development-with-ai-low-code/ba-p/14223384)
  in [Technology Blog Posts by Member...