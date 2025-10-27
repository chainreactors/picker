---
title: XCon2024议题||影子缓存：新型隐蔽域名劫持攻击
url: https://www.4hou.com/posts/Eylv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-19
fetch_date: 2025-10-06T17:40:44.058571
---

# XCon2024议题||影子缓存：新型隐蔽域名劫持攻击

XCon2024议题||影子缓存：新型隐蔽域名劫持攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# XCon2024议题||影子缓存：新型隐蔽域名劫持攻击

XCon组委会
[行业](https://www.4hou.com/category/industry)
2024-07-18 14:07:43

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)84319

收藏

导语：本议题将首次从 1,096 个 TLD 和 9 个主要 DNS 软件的域名资源记录配置角度对现实世界的胶水记录使用情况进行系统分析。··············································

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240718/1721282825172117.jpg "1721282221128768.jpg")

**循万变·见未来——技术前瞻**

**趋势一：自动化检测将成为研究焦点**

未来，越来越多的研究将聚焦于**开发自动化工具和机器学习算法来检测和响应DNS安全威胁**，例如恶意域名、DNS劫持和放大攻击。

**趋势二：对隐私保护的高度关注将推动加密技术的研究与应用**

随着用户对隐私关注度的提升，DNS-over-HTTPS (DoH) 和 DNS-over-TLS (DoT) 等**加密技术的研究和应用变得愈发重要**，旨在防止DNS查询被监听和篡改。

**趋势三：机构、组织间的合作频繁而广泛**

为应对复杂的DNS安全挑战，**不同机构、组织间的合作变得日益重要**，研究者们联合各方力量共同研究和解决全球DNS安全问题。

**——国防科技大学与清华大学联合培养博士生**

**张允义**

域名系统(DNS)从根本上依赖于胶水记录来提供权威的域名服务器IP地址，从而实现必要的域内委托。虽然以前的研究已经发现了与胶水记录相关的潜在安全风险，但由于这些记录本身的信任度较低，而且解析器处理这些记录的方式多种多样，因此对这些记录的利用（尤其是在域外委托的情况下）仍不明确。

**本届XCon2024大会中，国防科技大学与清华大学联合培养博士生 张允义将首次系统地探讨DNS 胶水记录带来的潜在威胁，揭示其在现实世界中的重大安全风险**。根据经验性的评估，演讲者及其团队发现 **1,096 个顶级域名中有 23.18% 的胶水记录是过****时的，但仍在被大量域名依赖着**。**更令人担忧的是，通过对 9 个主流 DNS 实现（如 BIND 9 和 Microsoft DNS）进行分析，发现与胶水记录相关的可操纵行为。**

基于这些系统性问题的组合，**演讲者及其研究团队提出了新的威胁模型**，从而实现大规模域名劫持和拒绝服务攻击，进一步发现了超过 193,558 条可利用资源记录，超过 600 多万个域名面临安全风险。对全球开放解析器的测量结果表明，90% 的解析器使用未经验证和过时的胶水记录。研究团队负责任的披露已经促使受影响的利益相关方采取了缓解措施。

**议题简介**

**《影子缓存：新型隐蔽域名劫持攻击》**

本议题将首次从 1,096 个 TLD 和 9 个主要 DNS 软件的域名资源记录配置角度对现实世界的胶水记录使用情况进行系统分析，同时提出新的攻击媒介——影子缓存，并构建针对陈旧胶水记录的新利用方法，尤其是在域外委派下，从而实现域劫持和拒绝服务攻击。

通过议题的分享，演讲者将解析威胁真实影响的评估结果——即超过 600 万个域名易受攻击，并通过实证研究证明 90% 的稳定开放解析器和 14 个主要公共 DNS 提供商容易受到新提出的攻击影响。

**演讲人介绍**

**张允义——**

**国防科技大学与清华大学联合培养博士生**

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240718/1721282826179979.jpg "1721282246158303.jpg")

张允义——国防科技大学与清华大学联合培养博士生

指导老师为张旻教授，段海新教授和刘保君老师。主要研究方向为**网络安全****，特别是基础协议安全，如DNS安全，新型网络犯罪检测与对抗**。研究成果发表在高级别学术会议及期刊，包括**USENIX Security, IMC, TDSC 和 TIFS 等**。研究成果产生巨大影响，**多次收到微软、亚马逊、百度、阿里、腾讯、雅虎等厂商的感谢**。

关于XCon2024议题更多相关信息请扫描：

![1721183352311139.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240718/1721282826139895.jpg "1721183352311139.jpg")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?RwVU58b7)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/FgeSuF0KtB-UlpRnM5_Lap8oHIWx)

# [XCon组委会](https://www.4hou.com/member/k2wX)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/k2wX)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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