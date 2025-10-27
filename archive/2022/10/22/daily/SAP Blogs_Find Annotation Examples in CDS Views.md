---
title: Find Annotation Examples in CDS Views
url: https://blogs.sap.com/2022/10/21/find-annotation-examples-in-cds-views/
source: SAP Blogs
date: 2022-10-22
fetch_date: 2025-10-03T20:35:26.724856
---

# Find Annotation Examples in CDS Views

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Find Annotation Examples in CDS Views

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160459&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Find Annotation Examples in CDS Views](/t5/technology-blog-posts-by-members/find-annotation-examples-in-cds-views/ba-p/13552430)

![Attila](https://avatars.profile.sap.com/2/4/id246473302c6b9eb106958b8c0b692e2e4ab11c10b92a6fcca8fd067f23fd8101_small.jpeg "Attila")

[Attila](https://community.sap.com/t5/user/viewprofilepage/user-id/129182)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160459)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160459)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552430)

‎2022 Oct 21
9:32 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160459/tab/all-users "Click here to see who gave kudos to this post.")

3,209

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

View products (3)

## Purpose

Help developers to find CDS annotation examples, especially when this error message appears in **ADT: Text search services are not supported**, because it is not available / not configured in the backend.

I created it to help my students to find samples and for myself when dealing with the [many possible annotations](https://help.sap.com/docs/SAP_NETWEAVER_750/cc0c305d2fab47bd808adcad3ca7ee9d/630ce9b386b84e80bfade96779fbaeec.html?locale=en-US) listed on the SAP Help Site, which explain all the properties of them. Unfortunately samples for them are split across the multiple developer guides of the corresponding frameworks. Why not to see a real use case right in the system ?!

## Features

* Search for CDS header / field / parameter annotations

* Type ahead value help for annotations existing in the system within CDS Entities

* Opens ADT, when running embedded, otherwise shows Data Definition in a popup

## Usage

Run report **ZSAPDEV\_CDS\_FIND\_ANNO** in ADT / SE38 / SA38 / SE80 and start typing to find an annotation you're looking for.

![](/legacyfs/online/storage/blog_attachments/2022/10/SelScreen.gif)

Execute (F8), then select a CDS Entity and press the Show CDS button.

![](/legacyfs/online/storage/blog_attachments/2022/10/CDS-Annotation-List.gif)

In case You executed it in ADT, it will open a new Tab, otherwise the Data Definition Source code will be displayed in a  popup window.

![](/legacyfs/online/storage/blog_attachments/2022/10/CDS-in-ADT-1.gif)

CDS Opened in ADT

![](/legacyfs/online/storage/blog_attachments/2022/10/CDS-in-GUI.gif)

CDS Opened in GUI

## Installation

Install this repository using ABAPGit online / offline

<https://github.com/attilaberencsi/cdsfindanno>

You will find here a more interactive demo as well.

Tested on ABAP Platform 1909, and the same time [good bye](https://blogs.sap.com/2021/02/15/sap-abap-platform-1909-developer-edition-available-soon/), such tool cannot be developed in the Trial Cloud for fun.

I wish You a joyful CDS and Fiori Development !

:)

* [abapcds](/t5/tag/abapcds/tg-p/board-id/technology-blog-members)
* [CDS](/t5/tag/CDS/tg-p/board-id/technology-blog-members)
* [CDS Annotation](/t5/tag/CDS%20Annotation/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Ffind-annotation-examples-in-cds-views%2Fba-p%2F13552430%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  33m ago
* [Calculation View Features of 2025 QRC3](/t5/technology-blog-posts-by-sap/calculation-view-features-of-2025-qrc3/ba-p/14192411)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [🚀 The Universal Journal is Calling: Master the Evolution to S/4HANA Intelligence](/t5/technology-blog-posts-by-members/the-universal-journal-is-calling-master-the-evolution-to-s-4hana/ba-p/14229512)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [🚀 Mastering the Essentials: Your Journey into SAP S/4HANA Starts Here!](/t5/technology-blog-posts-by-members/mastering-the-essentials-your-journey-into-sap-s-4hana-starts-here/ba-p/14229489)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/...