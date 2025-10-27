---
title: 手把手玩转路由器漏洞挖掘系列 - UPNP协议安全风险
url: https://www.4hou.com/posts/mk2A
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-24
fetch_date: 2025-10-06T18:47:07.361402
---

# 手把手玩转路由器漏洞挖掘系列 - UPNP协议安全风险

手把手玩转路由器漏洞挖掘系列 - UPNP协议安全风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 手把手玩转路由器漏洞挖掘系列 - UPNP协议安全风险

kkk
[技术](https://www.4hou.com/category/technology)
2024-10-23 13:43:58

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128080

收藏

导语：通用即插即用（英语：Universal Plug and Play，简称UPnP）是由“通用即插即用论坛”（UPnP™ Forum）推广的一套网络协议。该协议的目标是使家庭网络（数据共享、通信和娱乐）和公司网络中的各种设备能够相互无缝连接，并简化相关网络的实现。UPnP通过定义和发布基于开放、因特网通讯网协议标准的UPnP设备控制协议来实现这一目标。

## 1. 基本介绍

### 1.1 概要

通用即插即用（英语：Universal Plug and Play，简称UPnP）是由“通用即插即用论坛”（UPnP™ Forum）推广的一套网络协议。该协议的目标是使家庭网络（数据共享、通信和娱乐）和公司网络中的各种设备能够相互无缝连接，并简化相关网络的实现。UPnP通过定义和发布基于开放、因特网通讯网协议标准的UPnP设备控制协议来实现这一目标。

### 1.2 结构组成

* 设备 - UPNP规范中的最基本单元。代表一个物理设备或包含多个物理设备的逻辑设备。
* 服务 - UPNP规范中的最小控制单元。代表设备提供的服务及调用API接口。
* 控制点 - UPNP所在网络的其他网络中UPNP设备。

### 1.3 协议过程

* 发现 - 简单发现服务
* 描述 - 通过远程访问URL，XML文件格式显示服务相关信息
* 控制 - 控制信息使用SOAP协议，XML文件格式显示。

## 2. 安全风险

UPnP由于设计上的缺陷而产生的漏洞，这些其中大多数漏洞是由于服务配置错误或实施不当造成的。

* 路由器设备作为代理，对内网进行渗透测试
* 开启端口映射，访问内部计算机

## 3. 威胁分析

### 3.1 获得服务控制协议文档(SCPD)

##### (1) 部分开启服务 - 1

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OLBRuPLcbSgJTBWWBX5ZpEw389GjuTkQZjnnicLgWS4GetUHVfGzaXRg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

##### (2) 部分开启服务 - 2

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4O1pjvtkCMHdc4uWecEY5ZVvWhGC7r9CpuzVKibl3icQiaZiacaMLJLx9sSA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

开启服务汇总

```
<serviceType>urn:schemas-upnp-org:service:Layer3Forwarding:1serviceType>
<serviceId>urn:upnp-org:serviceId:L3Forwarding1serviceId>
<SCPDURL>/L3F.xmlSCPDURL>
<controlURL>/ctl/L3FcontrolURL>
<eventSubURL>/evt/L3FeventSubURL>

<serviceType>urn:schemas-upnp-org:service:DeviceProtection:1serviceType>
<serviceId>urn:upnp-org:serviceId:DeviceProtection1serviceId>
<SCPDURL>/DP.xmlSCPDURL>
<controlURL>/ctl/DPcontrolURL>
<eventSubURL>/evt/DPeventSubURL>

<serviceType>urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1serviceType>
<serviceId>urn:upnp-org:serviceId:WANCommonIFC1serviceId>
<SCPDURL>/WANCfg.xmlSCPDURL>
<controlURL>/ctl/CmnIfCfgcontrolURL>
<eventSubURL>/evt/CmnIfCfgeventSubURL>

<serviceType>urn:schemas-upnp-org:service:WANIPConnection:2serviceType>
<serviceId>urn:upnp-org:serviceId:WANIPConn1serviceId>
<SCPDURL>/WANIPCn.xmlSCPDURL>
<controlURL>/ctl/IPConncontrolURL>
<eventSubURL>/evt/IPConneventSubURL>

<serviceType>urn:schemas-upnp-org:service:WANIPv6FirewallControl:1serviceType>
<serviceId>urn:upnp-org:serviceId:WANIPv6Firewall1serviceId>
<SCPDURL>/WANIP6FC.xmlSCPDURL>
<controlURL>/ctl/IP6FCtlcontrolURL>
<eventSubURL>/evt/IP6FCtleventSubURL
```

ControlURL是与特定服务进行通信的SOAP端点（实质上，该URL的GET / POST将触发操作）。

### 3.2 服务操作(SOAP)

假若路由器设备SOAP API暴露，我们就可以对设备进行操作，从而绕过防护。

##### (1) 直接访问控制

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OA05bZgnfclMhctWG8e9YSAiboqialmDoZbEbJLc0ZReSW5CVHCZxB09Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

查看具体服务参数及对应接口

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OF4eiaLKwcSxgCdRltRCLibjsKC90jxDqYXaiadfF2ukl7j4TGaSnFRS2w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

##### (2) 端口映射操作

Miranda是Kali提供的一款基于Python语言的UPNP客户端工具。它可以用来发现、查询和操作UPNP设备，尤其是网关设置。当路由器开启UPNP功能，存在相应的漏洞，就可以通过Miranda进行渗透和控制。

https://github.com/kimocoder/miranda

优势 - 无需认证

* 将路由器80端口映射在外网端口8443

```
$ upnp> host send 0 WANConnectionDevice WANIPConnection AddPortMapping
```

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OaicoEYWvRFbuPhEFPlRVfEt9LINrd7sAmbnGXV36hqXSgyIFduVicErw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

* 获取设备端口映射列表

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OoH4VItrkQU8PHX0TCQZowqAEjAFlgdf6v9Rh1Xlx1jzUAiboaia6jbHA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

* 查看后端端口映射是否添加成功

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OlKR9d7Mvs6iadcorRaMQedibcuW8gdzwDZxAaXfeZo3EE20puAKlo8Pg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

* 查看映射是否成功

![Image](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQLOWYUmE1hHURRhq3n8m4OHvjKlFtHVEhrMBa0plh0HicDAicHh5sRKica2nNQia5zuOotTouXCRA0BA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

## 4. 安全风险

①代理跳板：黑客可以利用路由器的某些服务接管路由器的设备权限。

②内网渗透：边界设备开启UPNP没有做好鉴权处理，会导致攻击者通过该服务队内部网络进行内部渗透。

## 5. UPNP攻击面

* 通过SCPD获取服务控制协议文档，查看可利用服务。
* 通过SOAP进行可利用服务操作，获取设备相关敏感信息及相应权限。

## 总结

UPNP协议通过端口转发和映射等功能，简化网络设备的安全配置，提供更方便的用户体验的同时，也带来不小的安全威胁。这就需要管理者花时间去研究如何调整UPnP的设置，而不是通过部署或优化其他安全组件，来提高其所处网络的整体安全态势。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?w8DpDkJB)

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

![](https://img.4hou.com/portraits/98f79ba32940c0b6cefd012e336c1911.jpg)

# [kkk](https://www.4hou.com/member/RPoV)

NEURON

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/RPoV)

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

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文...