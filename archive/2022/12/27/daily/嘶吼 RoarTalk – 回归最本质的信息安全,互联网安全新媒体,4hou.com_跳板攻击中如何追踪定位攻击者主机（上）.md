---
title: 跳板攻击中如何追踪定位攻击者主机（上）
url: https://www.4hou.com/posts/8YJj
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-27
fetch_date: 2025-10-04T02:32:11.294733
---

# 跳板攻击中如何追踪定位攻击者主机（上）

跳板攻击中如何追踪定位攻击者主机（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 跳板攻击中如何追踪定位攻击者主机（上）

埃文科技
[行业](https://www.4hou.com/category/industry)
2022-12-26 11:10:36

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117107

收藏

导语：那么究竟什么是跳板攻击，跳板攻击究竟是如何做到信息进行匿名化的？

前段时间西北工业大学遭受NAS攻击事件中，TAO在针对西北工业大学的网络攻击行动中先后使用了54台跳板机和代理服务器，主要分布在日本、韩国、瑞典、波兰、乌克兰等17个国家，其中70%位于中国周边国家，如日本、韩国等。

同时，为了进一步掩盖跳板机和代理服务器与NSA之间的关联关系，NSA使用了美国Register公司的匿名保护服务，对相关域名、证书以及注册人等可溯源信息进行匿名化处理，无法通过公开渠道进行查询。

![abstract_digital_network_mapping_by_mf3d_gettyimages-888477728_1200x800-100768192-large.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672016165139777.jpeg "1672016165139777.jpeg")

**一、跳板攻击**

那么究竟什么是跳板攻击，跳板攻击究竟是如何做到信息进行匿名化的？

跳板攻击是指攻击者利用多个“跳板主机”, 即通过控制多个主机转发攻击数据包。

攻击者事先控制多个跳板主机, 利用跳板转发攻击数据包。但是在受害主机端, 只能看到攻击数据包来自于最后一跳的主机, 而不能识别出真正的攻击者，所以跳板攻击的真正目的就是隐藏攻击者。而且跳板路径越长, 越难追踪攻击者。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672016076890934.png "1672016076890934.png")

**二、跳板检测Step-stone Detection**

对于跳板攻击，取证人员在检测到攻击数据包后, 其源IP地址是最后一跳“跳板主机”的IP地址, 那么在这种情况下如何追踪定位攻击者的主机？

在这一问题中, 由于在受害主机端可以观察到最后一跳的IP地址, 因此追踪问题就转化为如何沿着攻击路径上的跳板, 逐跳验证是否确实存在“跳板主机”。

我们首先要解决：跳板检测(Step-stone Detection), 即如何确定本地网络中存在攻击者的跳板？

假设网络安全人员完全控制本地网络, 能够对进出本地网络的网络流量进行监控。

若攻击者的跳板位于本地网络内, 由于跳板只是起一个攻击数据包转发的功能, 一般不会对攻击数据包进行修改, 因此进出网络的攻击数据包会具有相似性, 通过对进出网络的网络流量进行监控, 检测这种攻击数据包的相似性, 即可判断本地网络内是否存在跳板。

若攻击者的主机就位于本地网络内, 则在一定时间内, 攻击者会发出攻击数据包, 而不会有进入本地网络的攻击数据包, 因此也可以通过对进出网络的网络流量进行监控。

如发现只有出的攻击数据包而没有进入的网络数据包, 则可以判断攻击者主机位于本地网络内。

在跳板攻击检测中, 存在一个前提条件, 即进入的攻击流量和转发的流量间隔时间不能很长, 否则很难将入的流量和出的流量关联在一起。

这一间隔时间用攻击者的最大容忍时间来表示。如果间隔时间大于最大容忍时间, 例如攻击者向跳板发送命令后, 跳板不是立即转发攻击者的命令, 而是采用计划任务等方式, 让跳板在设定的时间再转发数据, 则在这种情况下现有的方法都将失效。

由于攻击者为了逃避检测, 可以将数据流量进行加密, 因此将情况分为流量未加密情况和加密的情况。

1) 数据包未加密

 S.Staniford-Chen与L.Heberlein首次提出跳板检测问题。即使用数据包的明文内容的指纹来判断不同的数据包是否具有相同的内容, 从而建立流量间的关联。

2) 数据包加密

由于数据包进行了加密, 无法对数据包的内容进行检查, 因此主要思想是对数据流的特征进行检测, 如数据包的时序特征。

**(1) 假设攻击者不会有意识改变数据包的特征**

《 Detecing stepping stones》中首次提出基于数据包时序特征的检测方法。他们观察到在一个数据流中存在没有数据传输的时间间隔, 将这一时间间隔定义为“关”周期, 而在相似的数据流中, “关”周期的特征是相同的, 因此通过这一特征来关联入的流量和出的流量，但该方法要求连接是同步的。

《Finding a connection chain for tracing intruders》则定义了数据传输的平均延迟和最小延迟两个指标来识别数据流的模式, 通过这两个延迟时间计算两个数据流的偏离程度, 如偏离程度小于一定阀值, 则认为两个数据流具有较高的关联度。

文献《Inter-packet delay-based correlation for tracing encrypted connections through stepping stone》定义了一个滑动窗口, 计算滑动窗口内数据包之间的间隔时间, 根据数据包间隔时间的特征来进行关联。

《Mining and detecting connectionchains in network traffic》中测试了基于关联规则挖掘算法, 若“入”数据包和“出”数据包的时间差值小于预设的数值, 则将这两个数据包进行关联, 根据流中数据包关联的置信度和支持度。来判断“入”的数据流与“出”的数据流是否具有关联关系。

**(2) 假设攻击者有意识改变数据包特征**

①　攻击者改变数据包的时序特征

在《Multiscale stepping-stone detection: detecting pairs of jittered interactive streams by exploiting maximum tolerable delay》首次考虑攻击者可能会有意识改变数据包的时序特征, 但假设有一个攻击者的最大延迟容忍时间。它基于小波变换来检测流量的关联性。假设攻击者数据包的到达服从泊松分布或者帕累托分布, 进行了一些理论分析, 但没有给出需要捕获多少数据包才能以一定概率得到正确检测结果的分析。

《Robust correlation of encrypted attack traffic through stepping stones by manipulation of  inter-packet delays》给出了一个基于水印的方法检测流量关联性, 在入流量中填加水印信息, 在出流量中检测是否存在水印信息, 但它假设攻击者数据包之间的时间间隔是独立同分布的。《a robust and invisible non-blind watermark for network flows》同样采用嵌入水印的思想, 通过记录入流量数据包的到达时间, 在一个初始延迟时间的基础上, 再增加或减小一个微小的时间来作为水印信号, 能够获得更好的鲁棒性。

《A signal processing perspective to stepping-stone detection》中假设攻击者随机延迟数据包, 跳板中继的数据包不能丢包、不能乱序、不能增加数据包, 不依赖于数据包大小, 给出了检测方法和理论分析。

该方法根据两个约束条件: 出的数据包时间大于入的数据包时间; 出的数据包时间减去入的数据包时间小于最大延迟容忍时间, 将入的数据包关联到出的数据包, 然后假设数据包的顺序不会发生变化, 降低算法的复杂度。

②攻击者增加额外的数据包

攻击者可以有意识的在中继后的数据流中插入额外的无用数据包,来破坏输入和输出数据流之间的关联关系。针对这种情况假设攻击者在一段时间内能够插入的多余数据包数目是有限的, 通过匹配输入与输出的数据包, 给出了可以抵抗增加多余数据包的跳板检测算法。

③攻击者同时改变时序特征和增加额外数据包

在《A signal processing perspective to stepping-stone detection》中Ting He, Lang Tong假设攻击者在跳板中同时增加数据包的随机延时和多余的数据包, 并假设这两种改变是统计独立的, 基于数据包匹配的方法给出了检测算法。

前述方法都是针对攻击者主机到受害者主机的流量通过跳板时的入流量与出流量的关联分析, 而《Stepping stone detection via request-response traffic analysis》文章中是将攻击者主机到受害者主机的流量通过跳板时的出流量与受害者主机回传给攻击者的流量通过跳板时的出流量进行关联, 定义前者的数据包数为 Send, 后者的数据包数为 Echo, 指出如果两个流量具有相关性, 则(Echo-Send)和(Echo+Send)具有线性关系, 而如果两个流量没有关系, 则不具有这种线性关系。

实验表明, 即使攻击者有意增加数据延时和增加多余数据包, 该方法也能检测出两个流量的相关性。

因此，如何确定本地网络中存在攻击者的跳板可以采取以下解决方案：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221226/1672016225210495.png "1672016225210495.png")

在跳板攻击中确定完本地网络中存在攻击者的跳板，那么接下来如何追踪定位攻击者主机？

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Iw2ysIin)

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
[知乎](https://zhuanlan.z...