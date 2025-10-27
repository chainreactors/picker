---
title: ui5-translator CLI tool
url: https://blogs.sap.com/2022/10/28/ui5-translator-cli-tool/
source: SAP Blogs
date: 2022-10-29
fetch_date: 2025-10-03T21:13:25.538363
---

# ui5-translator CLI tool

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ui5-translator CLI tool

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160950&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ui5-translator CLI tool](/t5/technology-blog-posts-by-members/ui5-translator-cli-tool/ba-p/13555408)

![facundo_ferrer2](https://avatars.profile.sap.com/d/a/idda48e7763d258293c2a226142430858bbfa5d042a96f18d4d9e9aee316200088_small.jpeg "facundo_ferrer2")

[facundo\_ferrer2](https://community.sap.com/t5/user/viewprofilepage/user-id/339285)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160950)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160950)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555408)

‎2022 Oct 28
7:02 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160950/tab/all-users "Click here to see who gave kudos to this post.")

2,422

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Translation Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Translation%2520Hub/pd-p/73555000100800000086)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Translation Hub

  SAP Translation Hub](/t5/c-khhcw49343/SAP%2BTranslation%2BHub/pd-p/73555000100800000086)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (3)

Hi everyone!

I've always found it frustrating to have to maintain several i18n files by hand. Maybe when you need to support 2 languages is not a big deal. But when you have to support 4 or more, you can easily add the entry on the main i18n file but forget to update the said entry on the other i18n languages.

With this in mind I created a nodejs based CLI ui5-translator tool to ease the developer experience.

Just to give a demonstration of it's features I created a test project. project2 using the basic Project Template on BAS.

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-26-144426.png)

To begin, run the installer on the root of the UI5 Application project.
The CLI tool will look for the i18n file on ./webapp/i18n/i18n.properties

```
npm install -g @facuferrer86/ui5-translator
```

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-26-144541.png)
The CLI tools expects a list of target languages.
Also the source i18n file should be English.

```
ui5-translator spanish,german,italian
```

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-26-144838.png)

Note: The CLI tool looks for translations on 3 sources:

1. Previously created i18n files with already translated entries.

2. SAP Translation HUB.

3. Google Translator.

If it can't find the prior it will look it on the following source.

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-26-144926.png)

All languages on iso639-2 are supported.

Please do share feedbacks or thoughts in a comment section and feel free to follow me for more content updates.

Also, do follow SAPUI5 environment Topic page (<https://community.sap.com/topics/ui5>)

If you are interested in building your own CLI tools on nodejs look at:

<https://dev.to/rushankhan1/build-a-cli-with-node-js-4jbi>

--Edit 20/07/2023

I updated the library.

To get the latest version simply do:

```
npm update -g @facuferrer86/ui5-translator
```

I removed the dependency on [https://www.npmjs.com/package/@vitalets/google-translate-api](https://www.npmjs.com/package/%40vitalets/google-translate-api) and replaced it with <https://www.npmjs.com/package/google-translate-api-x>

Also, all translations are now executed in bulk rather than in series. I was reaching a threshold of too many calls, so I now call once every 60 seconds. It's slower.. but effective.

14 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fui5-translator-cli-tool%2Fba-p%2F13555408%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  35m ago
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  an hour ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  an hour ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Regarding update notifications for OSS note: 3594142](/t5/technology-q-a/regarding-update-notifications-for-oss-note-3594142/qaq-p/14233094)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/use...