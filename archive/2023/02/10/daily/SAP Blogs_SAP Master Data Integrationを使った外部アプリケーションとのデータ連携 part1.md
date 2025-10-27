---
title: SAP Master Data Integrationを使った外部アプリケーションとのデータ連携 part1
url: https://blogs.sap.com/2023/02/09/sap-master-data-integration%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%9f%e5%a4%96%e9%83%a8%e3%82%a2%e3%83%97%e3%83%aa%e3%82%b1%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3%e3%81%a8%e3%81%ae%e3%83%87%e3%83%bc%e3%82%bf/
source: SAP Blogs
date: 2023-02-10
fetch_date: 2025-10-04T06:13:52.020340
---

# SAP Master Data Integrationを使った外部アプリケーションとのデータ連携 part1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Master Data Integrationを使った外部アプリケーションとのデータ連携 p...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163193&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Master Data Integrationを使った外部アプリケーションとのデータ連携 part1](/t5/technology-blog-posts-by-sap/sap-master-data-integration%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E5%A4%96%E9%83%A8%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E9%80%A3%E6%90%BA-part1/ba-p/13566289)

![takuya_endo](https://avatars.profile.sap.com/7/f/id7fb87b2e7be72ee525f216ed1c5dbd63bb194c540cb571de48e96e672929c9f0_small.jpeg "takuya_endo")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[takuya\_endo](https://community.sap.com/t5/user/viewprofilepage/user-id/123795)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163193)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163193)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566289)

‎2023 Feb 09
11:01 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163193/tab/all-users "Click here to see who gave kudos to this post.")

2,972

* SAP Managed Tags
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (1)

# １    本ブログについて

本ブログではSAP Master Data Integration（以下、「MDI））を初めて使われる方を対象にその他SAPアプリケーションとのデータ連携において必要な設定と手順について解説いたします。

本ブログでは私が実際にセットアップした時の手順をもとに注意しなければいけない点等を補足しながらまとめておりますのでMDIをセットアップする際に参考にしていただければ幸いです。

# ２    MDIとは

まずは今回の主役であるMDIとは一体どんなものなのか解説します。

SAP Business Technology Platform（以下、「BTP」）上で提供されるサービスで名前の通りデータの連携を担うサービスです。

後程触れますが、実際にMDIの機能を利用するためにはMaster Data Orchestration（以下、「MDO」）のサービスのSubscriptionも必要になります。

何のためにMDIが提供されているか、ですが下記の通りアプリケーション間で直接データを連携する「Point-to-point integration」ではなく、「Central integration point」としてMDIを中心に各アプリケーションに保管されているデータを連携することでMDIによる一貫したマスタデータの管理・データ管理における運用コスト削減を目的としたサービスです。BTP上で提供されるサービスですのでInstanceを作成し、このInstanceによって「Central integration point」を構成します。

![](/legacyfs/online/storage/blog_attachments/2023/02/スクリーンショット-2023-02-10-094010.png)

図1：MDI Concept

InstanceとMDIで保管されるデータの関係についてご説明いたします。下記図2はMDIのLandscapeのイメージ図ですが青枠のClientがMDI Instance、緑枠のTenantがBTP Subaccountに該当します。MDIではデータはClient単位ではなく、Tenant単位で管理されます。例えば下記図2のClient1にてデータ変更が発生した場合は同じTenantに属するClient2とClient3にデータが連携され、異なるTenantに属するClient 4-6には反映されません。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像2.png)

図2：MDI Landscape

共有されるのであればなぜわざわざClient（MDI Instance）が複数存在するのでしょうか。それはClientと連携先のシステムが1:1の構成でMDI Instanceを用意する必要があるからです。下記図3はSAP Success Factors、S/4 HANA On Premise、S/4 HANA Cloudと連携する場合に必要なMDI Instanceのイメージ図です。連携するシステムは合計3つですのでMDI Instanceは3つ必要です。後述の設定手順の中でも触れますが各Instanceのパラメータの中で連携先となるシステムのBusiness Systemを設定します。この値によって連携先との関係を紐づかせるイメージです。さらに各Instanceでは書き込み権限などの権限設定が可能です。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像3.png)

図3：MDI インスタンス

# ３    制約事項

MDIの設定手順に入る前にBTP環境について確認しなければいけない点について共有いたします。

下記の条件を満たしているか確認してください。

[Global Account]

Cloud Foundry環境のGlobal Accountである。

[Subaccount]

SubaccountのRegionは下記のいずれかである。

・Europe (Frankfurt) - EU10

・US East (VA) - US10

・Australia (Sydney) - AP10

・Singapore - AP11

※2023年1月時点でMDIとMDOのサービスが利用可能なRegionは下記の通りです。MDIが利用できるRegionはMDOが利用できるRegionに包含されていますのでMDIがサポートされたRegionであれば問題ありません。

最新の情報は下記リンクをご確認ください。

[MDI - Technical Prerequisites](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/e20c915789f44fa2951a948116c335d7.html?locale=en-US)

[MDO - Technical Prerequisites](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/8ce78b673ef04cc1bcfeb01c93ef7885/61e0e494aca047c7b6127138d9dc62b5.html)

![](/legacyfs/online/storage/blog_attachments/2023/02/画像4.png)

図4：MDIとMDOが提供されるSubaccountのRegion（2023年1月時点）

[Space]

用意したSubaccountに紐づくSpaceが作成されている。

[Service]

Marketplaceにて下記サービスが確認できる。

・Master Data Integration

・Master Data Integration(Orchestration)

※下記図5の通り、似たもので「Master Data Orchestaraion」というサービスがありますがこちらはMDIとの連携では利用しません。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像6.png)

図5：BTP Subaccount - Service Marketplace

※Marketplaceに該当のサービスが見つからない場合はGlobal Accountから該当のSubaccountにBooster 「Set up SAP Master Data Integration」を割り当てる必要があります。BTP Boosterにつきましては[こちら](https://help.sap.com/docs/btp/sap-business-technology-platform/boosters)をご確認ください。

# ４    設定手順（MDIセットアップ）

早速、本題の設定手順につきまして解説いたします。SaaSアプリケーションということで手順はシンプルです。ただし、当手順はあくまでもMDIインスタンスをセットアップするための手順で連携するアプリケーションに依存せず共通で必要な手順です。この手順による設定が完了した後、連携するアプリケーション毎に追加の設定を実施する必要があります。

1. MDI Instance作成

2. Service Key作成

3. Business System付与

4. MDOのSubscription

## 1.     MDI Instance作成

まずは準備したBTPのspaceにMDIのInstanceを作成します。

①準備したSpaceよりMDIのInstanceを作成。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像6-1.png)

②下記の通り入力しNextをクリック。

- Service: Master Data Integration

- Plan: sap-integration

- Instance Name: [任意の値]

![](/legacyfs/online/storage/blog_attachments/2023/02/画像8.png)

③下記の通りパラメータを設定し、Nextをクリック。

※今回はMDI→S/4 HANA On Premiseに対してBusiness Partnerのデータを連携するための手順を確認しますので下記の通り入力しています。パラメータの使い方は[こちら](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/69ae614272654411a4c03acea8d488b3.html?locale=en-US)も参考にしてみてください。

- application: MDIと連携するアプリケーションの識別子を指定します。“ariba”, “c4c”, “cdc”, “commerceCloud”, “concur”, “cpq”, “mdg”, “s4”, “sfsf”, “hrc”から指定します。

- businessSystemId: 連携するアプリケーションの識別子です。

S/4 HANA On Premiseの場合は、LCR\_GET\_OWN\_BUSINESS\_SYSTEMファンクションを実行することで取得できる値を利用します。

S/4 HANA Cloudの場合は、Communication Systems より自身のSystemで確認できる「Business System」フィールドの値を利用します。

- writePermissions: 書き込み権限を許可するエンティティを指定します。

MDIではOne Domain Model（以下、「ODM」）に倣ってデータが管理されますのでそのエンティティの値を指定します。MDIにてサポートされているODMエンティティについては[こちら](https://help.sap.com/docs/SAP_MASTER_DATA_INTEGRATION/c7713d6177ad479d9ea00958db9f2f81/8882bf982aca461d89b15afe19483edb.html?locale=en-US)をご確認ください。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像9.png)

④「Create」をクリック。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像10.png)

⑤Statusが「Created」になっていることを確認。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像11.png)

## 2.     Service Key作成

作成したMDI InstanceでService Keyを作成します。ここには外部からアクセスするために必要なAPIのEnd PointやOAuth認証等で必要となる情報が含まれます。

①作成したMDI Instanceの「・・・」から「Create Service Key」をクリック。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像12.png)

②下記の通り入力し、「Create」をクリック。

Service Key Name: 「任意の値」

こちらは任意の値で問題ありませんが”ValidFromYYYYMMDD”のように作成日を入れていつから有効なのかわかるようにすることが推奨されています。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像13.png)

③作成されていることを確認。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像14.png)

右上の「View Credentials」から確認してみると下記のように情報が含まれていることが確認できます。認証に必要な情報もありますので外部に公開しないようにご注意ください。

![](/legacyfs/online/storage/blog_attachments/2023/02/画像15.png)

## 3.     Business System付与

「2 MDIとは」で少し触れたBusiness Systemの値をMDI ...