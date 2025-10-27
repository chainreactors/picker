---
title: 1500个APP暴露Algolia API密钥，影响超300万用户
url: https://www.4hou.com/posts/wgDX
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-24
fetch_date: 2025-10-03T23:36:49.215221
---

# 1500个APP暴露Algolia API密钥，影响超300万用户

1500个APP暴露Algolia API密钥，影响超300万用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 1500个APP暴露Algolia API密钥，影响超300万用户

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-11-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172292

收藏

导语：CloudSEK已联系了受影响的APP开发者，告知了密钥暴露情况和潜在的安全风险。

1500个APP暴露Algolia API密钥，影响超300万用户。

Algolia 成立于2012年，是一个面向开发者的搜索功能API接口，为网站及APP的开发者提供搜索功能接口，可以为其提供发现和推荐功能，用户超过11万企业。新加坡网络安全公司CloudSEK研究人员发现有1550个移动APP会泄露Algolia API密钥，敏感内部服务和存储的用户信息有泄露的风险。

Algolia API系统有5类API key，分别对应Admin、Search、Monitoring、Usage和Analytics功能。这些API key中只有Search是可公开的，可以在前端代码中看到，帮助用户在APP中执行搜索查询。Monitoring key 为管理员提供集群状态信息。Usage和Analytics为用户提供使用统计数据。Admin key提供对其他4类API服务的访问，以及：

浏览、删除索引；

添加、删除记录；

列出索引；

获取、设置索引设置；

获得访问记录。

滥用以上服务可以宝库用户的敏感数据，比如用户设备、网络访问信息、使用统计数据、检索记录和其他相关信息的操作。

CloudSEK自动扫描工具发现有1550个APP泄露了Algolia API key和应用ID，攻击者利用这些泄露的信息可以实现对内部信息的非授权访问。这些暴露Algolia Admin API key的APP下载次数累计超过325万，其中有APP下载次数超过百万。其中32个APP会泄露admin secret，其中包括57个唯一的管理员密钥，攻击者利用泄露的管理员密钥可以访问敏感用户信息或修改APP索引记录和设置。

攻击者利用admin API key可以执行许多关键操作，并实现对敏感数据的访问，比如攻击者可以检索或者查看敏感数据。根据APP的版本，攻击者可以利用这些敏感访问更多的敏感数据。

![API keys leak](https://www.bleepstatic.com/images/news/u/1220909/Diagrams/api-diagram.png)

图 API keys 暴露引发的攻击流程![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669123128126314.png "1669123128126314.png")

图 暴露API的APP种类和下载次数

暴露密钥最多的APP种类为商城APP，下载次数超过230万次。此外，还有新闻APP、食品和饮料、教育、健身、医疗和商业APP，累计下载量超过95万次。

CloudSEK已联系了受影响的APP开发者，告知了密钥暴露情况和潜在的安全风险。

完整技术分析参见：https://cloudsek.com/whitepapers\_reports/hardcoded-algolia-api-keys-could-be-exploited-by-threat-actors-to-steal-millions-of-users-data/

本文翻译自：https://www.bleepingcomputer.com/news/security/apps-with-over-3-million-installs-leak-admin-search-api-keys/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?NpDLmhvy)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)