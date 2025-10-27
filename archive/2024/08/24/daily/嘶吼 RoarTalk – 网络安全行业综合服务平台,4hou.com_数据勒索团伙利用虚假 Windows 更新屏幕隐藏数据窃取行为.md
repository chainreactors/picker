---
title: 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为
url: https://www.4hou.com/posts/PG7n
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-24
fetch_date: 2025-10-06T18:04:01.401683
---

# 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为

数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 数据勒索团伙利用虚假 Windows 更新屏幕隐藏数据窃取行为

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-08-23 13:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)78593

收藏

导语：安全研究人员指出，在 AnyDesk 连接请求之前，它没有看到 Mad Liberator 与目标互动，也没有记录任何支持攻击的网络钓鱼尝试。

近日，一个名为 Mad Liberator 的新数据勒索团伙瞄准了 AnyDesk 用户，并运行虚假的 Microsoft Windows 更新屏幕来分散注意力，同时从目标设备窃取数据。

该行动于 7 月开始出现，虽然观察该活动的研究人员没有发现任何涉及数据加密的事件，但该团伙在其数据泄露网站上指出，他们使用 AES/RSA 算法来锁定文件。

![MadLiberator_about.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240819/1724050310185982.png "1724049599202732.png")

Mad Liberator“关于”页面

**针对 AnyDesk 用户**

在网络安全公司 Sophos 的一份报告中，研究人员表示，Mad Liberator 攻击始于使用 AnyDesk 远程访问应用程序与计算机进行未经请求的连接，该应用程序在管理公司环境的 IT 团队中很受欢迎。

目前尚不清楚威胁者如何选择其目标，但有一种理论是，Mad Liberator 会尝试潜在的地址（AnyDesk 连接 ID），直到有人接受连接请求，但该说法尚未证实。

![anydesk.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240819/1724050312194431.png "1724049660100808.png")

AnyDesk 上的连接请求

一旦连接请求被批准，攻击者就会在受感染的系统上放置一个名为 Microsoft Windows Update 的二进制文件，该二进制文件会显示一个虚假的 Windows Update 启动画面。

![fake-update.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240819/1724050313115833.png "1724049713178905.png")

伪造的 Windows 更新启动画面

该诡计的唯一目的是分散受害者的注意力，同时威胁者使用 AnyDesk 的文件传输工具从 OneDrive 帐户、网络共享和本地存储中窃取数据。在虚假更新屏幕期间，受害者的键盘被禁用，以防止破坏数据泄露过程。

安全研究人员发现，Mad Liberator 的攻击持续了大约四个小时，在数据泄露后阶段，它没有进行任何数据加密。但它仍然在共享网络目录上留下勒索信，以确保在企业环境中获得最大程度的可见性。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240819/1724050315175250.png "1724049771190672.png")

被入侵的设备被泄露勒索信

安全研究人员指出，在 AnyDesk 连接请求之前，它没有看到 Mad Liberator 与目标互动，也没有记录任何支持攻击的网络钓鱼尝试。

关于 Mad Liberator 的勒索过程，威胁者在其暗网上声明，他们首先联系被入侵的公司，并表示如果满足他们的金钱要求，他们就会“帮助”他们修复安全问题并恢复加密文件。

如果受害公司在 24 小时内没有回应，他们的名字就会被公布在勒索门户网站上，并有七天的时间联系威胁者。

在发出最后通牒后的五天内，如果受害者没有支付赎金，所有被盗文件都会被公布在 Mad Liberator 网站上，目前该网站已列出了九名受害者。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-mad-liberator-gang-uses-fake-windows-update-screen-to-hide-data-theft/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ElBy4uJR)

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