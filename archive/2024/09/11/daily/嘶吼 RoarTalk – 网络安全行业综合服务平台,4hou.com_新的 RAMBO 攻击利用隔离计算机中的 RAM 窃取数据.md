---
title: 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据
url: https://www.4hou.com/posts/pnk6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-11
fetch_date: 2025-10-06T18:24:11.226246
---

# 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据

新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-09-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)92142

收藏

导语：建议实施严格的区域限制以增强物理防御、RAM 干扰以破坏源头的隐蔽通道、外部 EM 干扰以破坏无线电信号等。

一种被称为“RAMBO”（用于进攻的隔离内存总线辐射）的新型侧信道攻击会从设备的 RAM 产生电磁辐射，以从隔离的计算机发送数据。

隔离系统通常用于对安全性要求极高的任务关键型环境，例如政府、武器系统和核电站，这些系统与公共互联网和其他网络隔离，以防止恶意软件感染和数据盗窃。

尽管这些系统没有连接到更广泛的网络，但它们仍然可能受到通过物理介质如USB 驱动器，引入恶意软件感染或发起复杂供应链攻击。

该恶意软件可以秘密操作，以调制隔离系统的 RAM 组件，从而允许将机密从计算机传输到附近的接收者。属于此类攻击的最新方法来自以色列大学的研究人员，由 Mordechai Guri 领导，他是隐蔽攻击渠道方面经验丰富的专家，曾开发出使用网卡 LED、USB 驱动器 RF 信号、SATA 电缆和电源泄漏数据的方法。

**RAMBO 攻击如何运作**

为了实施 Rambo 攻击，攻击者会在隔离的计算机上植入恶意软件，以收集敏感数据并准备传输。它通过操纵内存访问模式（内存总线上的读/写操作）从设备的 RAM 产生受控的电磁辐射来传输数据。

这些发射本质上是恶意软件在 RAM 内快速切换电信号（开关键控“OOK”）的副产品，该过程不会受到安全产品的主动监控，也无法被标记或停止。

![ook-modulation.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240910/1725937557164165.png "1725937397739908.png")

执行 OOK 调制的代码

发射的数据被编码为“1”和“0”，在无线电信号中表示为“开”和“关”。研究人员选择使用曼彻斯特编码来增强错误检测并确保信号同步，从而减少接收端出现错误解释的可能性。

攻击者可能会使用带有天线的相对便宜的软件定义无线电 (SDR) 来拦截调制的电磁辐射并将其转换回二进制信息。

![signal.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240910/1725937559206663.png "1725937451186508.png")

单词“DATA”的EM信号

**性能和限制**

RAMBO 攻击的数据传输速率高达 1,000 比特每秒 (bps)，相当于每秒 128 字节，或 0.125 KB/s。

按照这个速率，窃取 1 兆字节数据大约需要 2.2 小时，因此 RAMBO 更适合窃取少量数据，如文本、按键和小文件。

研究人员发现，在测试攻击时可以实时进行键盘记录。但是，窃取密码需要 0.1 到 1.28 秒，窃取 4096 位 RSA 密钥需要 4 到 42 秒，窃取小图像需要 25 到 250 秒，具体取决于传输速度。

![transmit.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240910/1725937560123266.png "1725937501273666.png")

数据传输速度

快速传输的最大范围限制为 300 厘米，误码率为 2-4%。中速传输可将距离增加到 450 厘米，同时误码率相同。最后，误码率几乎为零的慢速传输可以在长达 7 米的距离内可靠地工作。

研究人员还尝试了高达 10,000 bps 的传输，但发现任何超过 5,000 bps 的速度都会导致信噪比非常低，从而无法进行有效的数据传输。

**阻止 RAMBO**

Arxiv 上发表的技术论文提供了几项缓解建议来减轻 RAMBO 攻击和类似的基于电磁的隐蔽通道攻击，但它们都引入了各种花费开销。

建议实施严格的区域限制以增强物理防御、RAM 干扰以破坏源头的隐蔽通道、外部 EM 干扰以破坏无线电信号，以及法拉第外壳以阻止气隙系统向外发出 EM 辐射。

研究人员针对虚拟机内运行的敏感进程测试了 RAMBO，发现它仍然有效。然而，由于主机内存容易与主机操作系统和其他虚拟机发生各种交互，攻击可能会很快被阻止。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-rambo-attack-steals-data-using-ram-in-air-gapped-computers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6k4DjFoB)

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