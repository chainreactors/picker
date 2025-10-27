---
title: PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器
url: https://www.4hou.com/posts/J18o
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-30
fetch_date: 2025-10-06T18:02:19.289564
---

# PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器

PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PoorTry Windows 驱动程序进化为功能齐全的 EDR 擦除器

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-08-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)76934

收藏

导语：EDR 擦除功能使该工具在应对攻击方面比防御者更具优势，但也可能为在加密前阶段检测攻击提供新的机会。

多个勒索软件团伙用来关闭端点检测和响应 (EDR) 解决方案的恶意 PoorTry 内核模式 Windows 驱动程序已演变为 EDR 擦除器，删除了对安全解决方案的运行至关重要的文件，并使恢复变得更加困难。

尽管 Trend Micro 自 2023 年 5 月以来就警告过 Poortry 上添加了此功能，但 Sophos 现已确认在野外看到了 EDR 擦除攻击。

PoorTry 从 EDR 停用器演变为 EDR 擦除器，代表了勒索软件参与者在策略上非常激进的转变，他们现在优先考虑更具破坏性的设置阶段，以确保在加密阶段获得更好的结果。

PoorTry，也称为“BurntCigar”，于 2021 年开发，作为内核模式驱动程序，用于禁用 EDR 和其他安全软件。

该套件被多个勒索软件团伙使用，包括 BlackCat、Cuba 和 LockBit，最初引起人们注意是因为其开发人员找到了通过 Microsoft 的认证签名流程对其恶意驱动程序进行签名的方法。其他网络犯罪团伙，如 Scattered Spider也被发现使用该工具实施以凭证盗窃和 SIM 卡交换攻击为重点的入侵。

在 2022 年和 2023 年期间，Poortry 不断发展，优化其代码并使用 VMProtect、Themida 和 ASMGuard 等混淆工具来打包驱动程序及其加载器（Stonestop）以进行逃避检测。

**Evolution to a wiper**

Sophos 的最新报告基于 2024 年 7 月的 RansomHub 攻击，该攻击利用 Poortry 删除关键的可执行文件 (EXE)、动态链接库 (DLL) 和安全软件的其他重要组件。

这确保了 EDR 软件无法被防御者恢复或重新启动，从而使系统在攻击的后续加密阶段完全不受保护。该过程从 PoorTry 的用户模式组件开始，识别安全软件的安装目录以及这些目录中的关键文件。

然后，它会向内核模式组件发送请求，系统地终止与安全相关的进程，然后删除它们的关键文件。

这些文件的路径被硬编码到 PoorTry 上，而用户模式组件支持按文件名或类型删除，这使其具有一定的操作灵活性，可以覆盖更广泛的 EDR 产品。

![filetype.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240829/1724898180508042.png "1724898180508042.png")

按文件类型删除功能

该恶意软件可以进行微调，只删除对 EDR 操作至关重要的文件，从而避免在攻击风险较高的第一阶段产生不必要的噪音。

Sophos 还指出，最新的 Poortry 变体采用签名时间戳操纵来绕过 Windows 上的安全检查，并使用 Tonec Inc. 的 Internet Download Manager 等其他软件的元数据。

![properties.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240829/1724898222423293.png "1724898222423293.png")

驱动程序属性

攻击者采用了一种被称为“证书轮盘”的策略，他们部署使用不同证书签名的相同有效载荷的多个变体，以增加至少一个成功执行的机会。

![certificates.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240829/1724898262952757.png "1724898262952757.png")

随着时间的推移，用于签署 Poortry 驱动程序的各种证书

尽管人们努力追踪 PoorTry 的演变并阻止其生效，但该工具的开发人员已经表现出了适应新防御措施的非凡能力。

EDR 擦除功能使该工具在应对攻击方面比防御者更具优势，但也可能为在加密前阶段检测攻击提供新的机会。

文章翻译自：https://www.bleepingcomputer.com/news/security/poortry-windows-driver-evolves-into-a-full-featured-edr-wiper/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?HYXyBPxT)

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