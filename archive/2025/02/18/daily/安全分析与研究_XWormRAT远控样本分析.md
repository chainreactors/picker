---
title: XWormRAT远控样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490557&idx=1&sn=3b47242b908df657f688b58fd9649f37&chksm=902fb4d5a7583dc395ae7c08fef52b5d5bfeb281ac2f783c3896cb825fa4a68b7465b9b980f0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-18
fetch_date: 2025-10-06T20:39:35.823161
---

# XWormRAT远控样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXJVicq5cxzeou29uVBHz19Hf868WGUVodFNmdEjUfJxqqlfFzqV9a6sdCl1TYevT9xjnDxBDePDDg/0?wx_fmt=jpeg)

# XWormRAT远控样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

XWorm是一种针对Windows操作系统的流行商业恶意软件，可通过暗网论坛以恶意软件即服务(MaaS)的形式购买，这种多功能恶意软件主要用作远程访问工具 (RAT)，允许攻击者控制受感染的系统，它以隐秘性和持久性以及广泛的恶意活动而闻名，从远程桌面控制到勒索软件和信息盗窃。

除了RAT功能外，XWorm通常还具有自我传播功能，使其能够在网络中自主传播，它也是一种可通过可移动驱动器(如USB闪存驱动器)传播的恶意软件，会感染Windows系统并可能窃取信息或允许远程访问。

样本分析

1.母体样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19HYMjVpu5qQFo1flmK6RIicgjaukuvhuII4vmasibuWCC0OBWPeib4kIiaBg/640?wx_fmt=png)

2.获取核心PayLoad代码，采用NET语言编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19H9GUAAuFet3riaWz2NdXQiazeXuCHjsrNRj7y6Eu0VVYbx5QqGExkibEvA/640?wx_fmt=png)

3.XWormRAT核心代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19H7iaic6YYd3jGOewe978RnjULDefTCFMcD6cz5iankdGk0RkvGwm95JbRA/640?wx_fmt=png)

4.解密C2配置信息代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19H9hDxqsicsWan4NhMGxxC8gIVQm3D2ZeuzydDqImF6KXyrRruYo4tRPg/640?wx_fmt=png)

5.动态调试获取远程服务器C2为favor.ydns.eu，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19HcZxDkQcO2aV8hka37qeSEhqKZJfB2N9eE3pYIQMiaEQ0Hw98dGKGicPQ/640?wx_fmt=png)

6.在威胁情报平台查询C2域名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19HAhibW34S7zvbxFXvjzqNicicYRT1bXxicpGSdMLF5GlkU7aYdiblFXBibdqw/640?wx_fmt=png)

7.此前有人在社交平台上分享XWormRAT5.6的源代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19Ht9Xo6m8OOzpGv3u4wLgZbyAAibvpAT6TYQILb2wXicIf74jrFIu2oVuw/640?wx_fmt=png)

8.初始化C2配置信息代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19HNaY8tRaiczF4HlyI3moX6bpZTrZTYtBeRGhRgwLXwNGM1QJD6onUSSg/640?wx_fmt=png)

9.前不久有人在GITHUB上分享XWormRAT远控全版本，现在链接己经取消，这些版本可能都带有后门，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19HAMdLCrzjjyAKgntEpicf1cYQbXgpNq7Ndl20drcWJsk4zIya9efL7aQ/640?wx_fmt=png)

针对XWormRAT远控样本，感有兴趣的可以自行研究。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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