---
title: 新恶意软件 Plague Linux 允许攻击者获得 SSH 访问权限
url: https://www.4hou.com/posts/42o1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-13
fetch_date: 2025-10-07T00:13:17.785396
---

# 新恶意软件 Plague Linux 允许攻击者获得 SSH 访问权限

新恶意软件 Plague Linux 允许攻击者获得 SSH 访问权限 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新恶意软件 Plague Linux 允许攻击者获得 SSH 访问权限

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)58523

收藏

导语：Plague后门对Linux基础设施构成了复杂而不断发展的威胁，它利用核心身份验证机制来保持隐身性和持久性。

新发现的Linux恶意软件在完成逃避检测后，开始允许攻击者获得持久的SSH访问权限，并绕过受感染系统的身份验证。

Nextron Systems 的安全研究人员发现了该恶意软件，并将其命名为“Plague”。他们将其描述为一种恶意的可插拔认证模块（PAM），使用分层混淆技术和环境篡改来逃避传统安全工具的检测。

该恶意软件具有反调试功能，以阻止分析和逆向工程尝试，字符串混淆以使检测更加困难，硬编码密码以实现秘密访问，以及隐藏会话痕迹的能力，这些会话工件通常会暴露攻击者在受感染设备上的活动。

一旦加载，它还将清除运行时环境中任何恶意活动的痕迹，方法是取消与SSH相关的环境变量，并将命令历史重定向到/dev/null以防止日志记录，消除审计跟踪和登录元数据，并从系统历史日志和交互式会话中清除攻击者的数字足迹。

Plague深入集成到身份验证堆栈中，在系统更新中幸存下来，几乎不会留下任何痕迹。结合分层混淆和环境篡改，这使得使用传统工具检测异常困难。

恶意软件会主动清除运行时环境，以消除SSH会话的证据。使用unsetenv取消SSH\_CONNECTION和SSH\_CLIENT等环境变量的设置，而HISTFILE被重定向到/dev/null以防止shell命令记录。

在分析恶意软件时，研究人员还发现了编译工件，表明在很长一段时间内进行了积极的开发，使用不同Linux发行版的各种GCC版本编译了示例。

此外，尽管在过去的一年中有多个后门变种被上传到VirusTotal，但没有一个反病毒引擎将其标记为恶意软件，这表明恶意软件的创建者一直在未被发现的情况下运行。

Pezier补充说：“Plague后门对Linux基础设施构成了复杂而不断发展的威胁，它利用核心身份验证机制来保持隐身性和持久性。”由于它使用高级混淆、静态凭证和环境篡改，使得使用传统方法检测特别困难。

今年5月，Nextron Systems发现了另一种恶意软件，它利用了PAM (Pluggable Authentication Modules) Linux身份验证基础设施的灵活性，使其创建者能够窃取凭证，绕过身份验证，并在受损设备上获得隐秘的持久性。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-plague-malware-backdoors-linux-devices-removes-ssh-session-traces/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KnvbWTrW)

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