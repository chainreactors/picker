---
title: SAP Product Footprint Managementのビジネスコンテンツのインポートと利用方法
url: https://blogs.sap.com/2022/12/26/how-to-import-sap-product-footprint-management-business-contents/
source: SAP Blogs
date: 2022-12-27
fetch_date: 2025-10-04T02:32:52.811256
---

# SAP Product Footprint Managementのビジネスコンテンツのインポートと利用方法

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Product Footprint Managementのビジネスコンテンツのインポートと利...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160844&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Product Footprint Managementのビジネスコンテンツのインポートと利用方法](/t5/technology-blog-posts-by-sap/sap-product-footprint-management%E3%81%AE%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88%E3%81%A8%E5%88%A9%E7%94%A8%E6%96%B9%E6%B3%95/ba-p/13558726)

![TakuhitoTanaka](https://avatars.profile.sap.com/7/e/id7e48c91d1928517cd12ae717501eb15e7a62f2aaf04773f00ba7902c1ffa0b94_small.jpeg "TakuhitoTanaka")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[TakuhitoTanaka](https://community.sap.com/t5/user/viewprofilepage/user-id/136110)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160844)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160844)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558726)

‎2022 Dec 26
1:02 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160844/tab/all-users "Click here to see who gave kudos to this post.")

1,380

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)

View products (1)

*※2023/1/18にモデルの説明を一部追記しました。*

**はじめに**

このブログポストではSAP Product Footprint Management（PFM）のビジネスコンテンツのインポートおよび利用方法を紹介します。また、本ブログは2022.08バージョンでの内容を記載しており、今後機能追加により、アップデートされる可能性があります。

**SAP Analytics Cloud****とSAP Product Footprint Managementの接続概要**

[コンテンツパッケージユーザガイド](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/42093f14b43c485fbe3adbbe81eff6c8/fa7e9b7df6cf4b8b9b91ee051aaa4858.html?locale=en-US)でPFMのビジネスコンテンツの内容を確認することが可能です。

以下はヘルプから抜粋したPFMのビジネスコンテンツの概要となります。

ODataサービスを利用して、PFMからフットプリントのデータを抽出し、SACのインポートモデルにデータを格納します。製品ごとの温室効果ガス（GHG）のフットプリント計算はPFMで実行し、SACは製品ごとのフットプリントの計算結果を分析するためのストーリーを提供しています。PFMのコンセプトについては、[オンラインヘルプ](https://help.sap.com/docs/SAP_BTP_PFM/b3e39aed098c41a2b0d49db0caf80711/97de4ce138d045328d59d5804ac081ea.html?locale=ja-JP)を参照してください。

![](/legacyfs/online/storage/blog_attachments/2022/12/image1-8.png)

2022年12月現在、PFMのビジネスコンテンツはサプライチェーン排出量Scope3のカテゴリ１（購入した製品・サービス）のみを対象としています。PFMで計算された購入した製品および製造した製品のフットプリントを期間/製品/サプライヤまたはプラントなどで分析することが可能です。

PFMでは輸送フットプリントの計算も可能となっていますが、PFMのビジネスコンテンツにはまだ反映されていません。

PFMおよびSACで提供される最新情報はブログで定期的に更新されているので、参考にしてください。

[SAP Product Footprint Management: Q1-22 Updates & Highlights](https://blogs.sap.com/2022/03/03/sap-product-footprint-management-q1-22-updates-highlights/)

[SAP Product Footprint Management: Q2-22 Updates & Highlights](https://blogs.sap.com/2022/06/02/sap-product-footprint-management-q2-22-updates-highlights/)

[SAP Product Footprint Management: Q3-22 Updates & Highlights](https://blogs.sap.com/2022/09/30/sap-product-footprint-management-q3-22-updates-highlights/)

[SAP Product Footprint Management: Q4-22 Updates & Highlights](https://blogs.sap.com/2022/12/21/sap-product-footprint-management-q4-22-updates-highlights/)

以下の順番でPFMのビジネスコンテンツを説明します。

1. PFMのビジネスコンテンツのインポート

2. SACとPFMの接続

3. データの更新

4. ビジネスコンテンツで提供されているストーリーの概要

5. ビジネスコンテンツで提供されているモデルとサンプルデータの概要

### **１．PFM****のビジネスコンテンツのインポート**

SAP Analytics CloudのコンテンツネットワークからPFMのビジネスコンテンツをインポートします。SACのビジネスコンテンツの探し方とインポート方法は以下のブログを参考にしてください。

[SAP Analytics Cloudのビジネスコンテンツの探し方とインストール手順](https://blogs.sap.com/2020/12/07/sap-analytics-cloud%E3%81%AE%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%81%AE%E6%8E%A2%E3%81%97%E6%96%B9%E3%81%A8%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC/)

コンテンツネットワークからビジネスコンテンツのタイルを選択し、PFMのビジネスコンテンツを選択します。以下は検索ウィンドウでproductを入力した検索結果です。![](/legacyfs/online/storage/blog_attachments/2022/12/image2-8.png)

インポートオプションですべてのオブジェクトを選択してインポートボタンをクリックします。サンプルデータも用意されており、インポート時にデータもインポートされます。もしデータが不要な場合は、データ取込のフラグを外してください。![](/legacyfs/online/storage/blog_attachments/2022/12/image3-8.png)

インポートが正常終了すると、以下のフォルダでインポートされたストーリーやモデルを確認することができます。

Myファイル/公開/SAP\_Content/SAP\PFM\_Product\_Footprint\_Management![](/legacyfs/online/storage/blog_attachments/2022/12/image4-6.png)

サンプルデータをインポートした場合、以下のようにストーリー（SAP\_\_SUS\_GEN\_FootprintAnalytics\_Overview）でデータを確認することが可能です。ただし、サンプルデータは2020年1月～2022年5月で提供されているため、ストーリーで選択されている期間によっては、データが表示されないので、注意してください。

以下のストーリーの場合、右上の選択で、サンプルデータのある年月を選択してください。![](/legacyfs/online/storage/blog_attachments/2022/12/image5-10.png)

サンプルデータでどんなデータが提供されているかは、SACのデータアナライザで確認することが可能です。

### **２．SAC****とPFMの接続**

次に、SACとPFMを接続します（[オンラインヘルプ](https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/42093f14b43c485fbe3adbbe81eff6c8/9974763fe4064a43a3b268257bb24e5b.html?locale=en-US)）。ビジネスコンテンツでインポートされた接続のパラメータを接続するPFMの値で更新することで接続を行います。

SACの接続メニューで「SAP\_\_PFM\_ProductFootprints\_OData」を検索します。![](/legacyfs/online/storage/blog_attachments/2022/12/image6-6.png)

接続を選択して、編集ボタンをクリックして、必要な情報を更新します。![](/legacyfs/online/storage/blog_attachments/2022/12/image7-7.png)

オンラインヘルプに記載されているように、BTPコックピットのインスタンスからView Credentialボタンをクリックし、必要な情報を取得します。![](/legacyfs/online/storage/blog_attachments/2022/12/image8-9.png)

|
 項目 |
 値 |

|
 データサービスURL |
 "apihost"の値に/footprintdata-analytics-service/v1/odata/v4/footprintdataanalytics/v1/を追加して入力します |

|
 OAuthクライアントID |
 "clientid"の値を入力します |

|
 シークレット |
 "clientsecret"の値を入力します |

|
 トークンURL |
 "url"の値に/oauth/tokenを追加して入力します |

### **３．データの更新**

PFMと接続した後に、PFMからデータを更新します。データ更新対象は、公開ディメンジョンと明細および集計のトランザクションとなります。

* **公開ディメンジョン**

PFMのモデルの公開ディメンジョンは「SAP\_\_SUS\_GEN\_ProductHierarchy」のみとなります。

以下の2つのデータソースがあるので、それぞれ実行してデータを更新します。 **![](/legacyfs/online/storage/blog_attachments/2022/12/image9-7.png)**

* **明細のフットプリント**

明細モデル「SAP\_\_SUS\_GEN\_IM\_ProductFootprints\_LineItem」に対して、データを更新します。モデルの管理画面のデータ管理からデータを更新します。![](/legacyfs/online/storage/blog_attachments/2022/12/image10-7.png)

* **集計のフットプリント**

集計モデル「SAP\_\_SUS\_GEN\_IM\_ProductFootprints\_Consolidated」に対して、データを更新します。モデルの管理画面のデータ管理からデータを更新します。![](/legacyfs/online/storage/blog_attachments/2022/12/image11-5.png)

ヘルプにも記載されている通り、公開ディメンジョンについては、PFMでマスタが追加・更新された後にデータ更新を行えば、十分です。また、フットプリントについては、PFMでフットプリント計算を実行した後に、データ更新を行う必要があるので、注意してください。

### **４．ビジネスコンテンツで提供されているストーリーの概要**

最後に、PFMのビジネスコンテンツで提供されているストーリーについて、簡単に説明します。冒頭で触れたように、現時点のビジネスコンテンツはScope3のカテゴリ１（購入した製品・サービス）が対象となっています。

ストーリーでは、サプライヤから購入した製品のフットプリント（購入数量×各製品の排出係数）と自社で製造した製品のフットプリント（購入した製品のフットプリントをBOMで積み上げたフットプリント）をインフローと在庫の観点から分析することが可能です。

また、使用されているキー数値は、基本的に以下の２つです。

* トータルフットプリント：特定期間の製品の計算された CO2e 値（数量×排出係数）

* ユニット別のフットプリント：特定の期間に対して計算された製品の単位数量ごとの CO2e 値 (例: Kgあたりの CO2e)

上記2つのキー数値を切り替えながら分析を行うことが可能です。

それでは、提供されている4つのストーリーについて、簡単に説明します。

* **Analyze Product Carbon Footprints**

PFMで提供されているストーリーで概要を分析することが可能なストーリーです。購入した製品および製造した製品のインフローおよび在庫（\*）の単月のフットプリントおよび2年間のトレンドを確認することができます。また、他の詳細ストーリーへのリンクが用意されており、他の詳細ストーリーへ遷移することが可能です。

\*在庫は選択した月の前月の在庫＋当月のインフロー－当月のアウトフローで計算されています。

このストーリーの右上の入力コントロ...