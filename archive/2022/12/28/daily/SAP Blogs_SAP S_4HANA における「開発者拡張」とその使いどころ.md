---
title: SAP S/4HANA における「開発者拡張」とその使いどころ
url: https://blogs.sap.com/2022/12/27/sap-s-4hana-%e3%81%ab%e3%81%8a%e3%81%91%e3%82%8b%e3%80%8c%e9%96%8b%e7%99%ba%e8%80%85%e6%8b%a1%e5%bc%b5%e3%80%8d%e3%81%a8%e3%81%9d%e3%81%ae%e4%bd%bf%e3%81%84%e3%81%a9%e3%81%93%e3%82%8d/
source: SAP Blogs
date: 2022-12-28
fetch_date: 2025-10-04T02:36:03.961477
---

# SAP S/4HANA における「開発者拡張」とその使いどころ

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA における「開発者拡張」とその使いどころ

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51722&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA における「開発者拡張」とその使いどころ](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B-%E9%96%8B%E7%99%BA%E8%80%85%E6%8B%A1%E5%BC%B5-%E3%81%A8%E3%81%9D%E3%81%AE%E4%BD%BF%E3%81%84%E3%81%A9%E3%81%93%E3%82%8D/ba-p/13559338)

![Takayo](https://avatars.profile.sap.com/3/a/id3a87fb361101246ea6f63c4b2d2fe31e800d0a0e070f7efcff508692ecfcc5da_small.jpeg "Takayo")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[Takayo](https://community.sap.com/t5/user/viewprofilepage/user-id/17065)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51722)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51722)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559338)

‎2022 Dec 27
12:31 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51722/tab/all-users "Click here to see who gave kudos to this post.")

10,374

* SAP Managed Tags
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (3)

## はじめに

SAP S/4HANA を拡張する方法として新たに登場した「開発者拡張 (Developer extensibility)」が、SAP S/4HANA Cloud, private editionおよび SAP S/4HANA (オンプレミスを意味します)でも利用可能になったことをご存じでしょうか？

* SAP S/4HANA Cloud, public edition: 2208 リリースから使用可能

* SAP S/4HANA Cloud, private edition および SAP S/4HANA: SAP S/4HANA 2022 リリースから使用可能

これで SAP S/4HANA 全てのABAPプラットフォームで開発者拡張が使用できるようになり、SAP S/4HANA Cloud, public editionと同じ拡張手法を使用することができます。

このブログ投稿では、SAP S/4HANA (オンプレミス)における開発者拡張とその使いどころについてご紹介します。なお、SAP S/4HANA Cloud, private editionでも状況は同じです。
開発者拡張の概要についてはこちらの[ブログ投稿](https://blogs.sap.com/2022/06/16/sap-s-4hana-%E6%8B%A1%E5%BC%B5-developer-extensibility-embedded-steampunk-%E6%A6%82%E8%A6%81/)で紹介していますので、ご参照ください。

## オンプレミスにおける開発者拡張の実装ルール

### ABAPクラウド開発モデルとは？

SAP S/4HANA で開発者拡張が一般リリースとなりましたが、開発者拡張の実装ルールは SAP S/4HANA Cloud, public edition の場合と同様です。コアとカスタムコードを分離するために、従来の実装ルールより制限が多い新しい実装ルールへの準拠が必要となります。これにより、アップグレードを阻害せず、クラウドにも対応したカスタムコードの実装が可能となります。

新しい実装ルールの主なポイントとしては、下記の3点が挙げられます。

1. SAP オブジェクトの使用制限 – リリース済オブジェクト (Public API) のみ使用可能
   [Release contract](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm?file=abenabap_versions_and_apis.htm#@@ITOC@@ABENABAP_VERSIONS_AND_APIS_2) という属性でリリースステータスが定義され、未リリースのオブジェクトは使用できず、構文エラーになります。

2. SAP オブジェクトの拡張は事前に定義されリリースされている拡張ポイントのみ
   モディフィケーションは許可されていません。

3. Restricted ABAP Language (Cloud-optimized ABAP language)
   使用できる ABAP 構文・オブジェクトタイプが制限され、クラウド環境に不要・不適切な ABAP 構文は使用できません。開発者拡張では、[ABAP言語バージョン](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm?file=abenabap_versions_and_apis.htm#@@ITOC@@ABENABAP_VERSIONS_AND_APIS_1)：ABAP for Cloud Development を使用する必要があります。

これらの新しい実装ルールに準拠したクラウド対応の開発は、従来のクラシックな開発モデルに対して、**ABAP****クラウド開発モデル** **(ABAP cloud development model)** とも呼ばれています。ABAPクラウド開発モデルに準拠した拡張手法としては、下記の3つが提供されています。

①キーユーザ拡張
②開発者拡張
③Side-by-Side拡張

![](/legacyfs/online/storage/blog_attachments/2022/12/Figure2-1.png)

*[Extend SAP S/4HANA in the cloud and on premise with ABAP based extensions - Guidelines for extension...](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html) より引用 (Page 5)*

SAP S/4HANA Cloud, public edition では ABAPクラウド開発モデルでの拡張・開発が必須となりますが、SAP S/4HANAでは必要に応じて使うことができます。

## 開発者拡張は SAP S/4HANAでどういう時に使える？

オンプレミスの場合、開発者拡張はあくまで開発・拡張手法の１つのオプションでしかありません。オンプレミスでは、従来のクラシック拡張を引き続き使うことができますし、新たに開発者拡張を使うこともできます。同一システム内で両方の拡張手法を並行して使うことができます。

では、どういう時に、開発者拡張を含むABAPクラウド開発モデルを採用するのがよいと考えられるでしょうか？

１つ目は、将来、パブリッククラウド化を考えている場合です。
SAP S/4HANA Cloud, public edition では従来のクラシック拡張・開発は使用できず、ABAP クラウド開発モデルでの拡張・開発が必須です。そのため、パブリッククラウドに移行するには、既存のカスタムコードを全てABAPクラウド開発モデルで作り直す必要があります。オンプレミス上で、開発者拡張を利用して、既存のカスタムコードを少しずつクラウド対応に改修・再開発していくことができます。

２つ目は、よりスムーズにアップグレードを行いたい場合です。
SAPソフトウェアのアップデートが自動で行われる SAP S/4HANA Cloud, public edition では、アップグレードをスムーズに行うために、下記の２つのルールが導入されています。
・モディフィケーションの禁止
・リリース済オブジェクト (Public API) および SAP拡張ポイントのみ使用可能
このルールをオンプレミス上で実現する手段として、開発者拡張を使用することができます。

## 開発者拡張を SAP S/4HANA で使う時のポイントは？

### Three-tier extensibility model

オンプレミスの場合、通常、カスタムコードの多くが従来のクラシック拡張手法で実装されており、これら既存のカスタムコードとの共存が前提となります。また、今後、リリース済オブジェクトは順次用意されていく方針ですが、全ての開発要件を開発者拡張（あるいはキーユーザ拡張、Side-by-Side拡張）で満たせるとは限りません。

そのため、ABAPクラウド開発モデルを導入していくには、従来のクラシック拡張手法も使用しつつ、拡張を３階層で考えるとよい (three-tier extensibility model) とされています。
詳細は、2022年10月に新しく発表された [SAP S/4HANA 拡張ガイド](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html) 第5章で紹介されていますので、ぜひ、ご参照ください。

![](/legacyfs/online/storage/blog_attachments/2022/12/Figure5-1-1.png)

*[Extend SAP S/4HANA in the cloud and on premise with ABAP based extensions - Guidelines for extension...](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html) より引用 (Page 24)*

* **第 1 層 – クラウド開発**
  ABAPクラウド開発モデルに準拠し、SAP S/4HANA Cloud, public editionの開発モデルに相当します。新しいアプリケーションや拡張を実装する際に、最初の選択肢として検討します。

* **第 2 層 – クラウド API の有効化**
  リリース済オブジェクト(Public API)が用意されていない場合、未リリースのオブジェクト(例えば BAPI など)をラップするカスタムオブジェクトを作成します。ラッパオブジェクトを第1層のクラウド開発で使用できるように、クラウド開発用にリリースしておきます。将来、未リリースオブジェクトに代わるリリース済オブジェクトがSAPから提供されたら、ラッパオブジェクトの代わりにリリース済オブジェクトを使用し、ラッパオブジェクトは廃止します。これにより、完全に第１層に移行することができます。

* **第 3 層 – 従来の開発**
  ABAP クラウド開発モデルに準拠しない、従来のクラシック拡張のカスタムコードです。よりスムーズなアップグレードを実現するには、この層での開発を削減・回避することが肝要です。

### 不要なカスタムコードの削除

しかし、第３層 - 従来の開発による既存のカスタムコードをABAPクラウド開発モデルに準拠させるには、開発者拡張を使用したとしてもほぼ作り直しとなり、多大な工数を要することが予想されます。そのため、ABAPクラウド開発モデルに移行する前に、不要なカスタムコードは可能な限り削除・廃止することが推奨されています。既存コードの分析には、[Custom Code Migration App](https://blogs.sap.com/2021/05/07/rise-with-sap-and-custom-code-migration-what-is-included/) を使用できます。

SAP ERP システム時代のカスタムコードの約30-60%がもう使用されていない、という統計\*も出ており、不要なカスタムコードを削除することは、ABAPクラウド開発モデルへの比較的容易な第１歩とも言えます。
詳細は、[SAP S/4HANA 拡張ガイド](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html) 第6章もご参照ください。

\* 出典：[Custom Extensions in SAP S\_4HANA Implementations - A Practical Guide for Senior IT Leadership](https://www.sap.com/documents/2020/03/ceeea71f-8a7d-0010-87a3-c30de2ffd8ff.html) (Page 24)

### できるところから少しずつ

それでも残るカスタムコードについては、できるところから少しずつ開発者拡張の実装ルールを取り入れることもできます。
例えば、モディフィケーションはリリース済 BAdI (Cloud BAdI) に変更する、DBテーブルへのアクセスはリリース済CDS ビューに置き換える、その他...