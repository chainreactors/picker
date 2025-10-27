---
title: Interlock勒索软件采用新的FileFix攻击方式推送恶意程序
url: https://www.4hou.com/posts/RXmq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-23
fetch_date: 2025-10-06T23:23:15.788333
---

# Interlock勒索软件采用新的FileFix攻击方式推送恶意程序

Interlock勒索软件采用新的FileFix攻击方式推送恶意程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Interlock勒索软件采用新的FileFix攻击方式推送恶意程序

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63701

收藏

导语：勒索软件操作利用ClickFix来感染目标，但它转向FileFix表明攻击者很快就适应了更隐蔽的攻击方法。这是首次公开证实FileFix被用于实际的网络攻击。

黑客在Interlock勒索软件攻击中采用了一种名为“FileFix”的新技术，在目标系统上投放远程访问木马（RAT）。在过去的几个月里，随着攻击者开始使用KongTuke网络注入器（又名“LandUpdate808”）通过受感染的网站传递有效载荷，Interlock勒索软件的操作有所增加。

DFIR Report和Proofpoint的研究人员自5月以来就观察到了这种操作方式的转变。当时，受感染网站的访问者会被提示通过一个虚假的CAPTCHA +验证，然后将内容粘贴到一个运行对话框中，自动保存到剪贴板中，这是一种与ClickFix攻击一致的策略。这个技巧引导用户执行一个PowerShell脚本，该脚本获取并启动了一个基于node .js的Interlock RAT变体。

今年6月，研究人员发现了一种在野外使用的基于php的Interlock RAT变体，该变体使用的是相同的KongTuke注射器。

本月早些时候，交付包装发生了重大变化，Interlock现在切换到ClickFix方法的FileFix变体作为首选交付方法。

![2-2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250717/1752738519961675.jpg "1752738514135881.jpg")

Interlock的FileFix攻击

FileFix是由安全研究员mr.d0x开发的一种社会工程攻击技术。它是ClickFix攻击的演变，ClickFix在过去一年中成为最广泛使用的有效负载分发方法之一。

在FileFix变体中，攻击者将受信任的Windows UI元素（如文件资源管理器和HTML应用程序（. hta））作为武器，诱骗用户执行恶意的PowerShell或JavaScript代码，而不显示任何安全提醒。

通过将复制的字符串粘贴到文件资源管理器的地址栏中，提示用户“打开文件”。该字符串是一个PowerShell命令，使用注释语法伪装成文件路径。

在最近的Interlock攻击中，目标被要求将一个伪装成假文件路径的命令粘贴到文件资源管理器上，导致从trycloudflare.com下载PHP RAT并在系统上执行。

感染后，RAT会执行一系列PowerShell命令来收集系统和网络信息，并将这些数据作为结构化JSON泄露给攻击者。

DFIR报告还提到了交互式活动的证据，包括Active Directory枚举、检查备份、导航本地目录和检查域控制器。

命令和控制（C2）服务器可以发送shell命令让RAT执行、引入新的有效负载、通过Registry运行键添加持久性，或者通过远程桌面（RDP）进行横向移动。

Interlock勒索软件于2024年9月发布，著名的受害者包括德克萨斯理工大学、DaVita和Kettering Health。

勒索软件操作利用ClickFix来感染目标，但它转向FileFix表明攻击者很快就适应了更隐蔽的攻击方法。这是首次公开证实FileFix被用于实际的网络攻击。随着威胁者探索将其纳入攻击链的方法，它可能会越来越受欢迎。

文章翻译自：https://www.bleepingcomputer.com/news/security/interlock-ransomware-adopts-filefix-method-to-deliver-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?bgZJrFnD)

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