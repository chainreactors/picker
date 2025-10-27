---
title: “噪音风暴”伪造大量互联网流量
url: https://www.4hou.com/posts/gy29
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-30
fetch_date: 2025-10-06T18:20:10.810578
---

# “噪音风暴”伪造大量互联网流量

“噪音风暴”伪造大量互联网流量 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “噪音风暴”伪造大量互联网流量

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103333

收藏

导语：TCP 流量还会调整窗口大小等参数来模拟不同的操作系统，使活动保持隐秘，难以被精确定位。

互联网情报公司 GreyNoise 报告称，自 2020 年 1 月以来，它一直在追踪包含伪造互联网流量的大量“噪音风暴”。

然而，尽管进行了广泛的分析，仍未得出其来源和目的的结论。这些噪音风暴被怀疑是秘密通信、DDoS 攻击协调信号、恶意软件操作的秘密指挥和控制 (C2) 通道，或配置错误的结果。

一个奇怪的方面是生成的 ICMP 数据包中存在“LOVE”ASCII 字符串，这进一步增加了对其目的的猜测，并使案件更加有趣。

GreyNoise 发布此信息，希望网络安全研究人员社区能够帮助解开这个谜团，并揭示出造成这些奇怪噪音风暴的原因。

**噪音风暴的特征**

GreyNoise 观察到大量伪造的互联网流量，这些流量来自 QQ、微信和 WePay 等各种来源的数百万个伪造 IP 地址。

这些“风暴”会向 Cogent、Lumen 和 Hurricane Electric 等特定互联网服务提供商发起大量流量，但会避开其他服务提供商，尤其是亚马逊网络服务 (AWS)。

流量主要集中于 TCP 连接，特别是针对端口 443，但也有大量 ICMP 数据包，最近其中包括嵌入的 ASCII 字符串“LOVE”，如下所示。

![icmp-love.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240920/1726811388113139.png "1726811329950190.png")

包含“Love”字符串的 ICMP 数据包

TCP 流量还会调整窗口大小等参数来模拟不同的操作系统，使活动保持隐秘，难以被精确定位。生存时间 (TTL) 值决定了数据包在被丢弃之前在网络上停留的时间，该值设置在 120 到 200 之间，以模拟真实的网络跳数。

总而言之，这些“噪音风暴”的形式和特征表明，是参与者的蓄意所为，而不是错误配置的大规模产物。

**GreyNoise 呼吁共同解决**

这种奇怪的流量模仿合法的数据流，虽然尚不清楚它是否是恶意的，但其真正目的仍然是个谜。GreyNoise 在 GitHub 上发布了最近两次噪音风暴事件的数据包捕获 (PCAP)，邀请网络安全研究人员加入调查，集思广益建言献策，以帮助解开这个谜团。

GreyNoise 强调：“噪声风暴提醒我们，威胁可能以不同寻常和怪异的方式出现，这恰恰凸显了超越传统安全措施的适应性策略和工具的必要性。”

文章翻译自：https://www.bleepingcomputer.com/news/security/unexplained-noise-storms-flood-the-internet-puzzle-experts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Ilh9etBo)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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