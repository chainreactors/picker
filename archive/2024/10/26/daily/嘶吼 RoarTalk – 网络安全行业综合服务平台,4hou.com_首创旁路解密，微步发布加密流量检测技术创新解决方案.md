---
title: 首创旁路解密，微步发布加密流量检测技术创新解决方案
url: https://www.4hou.com/posts/DxwY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-26
fetch_date: 2025-10-06T18:48:52.181975
---

# 首创旁路解密，微步发布加密流量检测技术创新解决方案

首创旁路解密，微步发布加密流量检测技术创新解决方案 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 首创旁路解密，微步发布加密流量检测技术创新解决方案

企业资讯
[行业](https://www.4hou.com/category/industry)
2024-10-25 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)78826

收藏

导语：目前，微步威胁感知平台TDP、威胁防御系统OneSIG已同时支持SSL/TLS加密流量的高性能解密和精准检测。

在面对越来越多的加密流量攻击时，对所有流量进行统一解密是最直接的办法。但如果采用串联部署，会因为解密过程消耗大量计算资源，导致多个网络出现性能明显下降；如果采用旁路部署，由于技术机制问题，绝大多数加密流量根本无法解密。

10月24日，微步在线发布加密流量检测技术创新解决方案，打破旁路无法解密的困境，并且同时支持旁路与串联两种部署方式，资源占用少，延迟低，无需对现有网络进行改造，即可精准检测各类加密流量攻击，整体误报率低于0.003%。目前，微步威胁感知平台TDP、威胁防御系统OneSIG已同时支持SSL/TLS加密流量的高性能解密和精准检测。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241025/1729823323137255.png "1729823323137255.png")

**加密流量检测的四大挑战**

整体而言，当前加密流量攻击检测存在四大挑战。

**第一是检测精准度低**。为了减少解密过程的资源占用，不解密检测是目前相对主流的做法。不过，该技术主要通过对会话特征、时空特征等进行分析，不能对核心加密内容进行深度拆包，在复杂网络环境中误报率甚至高达到10%以上。此外，不解密检测很难提供有效证据解释告警产生的根因，这对告警研判和进一步的关联分析都极为不利。

**第二是解密覆盖不全**。由于流量加密技术设计之初就是为了防止旁路监听窃取流量数据，因此传统旁路解密存在很大的局限性，只能解密TLS1.2以下RSA加密算法，对于椭圆曲线等加密算法无能为力。而且随着TLS1.3的大规模普及，RSA加密算法逐渐被抛弃，传统旁路解密变得更加不可用。

**第三是计算性能瓶颈**。在防火墙、WAF等网关设备上对所有流量进行中间人解密，是目前唯一能够实现完全解密的手段。但解密过程涉及到复杂的数学运算，需要消耗大量的时间和计算资源，容易出现网络波动、延迟甚至是拒绝服务，直接影响到业务的实时性和连续性。

**第四是网络改动较大**。部署独立的流量解密设备将所有资源仅用于解密计算，并将解密后的明文流量交给其他安全设备，是解决单一设备性能不足的重要手段。但独立的解密设备需要另行串接至所有网络出口，对网络结构改动较大，大幅提升了部署和运维成本，故障率也随之增加。

**轻量化+一体化解决加密流量攻击难题**

对此，微步TDP首次创新了旁路轻量化解密技术，通过在主机上部署轻量化解密Agent，可对99%以上的加密算法进行解密，打破了TLS1.3以上旁路解密几乎不可用的尴尬局面。解密后的明文流量则引流至TDP进行检测。

经过严格的实战环境测试，Agent资源占用极少，并且完美兼容各类操作系统和复杂的网络环境，不会影响业务运行。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241025/1729823344121065.png "1729823344121065.png")

在检测能力方面，TDP利用规则引擎、AI引擎、威胁情报等多项技术，可将整体误报率控制在0.003%以内，同时提供丰富的上下文帮助运营人员确定威胁跟进并进一步研判分析。

另一方面，微步OneSIG还提供了解密、检测一体化的模式，基于中间人技术实现所有入站HTTPS流量解密，有效弥补了旁路解密少量证书无法覆盖的空白，无需另行串接其他解密设备。

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241025/1729823361131240.png "1729823361131240.png")

在性能方面，OneSIG基于高性能底层架构，采用硬件解密，大幅提升了解密效率，几乎不会造成业务延迟；在防护能力方面，OneSIG可将90%以上网络攻击拦截于网络边界之外，其中0day检出率达到81%；在易用性方面，OneSIG支持透明网桥模式，能够即插即用，迅速部署上线。

值得注意的是，TDP与OneSIG既支持独立部署，也支持联动部署。经过OneSIG的自动拦截，可大幅度降低后续其他串行网关以及内网TDP等设备的告警数量，减少人工参与；当TDP发现绕过网络边界的网络攻击时，可联动OneSIG或者其他网关设备进行阻断。

微步技术合伙人赵林林表示，在近些年攻防演练中，几乎所有Web渗透、恶意软件投递都是通过加密流量发起的。此次微步TDP、OneSIG同时支持高性能解密，将为用户在未来的实战过程中，提供针对加密流量攻击的检测与响应的闭环。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?JXgbBnSZ)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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