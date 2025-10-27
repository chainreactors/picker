---
title: Flexible Programming Modelで「Fiori elements or フリースタイル」の壁を打ち破る
url: https://blogs.sap.com/2023/05/11/putting-to-an-end-to-fiori-elements-or-freestyle-discussion-with-flexible-programming-model/
source: SAP Blogs
date: 2023-05-12
fetch_date: 2025-10-04T11:39:23.168499
---

# Flexible Programming Modelで「Fiori elements or フリースタイル」の壁を打ち破る

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Flexible Programming Modelで「Fiori elements or フリース...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160562&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Flexible Programming Modelで「Fiori elements or フリースタイル」の壁を打ち破る](/t5/technology-blog-posts-by-members/flexible-programming-model%E3%81%A7-fiori-elements-or-%E3%83%95%E3%83%AA%E3%83%BC%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB-%E3%81%AE%E5%A3%81%E3%82%92%E6%89%93%E3%81%A1%E7%A0%B4%E3%82%8B/ba-p/13553116)

![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[MioYasutake](https://community.sap.com/t5/user/viewprofilepage/user-id/789)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160562)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160562)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553116)

‎2023 May 11
9:48 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160562/tab/all-users "Click here to see who gave kudos to this post.")

1,496

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP Inside Track](https://community.sap.com/t5/c-khhcw49343/SAP%2520Inside%2520Track/pd-p/72472722867005232775920452375500)

* [SAP Inside Track

  Event](/t5/c-khhcw49343/SAP%2BInside%2BTrack/pd-p/72472722867005232775920452375500)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (2)

## はじめに

この記事は、今年の [SAP Inside Track Tokyo 2023](https://blogs.sap.com/2022/11/17/sap-inside-track-tokyo-2023/) で発表した内容をベースとしています。

私はWeek2のDigital Transformation with SAP S/4HANA & AIのトラックで、Flexible Programming Modelで「Fiori elements or フリースタイル」の壁を打ち破るというタイトルで登壇しました。

##

## サマリ

* Flexible Programming ModelはOData V4ベースのFioriアプリを作成するときに使える開発手法

* Fiori elementsのような見た目を提供しながら比較的自由な拡張ができるという特徴がある

* Flexible Programming Modelを使うことで嬉しいのは、開発を始める前に「Fiori elementsか、フリースタイルか」で悩まなくてよいところ

* Fiori elementsにフリースタイルのページやセクションを組み込んだり、フリースタイルのアプリにFIori elementsのページや部品を組み込むことができる

![](/legacyfs/online/storage/blog_attachments/2023/05/fpm-overview.png)

Flexible Programming Modelの概要

![](/legacyfs/online/storage/blog_attachments/2023/05/Fiori-elementsにフリースタイルを組み込む-2.png)

Fiori elementsにフリースタイルを組み込む例

![](/legacyfs/online/storage/blog_attachments/2023/05/フリースタイルにFiori-elementsを組み込む-2.png)

フリースタイルにFiori elementsを組み込む例

## セッション内容

1. Flexible Programming Modelとは

2. Flexible Programming Modelは何がうれしいか

3. Flexible Programming Modelが提供する3本柱

4. どんなことができるか

5. Flexible Programming Modelを使うために必要なこと

* 資料は[こちら](https://speakerdeck.com/miyasuta/sittokyo2023-flexible-programming-modelde-fiori-elements-or-hurisutairu-nobi-woda-tipo-ru)

* 当日の録画は[こちら](https://youtu.be/0Lrcn7kxQfQ?t=5258)

## おわりに

セッションの中ではよいところばかりに焦点を当てていましたが、Flexible Programming Modelを実際に使うとなるとまだハードルが高いと感じています。主な理由はリソースの少なさです。以下の参考リンクに紹介したようなドキュメントやYoutubeの動画は存在していますが、SAP Communityにはまだ情報が少ないのが現状です。

ただ、ありがたいことにOData V4のFiori elementsテンプレートはそのままFlexible Programming Modelに対応しています。初めから「Flexible Programming Modelを使うぞ」と意気込んで始めるというよりは、Fiori elementsのテンプレートで初めて、拡張したい要件が出てきたらドキュメントなどで調べて足していく、という使い方がよいのではないかと考えています。

## 参考リンク

* ドキュメント：[Flexible Programming Model Explorer](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/overview/introduction)

* ブログ： [Leverage the flexible programming model to extend your SAP Fiori elements apps for OData V4](https://blogs.sap.com/2021/08/19/leverage-the-flexible-programming-model-to-extend-your-sap-fiori-elements-apps-for-odata-v4/)

* ブログ：[Creating a custom form entry page with Flexible Programming Model](https://blogs.sap.com/2023/01/18/creating-a-custom-form-entry-page-with-flexible-programming-model/)

* Youtube：[SAP Fiori elements Flexible Programming](https://www.youtube.com/watch?v=oqvHN8tbRRw&list=PLo17W6sWsxWM0yervb4VUxglVAop34_DQ)

* TechEd 2022ハンズオン：[DT181 – Boost Your Productivity in Developing SAP Fiori Apps](https://github.com/SAP-samples/teched2022-DT181)

* [chillSAP](/t5/tag/chillSAP/tg-p/board-id/technology-blog-members)
* [flexible programming model](/t5/tag/flexible%20programming%20model/tg-p/board-id/technology-blog-members)
* [sitTokyo](/t5/tag/sitTokyo/tg-p/board-id/technology-blog-members)
* [sitTokyoOrganizer](/t5/tag/sitTokyoOrganizer/tg-p/board-id/technology-blog-members)
* [sitTokyoSpeaker](/t5/tag/sitTokyoSpeaker/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fflexible-programming-model%25E3%2581%25A7-fiori-elements-or-%25E3%2583%2595%25E3%2583%25AA%25E3%2583%25BC%25E3%2582%25B9%25E3%2582%25BF%25E3%2582%25A4%25E3%2583%25AB-%25E3%2581%25AE%25E5%25A3%2581%25E3%2582%2592%25E6%2589%2593%25E3%2581%25A1%25E7%25A0%25B4%25E3%2582%258B%2Fba-p%2F13553116%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Optimizing Accessibility for Visual Impairment](/t5/technology-blog-posts-by-sap/optimizing-accessibility-for-visual-impairment/ba-p/14234652)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [how to mitigate "web.xml configuration file disclosure" for SAP crystal BO server BI Platform 4.2 SP](/t5/technology-q-a/how-to-mitigate-quot-web-xml-configuration-file-disclosure-quot-for-sap/qaq-p/14233378)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Thursday
* [Document Grounding: A (hidden) gem in SAP Business AI’s portfolio for smaller companies.](/t5/technology-blog-posts-by-sap/document-grounding-a-hidden-gem-in-sap-business-ai-s-portfolio-for-smaller/ba-p/14232864)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [5 Tips for Getting Started with the SAP Fiori for Web UI Kit](/t5/technology-blog-posts-by-sap/5-tips-for-getting-started-with-the-sap-fiori-for-web-ui-kit/ba-p/14232902)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a...