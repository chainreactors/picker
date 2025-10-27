---
title: SAP Graphチュートリアルシリーズ：【パート2】はじめてのSAP Graphアプリ開発
url: https://blogs.sap.com/2022/12/29/part-2-hello-graph-write-your-first-sap-graph-application-ja/
source: SAP Blogs
date: 2022-12-30
fetch_date: 2025-10-04T02:44:43.972145
---

# SAP Graphチュートリアルシリーズ：【パート2】はじめてのSAP Graphアプリ開発

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Graphチュートリアルシリーズ：【パート2】はじめてのSAP Graphアプリ開発

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161253&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Graphチュートリアルシリーズ：【パート2】はじめてのSAP Graphアプリ開発](/t5/technology-blog-posts-by-sap/sap-graph%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E3%83%91%E3%83%BC%E3%83%882-%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AEsap-graph%E3%82%A2%E3%83%97%E3%83%AA%E9%96%8B%E7%99%BA/ba-p/13560296)

![yasuhira_chiba](https://avatars.profile.sap.com/6/6/id66ec93f258162a724ba2e787f7e22e05b2895e6575ff72005c9825ae6deb0159_small.jpeg "yasuhira_chiba")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[yasuhira\_chiba](https://community.sap.com/t5/user/viewprofilepage/user-id/750022)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161253)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161253)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560296)

‎2022 Dec 29
2:08 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161253/tab/all-users "Click here to see who gave kudos to this post.")

923

* SAP Managed Tags
* [SAP Graph](https://community.sap.com/t5/c-khhcw49343/SAP%2520Graph/pd-p/da20f5de-7c9f-47c9-b766-b98820e5be12)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Graph

  Topic](/t5/c-khhcw49343/SAP%2BGraph/pd-p/da20f5de-7c9f-47c9-b766-b98820e5be12)
* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)

View products (3)

## はじめに

本ブログシリーズは[SAP Graph Multi-Part Tutorial: Information Map](https://blogs.sap.com/2021/06/08/sap-graph-multi-part-tutorial-information-map/)の日本語翻訳です。簡潔な翻訳のために、いくつかの細かいニュアンスは削ぎ落としています。最新の正しい情報は翻訳元や[What’s New for SAP Graph](https://help.sap.com/docs/SAP_GRAPH/84bbf6acb5384861add4cb6939bef647/a509e6a5a1f64abeb95b8ceb348ad939.html?locale=en-US)をご参照ください。

#### ブログシリーズ一覧

* インフォメーションマップ：SAP Graphチュートリアルシリーズ（[日本語翻訳版](https://blogs.sap.com/2022/06/22/sap-graph-multi-part-tutorial-information-map-ja/)）（[オリジナル英語版](https://blogs.sap.com/2021/06/08/sap-graph-multi-part-tutorial-information-map/)）

  + パート1：SAP Graphのイントロダクション（[日本語翻訳版](https://blogs.sap.com/2022/06/23/part-1-introduction-to-sap-graph-ja/)）（[オリジナル英語版](https://blogs.sap.com/2021/06/08/part-1-introduction-to-sap-graph/)）

  + **パート2：はじめてのSAP Graphアプリ開発（日本語翻訳版）（[オリジナル英語版](https://blogs.sap.com/2021/06/15/part-2-hello-graph-write-your-first-sap-graph-application/)****）** <-このブログ

  + パート3：SAP Graphにおける認証認可の実装（日本語翻訳版）（[オリジナル英語版](https://blogs.sap.com/2021/06/25/part-3-use-sap-graph-securely-with-real-data-authentication/)）

  + パート4：SAP Graphとプロトコル（日本語翻訳版）（[オリジナル英語版](https://blogs.sap.com/2021/07/28/part-4-the-sap-graph-data-protocol/)）

  + パート5：SAP Graphと自前のデータの用意（日本語翻訳版）（[オリジナル英語版](https://blogs.sap.com/2022/01/18/part-5-use-sap-graph-with-your-own-data/)）

  + パート6：SAP GraphでBusiness Data Graphを作成（日本語翻訳版）（[オリジナル英語版](https://blogs.sap.com/2022/02/03/part-6-construct-an-sap-graph-business-data-graph/)）

  + パート7：SAP Graphにおけるキーマッピング(日本語翻訳版)（[オリジナル英語版](https://blogs.sap.com/2022/03/31/part-7-key-mapping-with-sap-graph/)）

Thanks stephanie.lewellen and chaimbendelac for your cool blogs and for allowing me to translate!

## 日本語訳

こんにちは！

このブログはSAP Graphチュートリアルシリーズの２つ目のブログです。

SAP Graphの紹介はこのチュートリアルシリーズの[パート1](https://blogs.sap.com/2022/06/23/part-1-introduction-to-sap-graph-ja/)、チュートリアルシリーズ全体の紹介は[インフォメーションマップ](https://blogs.sap.com/2022/06/22/sap-graph-multi-part-tutorial-information-map-ja/)を参照してください。

このチュートリアルシリーズのパート3では、古典的かつ初歩的なエンタープライズ拡張のWebアプリである下図の様な*list-details-navigate application*を開発します。

![](/legacyfs/online/storage/blog_attachments/2021/06/blog2_image1.png)

本ブログであるパート２では基本的なHello Worldアプリケーションを通じて要点を掴んで頂く事を目的としています。このチュートリアルでは予備知識は必要なく、SAP Graph開発者になるために必要なことは全てこのブログの中に書いてあります。ブログ中では[パート１](https://blogs.sap.com/2022/06/23/part-1-introduction-to-sap-graph-ja/)でも利用したSAP API Business Hub sandboxとして設定されたSAP Graphサーバーを再利用します。

### Node.jsの利用

今回のアプリケーションの構築には**Node.js**と**npm**を使用し、シンプルにするためにWebフレームワークのExpressを利用します。Node.jsとExpressに馴染みがない場合[この記事](https://developer.mozilla.org/ja/docs/Learn/Server-side/Express_Nodejs/Introduction)をお勧めします。この記事では、Node.jsの開発環境をWindows、MacOS、Linuxどれを使って居ても簡単にセットアップする方法についても説明しています。

お使いのコンピュータに何もインストールせずにクラウド上で開発したい場合、SAPはSAP Business Application Studioという素晴らしいクラウドベースの開発環境を提供しています。利用方法ついては、[このリンク](https://developers.sap.com/tutorials/appstudio-onboarding.html)を参照してください。このチュートリアルではお使いのコンピュータにNode.jsとnpmをインストールしたことを前提に進めていきます。

### package.jsonの設定

まずアプリケーション開発を行うフォルダ（ディレクトリ）を開き、package.jsonという名前のファイルを作成します。ファイルの中には以下を記述してください。

```
{

    "name": "hello-graph",

    "version": "0.0.0",

    "private": true,

    "dependencies": {

        "express": "4.17.1",

        "node-fetch": "2.6.1",

        "universal-cookie": "4.0.4"

    }

}
```

ファイルを保存後、コンソールから以下のコマンドを実行します。

```
npm install
```

node.js環境が適切にセットアップされていれば、このコマンドでnode\_modulesという新しいサブフォルダにライブラリがインストールされます。

次にnode\_modulesフォルダの隣にsrcというフォルダを作成します。このフォルダの中で開発を進めていきます。

### graph.js

まずsrc フォルダに graph.js と言う名前のファイルを作成します。このファイルは今後すべての SAP Graph チュートリアルやあなた自身のプロジェクトで、小さな変更を加えながら再利用することになります。このファイルには SAP Graph を使用するためのラッパーを提供するGraph というクラスが含まれています。今回は、get()関数を使ってデータを読み込む方法を紹介します。

以下のコードをファイルに貼り付けて保存してください。見ての通り非常にシンプルで、node-fetch パッケージを利用しています。

```
const fetch = require("node-fetch");

class Graph {

    async get(req, entity, params) {

        const url = `https://sandbox.api.sap.com/sapgraph/${entity}${params ? `?${params}` : ""}`;

        console.log(url) //for debugging

        const options = {

            method: "get",

            headers:{

                "Accept": "application/json",

                "apiKey": "your APIkey"

            }

        };

        const response = await fetch(url, options);

        console.log(`${response.status} (${response.statusText})`) // for debugging

        const json = await response.json();

        return json;

    }

}

module.exports = Graph;
```

SAP API Business Hub sandboxを使用するSAP Graphサーバーをハードコードしていることに注意してください。こうすることでここでは独自のSAP Graphビジネスデータグラフを構成する手間を省きデータアクセスAPIに焦点を当てることが出来ます。セキュリティや認証などの複雑な側面は今後のチュートリアルで扱っていきます。

SAP API Business Hub を介してサンドボックスのデータにアクセスしているため、上記のコードに API Key (短い文字列) を挿入する必要があります。[ここ](https://api.sap.com/settings)にログインし、**Show API Key** をクリックするとAPI Keyが表示され保存できるようになります。

**hellograph.js**

SAP Graphを利用したシンプルなサーバーサイドアプリケーションを書いていきましょう。**hellograph.js**という名前のファイルをsrcフォルダ中に作成し、下記のコードを...