---
title: 黑客利用伪造的恶意软件构建器感染了18,000个“script kiddies”
url: https://www.4hou.com/posts/yzAR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-27
fetch_date: 2025-10-06T20:08:02.988741
---

# 黑客利用伪造的恶意软件构建器感染了18,000个“script kiddies”

黑客利用伪造的恶意软件构建器感染了18,000个“script kiddies” - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用伪造的恶意软件构建器感染了18,000个“script kiddies”

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-01-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105492

收藏

导语：他们向所有听众客户端发送了一个大规模卸载命令，遍历以前从电报日志中提取的所有已知机器ID。

黑客分子利用伪造的恶意软件构建器以被称为 “script kiddies（脚本小子）” 的低技能黑客为目标，通过后门秘密感染他们，以窃取数据并接管其计算机。

CloudSEK 的安全研究人员报告称，该恶意软件感染了全球 18,459 台设备，其中大部分位于俄罗斯、美国、印度、乌克兰和土耳其。 CloudSEK 报告中写道：“XWorm RAT 构建器的木马版本已被武器化并传播。” CloudSEK 发现该恶意软件包含一个终止开关，该开关被激活以从许多受感染的计算机上卸载恶意软件，但由于实际限制，某些计算机仍然受到损害。

![hackers.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250126/1737860532172950.png "1737860204168501.png")

受感染设备的位置

**假 RAT 构建器安装恶意软件**

研究人员表示，他们最近发现了一个木马化的 XWorm RAT 构建器通过各种渠道分发，包括 GitHub 存储库、文件托管平台、Telegram 频道、YouTube 视频和网站。这些消息来源宣传了 RAT 构建器，称它将允许其他威胁者利用该恶意软件而无需付费。

它是用恶意软件感染受害者设备，一旦计算机感染了机器，X虫恶意软件就会检查Windows注册表是否有迹象是否在虚拟化环境上运行，如果结果为正面，则停止。如果主机有资格获得感染，则恶意软件会执行所需的注册表修改，以确保系统启动之间的持久性。每个受感染的系统都使用硬编码的电报机器人ID和令牌注册为基于电报的命令和控制服务器（C2）服务器。

恶意软件还会自动窃取Diskord令牌，系统信息和位置数据（来自IP地址），并将其删除到C2服务器。然后，它等待运营商的命令。在总共支持的56个命令中，以下特别危险：

**·**/machine\_id\*browsers – 从网络浏览器窃取保存的密码、cookie 和自动填充数据

**·**/machine\_id\*keylogger – 记录受害者在计算机上输入的所有内容

**·**/machine\_id\*desktop – 捕获受害者的活动屏幕

**·**/machine\_id\*encrypt\*

**·**/machine\_id\*processkill\*

**·**/machine\_id\*上传\*

**·**/machine\_id\*uninstall – 从设备中删除恶意软件

CloudSEK 发现恶意软件操作者从大约 11% 的受感染设备中窃取了数据，主要是截取受感染设备的屏幕截图（如下所示）并窃取浏览器数据。

![screenshot.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250126/1737860533141526.png "1737860349340090.png")

来自黑客桌面的屏幕截图

**利用开关破坏僵尸网络**

Cloudsek的研究人员通过使用硬编码的API令牌和内置的杀伤开关来破坏僵尸网络，从而从受感染的设备中卸载了恶意软件。

为此，他们向所有听众客户端发送了一个大规模卸载命令，遍历以前从电报日志中提取的所有已知机器ID。他们还假设一个简单的数字模式，从1到9999刻录了机器ID。

![unisntall.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250126/1737860534174374.png "1737860412203787.png")

发送卸载命令

尽管这导致恶意软件被从许多受感染的机器中删除，但在发出命令时未在线的机器仍被操控。此外，某些卸载命令可能在运输中丢失，这是一种常见情况。

文章翻译自：https://www.bleepingcomputer.com/news/security/hacker-infects-18-000-script-kiddies-with-fake-malware-builder/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2EKsIK6w)

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