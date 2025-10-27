---
title: 攻防演练场景资产失陷后常见加密流量概况
url: https://www.4hou.com/posts/EXqm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-28
fetch_date: 2025-10-04T11:51:41.037288
---

# 攻防演练场景资产失陷后常见加密流量概况

攻防演练场景资产失陷后常见加密流量概况 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻防演练场景资产失陷后常见加密流量概况

北京观成科技
[技术](https://www.4hou.com/category/technology)
2023-07-27 09:57:03

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144893

收藏

导语：在攻防演练期间，经过信息搜集、打点后，部分攻击者利用漏洞攻击、钓鱼等方式成功获得内网资产的控制权，为了保证对失陷资产的持续控制与后续扩大战果的需要，攻击者会上传木马运行，在失陷资产与外部控制端之间建立持续的通信信道。然而，在企业网络边界上通常部署了大量的网络防护和监测设备，因此，攻击者为了躲避流量监测设备的发现，会对其使用的命令与控制信道使用各种隐藏手段，如加密、编码、伪装、利用隐蔽隧道等。

**1、概述**

在攻防演练期间，经过信息搜集、打点后，部分攻击者利用漏洞攻击、钓鱼等方式成功获得内网资产的控制权，为了保证对失陷资产的持续控制与后续扩大战果的需要，攻击者会上传木马运行，在失陷资产与外部控制端之间建立持续的通信信道。然而，在企业网络边界上通常部署了大量的网络防护和监测设备，因此，攻击者为了躲避流量监测设备的发现，会对其使用的命令与控制信道使用各种隐藏手段，如加密、编码、伪装、利用隐蔽隧道等。

**2、攻防演练场景资产失陷后常见加密流量**

我们可以将攻防演练场景中，内部资产失陷后常见的加密流量总结为两大类：正向C&C加密通道和反弹C&C加密通道。

正向的C&C加密通道，主要是HTTP/HTTPS的Webshell连接和正向HTTP隧道代理；反弹C&C加密通道包括：TLS/SSL木马回连以及各种隐蔽隧道通信。

能够在内外网之间构建加密C&C通道的工具有很多，有的工具小巧且专业，能够搭建某一种加密信道并灵活配置，如：dns2cat，icmptunnel等；有的则具备平台级的强大功能，可以生成具备多种加密隧道的攻击载荷，如：CobaltStrike，MSF等；另外，还可以组合隧道工具与平台级攻击载荷在极端条件下实现命令与控制，如：利用代理转发工具、隧道工具上线CS等，下面是一些攻击类型与攻击工具的梳理：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422950147349.png "1690422911886976.png")

**2.1正向C&C加密通道**

**·** HTTP/HTTPS Webshell连接

通常，针对Web服务的漏洞利用成功后，攻击者会上传Webshell，如：冰蝎、哥斯拉、蚁剑等。这些Webshell即能在失陷的Web服务器与攻击者之间维持命令执行通道，又能用来上传具有更强大功能的平台级木马。随着Web服务的全面加密化，Webshell的通信经过了HTTPS加密，即使能够解密HTTPS流量，其HTTP载荷中也会经过二次加密和编码，尽可能不暴露明文特征，给流量检测带来很大挑战，去年攻防演练第一天更新上线的冰蝎4.0版本，临时增加可自定义的加密通信方式，给防守方带来了一波突然袭击，让人记忆犹新。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422951164366.png "1684231098743058.png")

往期回顾：冰蝎4.0 <https://www.viewintech.com/html/articledetails.html?newsId=20>

**·**HTTP隧道正向代理

当攻击者想要访问的内网资产无法出网时，可以通过在失陷的边界资产搭建HTTP隧道正向代理的方式，中转访问内网资产，常见工具包括reDuh，neo-regeorg等，其原理如下图：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422952335798.png "1684231106166143.png")

**2.2反弹C&C加密通道**

**·**TLS/SSL木马回连

出入企业网络边界最常见的加密协议是TLS/SSL，其广泛应用于Web服务、邮件服务、文件传输、移动APP等应用领域，可以保护用户通信数据的机密性和完整性。因此，大量攻击者同样通过TLS/SSL构建自己的恶意C&C加密通信信道，特别是网络边界设备通常不对出网的TLS/SSL流量做拦截，失陷资产上的木马可以通过这种方式将自己的流量混在大量访问网络正常应用的TLS/SSL加密流量中，神不知鬼不觉的与外网控制端维持C&C通信，这类工具或木马比较常见的像CobaltStrike、Sliver等，高水平的攻击者还会使用诸如：域前置、CDN、云函数等C&C隐匿技术，进一步隐藏自己的流量和控制端信息。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422953526690.png "1684231114815432.png")

攻击者在构建真实的TLS/SSL加密C&C信道时，由于SSL证书的购买和认证需要填写真实身份信息，且价格不低，导致攻击者会倾向于使用免费或自签名证书，从而为检测提供线索。于是，有些攻击者使用Fake TLS或Shadow TLS的技术，利用知名网站的证书将其木马C&C通信的流量伪装成与白站的通信，再将自己实现的加密通信协议隐藏在TLS/SSL加密载荷中，从而做到逃避检测。

**·**隐蔽隧道

在2022年攻防演练中，我们发现多起利用DNS隧道和ICMP隧道作为隐蔽信道的加密C&C通信事件，是最有代表性的隐蔽隧道通信方式。

**DNS隧道**

DNS是互联网上重要的域名服务，主要用于域名与IP地址的相互转换，因此，在企业网络中DNS流量通常不会被防火墙、入侵检测系统、安全软件等一般安全策略阻挡。攻击者利用这一特点使用DNS协议作为内外网之间通信的隐蔽信道，在攻防演练场景下常见的DNS隧道原理大致如下图所示：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422953846261.png "1684231122933865.png")

攻击者攻陷内网资产后，植入木马，木马使用DNS协议中的子域名加密编码隐藏信息，并发出DNS请求查询；内网DNS服务器将查询转发到互联网DNS服务器，通常网络监测设备捕获的是位于这一段链路上的流量；外网DNS服务器经过递归查询重定向到伪造的DNS服务器，解析隐蔽传输的信息后利用DNS响应包返回控制命令；DNS响应包穿透网络边界最终返回到内网受控资产；受控资产上的木马解析响应包中的控制命令，继续后续攻击动作。

**ICMP隧道**

类似的，ICMP协议作为网络中传递控制信息的常见重要协议，往往限制较少或不加限制，所以攻击方在攻入内网后也可能使用ICMP协议的载荷数据（Data）部分隐蔽的进行控制指令或窃密数据的传输，这些被传输的内容大多数进行了加密保护。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422954347064.png "1684231131178761.png")

如下图所示，利用ICMP回显请求和响应包（PING）载荷隐蔽实现C&C通信。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422955135055.png "1684231137452294.png")

**其他隧道**

除此以外，利用应用层常见协议HTTP、SSH的隐蔽隧道，利用TCP、UDP载荷实现自定义协议的TCP、UDP隧道，或者支持多种隧道通信的各种代理转发工具，也是攻击者较常使用的隐蔽C&C通信手段，他们在不同的网络环境下，都具有穿透网络边界隐蔽传输数据的能力。在某些内网目标不能出网的环境，攻击者还可以组合使用各种隐蔽隧道、代理转发手段，来间接上线CS、MSF木马，实现远程控制。

**3、总结**

随着近年来，加密流量在攻防对抗中的使用频率越来越高，针对攻防演练场景下的加密流量威胁，特别是资产失陷后的加密C&C通信的检测，可以说是守护企业网络的最后一道防线。观成科技多年来专注于加密流量威胁检测技术研究，形成了一套综合利用多模型机器学习、指纹检测、行为检测、加密威胁情报的解决方案，对各种不同类型的加密威胁进行有针对性的检测。在2022年的攻防演练中，观成瞰云-加密威胁智能检测系统首次参与即有亮眼发挥，多次独家检出攻击失陷阶段的加密C&C通信行为，做到及时发现，及时预警，为客户最大程度减少损失做出贡献。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230727/1690422956897237.png "1684231149314909.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ghNrI0zY)

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