---
title: 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序
url: https://www.4hou.com/posts/ArWp
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-24
fetch_date: 2025-10-06T19:37:02.537353
---

# 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序

新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 DroidBot Android 恶意软件针对 77 个银行加密应用程序

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-12-24 00:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)106014

收藏

导语：为了减轻这种威胁，建议 Android 用户仅从 Google Play 下载应用程序，在安装时仔细检查权限请求，并确保 Play Protect 在其设备上处于活动状态。

一种名为“DroidBot”的新 Android 银行恶意软件试图窃取英国、意大利、法国、西班牙和葡萄牙超过 77 个加密货币交易所和银行应用程序的凭据。

据发现新 Android 恶意软件的 Cleafy 研究人员称，DroidBot 自 2024 年 6 月以来一直活跃，并作为恶意软件即服务 (MaaS) 平台运行，该工具的售价为每月 3,000 美元。至少有 17 个附属组织已被发现使用恶意软件构建器来针对特定目标定制其有效负载。

尽管 DroidBot 缺乏任何新颖或复杂的功能，但对其僵尸网络之一的分析显示，英国、意大利、法国、土耳其和德国有 776 种独特的感染，表明存在重大活动。此外，Cleafy 表示，该恶意软件似乎正在大力开发，有迹象表明试图扩展到包括拉丁美洲在内的新地区。

**DroidBot MaaS 操作**

DroidBot 的开发人员似乎是土耳其人，他们为附属公司提供了进行攻击所需的所有工具。这包括恶意软件构建器、命令和控制 (C2) 服务器以及中央管理面板，他们可以从中控制操作、检索被盗数据和发出命令。

![ad.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733734814115171.png "1733734631257425.png")

创作者声称 DroidBot 在 Android 14 上运行良好

多个附属机构在同一 C2 基础设施上运行，并为每个组织分配了唯一的标识符，使 Cleafy 能够识别 17 个威胁组织。

![affiliates.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733734816712489.png "1733734663841581.png")

从样本配置中提取的附属机构

有效负载构建器允许附属机构自定义 DroidBot 以针对特定应用程序、使用不同的语言并设置其他 C2 服务器地址。关联公司还可以访问详细文档、恶意软件创建者的支持以及定期发布更新的 Telegram 频道。

总而言之，DroidBot MaaS 操作使缺乏经验或低技能的网络犯罪分子的进入门槛相当低。

![panel.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733734817202546.png "1733734703182068.png")

管理面板为附属公司提供完全控制

**冒充流行应用程序**

DroidBot 通常伪装成 Google Chrome、Google Play 商店或“Android Security”来欺骗用户安装恶意应用程序。然而，在所有情况下，它都会充当试图从应用程序窃取敏感信息的特洛伊木马。

![apps.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733734818142574.png "1733734743197414.png")

DroidBot 的屏蔽应用程序

该恶意软件的主要特征是：

**·**按键记录 – 捕获受害者输入的每一次按键。

**·**覆盖 – 在合法的银行应用程序界面上显示虚假的登录页面。

**·**短信拦截 – 劫持传入的短信，特别是那些包含用于银行登录的一次性密码 (OTP) 的短信。

**·**虚拟网络计算 – VNC 模块使附属机构能够远程查看和控制受感染的设备、执行命令以及使屏幕变暗以隐藏恶意活动。

DroidBot 操作的一个关键方面是滥用 Android 的辅助功能服务来监控用户操作，并代表恶意软件模拟滑动和点击。因此，如果用户安装了请求奇怪权限的应用程序（例如辅助功能服务），应该立即产生怀疑并拒绝该请求。

在 DroidBot 试图窃取凭证的 77 个应用程序中，一些突出的应用程序包括 Binance、KuCoin、BBVA、Unicredit、Santander、Metamask、BNP Paribas、Credit Agricole、Kraken 和 Garanti BBVA。

为了减轻这种威胁，建议 Android 用户仅从 Google Play 下载应用程序，在安装时仔细检查权限请求，并确保 Play Protect 在其设备上处于活动状态。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-droidbot-android-malware-targets-77-banking-crypto-apps/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?FNY5hHM5)

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