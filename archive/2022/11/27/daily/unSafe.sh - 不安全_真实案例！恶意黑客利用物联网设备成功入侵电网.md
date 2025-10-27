---
title: 真实案例！恶意黑客利用物联网设备成功入侵电网
url: https://buaq.net/go-137337.html
source: unSafe.sh - 不安全
date: 2022-11-27
fetch_date: 2025-10-03T23:52:29.245295
---

# 真实案例！恶意黑客利用物联网设备成功入侵电网

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9ba0cb4d901a5746ef7bb9307e47e561.jpg)

真实案例！恶意黑客利用物联网设备成功入侵电网

微软报告揭示，有攻击者利用某个停止维护的物联网产业链基础软件漏洞，成功入侵印度电网，该漏洞目前正被持续利用。安全内参11月25日消息，微软近期发布一份报告，揭示了使用已停止维护软件的物联网设备面临的风
*2022-11-26 08:48:50
Author: [mp.weixin.qq.com(查看原文)](/jump-137337.htm)
阅读量:50
收藏*

---

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sxBW1ibfKcn30WEk1AvibFbHql7y3AGewKS62le7icXRqKKQzFn0tVzWXXgaWdtMbMq8vFsoQ4Z1xng/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**微软报告揭示，有攻击者利用某个停止维护的物联网产业链基础软件漏洞，成功入侵印度电网，该漏洞目前正被持续利用。**

安全内参11月25日消息，微软近期发布一份报告，揭示了使用已停止维护软件的物联网设备面临的风险。从最新案例来看，**已经有黑客利用软件中的漏洞攻击能源组织**。

本周二，微软研究人员在一份分析报告中透露，他们在**Boa Web Server软件中发现了一个易受攻击的开源组件**，被广泛应用于一系列路由器、安保摄像头以及流行的软件开发工具包（SDK）。

尽管**Boa Web Server在2005年就已停止更新，但它仍被广泛应用**，并由此掀起一轮新的危机。由于Boa已经内置到物联网设备供应链的复杂构建方式，防御方其实很难缓解这一安全缺陷。

微软报告称，恶意黑客试图利用Boa Web Server的多个漏洞，包括一个高危级别的信息泄露漏洞（**CVE-2021-33558**）和一个任意文件访问漏洞（**CVE-2017-9833**）。未经身份验证的攻击者可以利用这些漏洞获取用户凭证，并远程执行代码。

“影响该组件的两个漏洞，可以让恶意黑客在发起攻击之前就收集到关于目标网络资产的信息，并获取有效凭证以访问更多未被检测到的网络。**在关键基础设施网络中，恶意黑客能够在攻击之前收集未检测的信息。一旦攻击发起，黑客方就能引发更大影响，甚至可能造成数百万美元损失、破坏数百万人的正常生活**。”微软表示。

**微软最初发现这个易受攻击的组件，是在调查一起针对印度电网的入侵事件中**。此前，美国威胁情报公司Recorded Future曾在2021年发布报告，详细介绍某个国家威胁组织正在将攻击矛头指向印度电网内的运营资产。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sxBW1ibfKcn30WEk1AvibFbHKHz8hoBoAaDBWTIabSHiaXZj52nBAMa5c7t6H2sr0wtBz967L9ibSbAw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

2022年4月，Recorded Future又发布一份报告，介绍了另一个国家支持的恶意黑客团伙。报告称，该团伙利用物联网设备在用于监视/控制物理工业系统的运营技术（OT）网络上开辟登陆点。

在此之后，**微软在一周内在全球范围内发现了上百万个暴露在互联网上的Boa服务器组件**。可以预见，这个易受攻击的组件很可能给整个世界带来巨大威胁。

另一个重要问题在于，由于经常被整合在流行的SDK当中，所以很多用户根本不确定自己的产品中是否存在Boa Web Server。比如Realtek SDK，这款软件开发工具包在路由器、接入点及其他网关设备制造商中得到广泛使用，而它正好包含Boa Web服务器。

**由于持续观察到针对Boa漏洞的攻击，微软决定就广泛使用的各网络组件的安全缺陷发布供应链风险警报**。

**参考资料：hackread.com**

> **文章来源：安全内参**

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3xxicXNlTXL8fHInwic65QarBzLTDecgAlRicyRRNJu5ItVq0eGBmhibeaUEib2sMnAsOTOHicWtz7P2iaAeftdlNQGCg/640?wx_fmt=jpeg)

多一个点在看![](https://mmbiz.qpic.cn/mmbiz_gif/zYdFdnRZ0h95ZAL5c8h6iaMiaqbgljvZ80YraNgwWAtyyZRGT8INEgx8qWKgf9wXribCDNibDvDa2R1EQB4grqAKDg/640?wx_fmt=gif)多一条小鱼干

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzAxMjE3ODU3MQ==&mid=2650557032&idx=2&sn=d5dafe4d5ee2882a9cc82880c6ce3de0&chksm=83bd2f8cb4caa69a46fd1244c245c68f08afa61abc82227c23b91fece2e1d0e922a0938282e2#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)