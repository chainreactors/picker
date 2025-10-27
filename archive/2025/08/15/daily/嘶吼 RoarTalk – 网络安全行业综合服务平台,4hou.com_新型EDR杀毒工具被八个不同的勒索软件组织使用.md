---
title: 新型EDR杀毒工具被八个不同的勒索软件组织使用
url: https://www.4hou.com/posts/gy46
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-15
fetch_date: 2025-10-07T00:18:12.733595
---

# 新型EDR杀毒工具被八个不同的勒索软件组织使用

新型EDR杀毒工具被八个不同的勒索软件组织使用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型EDR杀毒工具被八个不同的勒索软件组织使用

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)59328

收藏

导语：该工具不太可能是被泄露后再被其他威胁者复用，而更可能是通过一个共享协作框架开发的。

一种新型端点检测与响应（EDR）杀毒工具已在8个不同勒索软件团伙的攻击中被发现，该工具被认为是RansomHub开发的“EDRKillShifter”的升级版。

这类工具能帮助勒索软件操作者关闭已入侵系统上的安全产品，从而在不被发现的情况下部署有效载荷、提升权限、尝试横向移动，并最终加密网络中的设备。

据Sophos安全研究人员介绍，这款尚未被赋予特定名称的新工具，已被RansomHub、Blacksuit、Medusa、Qilin、Dragonforce、Crytox、Lynx和INC等团伙使用。

这款新型EDR杀毒工具采用高度混淆的二进制文件，在运行时会自行解码并注入到合法应用程序中。

该工具会搜索一个带有随机五字符名称的数字签名驱动程序（签名可能是被盗或过期的），这个名称被硬编码到可执行文件中。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250811/1754899097128365.png "1754898357147969.png")

恶意驱动程序使用的被盗和过期的证书

一旦找到，恶意驱动程序就会加载到内核中——这是执行“自带漏洞驱动程序”（BYOVD）攻击并获取关闭安全产品所需的内核权限的必要步骤。

该驱动程序伪装成合法文件（如CrowdStrike Falcon传感器驱动程序），但一旦激活，就会终止与反病毒（AV）/EDR相关的进程，并停止安全工具的关联服务。

其针对的厂商包括Sophos、Microsoft Defender、Kaspersky、Symantec、Trend Micro、SentinelOne、Cylance、 McAfee、F-Secure、HitmanPro和Webroot。

尽管这款新型EDR杀毒工具的不同变体在驱动程序名称、目标反病毒软件和构建特征上存在差异，但它们都使用HeartCrypt进行打包，且有证据表明，即便是相互竞争的威胁团伙之间也存在知识和工具共享。

Sophos特别指出，该工具不太可能是被泄露后再被其他威胁者复用，而更可能是通过一个共享协作框架开发的。需要明确的是，并非是某个EDR的单一二进制文件被泄露后在威胁者之间共享，而是每次攻击都使用了这款专有工具的不同构建版本。这种工具共享策略，尤其是在EDR杀毒方面，在勒索软件领域十分常见。

除了EDRKillShifter，Sophos还发现了另一个名为AuKill的工具，已被Medusa Locker和LockBit用于攻击中。SentinelOne去年也曾报告，FIN7黑客将其定制的“AvNeutralizer”工具出售给多个勒索软件团伙，包括BlackBasta、AvosLocker、MedusaLocker、BlackCat、Trigona和LockBit。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-edr-killer-tool-used-by-eight-different-ransomware-groups/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?sgIQ9BWi)

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