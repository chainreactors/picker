---
title: ディメンションとなるGL勘定階層データ の連携
url: https://blogs.sap.com/2023/07/19/%e3%83%87%e3%82%a3%e3%83%a1%e3%83%b3%e3%82%b7%e3%83%a7%e3%83%b3%e3%81%a8%e3%81%aa%e3%82%8bgl%e5%8b%98%e5%ae%9a%e9%9a%8e%e5%b1%a4%e3%83%87%e3%83%bc%e3%82%bf-%e3%81%ae%e9%80%a3%e6%90%ba/
source: SAP Blogs
date: 2023-07-20
fetch_date: 2025-10-04T11:54:34.921984
---

# ディメンションとなるGL勘定階層データ の連携

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* ディメンションとなるGL勘定階層データ の連携

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158747&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ディメンションとなるGL勘定階層データ の連携](/t5/technology-blog-posts-by-sap/%E3%83%87%E3%82%A3%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%81%AA%E3%82%8Bgl%E5%8B%98%E5%AE%9A%E9%9A%8E%E5%B1%A4%E3%83%87%E3%83%BC%E3%82%BF-%E3%81%AE%E9%80%A3%E6%90%BA/ba-p/13552758)

![MayukoKita](https://avatars.profile.sap.com/4/0/id4004d8e9c7825aec4721c52c458bb308a1f9f0ddf4fea1f5b2fc46a5eeaf9156_small.jpeg "MayukoKita")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[MayukoKita](https://community.sap.com/t5/user/viewprofilepage/user-id/149828)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158747)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158747)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552758)

‎2023 Jul 19
9:59 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158747/tab/all-users "Click here to see who gave kudos to this post.")

2,893

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

本ブログは、S/4HANAと連携したSAP Datasphereでのモデリングのポイント解説 STEP1の続編になります。

ステップごとに全3回のシリーズでご紹介しています。
このブログは、STEP2についてです。

**分析モデル構築までの****3ステップ**

[STEP1：ファクトとなる 会計伝票明細データ の連携](https://blogs.sap.com/2023/07/18/s-4hana%E3%81%A8%E9%80%A3%E6%90%BA%E3%81%97%E3%81%9Fdatasphere%E3%81%A7%E3%81%AE%E3%83%A2%E3%83%87%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AE%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E8%A7%A3%E8%AA%AC/)

STEP2：ディメンションとなるGL勘定階層データ の連携

[STEP3：換算レートの連携 と 通貨換算ビューの有効化](https://blogs.sap.com/2023/07/17/%E6%8F%9B%E7%AE%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%AE%E9%80%A3%E6%90%BA-%E3%81%A8-%E9%80%9A%E8%B2%A8%E6%8F%9B%E7%AE%97%E3%83%93%E3%83%A5%E3%83%BC%E3%81%AE%E6%9C%89%E5%8A%B9%E5%8C%96/)

STEP2では、GL勘定階層データ を付加することによって、SAP Analytics Cloudのストーリー上でSTEP1で連携した会計データが階層を使って集計されていることが確認できるようにします。併せて、GL勘定コードがテキスト表示されるようテキストデータを連携し、定義していきます。

S/4HANAからGL勘定階層データとテキストデータを連携し、SAP Datasphere上で階層を定義する際に、S/4HANAの階層を表現するデータの持ち方 とSAP Datasphereの階層を表現するデータの持ち方が異なるため考慮が必要です。

S/4HANAから3つの標準CDS View GL勘定階層ノード、GL勘定階層ノード - テキスト、GL勘定 - テキストを連携し、SAP Datasphere上にディメンションビュー（親子階層）とテキストビューを作成します。SAP Datasphere階層を表現するデータの持ち方に合わてデータのレイアウトを変換する処理は、SAP DatasphereのGL勘定階層ビューとGL勘定階層テキストビューの中でそれぞれ行います。

実際のビューの作成内容については作業の流れの中で記載しています。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-24.png)

**分析モデル概要**

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-20.png)

**STEP2構****成****図**

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-16.png)

使用するCDS Viewの定義のリストを以下に示します。

* I\_GLAccountHierarchyNode（[GL勘定階層ノード](https://api.sap.com/cdsviews/I_GLACCOUNTHIERARCHYNODE)）

* I\_GLAccountHierarchyNodeT（[GL勘定階層ノード-テキスト](https://api.sap.com/cdsviews/I_GLACCOUNTHIERARCHYNODET)）

* I\_GLAccountHierarchyText（[GL勘定-テキスト](https://api.sap.com/cdsviews/I_GLACCOUNTTEXT)）

**作業の流れ**

1.GL勘定ディメンションビューの作成 と 親子階層定義

2.GL勘定テキストビューの作成 と　ディメンションビューへアソシエーション

3.分析モデルへの反映

4.SAP Analytics Cloudストーリーからデータを取得

### **1.GL勘定ディメンションビューの作成 と 親子階層定義**

ディメンジョンビュー（親子階層）を作成し、ソースにGL勘定階層ノードを設定します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture4-13.png)

**①使用する財務諸表バージョンを抽出**

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-13.png)

**②GL勘定コードの内部書式変換**

GL勘定コードは、内部書式（前0ゼロあり）で連携されるため、ABAP\_ALPHANUM関数を使用して外部書式（前0ゼロなし）に変換します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture6-14.png)

式：CASE WHEN "NODETYPE" = 'L' THEN
ABAP\_ALPHANUM("HIERARCHYNODEVAL",8)
　　ELSE "HIERARCHYNODE"
　　END

ディメンションビュー上で親子階層を設定します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture7-10.png)

プレビュー

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture8-9.png)

ファクトビュー GL勘定明細　から　GL勘定ディメンションビュー を指定しアソシエーションします。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture9-10.png)

###

### **2. GL勘定階層テキストビューの作成 と　ディメンションビューへアソシエーション**

次に、1.で定義したGL勘定階層をテキストで表示するために、GL勘定階層テキストビューを作成します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture10-8.png)

**①上位ノード（最下層のＧＬ勘定コード以外）のテキスト情報を取得**

GL勘定階層ノード の 全階層ノードに　左結合で GL勘定階層ノード - テキストから、上位ノードのテキスト情報（最下層のGL勘定コード以外）を取得します。結合前に、特定の財務諸表バージョンをフィルタで抽出しておきます。

次に、②のGL勘定コードと結合するための前処理として、計算（fx）で階層ノードに以下の計算式を作成します。階層ノードタイプが「Ｌ」の最下層の階層ノードにGL勘定コードを設定します。GL勘定コードを設定する際に内部書式で前ゼロ埋めされているので、文字列をALPHANUM型に変換して8桁の文字列に戻します。 その後、不要な項目を削除します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture11-8.png)

式：CASE WHEN "NODETYPE" = 'L' THEN
ABAP\_ALPHANUM("HIERARCHYNODEVAL",8)
　　ELSE "HIERARCHYNODE"
　　END

プレビュー

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture12-9.png)

GL勘定コードのテキストは②で取得します。

**②GL勘定コードのテキストを取得**

GL勘定階層ノード-テキストには最下層のGL勘定のテキストを持っていないので、GL勘定テキストから取得します。特定の財務諸表バージョンのGL勘定階層を抽出し、計算（fx）でGL勘定テキストのGL勘定を内部書式のままで0埋めされているので、文字列をALPHANUM型に変換して8桁の文字列に戻します。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture13-10.png)

式：ABAP\_ALPHANUM("GLACCOUNT",'8')

プレビュー

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture14-5.png)

**③　①、②を統合**

①と② をGL勘定コードで結合し、テキストを取得します。このとき、言語キーとGL勘定テキストは項目が分かれてしまうため以下の計算（fx）で1つの項目に統合する計算を設定します。

**・計算前**

テキスト、言語キーがそれぞれ2列に分かれている。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture15-5.png)

GL勘定階層テキスト と GL勘定テキストの統合

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture16-6.png)

式：IFNULL(HIERARCHYNODETEXT,GLACCOUNTNAME)

言語キーの統合

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture17-5.png)

式：IFNULL(LANGUAGE, LANGUAGE\_2)

**・計算後**

それぞれの項目が統合された。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture18-4.png)

ビューの定義が完了したら属性のセマンティックタイプを以下のように設定します。言語キーを設定することによってテキストの言語切替が可能になります。

階層ノードテキスト：テキスト

言語キー：言語

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture19-3.png)

GL勘定マスタ階層と紐づくGL勘定マスタ階層テキストの作成ができました。

最後に、ディメンションビューからアソシエーションします。

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture20-2.png)

### **3.分析モデルへの反映**

STEP1で作成した分析モデルを開き、ファクトソース「GL勘定明細」を選択すると、関連ディメンジョンに「勘定コード表」が表示されているので、チェックボックスにチェックを入れると有効になります。

*デプロイを実行します。*

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture21-2.png)

### **4.SAP Analytics Cloudストーリーからデータを取得**

階層をドリルダウンして最下位のGL勘定のテキストが正しく表示されているのが確認できます。

・ログオン言語：JA

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture22-2.png)

また、ログイン言語によってテキストが切り替わっていることも確認できます。

・ログオン言語：EN

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture23-2.png)

###

### **最後に**

本ブログでは、S/4HANAで設定したGL勘定階層、階層テキストをSAP Datasphereに取り込む方法をご紹介しました。現時点では、ご紹介した方法で階層とテキストを定義していますが、[ロードマップ](https://roadmaps.sap.com/board?PRODUCT=73555000100800002141&range=CURRENT-LAST#Q2%202023)上は2023年第3四半期には、S/4HANA 上でディレクトリを使用しモデル化された階層をインポートで使用できるようになることが予定されています。公開後、ブログでご紹介できればと思います。

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

* [CoE Platform Japan](/t5/tag/CoE%20Platfo...