---
title: WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell
url: https://www.4hou.com/posts/gDJ9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-07
fetch_date: 2025-10-04T11:37:52.793844
---

# WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell

WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell

lucywang
[新闻](https://www.4hou.com/category/news)
2023-05-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161212

收藏

导语：WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell，允许攻击者在不触发目标系统上的安全代理的情况下植入后门，绕过系统身份验证，绕过用户身份验证。

![微信截图_20230410000459.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681056807202362.png "1681056807202362.png")

WinRAR SFX 压缩包可以在不被发现的情况下运行 PowerShell，允许攻击者在不触发目标系统上的安全代理的情况下植入后门，绕过系统身份验证，绕过用户身份验证。 Utilman.exe 受密码保护并包含一个用作装饰的空文本文件

黑客正在向WinRAR自解压档案中注入恶意功能，这些档案包含无害的诱饵文件，允许他们在不触发目标系统上的安全代理的情况下植入后门。

使用WinRAR或7-Zip等压缩软件创建的自提取档案(SFX)本质上是包含档案数据和内置解压存根(用于解压缩数据的代码)的可执行文件。可以对SFX文件进行密码保护，以防止未经授权的访问。

SFX文件的目的是简化向没有工具提取包的用户分发档案化的数据。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681056819449303.png "1681056819449303.png")

使用7-Zip创建受密码保护的SFX

网络安全公司CrowdStrike的研究人员在最近的事件响应调查中发现了SFX滥用。

**野外发现的SFX攻击**

Crowdstrike的分析发现，攻击者使用窃取的凭据来滥用“utiman .exe”，并将其设置为启动之前植入系统上的受密码保护的SFX文件。

Utilman是一个可访问性应用程序，可以在用户登录之前执行，经常被黑客滥用以绕过系统身份验证。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681056836763687.png "1681056836763687.png")

登录界面上的utilman工具

由utiman .exe触发的SFX文件有密码保护，其中包含一个用作诱饵的空文本文件。

SFX文件的真正功能是滥用WinRAR的设置选项，以系统权限运行PowerShell、Windows命令提示符（cmd.exe）和任务管理器。

CrowdStrike的Jai Minton仔细研究了所使用的技术，发现攻击者在目标提取档案的文本文件后添加了多个命令来运行。

虽然档案中没有恶意软件，但攻击者在设置菜单下添加了创建SFX档案的命令，该档案将打开系统的后门。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681056853359180.png "1681056853359180.png")

WinRAR SFX设置中允许后门访问的命令

如上图所示，注释显示攻击者自定义了SFX档案，以便在提取过程中不显示对话框和窗口。攻击者还添加了运行PowerShell、命令提示符和任务管理器的指令。

WinRAR提供了一组高级SFX选项，允许添加一个可执行文件列表，以便在进程之前或之后自动运行，如果存在同名条目，还可以覆盖目标文件夹中的现有文件。

Crowdstrike解释说：“因为这个SFX档案可以从登录屏幕上运行，所以攻击者实际上有一个持久的后门，只要提供了正确的密码，就可以访问它来运行PowerShell、Windows命令提示符和具有NT AUTHORITY\SYSTEM权限的任务管理器。这种类型的攻击很可能不会被传统的防病毒软件发现，因为传统的防病毒软件寻找的是档案(通常也有密码保护)内部的恶意软件，而不是来自SFX档案解压缩存根的行为。”

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681056867207176.png "1681056867207176.png")

观察到的攻击链

Crowdstrike声称恶意SFX文件不太可能被传统的反病毒解决方案捕获。但在实际测试中，当我们创建自定义的SFX档案以在提取后运行PowerShell时，Windows Defender还是会做出反应。

微软的安全代理检测到生成的可执行文件是一个被追踪为Wacatac的恶意脚本，并将其隔离。然而，我们只记录了一次这种反应，无法复制。

研究人员建议用户特别注意SFX档案，并使用适当的软件检查档案的内容，并寻找提取时计划运行的潜在脚本或命令。

本文翻译自：https://www.bleepingcomputer.com/news/security/winrar-sfx-archives-can-run-powershell-without-being-detected/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GwFo0bSf)

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

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

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

[查看更多](https://www.4hou.com/member/eXPv)

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