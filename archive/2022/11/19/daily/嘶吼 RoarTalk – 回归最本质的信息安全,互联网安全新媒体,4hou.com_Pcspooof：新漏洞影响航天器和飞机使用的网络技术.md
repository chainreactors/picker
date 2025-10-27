---
title: Pcspooof：新漏洞影响航天器和飞机使用的网络技术
url: https://www.4hou.com/posts/GKJ3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-19
fetch_date: 2025-10-03T23:10:51.081432
---

# Pcspooof：新漏洞影响航天器和飞机使用的网络技术

Pcspooof：新漏洞影响航天器和飞机使用的网络技术 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Pcspooof：新漏洞影响航天器和飞机使用的网络技术

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)132844

收藏

导语：近日研究人员披露了一种针对时间触发的以太网（TTE）的新型攻击方法，这种关键的技术被用于安全性至关重要的基础设施，可能会导致航天器和飞机的核心系统出现故障。

![00.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221118/1668737670154237.png "1668546213213809.png")

近日研究人员披露了一种针对时间触发的以太网（TTE）的新型攻击方法，这种关键的技术被用于安全性至关重要的基础设施，可能会导致航天器和飞机的核心系统出现故障。

来自密歇根大学、宾夕法尼亚大学和美国宇航局约翰逊航天中心的一群学者和研究人员将这种攻击技术称之为PCspooF，该技术旨在违反TTE的安全保证，诱导TTE设备在长达1秒的时间内失去同步，这种行为甚至会导致航天任务中出现不受控制的动作，并威及到机组人员的安全。

多种联网技术组成了所谓的混合关键网络，而TTE是其中之一。在混合关键网络中，定时和容错要求各异的流量共存于同一个物理网络中。这就意味着实现航天器/飞机控制的关键设备和用于监测和数据收集的非关键设备都可以共享同一个网络。

这种方法的一个明显优势是，由于仅仅依赖一种技术，所以重量和功率方面的要求比较低，开发和时间成本也较低，但它也有自身的缺点。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221118/1668737671894620.png "1668546243179532.png")

图1

这项研究报告的第一作者Andrew Loveless告诉The Hacker News网站，这种混合关键方法给网络设计在提供隔离机制方面带来的压力大得多。鉴于关键系统和非关键系统可以连接到同一台交换机，网络协议和硬件就需要做额外的工作，才能确保总是能够保证关键流量成功且准时传输。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221118/1668737671206080.png "1668546256179048.png")

图2（图片来源：欧洲航天局）

除此之外，虽然网络中的关键设备要经过彻底全面的检查，但非关键设备不仅是商用现成（COTS）设备，还缺少同样严格的流程，从而导致供应链可能被攻击的途径，随后攻击者只要将未经授权的第三方组件整合到系统中，就可以激活攻击。

这时候混合关键网络派得上用场，帮助确保：即使COTS设备是恶意的，也无法干扰关键流量。

![33.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221118/1668737672258934.png "1668546302191503.png")

图3

密歇根大学电子工程和计算机科学系的助理教授Baris Kasikci表示，研究团队在PCspooF中发现了一种方法，可以让恶意的非关键设备违反TTE网络中的隔离保证。

反过来，这可以通过使用恶意设备经由以太网电缆向TTE交换机注入电磁干扰（EMI）来实现，实际上欺骗交换机发送看起来真实的同步消息（即协议控制帧或pcf），并使它们被其他TTE设备接受。

这种生成“电噪声”的电路在单层印刷电路板上仅占2.5cm × 2.5cm的空间，只需要极小的电力，并且可以隐藏在best-effort设备中，整合到TTE系统中，不会引发任何危险信号。

提到缓解措施，研究人员建议使用光耦合器或电涌保护器来阻止电磁干扰，检查源MAC地址以确保它们是真实有效的，隐藏关键PCF字段，使用像IEEE 802.1AE这样的链路层验证协议，增加同步主程序的数量，并禁用危险状态转换。

研究人员指出，研究结果表明，在一个旨在提供严格隔离保证的系统中使用通用硬件有时恰恰会破坏那些保护机制，应该以类似的方式认真检查混合关键软件系统的添加，以确保隔离机制万无一失。

Kasikci表示，TTE协议非常成熟，并且经过了严格审查，许多最重要的部分都得到了正式验证。

从某种程度上来说，这正是这种攻击令人关注的地方：研究人员能够弄清楚如何违反协议的一些保证，尽管它很成熟。但要做到这一点，又得另辟蹊径，搞清楚如何让硬件以一种协议未曾料到的方式运行。

本文翻译自：https://thehackernews.com/2022/11/pcspoof-new-vulnerability-affects.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lOUoDFXT)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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