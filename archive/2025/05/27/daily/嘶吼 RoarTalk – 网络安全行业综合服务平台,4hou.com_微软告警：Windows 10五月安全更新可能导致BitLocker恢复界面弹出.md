---
title: 微软告警：Windows 10五月安全更新可能导致BitLocker恢复界面弹出
url: https://www.4hou.com/posts/J1xJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-27
fetch_date: 2025-10-06T22:27:05.077370
---

# 微软告警：Windows 10五月安全更新可能导致BitLocker恢复界面弹出

微软告警：Windows 10五月安全更新可能导致BitLocker恢复界面弹出 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微软告警：Windows 10五月安全更新可能导致BitLocker恢复界面弹出

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)57774

收藏

导语：目前，这些报告指出联想、戴尔和惠普的各种系统配置和设备都受到了影响，所以目前还不清楚这是由特定的硬件还是软件问题引起的。

微软已经确认，一些Windows 10和Windows 10企业LTSC 2021系统将在安装2025年5月的安全更新后启动到BitLocker恢复。

BitLocker Windows安全功能对存储驱动器进行加密，以防止数据被盗，Windows计算机通常在TPM（可信平台模块）更新或硬件更改等事件后进入BitLocker恢复模式，以重新访问受保护的驱动器。

上周，微软证实了这个问题，并表示正在调查“少数”Windows 10电脑在安装KB5058379更新后显示BitLocker恢复屏幕的报告。

在受影响的设备上，在安装更新后，Windows可能无法启动足够多的时间来触发自动修复。在启用了BitLocker的设备上，BitLocker需要输入用户的BitLocker恢复密钥来启动自动修复。

检查Windows事件查看器的受影响用户还将在系统事件日志中看到带有0x800F0845错误的LSASS错误和安装失败事件。此外，虽然有些设备在启动修复失败后会进入BitLocker恢复循环，但其他设备在多次尝试安装KB5058379后会成功回滚到以前安装的更新。

用户可以通过登录到BitLocker恢复屏幕门户与微软帐户检索BitLocker恢复密钥。此支持页提供了有关如何在Windows中查找恢复密钥的进一步详细信息。

微软表示，他们正在调查这一问题，一旦获得有关根本原因的更多信息，他们将提供更新。

![BitLocker recovery screen.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250519/1747625689160311.png "1747625663158644.png")

BitLocker恢复屏幕

在微软承认这个问题之前，许多Windows用户和管理员报告说，在安装了KB5058379累积更新（作为2025年5月补丁星期二的一部分发布）后，他们看到设备意外地进入Windows恢复环境（WinRE）并显示BitLocker恢复屏幕。

目前，这些报告指出联想、戴尔和惠普的各种系统配置和设备都受到了影响，所以目前还不清楚这是由特定的硬件还是软件问题引起的。

要在系统卡在BitLocker恢复提示符上回到Windows，可以尝试从BIOS中禁用英特尔可信执行技术（TXT）。如果失败了，也可以尝试禁用安全引导、虚拟化技术（如果问题仍然存在）或固件保护。

2024年8月，微软修复了另一个问题，即在安装2024年7月的Windows安全更新后，在Windows 10、Windows 11和Windows Server系统上触发BitLocker恢复提示。

2022年8月，在KB5012170安全更新导致一些设备启动进入BitLocker恢复屏幕后，Windows设备也受到了类似问题的影响。

文章翻译自：https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-may-windows-10-updates-trigger-bitlocker-recovery/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?O17hpv5n)

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