---
title: CAPのTips(外部APIの呼び出し、素のExpressを利用する)
url: https://blogs.sap.com/2022/12/03/cap%e3%81%aetips%e5%a4%96%e9%83%a8api%e3%81%ae%e5%91%bc%e3%81%b3%e5%87%ba%e3%81%97%e3%80%81%e7%b4%a0%e3%81%aeexpress%e3%82%92%e5%88%a9%e7%94%a8%e3%81%99%e3%82%8b/
source: SAP Blogs
date: 2022-12-04
fetch_date: 2025-10-04T00:28:45.576637
---

# CAPのTips(外部APIの呼び出し、素のExpressを利用する)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CAPのTips(外部APIの呼び出し、素のExpressを利用する)

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162842&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CAPのTips(外部APIの呼び出し、素のExpressを利用する)](/t5/technology-blog-posts-by-members/cap%E3%81%AEtips-%E5%A4%96%E9%83%A8api%E3%81%AE%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%97-%E7%B4%A0%E3%81%AEexpress%E3%82%92%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B/ba-p/13566058)

![yasuyukiuno](https://avatars.profile.sap.com/5/b/id5ba93ce241016316bb8b5d52868b46b52dc51dbf06a3799256fdbf635ab6df01_small.jpeg "yasuyukiuno")

[yasuyukiuno](https://community.sap.com/t5/user/viewprofilepage/user-id/557133)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162842)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162842)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566058)

‎2022 Dec 03
6:33 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162842/tab/all-users "Click here to see who gave kudos to this post.")

2,646

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (1)

この記事は [SAP Advent Calendar 2022](https://adventar.org/calendars/7484) の12月4日分の記事として執筆しています。

日本語のCAP情報が不足していると感じたため、本記事ではCAP初心者向けのTipsや参考情報を紹介したいと思います。

## CAPについて

SAP Cloud Application Programing Modelとは、サーバサイドアプリケーションを作成するためのフレームワークであり、簡単にODataサービスを作成することができます。
Fiori ElementsやUI5の相棒として使われます。

なお、CAPはNode.jsで開発するか、Javaで開発するかを選択することができますが、本記事ではNode.jsを選択することとします。

## CAPの使い方(基本)

CAPの最もオーソドックスな使い方は、HANA Cloud内のテーブルを読み書きするためのODataサービスを作成する。
ということになります。

下記の記事やチュートリアルを参考にすると良いでしょう。

<https://qiita.com/tami/items/d1b69a93da14e288faf2>

<https://developers.sap.com/tutorials/appstudio-cap-app.html>

## 外部APIを呼び出す

外部のOData APIを呼び出すケースも考えられます。

例えばS/4HANAの拡張アプリケーションをUI5+CAPで作成する場合には、アプリからはHANA Cloudの読み書きができるだけでは不十分で、S/4HANAのAPIも呼び出す必要があるでしょう。

下記のチュートリアルが参考になります。

<https://developers.sap.com/tutorials/btp-app-ext-service-add-consumption.html>

## Expressを利用する

Node.jsでWebアプリケーションを作成するときに最もよく使われるフレームワークがExpressです。

そもそもCAPはExpress上で動いているのですが、素のExpressを利用したくなることがあります。

CAPの標準機能だけではどのように実装すれば良いかわからない場合があったとしても、ExpressはWeb上にサンプルコードや参考情報が非常に多く、大抵のことはできるようになるでしょう。

例えばエクセルやCSVをアップロードして、サーバ側で処理してDBに格納するなどもExpressであれば簡単です。

Expressを利用するには、server.jsという名前でファイル作成し、srv直下に置くだけで利用できます。

![](/legacyfs/online/storage/blog_attachments/2022/12/cap-server.png)

中身は下記のようにして下さい。

<https://<ホスト名>/endpoint> や [https://<ホスト名>/endpoint2にブラウザでアクセスすると、Expressのルーティングが有効になっていることを確認できます。](https://<ホスト名>/endpoint2%E3%81%AB%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%A7%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%99%E3%82%8B%E3%81%A8%E3%80%81Express%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%8C%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E3%81%93%E3%81%A8%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82)

もちろん、server.jsのソースコード上部で必要なモジュールをどんどんrequireし、様々なNode.js向けのモジュール(ライブラリ)を活用した複雑な処理を実装することが可能です。

```
const cds = require('@sap/cds');

cds.on('bootstrap', app => {

	app.post('/endpoint', function(req, res, next) {

		// express handler logic here.

		res.status(202).send("OK");

	});

	app.get('/endpoint', function(req, res, next) {

		// express handler logic here.

		res.status(202).send("OK");

	});

	app.get('/endpoint2', function(req, res, next) {

		// express handler logic here.

		res.send("OKです");

	});

});

module.exports = cds.server;
```

## おわりに

以上、CAPのチュートリアルから少し踏み込んで、実案件で出てきそうなTipsについて紹介しました。

簡単にODataが作れて、自由度の高いサーバ(素のExpress併用)としても使えて、CAPは非常に使い勝手が良いと感じています。これまでCAPを触ったことが無い方も是非チャレンジしてみて下さい。

* [Node.js](/t5/tag/Node.js/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcap%25E3%2581%25AEtips-%25E5%25A4%2596%25E9%2583%25A8api%25E3%2581%25AE%25E5%2591%25BC%25E3%2581%25B3%25E5%2587%25BA%25E3%2581%2597-%25E7%25B4%25A0%25E3%2581%25AEexpress%25E3%2582%2592%25E5%2588%25A9%25E7%2594%25A8%25E3%2581%2599%25E3%2582%258B%2Fba-p%2F13566058%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![MioYasutake](https://avatars.profile.sap.com/5/e/id5e79c604027d7add255f696da403a5a6dc6fa0244486f41819b07572e8c1330c_small.jpeg "MioYasutake")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") MioYasutake](/t5/user/viewprofilepage/user-id/789) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")  Sharathmg](/t5/user/viewprofilepage/user-id/174516) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewprofilepage/user-id/197587) | 3 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f71...