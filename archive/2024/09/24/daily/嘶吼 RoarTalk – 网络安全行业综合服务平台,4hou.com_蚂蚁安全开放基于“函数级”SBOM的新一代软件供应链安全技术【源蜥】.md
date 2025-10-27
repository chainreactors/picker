---
title: 蚂蚁安全开放基于“函数级”SBOM的新一代软件供应链安全技术【源蜥】
url: https://www.4hou.com/posts/kg7x
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-24
fetch_date: 2025-10-06T18:24:48.729336
---

# 蚂蚁安全开放基于“函数级”SBOM的新一代软件供应链安全技术【源蜥】

蚂蚁安全开放基于“函数级”SBOM的新一代软件供应链安全技术【源蜥】 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 蚂蚁安全开放基于“函数级”SBOM的新一代软件供应链安全技术【源蜥】

企业资讯
[新闻](https://www.4hou.com/category/news)
2024-09-23 09:41:52

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)122585

收藏

导语：近日，蚂蚁安全正式对外开放新一代软件供应链安全技术——源蜥

近日，蚂蚁安全正式对外开放新一代软件供应链安全技术——源蜥，2024年源蜥将开放200名免邀请试用名额（<https://cybersec.antgroup.com/>），推动行业软件供应链安全技术升级。

与传统软件组成成份分析技术（Software Composition Analysis，SCA）相比，源蜥“新”在哪里？能解决用户的哪些痛点？

**1、传统SCA用户面临的问题**

传统SCA的用户，经常会遇到SCA扫描动辄报出数万个漏洞，即使只关注高危以上的漏洞，也有数千个。面对这数以千计的高危漏洞：

一方面，漏洞修复的成本很高，全部修复会严重拖累业务的快速发展，在企业内部难以落地；

另一方面，如果不修复这些漏洞，对企业有严重安全威胁的漏洞也会淹没在其中，使企业面临着较大的安全风险。

**2、原因分析**

传统SCA检测漏洞主要包括三个环节，如图1所示：

（1）对应用程序做软件物料清单(Software Bill of Materials，简称SBOM）分析得到依赖的组件清单

（2）采集和分析得到漏洞情报

（3）通过组件清单关联漏洞情报得到漏洞

![1726835790157265.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442288160914.png "1726835790157265.png")

图1 传统SCA漏洞检测原理

传统SCA之所以会动辄报出数万个漏洞，主要原因有两点：

（1）传统SCA做SBOM分析的粒度都是组件级，只要应用程序依赖了含漏洞的组件，不管应用程序是否调用了漏洞的触发点，都会被认为存在漏洞，导致了大量的误报

（2）业界公开的漏洞情报非常多，传统SCA只关注了漏洞自身的危害等级，而没关注漏洞实际在业界被利用的风险，从而将大量不存在利用风险的漏洞也推给用户去修复。

例如，仅2023年披露的CVE漏洞就超过2.6万个，但即使是其中一些危害等级很高的漏洞，很可能也没有公开的POC或被在野利用尝试，利用风险很低，也无需用户重点关注。

**3、源蜥技术“新”在哪**

【源蜥】针对以上用户痛点，依托蚂蚁安全团队在【程序分析】和【威胁情报】领域业界领先的技术优势，创新的提出并实现了【“函数级”SBOM】和【漏洞利用风险分析】两项技术，让用户聚焦应用程序实际会触发、且业界实际存在较大利用风险的漏洞，大幅降低用户的软件供应链漏洞运营成本，如图2。

![1726835844239194.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442289118625.png "1726835844239194.png")

图2 源蜥漏洞检测原理

**3.1 函数级SBOM技术**

由于绝大多数漏洞的触发都是有一个或多个触发函数，只有应用程序及其依赖的二三方组件实际调用了一个漏洞触发点的函数，漏洞才有可能被实际触发，才是需要用户重点关注的漏洞。

函数级SBOM就是在组件级SBOM分析的基础上，利用蚂蚁安全海量的源码分析、存储和查询技术，对应用及其依赖的二三方组件进一步“画像”，“绘制”出应用程序依赖的所有函数的清单。

源蜥通过将应用的SBOM分析能力从【组件级】提升到【函数级】，帮助用户精准过滤了大量误报“漏洞”，提效60%以上。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442289346630.png "1726835887317017.png")

图3 源蜥函数级SBOM分析技术

**3.2 漏洞利用风险分析**

源蜥通过多维度的漏洞情报信息，只对用户透出经过分析存在被实际利用风险的漏洞，如POC已公开的漏洞/已被在野尝试利用的漏洞，减少无利用风险的漏洞情报80%以上。

在筛选出高利用风险漏洞情报的基础上，源蜥还会分析出该漏洞的触发点函数，从而结合函数级SBOM精准分析出实际有影响的漏洞。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442290306449.png "1726835920366757.png")

图4 源蜥漏洞利用风险分析技术

**4、小结**

软件供应链漏洞一般影响面较广，容易被外部攻击者利用，对企业的安全性有较大威胁，也是每年HW Top类型的风险，是企业高优先级要关注和处置的安全风险。

但传统SCA工具由于SBOM粒度较粗、漏洞情报不区分实际被利用的风险，导致动辄扫描出上万漏洞，在企业难以落地。

针对这一用户痛点，蚂蚁安全在业界率先提出了新一代软件供应链安全技术——源蜥，源蜥利用蚂蚁安全团队在程序分析和威胁情报领域业界领先的技术优势，创新的提出并实现了【“函数级”SBOM】和【漏洞利用风险分析】两项技术，让用户聚焦应用程序实际会触发、且业界实际存在较大利用风险的漏洞，不再苦于动辄扫描出的数万漏洞而束手无策，大幅提升了安全团队的运营效率。

源蜥新一代软件供应链安全技术与传统SCA核心能力对比

![微信图片_20240922201835.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442290136957.jpg "1727007366132784.jpg")

**技术体验**

<https://cybersec.antgroup.com/>

2024年对外开放200名免邀请试用名额，有任何技术相关的问题或建议，欢迎扫码加入钉钉群沟通

![1727008402777888.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241009/1728442290771246.jpg "1727008402777888.jpg")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?zCiu5jfB)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

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

[查看更多](https://www.4hou.com/member/aQWl)

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