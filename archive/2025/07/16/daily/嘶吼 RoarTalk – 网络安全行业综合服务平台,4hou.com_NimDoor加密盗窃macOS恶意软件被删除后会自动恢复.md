---
title: NimDoor加密盗窃macOS恶意软件被删除后会自动恢复
url: https://www.4hou.com/posts/qoEG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-16
fetch_date: 2025-10-06T23:29:08.029694
---

# NimDoor加密盗窃macOS恶意软件被删除后会自动恢复

NimDoor加密盗窃macOS恶意软件被删除后会自动恢复 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# NimDoor加密盗窃macOS恶意软件被删除后会自动恢复

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-07-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)74460

收藏

导语：该攻击链包括通过Telegram联系受害者，引诱他们运行假的Zoom SDK更新，通过Calendly和电子邮件发送，类似于最近与BlueNoroff关联的一个由Huntress管理的安全平台。

安全研究人员发现，有黑客一直在使用一种名为NimDoor的新macOS恶意软件系列，以web3和加密货币组织为目标。分析有效载荷的研究人员发现，攻击者依赖于不寻常的技术和以前未见过的基于信号的持久性机制。

该攻击链包括通过Telegram联系受害者，引诱他们运行假的Zoom SDK更新，通过Calendly和电子邮件发送，类似于最近与BlueNoroff关联的一个由Huntress管理的安全平台。

**高级macOS恶意软件**

网络安全公司SentinelOne的研究人员表示，黑客在macOS上使用c++和NimDoor编译的二进制文件（统称为NimDoor），这“是一种更不寻常的选择”。

其中一个由nimm编译的二进制文件，‘installer’，负责初始设置和分级，准备目录和配置路径。它还会将另外两个二进制文件“GoogIe LLC”和“CoreKitAgent”放入受害者的系统中。

GoogIe LLC接管收集环境数据并生成十六进制编码的配置文件，将其写入临时路径。它为持久性设置了macOS LaunchAgent (com.google.update.plist)，它在登录时重新启动GoogIe LLC，并为以后的阶段存储身份验证密钥。

攻击中使用的最先进的组件是CoreKitAgent，这是NimDoor框架的主要有效载荷，它作为事件驱动的二进制文件运行，使用macOS的kqueue机制来异步管理执行。

它实现了一个带有硬编码状态转换表的10例状态机，允许基于运行时条件的灵活控制流。最显著的特性是它基于信号的持久性机制，它为SIGINT和SIGTERM安装自定义处理程序。

![handlers.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250703/1751533359656584.jpg "1751533206131632.jpg")

为SIGINT和SIGTERM注册自定义信号处理程序

这些信号通常用于终止进程，但是当其中任何一个被捕获时，CoreKitAgent会触发一个重新安装例程，重新部署GoogIe LLC，恢复持久链。

当触发时，CoreKitAgent捕获这些信号并写入LaunchAgent用于持久化，GoogIe LLC的副本作为加载器，以及自身的副本作为木马，通过addExecutionPermissions\_user95startup95mainZutils\_u32函数设置后两者的可执行权限。这种行为确保了任何用户发起的恶意软件终止都会导致核心组件的部署，使代码能够抵御基本的防御行动。

![what.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250703/1751533360968908.jpg "1751533267136203.jpg")

当进程终止时将恶意软件组件写回磁盘

CoreKitAgent解码并运行十六进制编码的AppleScript，该AppleScript每30秒向攻击者基础设施发出信标，泄露系统数据，并通过osascript执行远程命令，提供轻量级后门。

与NimDoor执行并行，zoom\_sdk\_support.scpt触发涉及trojan1\_arm64的第二个注入链，它启动基于wss的C2通信并下载两个脚本（upl和tlgrm），以促进数据盗窃。

在“zoom\_sdk\_support. conf”的情况下，在Scpt的加载器中，研究人员注意到它包含超过10000行用于混淆目的的空白行。

Upl从web浏览器中提取数据，抓取Keychain，.bash\_history和.zsh\_history，并使用curl将其泄露到dataupload[.]store。Tlgrm专注于窃取Telegram数据库和. tempkeyencrypted，很可能使用它们来解密目标在平台上交换的消息。

![tlgrm.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250703/1751533361989675.jpg "1751533309155779.jpg")

针对Telegram数据的tlgrm脚本

总的来说，NimDoor框架和SentinelLABS分析的其他后门是与朝鲜威胁者有关的最复杂的macOS恶意软件家族。

该恶意软件的模块化使其具有灵活性，并且使用了新的技术，如基于信号的持久性，这表明朝鲜网安人员正在发展他们的工具包以扩展其跨平台能力。

文章翻译自：https://www.bleepingcomputer.com/news/security/nimdoor-crypto-theft-macos-malware-revives-itself-when-killed/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?PyKX2IyA)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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