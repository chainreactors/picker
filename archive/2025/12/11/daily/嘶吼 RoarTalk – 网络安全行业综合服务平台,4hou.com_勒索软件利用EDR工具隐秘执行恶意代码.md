---
title: 勒索软件利用EDR工具隐秘执行恶意代码
url: https://www.4hou.com/posts/KGwl
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-11
fetch_date: 2025-12-12T03:20:55.112217
---

# 勒索软件利用EDR工具隐秘执行恶意代码

勒索软件利用EDR工具隐秘执行恶意代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件利用EDR工具隐秘执行恶意代码

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9461

收藏

导语：Storm-0249开展的初始访问入侵活动，是根据其主要客户（即勒索软件附属团伙）的需求量身定制的。

代号为Storm-0249的初始访问中间人，正通过滥用终端检测与响应解决方案及受信任的微软Windows系统工具，实现恶意软件加载、通信链路建立与持久化驻留，为后续勒索软件攻击预先部署环境。

Storm-0249已摒弃大规模钓鱼攻击手段，转而采用更隐蔽、更高级的攻击方法。这些方法不仅攻击效果显著，且即便相关攻击路径已有详细公开文档，防御方依旧难以有效应对。

研究人员在分析一起攻击事件时发现，Storm-0249借助SentinelOne EDR组件的特性隐藏恶意活动。这一攻击手法同样适用于其他品牌的EDR产品。

**对SentinelOne EDR的滥用手段**

Storm-0249的攻击始于ClickFix社会工程学骗局，诱导用户在Windows运行对话框中粘贴并执行curl命令，以系统权限（SYSTEM）下载恶意MSI安装包。

与此同时，攻击者还会从伪造的微软域名中获取恶意PowerShell脚本，该脚本会被直接载入系统内存，全程不写入磁盘，以此规避杀毒软件的检测。

恶意MSI文件会释放一个名为SentinelAgentCore.dll的恶意动态链接库文件。研究人员表示：“攻击者将该恶意DLL文件特意放置在受害终端已安装的、合法的SentinelOne EDR组件程序SentinelAgentWorker.exe所在目录下。”

随后，攻击者通过已签名的SentinelAgentWorker程序加载该恶意DLL（即DLL侧加载技术），让恶意代码在受信任的高权限EDR进程中执行，进而实现可抵御系统更新的隐蔽持久化驻留。

ReliaQuest解释道：“由合法进程全权执行攻击者的恶意代码，其行为在安全工具看来与常规SentinelOne组件活动无异，从而绕过检测机制。”

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765359410113781.png "1765356002548877.png")

签署的可执行文件侧载恶意DLL

攻击者获取目标设备访问权限后，会借助SentinelOne组件，通过reg.exe、findstr.exe等Windows合法工具收集系统标识信息，并以加密HTTPS流量的形式传输命令与控制数据。

正常情况下，注册表查询与字符串检索这类操作会触发安全警报，但当操作源于受信任的EDR进程时，安全机制会将其判定为常规行为并忽略。

攻击者会利用MachineGuid（一种基于硬件的唯一标识符）对受入侵系统进行画像。LockBit、ALPHV等勒索软件团伙常利用该标识符将加密密钥与特定受害对象进行绑定。

这一特征表明，Storm-0249开展的初始访问入侵活动，是根据其主要客户（即勒索软件附属团伙）的需求量身定制的。

对受信任的已签名EDR进程的滥用，可绕过几乎所有传统监控手段。研究人员建议系统管理员采用基于行为的检测机制，重点识别受信任进程从非标准路径加载未签名DLL文件的异常行为。此外，加强对curl、PowerShell及各类二进制文件的执行权限管控，也有助于提升防御效果。

文章来源自：https://www.bleepingcomputer.com/news/security/ransomware-iab-abuses-edr-for-stealthy-malware-execution/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Ha7q2pYg)

#### 你可能感兴趣的

* [![]()

  AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
* [![]()

  勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
* [![]()

  Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
* [![]()

  安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
* [![]()

  国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
* [![]()

  Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)
  2025-12-11 14:17:49
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)
  2025-12-11 12:00:00
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
  2025-12-10 12:00:00
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
  2025-12-05 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

  山卡拉
* [勒索软件利用EDR工具隐秘执行恶意代码](https://www.4hou.com/posts/KGwl)

  胡金鱼
* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

  胡金鱼
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

  胡金鱼
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)

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