---
title: 度量BGP监测源数量对AS可见性的影响
url: https://www.4hou.com/posts/l6oV
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-22
fetch_date: 2025-10-03T23:22:20.133579
---

# 度量BGP监测源数量对AS可见性的影响

度量BGP监测源数量对AS可见性的影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 度量BGP监测源数量对AS可见性的影响

埃文科技
[行业](https://www.4hou.com/category/industry)
2022-11-21 16:58:23

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124432

收藏

导语：本文介绍了两个公开的BGP数据源项目情况；其次，从可见AS数量和可见AS边关系数量两个方面来分析度量BGP监测源中对等AS的可见性。

首先，本文介绍了两个公开的BGP数据源项目情况；其次，从可见AS数量和可见AS边关系数量两个方面来分析度量BGP监测源中对等AS的可见性。

![图片01.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997086128844.png "1668997086128844.png")

BGP数据源有2个公开的项目，分别是RIPE RIS和Route Views，它们使用路由采集器周期性地收集和存储BGP数据，能够为监测全球网络波动提供BGP数据支撑。其中，RIPE RIS项目（https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris）是RIPE机构下一个项目，该项目是一个全球路由数据采集平台；Route Views项目（http://www.routeviews.org/routeviews/）是俄勒冈州大学的一个项目，该项目实时采集全球网络路由数据。

表1：公开的BGP数据源情况

![微信图片_20221116085502.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997145121156.png "1668997145121156.png")

2、BGP监测源中对等AS的可见性度量

如表1所示，RIPE RIS有23个采集器，760个源（727个IPv4源和597个IPv6源，每8小时保存一个RIB类型文件（存放当时的完整的路由信息库），每5分钟保存一个Update类型文件（更新路由的信息）。Route Views有35个采集器，523个源（481个IPv4源和315个IPv6源），每2小时保存一个RIB类型文件，每15分钟保存一个Update类型文件。RIPE RIS和Route Views数据可分别追溯到1999年和2003年。

2.1 单个监测源对等AS的可见性度量

以RIPE RIS项目的一个监测源RRC13为研究对象，详细分析该监测源中对等AS的可见性。监测源RRC13位于俄罗斯莫斯科的交换中心，有16个对等AS。

从可见AS数量和可见AS边关系数量两个方面来分析度量监测源中对等AS的可见性。随着对等AS数量的增加，该监测源的可见AS数量和可见边关系数量的变化情况如图1所示。

![02.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997178922558.png "1668997178922558.png")图1：单个监测源中对等AS可见性趋势图

从图1中可以看出，1）在对等AS数量增加到7个时，可见AS数量已达到最大7.3万个，与全球已使用AS数量接近。也就是说，当对等AS数量达到7个时，可以看到全球已使用的所有AS。2）可见AS边关系数量随着对等AS数量的增加一直在增加，但是，在可见AS数量增加到11个之后，可见AS边关系数量增速明显减少。也就是说，为了获取足够多的可见AS边关系，对等AS的数量不应该少于11个。

更进一步地，从两个项目剩余的BGP数据监测源中随机抽取了两个，所得到的结论与RCC13类同。因此，在建立BGP数据监测源时，对等AS数量不应该少于11个。

2.2 三个监测源对等AS的可见性度量

以RIPE RIS项目的三个监测源RRC03、RRC11和RRC13为研究对象，详细分析三个监测源中对等AS的可见性。三个监测源RRC03、RRC11和RRC13分别位于荷兰阿姆斯特丹、美国纽约和俄罗斯莫斯科的交换中心，它们的对等AS号数量分别是93、23和16，去重复后对等AS号的数量是123。

从可见AS数量和可见AS边关系数量两个方面来分析度量监测源中对等AS的可见性。随着对等AS数量的增加，三个监测源的可见AS数量和可见边关系数量的变化情况如图2所示。

![03.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997191240862.png "1668997191240862.png")

图2：三个监测源中对等AS可见性趋势图

从图2中可以看出，1）在对等AS数量增加到10个时，可见AS数量已达到最大近7.6万个，与全球已使用AS数量一致。也就是说，当对等AS数量达到10个时，可以看到全球已使用的所有AS。2）可见AS边关系数量随着对等AS数量的增加一直在增加，但是，在可见AS数量增加到11个之后，可见AS边关系数量增速减少。当对等AS增加到120个时，可见AS边关系数量为24.4万，相当于全球AS边关系总量46.9万的53.03%。

2.3 所有监测源对等AS的可见性度量

为RIPE RIS和Route Views两个项目的所有监测源为研究对象，详细分析所有监测源中对等AS的可见性。所有监测源中的对等AS去重后有1,195个。

从可见AS数量和可见AS边关系数量两个方面来分析度量监测源中对等AS的可见性。随着对等AS数量的增加，所有监测源的可见AS数量和可见边关系数量的变化情况如图3所示。

![04.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997198180405.png "1668997198180405.png")

图3：所有监测源中对等AS可见性趋势图

从图3中可以看出，1）在对等AS数量增加到10个时，可见AS数量已达到最大近7.6万个，与全球已使用AS数量一致。也就是说，当对等AS数量达到10个时，可以看到全球所有已使用AS。2）可见AS边关系数量随着对等AS数量的增加一直在增加。当对等AS增加到1195个AS时，可见AS边关系数量为46.0万，与全球AS边关系总量46.9万接近。

![05.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221121/1668997221112147.png "1668997221112147.png")

因此，为了获取足够多的AS边关系，需要在不同地方与不同运营商建立的对等关系。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?zzanZ3NQ)

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