---
title: （日本語版）SAP Data Warehouse Cloudのメール通知機能
url: https://blogs.sap.com/2022/12/28/sap-data-warehouse-cloud%e3%81%ae%e3%83%a1%e3%83%bc%e3%83%ab%e9%80%9a%e7%9f%a5%e6%a9%9f%e8%83%bd/
source: SAP Blogs
date: 2022-12-29
fetch_date: 2025-10-04T02:39:41.821697
---

# （日本語版）SAP Data Warehouse Cloudのメール通知機能

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* （日本語版）SAP Data Warehouse Cloudのメール通知機能

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161068&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [（日本語版）SAP Data Warehouse Cloudのメール通知機能](/t5/technology-blog-posts-by-sap/%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88-sap-data-warehouse-cloud%E3%81%AE%E3%83%A1%E3%83%BC%E3%83%AB%E9%80%9A%E7%9F%A5%E6%A9%9F%E8%83%BD/ba-p/13559610)

![hiroki_ito](https://avatars.profile.sap.com/b/4/idb4640ab1d7b19ce32a5f70ccf4194a3bdd1388229d61fd8415a3b7c16c2a5bb5_small.jpeg "hiroki_ito")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[hiroki\_ito](https://community.sap.com/t5/user/viewprofilepage/user-id/794116)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161068)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161068)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559610)

‎2022 Dec 28
12:33 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161068/tab/all-users "Click here to see who gave kudos to this post.")

864

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

## はじめに

本ブログは[こちら](https://blogs.sap.com/2022/01/27/custom-email-notification-solution-in-sap-data-warehouse-cloud/)のブログの日本語版になります。SAP Data Warehouse Cloudによるメール通知機能ついて解説しています。

## コンテンツ

1. 概要

2. 前提

3. SAP Data Warehouse Cloud Viewsのセットアップ

4. 通知テンプレート

5. 設定: サービスインスタンス

6. SAP Business Application Studioを使用したデプロイメント

7. スケジューリング

8. テストとメッセージ

## 1. 概要

2022年現在、SAP Data Warehouse Cloudは標準機能によるメールでの通知機能は提供されていません。本ブログでは、お客様がSAP Data Warehouse Cloud内の通知に対してメールでの通知機能を設定できるようにする方法を解説します。

## 2. 前提

以下を使用します。お客様のIT環境で使用可能かご確認ください。

* [@Sisn](/t5/user/viewprofilepage/user-id/1387241)/hana-client ^2.10.13

* express ^4.17.1

* node-json2html ^2.1.0

* nodemailer ^6.6.5

* nodemailer-smtp-transport ^2.7.4

* sap-cf-mailer 0.0.5

また、SAP Data Warehouse Cloud テナントと SAP BTP テナントも必要です。SAP BTPテナントでは、以下のサービスを有効にする必要があります。

* Job Scheduling Service

* SAP Business Application Studio

* Authorization and Trust Management Service

## 3. SAP Data Warehouse Cloud Viewsのセットアップ

以下のテーブルとビューを作成してください。

**A) 通知タスクテーブル – SAP\_TCT\_NOTE\_TASK\_V\_01 and/or 通知ANYテーブル – SAP\_TCT\_NOTE\_ANY\_V\_01**

このテーブルには、通知をトリガーする際の全てのログが含まれています。項目は以下のようにします。

* Notification\_ID (String 100)

* Notification\_Type (String 100)

* SPACE\_ID (String 64)

* OBJECT\_ID (String 256)

* EMAIL (String 256)

* LINK (String 1000)

* VAR\_1 (String 5000)

* …

* VAR\_5 (String 5000)

**B) 通知タスクビュー – SAP\_TCT\_NOTE\_UNION\_V\_01**

通知タスクテーブルの結合ビューです。

* Notification\_ID (String 100)

* Notification\_Type (String 100)

* SPACE\_ID (String 64)

* OBJECT\_ID (String 256)

* STATUS (String 256)

* EMAIL (String 256)

* LINK (String 1000)

* VAR\_1 (String 5000)

* …

* VAR\_5 (String 5000)

**C) 通知ステータステーブル – SAP\_TCT\_NOTE\_STATUS\_O\_01 (OpenSQL) and/or 通知ステータステーブル****– SAP\_TCT\_NOTE\_STATUS\_T\_01**

通知ステータステーブルです。

* Notification\_ID (String 100)

* Notification\_Type (String 100)

* EMAILSENT (Boolean)

* LAST\_CHANGE\_AT (Timestamp)

**D) 通知ステータスビュー –** **SAP\_TCT\_NOTE\_STATUS\_V\_01**

通知ステータステーブルの結合ビューです。

* Notification\_ID (String 100)

* Notification\_Type (String 100)

* EMAILSENT (Boolean)

* LAST\_CHANGE\_AT (Timestamp)

**E) 通知タイプテンプレートテーブル –** **SAP\_TCT\_NOTE\_TEMPL\_T\_01**

通知タイプごとのテンプレートテーブルです。

* Notification\_Type (String 100)

* Template (String 5000)

**F) オープン通知ビュー – SAP\_TCT\_NOTE\_OPEN\_V\_01**

オープン通知ビューです。

* Notification\_ID (String 100)

* Notification\_Type (String 100)

* SPACE\_ID (String 64)

* OBJECT\_ID (String 256)

* STATUS (String 256)

* EMAIL (String 256)

* LINK (String 1000)

* VAR\_1 (String 5000)

* …

* VAR\_5 (String 5000)

* EMAILSENT (Boolean)

* STATUS (String 60)

* LAST\_CHANGE\_AT (Timestamp)

* Template (String 5000)

## 4. 通知テンプレート

すべての通知テンプレートは、SAP\_TCT\_NOTE\_TEMPL\_T\_01テーブルに格納されています。このテーブルには、成功メッセージ、エラーメッセージ、警告メッセージのテンプレートなど、あらゆる種類の通知タイプのレイアウトが保存されています。以下は、SAP Data Warehouse Cloud 内でエラーとなったタスクのテンプレートがどのように見えるかの例です。

```
{ "<>": "div", "style": "margin: 0; padding: 0; text-align: center;", "html": [ { "<>": "li", "style": "width: 80%; margin: 2% .35%; display: inline-flex; box-shadow: 0 2px 4px rgba(0,0,0, .2);", "html": [ { "<>": "ul", "style": "width: 100%; padding: 1% 2%; background: #fff; max-height: 220px; box-sizing: border-box;", "html": [ { "<>": "h3", "style": "text-align: center;", "html": "Failed Task" }, { "<>": "ul", "style": "list-style-type: disc; text-align: left;", "html": [ { "<>": "li", "html": "Where: ${VAR_4} ${OBJECT_ID} in ${SPACE_ID}" }, { "<>": "li", "html": "StartTime: ${VAR_2}" }, { "<>": "li", "html": "Activity: ${VAR_3}" }, { "<>": "li", "html": "Triggered: ${VAR_5}" }, { "<>": "li", "html": [ { "<>": "a", "href": "https://******.eu10.hcs.cloud.sap/dwaas-ui/index.html#/*******&/di/*****${LINK}", "html": "Integration Monitor" } ] } ] } ] } ] } ] }
```

メールテンプレートは、要望に応じて自由に変更ください。

## 5. 設定: サービスインスタンス

SAP BTPのスペース内に2 つのサービスインスタンスを作成する必要があります。アプリがデプロイされるターゲットスペースに移動し、インスタンスセクションからサービスインスタンスを作成します。

１つめのインスタンス “**dwc-notification-secret**”:

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild1-2.png)

２つ目のインスタンス “**dwc-notification-mailconfig**”:

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild2-2.png)

通知ソリューションをデプロイした後、これら2つのサービスインスタンスをnode.jsアプリとバインドします。

## 6. SAP Business Application Studioを使用したデプロイメント

スペース内でSAP Business Application Studio Serviceを開きます。Dev Space（最初はBasic tools and extensions + HTML5 Runner + MTA Toolsを選択）を作成し、SAP Data Warehouse Cloud Notification Solutionのリポジトリを複製してください。

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild3-1.png)

通知ソリューションのリポジトリを複製します。複製後、親ディレクトリのmta.yamlファイルを開き、前のステップで作成したインスタンスがこのmtaファイルに記述されたとおりの名前になっているかどうかを確認します。

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild4-1.png)

問題がなければ、mtarプロジェクトをビルドし、zip圧縮したmtarプロジェクトをターゲットスペースにデプロイします。

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild5-1.png)

成功すると、ターミナルの出力に実行中のアプリケーションへのリンクが表示されます。

ここで、もう一度サービスインスタンスセクションを開き、先ほど作成した2つのユーザー提供サービスインスタンスとこの実行中のアプリのバインドが成功したかどうかを確認します。

アプリケーションへのリンクを開き、正しく起動しているか確認します。問題がなければ以下のように表示されます。

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild6-1.png)

## 7. スケジューリング

SAP BTPのサブアカウントに移動して、Service Marketplaceを開きます。"Authorization and Trust Management Service"を検索し、インスタンスを作成して新しくデプロイされたアプリにバインドします。

再びService Marketplaceで今度は"Job Scheduling Service"を検索し、インスタンスを作成します。インスタンス名 + パラメータ JSON: { "enable-xsuaa-support": true } を指定し、Instances and Subscription セクションに移動すると、新しく作成されたサービスが表示されます。このインスタンスをクリックし、ジョブスケジューリングインスタンスをアプリにバインドします。

![](/legacyfs/online/storage/blog_attachments/2022/01/Bild7-1.png)

スケジューラインスタンスを展開し、右上のドットメニューをクリックすると、ジョブスケジューラダッシュボードが表示されます。Configurationsページで、実行タイムアウトを編集できます。デフォルトは3時間に設定されています。

## 8. テストとメッセージ

通知ソリューションをローカルに複製し、親デ...