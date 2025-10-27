---
title: 【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道
url: https://www.4hou.com/posts/9AGJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:38.566061
---

# 【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道

【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道

北京观成科技
[技术](https://www.4hou.com/category/technology)
2023-07-31 10:02:45

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125154

收藏

导语：在网络安全领域，隐蔽隧道是一种基于主流常规协议将恶意流量伪装成正常通信起到夹带偷传数据、下发控制指令等作用，同时对数据进行加密以最大限度的规避网络安全设备检测的传输技术。

**一、概述**

在网络安全领域，隐蔽隧道是一种基于主流常规协议将恶意流量伪装成正常通信起到夹带偷传数据、下发控制指令等作用，同时对数据进行加密以最大限度的规避网络安全设备检测的传输技术。由于隐蔽隧道更容易绕过网络安全设备的检测，因此黑客对其的使用越来越广泛，在攻防演练中，隐蔽隧道更是攻击中必不可少的一环，在攻击队完成初始打点后，通常会建立外联隐蔽隧道以维持内网权限，并进一步通过横向移动最终获得靶标，而隐蔽隧道的种类繁多，从协议的视角来看，常见的隧道种类有HTTP隧道、DNS隧道、ICMP隧道、SSH隧道、TCP隧道、UDP隧道等，这其中最为常见的当属HTTP隧道，所以了解HTTP隐蔽隧道的特点及其对应的黑客工具，对于防御方来说是至关重要的。

**二、HTTP隧道详解**

HTTP隧道是一种基于HTTP协议实现的网络隧道，可以将任意类型的网络流量通过HTTP协议的数据包进行传输，从而实现对网络流量的加密和隐藏，WebShell、代理转发、远控回连等场景都能看到HTTP隧道活跃的身影。HTTP隧道的主要特点包括：高效稳定、灵活隐蔽、适合加密，本文将详细介绍HTTP隧道的主要特点和常用工具。

**1、HTTP隧道的主要特点**

高效稳定：得益于作为隧道载体的HTTP协议成熟且强大，攻击者可以使用标准HTTP协议带来的一切便利，例如：简单请求-响应模式带来的稳定性、支持长连接与数据压缩带来的高传输性能与易于控制和管理等，这让它可以很容易的适用于不同类型的网络环境和应用场景。

灵活隐蔽：HTTP隧道良好扩展性带来的高度可定制化能力，它可以自由的将需要传输的数据放在HTTP请求/响应头或者HTTP载荷数据中的任意位置，不必局限于固定的某个字段，并且偷传数据的同时还可以伪装成正常的上网行为或者普通的HTTP业务流量，在网络基础设施高度发达的今天，还有CDN、云函数等正经业务被用作其保护伞，这种隐蔽性非常强，可以很好的避免其被流量检测设备和防火墙检测出来，有效提高了隧道通信的存活能力。

![【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道-v2(4)874.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230720/1689823666642611.png "1689823564644495.png")

图 1 利用CDN传输数据

适合加密：HTTP隧道天生适合加密传输数据，因为HTTP协议本身就支持了URL编码、Base64编码、Gzip编码、Deflate编码、二进制编码、Multiformat编码等各式各样的加密、压缩与传输编码方式，所以在此之上再对数据进行一层从简单如XOR到复杂如AES的加密就让真实的攻击更难被与正常业务流量区分开来。不仅如此，HTTP隧道很多时候还可以披上TLS的外衣摇身一变成为HTTPS协议，这种嵌套加密技术成本极低，但检测难度却变的极大。

![【攻防演练篇】攻防演练场景中面临的常见加密威胁-HTTP隐蔽隧道-v2(4)1135.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230720/1689823667547543.png "1689823594147614.png")

图 2 叠加了多种编码方式的加密数据

**2、支持HTTP隧道的常用工具**

攻击者常用的黑客工具很多都支持HTTP隧道功能：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230720/1689823665208446.png "1689823665208446.png")

**1. Chaos：**一款C2工具，客户端上线后能够执行Shell、截屏、文件上传下载、访问指定url等功能。通信只使用HTTP协议，两秒一次的心跳包，通信全程没有加密，部分内容使用了Base64编码。

**2. CobaltStrike：**Cobalt Strike是一款流行的渗透测试工具，由Raphael Mudge开发。它提供了一个高级的图形界面，可用于通过社会工程学技术、漏洞利用和后期特权升级攻击等手段入侵受控机器，并支持使用命令和控制服务器（C2）对受感染的主机进行远程控制。它支持动态HTTP隧道，即在隧道连接过程中可以更改隧道参数，增加隧道的安全性，同时具有丰富的配置选项，可以根据具体的攻击需求进行定制，包括端口号、请求头、响应头与各种编码、加密方式等。

**3.Empire：**Empire是一款开源的渗透测试工具，可用于生成、编码和部署各种类型的攻击负载（Payload），并通过HTTP/HTTPS等协议与攻击目标进行通信。 Empire提供了一个强大的命令行界面，可用于建立、配置和控制攻击载荷，支持模块化插件架构，使其可以轻松地扩展功能。这款工具结合了HTTP摔倒与TCP隧道：木马发送HTTP请求时服务端会通过tcp返回指令内容，tcp载荷全部加密传输，当指令传输完毕，服务端会返回响应200，该响应的载荷也是加密的。

**4. Octopus：**Octopus旨在与C2进行通信时保持高度隐秘，它的第一次请求url是生成木马时自定义设置的，同时返回体中定义了aes-key、aes-iv、心跳时间以及后续使用的临时命令下发url与心跳url，在这之后将隧道使用AES-256的方式加密。在此之上还可以通过为C2服务器配置有效的证书以使用HTTPS加强隐秘性。

**5. ABPTTS：**ABPTTS是NCC Group在2016年blackhat推出的一款将TCP流量通过HTTP/HTTPS进行流量转发，在目前云主机的大环境中，发挥了比较重要的作用，可以通过脚本进行RDP,SSH,Meterpreter的交互与连接。这也意味着这样可以建立一个通过80端口的隧道流量出站来逃避防火墙。与其它http隧道不同的是，abptts是全加密。但是可惜的是，ABPTTS只支持aspx和jsp。

**三、总结**

由于HTTP隐蔽隧道拥有灵活且隐蔽的特性，传统字符串与弱特征匹配的检测方式容易被绕过，并且从单包和单会话层面想找到隧道的明显特点也非常困难。观成科技安全研究团队经过研究发现，对于HTTP隧道，可以从隧道通信的行为本身，以及攻击者对HTTP协议的使用与正常业务的区别等方面挖掘特征进行检测。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tEG5bWeC)

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

![](https://img.4hou.com/portraits/46f5700c82281335cc3d60386789cc75.png)

# [北京观成科技](https://www.4hou.com/member/KrJr)

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

[查看更多](https://www.4hou.com/member/KrJr)

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