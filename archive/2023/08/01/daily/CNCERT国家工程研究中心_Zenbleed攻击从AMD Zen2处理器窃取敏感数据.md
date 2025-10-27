---
title: Zenbleed攻击从AMD Zen2处理器窃取敏感数据
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247538972&idx=2&sn=1b32b64a3856b541becb69f782fec1c1&chksm=fa93efddcde466cbad3b57783bca43d795accfa7ca1e084e98addda4cdb419eb5e91080534cd&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-08-01
fetch_date: 2025-10-06T17:02:47.934581
---

# Zenbleed攻击从AMD Zen2处理器窃取敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lDIaRiaPK2kG6PAibibJ3RIHbIZLjRjC87Fvo6pbtP8zgMI5S0AnCgFtY8EG426jyStdJb5zHh6ibnQw/0?wx_fmt=jpeg)

# Zenbleed攻击从AMD Zen2处理器窃取敏感数据

网络安全应急技术国家工程中心

Zenbleed攻击从AMD Zen2处理器窃取敏感数据。

谷歌安全研究人员Tavis Ormandy发现了一个影响AMD Zen2 CPU处理器的安全漏洞——Zenbleed，漏洞CVE编号为CVE-2023-20593。攻击者利用该漏洞可以以30Kb/s的速度从CPU中窃取密码、加密密钥等敏感数据。

# **漏洞概述**

推测执行是主流处理器使用的一种增强处理器性能的方法。Zenbleed漏洞产生的原因是推测执行过程中名为'vzeroupper'的指令处理不当导致的。

Ormandy使用和模糊和性能计数器发现了特定硬件事件，并使用Oracle序列化方法验证了结果。使用该方法可以检测到随机生成的程序和其序列化Oracle之间的不一致，最终成功发现了Zen2 CPU中的漏洞。

触发该漏洞后，研究人员成功从系统中窃取了敏感信息，包括虚拟机、隔离沙箱、容器等环境。30kb/s的信息窃取速度足以监控加密密钥和用户的登录密码等。

# **漏洞影响**

虽然漏洞利用PoC是针对Linux系统的，但是该漏洞是操作系统无关，因此所有影响在Zen 2 CPU上的操作系统都受到该漏洞的影响。漏洞影响所有基于Zen 2架构的AMD CPU，包括Ryzen 3000、Ryzen 4000U/H ("Renoir")、Ryzen 5000U ("Lucienne")、Ryzen 7020、ThreadRipper 3000 和Epyc 服务器处理器。

但该漏洞对普通用户的实际影响并不大，因为漏洞利用需要对受影响的系统有物理访问权限，并且漏洞的利用需要很高程度的专业知识。

# **漏洞补丁**

5月15日，研究人员将该漏洞提交给了AMD。7月24日，AMD针对受影响的系统发布了微代码。研究人员建议使用AMD Zen 2 CPU的用户尽快应用AMD的微代码更新。此外，研究人员称还可以通过将"chicken bit"设置为DE\_CFG来缓解该漏洞的影响，但这一操作会降低CPU的性能。

Ormandy称检测Zenbleed漏洞利用基本不可能，因为'vzeroupper'的不当使用并不需要很高的权限或特殊的系统调用，因此非常隐秘。

完整技术分析参见：

https://lock.cmpxchg8b.com/zenbleed.html

**参考及来源：**

https://www.bleepingcomputer.com/news/security/zenbleed-attack-leaks-sensitive-data-from-amd-zen2-processors/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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