---
title: SAP Datasphereの分析モデルでの各種メジャー作成機能のご紹介
url: https://blogs.sap.com/2023/07/31/sap-datasphere%e3%81%ae%e5%88%86%e6%9e%90%e3%83%a2%e3%83%87%e3%83%ab%e3%81%a7%e3%81%ae%e5%90%84%e7%a8%ae%e3%83%a1%e3%82%b8%e3%83%a3%e3%83%bc%e4%bd%9c%e6%88%90%e6%a9%9f%e8%83%bd%e3%81%ae%e3%81%94/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T16:59:56.102085
---

# SAP Datasphereの分析モデルでの各種メジャー作成機能のご紹介

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphereの分析モデルでの各種メジャー作成機能のご紹介

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/165218&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphereの分析モデルでの各種メジャー作成機能のご紹介](/t5/technology-blog-posts-by-sap/sap-datasphere%E3%81%AE%E5%88%86%E6%9E%90%E3%83%A2%E3%83%87%E3%83%AB%E3%81%A7%E3%81%AE%E5%90%84%E7%A8%AE%E3%83%A1%E3%82%B8%E3%83%A3%E3%83%BC%E4%BD%9C%E6%88%90%E6%A9%9F%E8%83%BD%E3%81%AE%E3%81%94%E7%B4%B9%E4%BB%8B/ba-p/13571791)

![kana_tsukui79](https://avatars.profile.sap.com/e/b/ideb7bb4af95a515d3e94c8bd078048cf01daf072e1e7eecc4bd321e84330e4e7e_small.jpeg "kana_tsukui79")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[kana\_tsukui79](https://community.sap.com/t5/user/viewprofilepage/user-id/149014)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=165218)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/165218)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571791)

‎2023 Jul 31
10:22 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/165218/tab/all-users "Click here to see who gave kudos to this post.")

1,676

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

SAP Datasphereは新機能として[「分析モデル」](https://blogs.sap.com/2023/07/06/new-modelling-analytic-model-and-analytical-dataset/)が追加されました。

「分析モデル」では、ファクトに保持するメジャー、ディメンション、ディメンションの属性情報からの選択、分析データのプレビューなどの機能が追加されたことにより分析オブジェクトの設計において、さらに多くの自由度が提供されました。

本ブログでは「分析モデル」の新機能のうち各種集計用のメジャー作成機能について紹介します。

**1.計算メジャー**

これまでの「分析データセット」では集計処理前のレコード毎に計算するメジャーのみ作成することができましたが、「分析モデル」の計算メジャーは特定のディメンションで集計処理後のデータを利用して計算処理を行った数値を作成することができます。

**2.制限メジャー**

1つまたは複数のディメンションの特定の値でフィルタした数値を作成することができます。

**3.固有値カウントメジャー**

特定のディメンション毎のメンバー数をカウントすることができます。

**4.[通貨換算メジャー](https://blogs.sap.com/2023/07/17/%E6%8F%9B%E7%AE%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%AE%E9%80%A3%E6%90%BA-%E3%81%A8-%E9%80%9A%E8%B2%A8%E6%8F%9B%E7%AE%97%E3%83%93%E3%83%A5%E3%83%BC%E3%81%AE%E6%9C%89%E5%8A%B9%E5%8C%96/)**

参照日付を元にして通貨を目標通貨に変換することができます。

※別ブログの換算レートの連携 と 通貨換算ビューの有効化をご確認ください。

### **1. 計算メジャー**

![](/legacyfs/online/storage/blog_attachments/2023/07/画像3-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/画像11.jpg)「分析データセット」の2023年データ詳細

「分析データセット」を利用して単価を計算するためにビュー（ファクト）で「金額」 ÷ 「数量」の計算式を追加します。

各レコードのキー項目に基づいて計算された結果を「金額/数量」という項目で保持します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像17-scaled.jpg)![](/legacyfs/online/storage/blog_attachments/2023/07/画像17-1.png)

「分析データセット」の場合は、キー項目に基づいてレコード単位で計算された計算結果を表示しているので、単純に「会計年度」の項目を集約し、計算結果を合計した値が表示さていますので、正しい値ではありません。

SAP Analytics Cloudで会計年度をドリルダウンし表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像19-3.png)

そこで、分析モデルを利用して計算メジャーを追加します。

新規->計算メジャーをクリックします。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像22-3.png)

式を入力しましたらデプロイをします。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像23-4.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/画像24-2.png)

SAP Datasphereでプレビュー表示します。

※データプレビューの詳細内容はこちらの[ブログ](https://blogs.sap.com/2023/08/16/sap-datasphere%E3%81%AE%E5%88%86%E6%9E%90%E3%83%A2%E3%83%87%E3%83%AB%E3%81%A7%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%83%97%E3%83%AC%E3%83%93%E3%83%A5%E3%83%BC%E3%81%AE%E3%81%94%E7%B4%B9%E4%BB%8B/)をご確認ください。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像26-2.png)

SAP Analytics Cloudで会計年度をドリルダウンし表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像27-1.png)

メジャーが**集計後**に実行され正しい結果が表示されていることがわかります。

（使用例）

・対前年比を計算するために“前年売上金額÷当年売上金額”

・達成率を計算するために“目標金額÷金額×100”

### **2.制限メジャー**

制限付きメジャーは、1つまたは複数のディメンションと値でデータをフィルタリングすることができます。
今回の例では金額(グローバル通貨)に会計年度で制限をかけた値のメジャーを作成します。

値を確認するため、SAP Analytics Cloudで会計年度と会社コードをドリルダウンし表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像28-1.png)

メジャーの追加->制限メジャーをクリックし式を追加します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像29-2.png)

ソースメジャーに制限を追加したいメジャー項目を指定し、式に制限を入力しましたらデプロイをします。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像30-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/画像31-1.png)

同様に会計年度を2017～2023年分の制限メジャーを作成します。

SAP Datasphereでプレビュー表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像32-2.png)

SAP Analytics Cloudストーリーで会計年度と会社コードをドリルダウンし表示した金額と同様の値が作成した制限メジャーで表示されていることがわかります。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像33-1.png)

制限メジャーで設定する式では複数の式を設定することもできますので、必要に応じた設定を行ってください。

また、制限メジャーをクリックし式の追加の時に設定した集計タイプのSUMをMAX、MIN、Averageに置き換えることもできます。

詳細については[こちら](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/328d28fa8e324f759ff87751efc3b89e.html?locale=ja-JP)をご確認ください。

（使用例）

・区分に0：実績　1：予算とデータがある場合に区分毎に金額や数量の合計を集計する

・組織の区分毎に金額や数量の合計を集計する

### **3.固有値カウントメジャー**

*個別のメジャーのカウントは、現在のドリルダウンのディメンションメンバーをカウントすることができます。*今回の例では会計年度の数をカウントするメジャーを作成します。

値を確認するため、SAP Analytics Cloudで会計年度をドリルダウンし表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像34.png)

2016年～2023年の8年分のデータがあることが確認できます。

メジャーの追加->固有値カウントメジャーをクリックし式を追加します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像35.png)

ディメンションにカウントをしたいディメンション項目を指定しデプロイをします。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像36.png)

SAP Datasphereでプレビュー表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像38.png)

SAP Analytics Cloudストーリーで作成した固有値カウントメジャーを表示すると8年分のデータがあるために、8個とカウントされていることがわかります。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像39.png)

SAP Analytics Cloudストーリーでドリルダウンの状態に基づいて計算を表現することができますので、会社コードをドリルダウンしてみます。

値を確認するために、会社コードをドリルダウンして金額(グローバル通貨)を表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像40.png)

SAP Datasphereでプレビュー表示します。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像41.png)

それぞれの会社コードに何年分のデータがあるかをカウントすることができます。

![](/legacyfs/online/storage/blog_attachments/2023/07/画像42.png)

（使用例）

・社員数をカウントする

・顧客毎の購入回数をカウントする

### **ヘルプリンク**

[SAP Datasphere モデリング : 新しい「分析モデル」の利用と「分析データセット」](https://blogs.sap.com/2023/07/06/new-modelling-analytic-model-and-analytical-dataset/)

[Introducing the Analytic Model in SAP Datasphere](https://blogs.sap.com/2023/03/13/introducing-the-analytic-model-in-sap-datasphere/)

### **最後に**

本ブログでは、分析モデルでの通貨換算メジャー以外の計算・制限・固定値カウントメジャーの利用方法をご紹介いたしました。

メジャー、属性、ファクトに関連する全てのディメンションの選択、分析データのプレビューなど、分析オブジェクトの設計において、さらに多くの自由度が提供されました。

SAP Analytics Cloudなどのツールでの分析データ活用の幅が広がりましたのでご参考になると幸いです。

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [CoE Platform Japan](/t5/tag/CoE%20Platform%20Japan/tg-p/board-id/technology-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology...