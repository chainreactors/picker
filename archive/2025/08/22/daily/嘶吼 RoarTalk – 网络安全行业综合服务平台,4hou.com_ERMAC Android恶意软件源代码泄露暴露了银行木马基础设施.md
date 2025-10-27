---
title: ERMAC Android恶意软件源代码泄露暴露了银行木马基础设施
url: https://www.4hou.com/posts/QXEY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-22
fetch_date: 2025-10-07T00:16:51.723914
---

# ERMAC Android恶意软件源代码泄露暴露了银行木马基础设施

ERMAC Android恶意软件源代码泄露暴露了银行木马基础设施 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ERMAC Android恶意软件源代码泄露暴露了银行木马基础设施

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-21 18:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)62172

收藏

导语：Hunt.io发现并分析了ERMAC的PHP命令与控制（C2）后端、React前端面板、基于Go语言的数据窃取服务器、Kotlin后门，以及用于生成定制化木马化APK的生成器面板。

ERMAC安卓银行木马3.0版本的源代码已在网上泄露，这使得该恶意软件即服务平台的内部机制以及运营者的基础设施被迫曝光。

2024年3月，Hunt.io的研究人员在扫描暴露的资源时，于一个开放目录中发现了这一代码库。

他们找到了一个名为“Ermac 3.0.zip”的压缩包，其中包含该恶意软件的代码，涵盖后端、前端、数据窃取服务器、部署配置，以及木马的生成器和混淆器。研究人员对代码进行分析后发现，与之前的版本相比，其目标攻击能力大幅提升，可针对超过700个银行、商城及加密货币相关应用。

ERMAC最早于2021年9月由ThreatFabric（一家为金融服务领域提供在线支付欺诈解决方案及情报的供应商）记录在案。它是Cerberus银行木马的升级版，由名为“BlackRock”的威胁者操控。

2022年5月，ESET发现了ERMAC 2.0版本，该版本以每月5000美元的费用租给网络犯罪分子，当时可攻击467个应用，较上一版本的378个有所增加。

2023年1月，ThreatFabric观察到BlackRock在推广一款名为Hook的新型安卓恶意软件工具，该工具似乎是ERMAC的进一步演进版本。

**ERMAC 3.0的功能**

Hunt.io发现并分析了ERMAC的PHP命令与控制（C2）后端、React前端面板、基于Go语言的数据窃取服务器、Kotlin后门，以及用于生成定制化木马化APK的生成器面板。

研究人员表示，ERMAC 3.0目前可针对超过700个应用中的用户敏感信息。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250819/1755587365904833.png "1755586821151499.png")

ERMAC的一个表单注入

此外，这个最新版本在以往记录的表单注入技术基础上进行了拓展，采用AES-CBC进行加密通信，对运营者面板进行了全面改造，并增强了数据窃取和设备控制能力。

具体而言，Hunt.io已记录了ERMAC最新版本的以下功能：

**·**窃取短信、联系人及已注册账户信息

**·**提取Gmail邮件主题及内容

**·**通过“列表”和“下载”命令访问文件

**·**发送短信及呼叫转移，滥用通信功能

**·**通过前置摄像头拍摄照片

**·**全面的应用管理（启动、卸载、清除缓存）

**·**显示虚假推送通知以实施欺骗

**·**远程卸载（killme）以实现规避

**基础设施暴露**

Hunt.io的分析师通过SQL查询识别出威胁者当前正在使用的、处于暴露状态的活跃基础设施，包括C2端点、面板、数据窃取服务器及生成器部署。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250819/1755587366125266.png "1755586786204508.png")

暴露的ERMAC C2服务器

除了泄露恶意软件的源代码外，ERMAC的运营者还存在其他几处严重的操作安全失误，例如硬编码的JWT令牌、默认的root凭据，以及管理面板缺乏注册保护，这使得任何人都能访问、操纵或破坏ERMAC的相关面板。

最后，面板名称、标题、包名以及其他各种操作痕迹，无疑为溯源提供了依据，也让基础设施的发现和映射工作变得容易许多。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250819/1755587367743285.png "1755586939958891.png")

访问ERMAC面板

ERMAC 3.0源代码的泄露削弱了该恶意软件的运营——首先，它削弱了客户对这一恶意软件即服务平台的信任，客户会怀疑其能否保护信息不被执法部门获取，或是能否在低检测风险下开展攻击活动。

威胁检测解决方案也可能会在识别ERMAC方面变得更加高效。然而，如果源代码落入其他威胁者手中，未来有可能会出现更难检测的ERMAC修改变体。

文章翻译自：https://www.bleepingcomputer.com/news/security/ermac-android-malware-source-code-leak-exposes-banking-trojan-infrastructure/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?THqgTEm8)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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