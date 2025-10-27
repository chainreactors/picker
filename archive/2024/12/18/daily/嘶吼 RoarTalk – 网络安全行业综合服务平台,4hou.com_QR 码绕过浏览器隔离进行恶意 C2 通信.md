---
title: QR 码绕过浏览器隔离进行恶意 C2 通信
url: https://www.4hou.com/posts/wx2z
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-18
fetch_date: 2025-10-06T19:36:08.177457
---

# QR 码绕过浏览器隔离进行恶意 C2 通信

QR 码绕过浏览器隔离进行恶意 C2 通信 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# QR 码绕过浏览器隔离进行恶意 C2 通信

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-12-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113125

收藏

导语：其研究没有考虑额外的安全措施，例如域名信誉、URL 扫描、数据丢失防护和请求启发式，这些措施在某些情况下可能会阻止这种攻击或使其无效。

浏览器隔离是一种日益流行的安全技术，它通过云环境或虚拟机中托管的远程 Web 浏览器路由所有本地 Web 浏览器请求，所访问网页上的任何脚本或内容都在远程浏览器而不是本地浏览器上执行。

然后，页面的渲染像素流被发送回发出原始请求的本地浏览器，仅显示页面的外观并保护本地设备免受任何恶意代码的侵害。许多命令和控制服务器利用 HTTP 进行通信，导致远程浏览器隔离以过滤恶意流量，并使这些通信模型无效。

Mandiant 发现了一种绕过浏览器隔离技术并通过 QR 码实现命令和控制操作的新方法，Mandiant的新技术试图绕过这些限制，尽管它有一些实际限制，但它表明浏览器中现有的安全保护还远远不够完美，需要结合额外措施的“纵深防御”策略。

**C2 和浏览器隔离的背景**

C2 通道支持攻击者和受感染系统之间的恶意通信，使远程攻击者能够控制受破坏的设备以及执行命令、窃取数据等。由于浏览器在设计上不断与外部服务器交互，因此会激活隔离措施，以防止攻击者在安全关键环境中访问底层系统上的敏感数据。

这是通过在云端、本地虚拟机或本地托管的单独沙盒环境中运行浏览器来实现的。当隔离处于活动状态时，隔离的浏览器会处理传入的 HTTP 请求，并且只有页面的可视内容会流式传输到本地浏览器，这意味着 HTTP 响应中的脚本或命令永远不会到达目标。

这会阻止攻击者直接访问 HTTP 响应或向浏览器注入恶意命令，从而使隐蔽的 C2 通信变得更加困难。

![isolation.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733730224839836.png "1733729142145470.png")

浏览器隔离概述

**Mandiant的绕行技巧**

Mandiant 研究人员设计了一种新技术，可以绕过现代浏览器中现有的隔离机制。攻击者不是将命令嵌入到 HTTP 响应中，而是将它们编码在网页上直观显示的二维码中。

由于在浏览器隔离请求期间网页的视觉渲染不会被剥离，因此二维码能够将其返回给发起请求的客户端。在 Mandiant 的研究中，“受害者”的本地浏览器是一个无头客户端，由之前感染过该设备的恶意软件控制，该客户端会捕获检索到的二维码并对其进行解码以获取指令。

![attack.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733730224901434.png "1733729199114873.png")

使用二维码绕过浏览器隔离

Mandiant 的概念验证演示了对最新 Google Chrome 网络浏览器的攻击，通过 Cobalt Strike 的外部 C2 功能（一种广泛滥用的笔测试工具包）集成植入程序。

虽然 PoC 显示攻击是可行的，但该技术并非完美无缺，特别是考虑到现实世界的适用性。

首先，数据流的最大大小被限制为 2,189 字节，大约是 QR 码可以携带的最大数据的 74%，如果在恶意软件的解释器上读取 QR 码时出现问题，则数据包的大小需要进一步减小。 其次，需要考虑延迟，因为每个请求大约需要 5 秒。这将数据传输速率限制为大约 438 字节/秒，因此该技术不适合发送大负载或促进 SOCKS 代理。

最后，Mandiant 表示，其研究没有考虑额外的安全措施，例如域名信誉、URL 扫描、数据丢失防护和请求启发式，这些措施在某些情况下可能会阻止这种攻击或使其无效。尽管Mandiant基于QR码的C2技术的带宽较低，但如果不被阻止，它仍然可能很危险。

文章翻译自：https://www.bleepingcomputer.com/news/security/qr-codes-bypass-browser-isolation-for-malicious-c2-communication/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lVWzatNC)

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