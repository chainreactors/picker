---
title: SmartAttack攻击利用智能手表从物理隔离系统窃取数据
url: https://www.4hou.com/posts/7Mqr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-18
fetch_date: 2025-10-06T22:52:25.756330
---

# SmartAttack攻击利用智能手表从物理隔离系统窃取数据

SmartAttack攻击利用智能手表从物理隔离系统窃取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SmartAttack攻击利用智能手表从物理隔离系统窃取数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)71597

收藏

导语：SmartAttack需要恶意软件以某种方式感染与互联网物理隔离的计算机，以收集诸如键盘输入、加密密钥和凭证等敏感信息。然后，它可以利用计算机的内置扬声器向环境中发出超声波信号。

一种名为“SmartAttack”的新攻击利用智能手表作为隐蔽的超声波信号接收器，从物理隔离（air-gapped）系统中窃取数据。

物理隔离系统通常部署在关键任务环境中，如政府设施、武器平台和核电站，它与外部网络物理隔离，以防止恶意软件感染和数据盗窃。

尽管如此，它们仍然容易受到内部威胁的影响，比如恶意员工使用USB驱动器或国家支持的供应链攻击。一旦被渗透，恶意软件就可以秘密运作，使用隐秘的技术来调节硬件组件的物理特性，在不干扰系统正常运行的情况下将敏感数据传输到附近的接收器。

SmartAttack是由Mordechai Guri领导的以色列大学研究人员设计的。虽然在许多情况下，对空气间隙环境的攻击是理论上的，而且很难实现，但它们仍然提供了有趣和新颖的方法来窃取数据。

**SmartAttack如何工作**

SmartAttack需要恶意软件以某种方式感染与互联网物理隔离的计算机，以收集诸如键盘输入、加密密钥和凭证等敏感信息。然后，它可以利用计算机的内置扬声器向环境中发出超声波信号。

通过使用二进制频移键控（B-FSK），音频信号频率可以被调制以表示二进制数据，即“0”和“1”。18.5 kHz的频率表示“0”，而19.5 kHz表示“1”。

![inter.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250617/1750124448154344.jpg "1749698244846423.jpg")

隐蔽信道和键盘输入的干扰

人类听不到这个范围的频率，但附近的人戴的智能手表麦克风却可以捕捉到它们。智能手表中的声音监测应用程序使用信号处理技术来检测频移并解调编码信号，同时还可以应用完整性测试。数据的最终泄露可以通过Wi-Fi、蓝牙或蜂窝连接进行。智能手表可能会被恶意员工故意安装这种工具，也可能在佩戴者不知情的情况下被外部人员感染。

**性能和局限性**

研究人员指出，与智能手机相比，智能手表使用的是更小、信噪比更低的麦克风，因此信号解调相当具有挑战性，尤其是在更高频率和更低信号强度的情况下。

研究发现，即使手腕的方向对攻击的可行性也起着至关重要的作用，当手表与电脑扬声器处于“视线范围”时，攻击效果最好。

根据发射器（扬声器类型），最大传输范围在6到9米（20 - 30英尺）之间。

![transmitter.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250617/1750124449189484.png "1749698322171625.png")

发射机性能

数据传输速率范围为5bps ~ 50bps，随着速率和距离的增加，可靠性逐渐降低。

![table(2).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250617/1750124450133854.png "1749698370685466.png")

性能测量（信噪比、误码率）

研究人员表示，最好的应对 SmartAttack 的方法是禁止在安全环境中使用智能手表。另一种措施是移除空气隔离机器中的内置扬声器。这将消除所有声学秘密通道的攻击面，而不仅仅是SmartAttack。

如果以上方法都不可行，通过发射宽带噪声进行超声波干扰、基于软件的防火墙和音频阻塞仍然可能有效。

文章翻译自：https://www.bleepingcomputer.com/news/security/smartattack-uses-smartwatches-to-steal-data-from-air-gapped-systems/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OcZG6XQC)

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