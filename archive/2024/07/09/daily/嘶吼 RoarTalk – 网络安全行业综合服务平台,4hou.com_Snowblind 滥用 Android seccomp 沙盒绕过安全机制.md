---
title: Snowblind 滥用 Android seccomp 沙盒绕过安全机制
url: https://www.4hou.com/posts/l0Qr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-09
fetch_date: 2025-10-06T17:39:33.089817
---

# Snowblind 滥用 Android seccomp 沙盒绕过安全机制

Snowblind 滥用 Android seccomp 沙盒绕过安全机制 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Snowblind 滥用 Android seccomp 沙盒绕过安全机制

山卡拉
[漏洞](https://www.4hou.com/category/vulnerable)
2024-07-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113707

收藏

导语：当目标防篡改库尝试打开文件时，过滤器会触发 SIGSYS 信号。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719908176207700.jpg "1719908176207700.jpg")

安全研究人员最近发现了一种名为Snowblind的新型Android银行木马，它利用了Linux内核特性seccomp，这一特性是传统上用于安全防护的。Snowblind安装了一个seccomp过滤器，用于拦截系统调用并绕过应用程序中的反篡改机制，即使这些应用程序具有强大的混淆和完整性检查。

这种新的攻击向量使得该恶意软件能够窃取登录凭据、绕过双因素认证，并窃取数据，功能非常强大。有人认为这种技术有潜力以多种方式被利用来攻击应用程序。

传统上，安卓恶意软件可利用辅助功能服务窃取用户输入或控制应用程序，但现在应用程序可以检测到恶意的辅助功能服务，迫使攻击者采用重新打包攻击来绕过检测。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719907779818731.jpg "1719907779818731.jpg")

Snowblind 的工作原理

Snowblind 是一种新恶意软件，它利用 Linux 内核安全功能 seccomp 来发起更为复杂的重新打包攻击。

与使用虚拟化的 FjordPhantom 不同，Snowblind 在应用程序的防篡改代码运行之前注入了一个带有 seccomp 过滤器的本机库，从而重定向系统调用，使应用程序无法检测到篡改，并允许恶意辅助功能服务在不被发现的情况下运行。

Seccomp 是一种Linux 内核功能，它允许用户进程定义系统调用策略，并充当沙盒机制以减少攻击面。

引入了两种模式，严格模式只允许有限的系统调用，而seccomp-bpf通过Berkeley Packet Filters提供了精细的控制。

尽管传统上 seccomp 在设备制造商的自定义内核中是分散的，但它在 Android 8（Oreo）中获得了关注，其中 Google 在 Zygote 中实现了 seccomp 来限制应用程序的系统调用，并在 CTS（兼容性测试套件）中添加了测试以确保更广泛的采用，这表明 seccomp-bpf 可能在大多数运行 Android 8 及更高版本的设备上可用，甚至可能在更早的版本上可用。

Seccomp-bpf 是 Linux 内核的一项功能，它允许进程限制其可以进行的系统调用，通过阻止进程进行未经授权的系统调用来提高安全性。

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719908015185457.jpg "1719908015185457.jpg")

结构已定义

要使用 seccomp-bpf，开发人员首先定义一个 BPF（伯克利数据包过滤器）程序，该程序指定允许哪些系统调用，可以基于系统调用号、系统调用的参数或调用进程。

一旦定义了 BPF 程序，就会使用 prctl() 系统调用将其应用于进程。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719908037212742.jpg "1719908037212742.jpg")

整合所有内容

带有 PR\_SET\_SECCOMP 选项的 prctl() 系统调用允许进程安装 seccomp 过滤器，该过滤器是一个指向 BPF 程序的指针，用于定义允许哪些系统调用。

当进程尝试进行系统调用时，内核首先检查 seccomp 过滤器，如果过滤器允许该系统调用，内核就会进行系统调用。

如果过滤器不允许系统调用，内核就会向进程返回一个错误。

![5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719908077123771.jpg "1719908077123771.jpg")

在 arm64 上执行的示例

应用程序已经采取了诸如实现自己的系统调用和混淆等对策。

Snowblind 注入了一个安装 seccomp 过滤器的本机库，允许除 open() 之外的所有系统调用。

当目标防篡改库尝试打开文件时，过滤器会触发 SIGSYS 信号。自定义信号处理程序在重新执行 open() 调用之前将原始应用程序的文件路径注入其中，从而有效地绕过防篡改检查。

本文翻译自：https://gbhackers.com/snowblind-android-seccomp-bypass/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UFS7vQxq)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/azxO)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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