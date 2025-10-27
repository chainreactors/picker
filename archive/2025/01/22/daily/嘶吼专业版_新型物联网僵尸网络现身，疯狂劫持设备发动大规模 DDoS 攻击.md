---
title: 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580915&idx=2&sn=49c81661b58dadfafc5d8436f0511377&chksm=e9146cc9de63e5dfbdd06a3273f839512dbc6283cb8218a470ff5f749b412c27647cc876904d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-22
fetch_date: 2025-10-06T20:11:20.450797
---

# 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHH7Y0bcfZmW7GQ8tjpJhp1rjIiajHEzW6fSNDiaZ5iaicz9icL56x5Q4tBDjQ/0?wx_fmt=jpeg)

# 新型物联网僵尸网络现身，疯狂劫持设备发动大规模 DDoS 攻击

山卡拉

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

自 2024 年底起，IoT 僵尸网络的 C＆C 服务器便开始向日本及其他国家和地区发送大规模 DDoS 攻击命令。这些命令的目标涵盖了多家公司，其中不乏日本的大型企业与银行。

尽管目前无法确认直接联系，但一些目标组织反馈，在此期间出现了临时连接异常和网络中断的情况，而这些状况与观察到的攻击命令高度吻合。

![](https://mmbiz.qpic.cn/mmbiz_png/wpkib3J60o287jwk8LWD9icmgWlahS21WB8lECGmeJOXSiafEcxpJYOHrph36wNX7lyjD7jckJk6EMZ4bGp59RNrA/640?wx_fmt=png)

# 物联网僵尸网络的新威胁聚焦日本

这个基于 Mirai/Bashlite 的僵尸网络利用 RCE 漏洞或弱密码来感染物联网设备。感染阶段包括下载一个脚本，该脚本会从分发服务器获取加载程序可执行文件。

之后，加载程序使用专门的 User-Agent 标头从服务器成功检索实际的恶意软件负载，然后在内存中执行它。

该恶意软件与 C＆C 服务器通信，以获取发起 DDoS 攻击（SYN Flood、TCP ACK Flood、UDP Flood 等）或将设备转变为代理服务器的命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHHMXlsicAchPsgCtnetEMYveqT2Cz775j3yKYsqb0johc67AUOCgt1uXw/640?wx_fmt=png&from=appmsg)

使用自定义 User-Agent 标头从分发服务器下载二进制文件的代码

它采用了多种规避技术，并通过镜像过去的 Mirai 僵尸网络行为来 停用阻止DDoS 攻击期间由高负载触发的系统重启的看门狗计时器。

它还操纵 iptables 规则来阻碍感染检测和 DDoS 攻击可见性。通过阻止 WAN 端 TCP 连接，它旨在防止交叉感染，同时保持内部管理访问。

通过使用动态配置的 iptables 规则，恶意软件能够接收来自外界的 UDP 数据包，并通过隐藏其活动来抑制 TCP RST 数据包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHHVrjZmHBHptlWokC9dXM7qwb6W5gVQTdicpkJaH4SxsuLSF01ybmQwZQ/640?wx_fmt=png&from=appmsg)

用于禁用看门狗定时器的恶意软件代码

2024 年 12 月 27 日至 2025 年 1 月 4 日期间观察到的 DDoS 攻击针对的是北美、欧洲和亚洲的组织，主要集中在美国、巴林和波兰。

趋势科技的分析显示，不同目标地区的命令模式有所不同。针对日本目标的攻击经常使用“stomp”命令，而针对国际目标的攻击则更常使用“gre”命令。

攻击主要集中在交通运输、信息通信、金融保险等领域。而国际攻击也主要集中在信息通信、金融保险行业，针对交通运输领域的攻击明显较少。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHH4UfrMhpE4cWr7xyh4pIrxia2F194j8lPo2fBBoj5mBxbuassYw3zDAg/640?wx_fmt=png&from=appmsg)

目标行业

这些攻击背后的实施者表现出了适应性，并在实施初步防御措施后针对日本组织测试了“套接字”和“握手”等新命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHH0YyTboibSOQ4QTvJ1fr2zQcFtq9j7MptYEW3ib4ia20AzaRxLic2fgJ5Xg/640?wx_fmt=png&from=appmsg)

恶意软件在初始化阶段设置的 iptables 规则

僵尸网络分析结果显示，共有 348 台设备遭到感染。受感染设备中，80% 主要是 TP-Link 和 Zyxel 等供应商生产的无线路由器，此外，来自海康威视的 IP 摄像机在受感染设备中也占了相当比例。

导致其被利用的因素包括默认设置的持久性、过时的固件和安全功能不充分，这些因素使攻击者能够轻易破坏这些设备并利用它们进行 DDoS 攻击和网络入侵等恶意活动。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHHbEZ6rdv9RzibEVHtCWSH4eS2kiaxDlic5X0kGpDfVyqSZTWx6yQ8F7Tiaw/640?wx_fmt=png&from=appmsg)针对 DDoS 攻击和物联网漏洞的缓解策略

为了减轻僵尸网络感染和 DDoS 攻击，请实施强大的安全措施。通过更改默认凭据、定期更新固件和分段物联网网络来保护物联网设备。

同时，要严格限制设备的远程访问权限，对设备进行行之有效的管理，密切监控网络流量，一旦发现异常即刻响应处理。

针对 UDP 洪水攻击，可通过阻止特定的 IP 地址和协议来进行防范；还可以积极与服务提供商展开深度合作，共同应对风险；另外，加强路由器硬件的防护能力，也是减轻 UDP 洪水攻击影响的重要举措 。

参考及来源：https://gbhackers.com/new-iot-botnet-launches-large-scale-ddos-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHHRsIQXZmhTPiclM3cxibRhqy0HrkrU9zWlyTicJ8Uh9ntnmF5elKh0j1MA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYya1aH9gfAPyHBQlKeSHHnCMlbTniblTmc4DCmknficHzjicRdtev5iaPQz3UOw5mcIEJXdR9NILUdA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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