---
title: 跳板攻击原理及如何追踪定位攻击者主机（下）
url: https://www.4hou.com/posts/QLw9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-04
fetch_date: 2025-10-04T02:58:50.737707
---

# 跳板攻击原理及如何追踪定位攻击者主机（下）

跳板攻击原理及如何追踪定位攻击者主机（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 跳板攻击原理及如何追踪定位攻击者主机（下）

埃文科技
[行业](https://www.4hou.com/category/industry)
2023-01-03 14:00:40

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)123606

收藏

导语：在本地网络中发现跳板后，又要如何追踪定位攻击者主机？

跳板攻击溯源中，我们需要先确定本地网络中是否存在攻击者的跳板。具体可参考（[跳板攻击原理及如何追踪定位攻击者主机（上）](https://www.4hou.com/posts/8YJj)）

那么在本地网络中发现跳板后，又要如何追踪定位攻击者主机？

这种情况下需要和其上游的网络管理域进行协作，按照相同的方法进行检测，直至发现真正的网络攻击源，检测方法如下：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672712193102348.png "1672712193102348.png")

由于这一过程需要人工参与，在《Cooperative intrusion traceback and response architecture (CITRA)》一文中给出了一个自动协作的框架机制。该方法综合各个网络域中的网络设备，如防火墙、路由器等，通过多个网络域的协作来追踪攻击源。

《Inter-packet delay-based correlation for tracing encrypted connections through stepping stone》一文指出，可以对攻击路径上的各个跳板采用计算机取证的方法，通过各个跳板的日志记录来进行追踪。但这种方法受限较大，因为攻击者可能已经完全控制了跳板主机，那么这些跳板主机上的日志记录也可能已被攻击者所修改。

上述方法需要各个网络域的协作，但如果上游攻击路径上有一个或多个网络管理域无法进行合作，则很难定位真正的攻击者。

根据检测人员所掌握的资源，可以分为两种情况:

**1. 检测人员可以在网络上部署传感器**

根据攻击者的数据包是否加密，可以分为两种情况

(1) 数据包未加密

文献《Sleepy watermark tracing: an active network-based intrusion response framework》给出了一个主动的方法，即在回传给攻击者的数据包中注入水印特征，在攻击路径上部署传感器，从而追踪到攻击者。

(2) 数据包加密

文献《Robust correlation of encrypted attack traffic through stepping stones by flow watermarking》对这种情况进行了研究，所提方法实际上是《 Robust correlation of encrypted attack traffic through stepping stones by manipulation of interpacket delays》这种情况下的自然延伸。通过改变回送给攻击者的数据包的时序特征，也就是以数据包之间的间隔时间为载体来填加水印信息，从而追踪数据包的流向。

还有研究员采用对数据包的来回时间进行测量。该方法基于这样一个假设，正常的数据包发送和回复时间相差应该在一个有限的时间内， 而回传数据包经过跳板进行中继，这个时间必然远高于正常的时间差。这个时间越长，说明检测点离攻击者主机的距离越远。

**2. 检测人员无法在网络上部署传感器**

在这种情况下，攻击源定位问题仍然是一个开放的问题。目前暂未发现有研究员在这一约束条件下进行研究。

但部分研究员也有一个朴素的想法，类似于针对僵尸网络溯源的方法。

如果检测人员在攻击者未察觉的情况下能控制跳板主机在跳板主机回传给攻击者的消息中插入可执行代码，当攻击者接收到消息后， 可执行代码在攻击者主机上运行，把攻击者主机的信息发送给检测人员。不过这一思路需要根据攻击者所使用的软件工具，挖掘其漏洞，难度较大，且不具有通用性。

综上所述，对于在本地网络中发现跳板后，如何追踪定位攻击者主机？主要是以下几种解决方案:

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230103/1672712203778673.png "1672712203778673.png")

跳板攻击的隐匿性性，给互联网安全带来了很大的隐患。未来，网络安全的难度和整个网络架构的设计都将面临更大的挑战。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?g376APN6)

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

![]()

# [埃文科技](https://www.4hou.com/member/RD0Y)

埃文科技是全球领先的网络空间地图大数据服务提供商。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/RD0Y)

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