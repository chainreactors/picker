---
title: 【安全圈】名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064456&idx=3&sn=87bccc3f00395c9c6bea0ad453226787&chksm=f36e6688c419ef9e614411dab424ce647290ad6ec683d5972cbe8d8a1194142529766aa8f942&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-17
fetch_date: 2025-10-06T18:26:50.275032
---

# 【安全圈】名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBcJDicQscLhw6FIdDXFkmS9nCuQ9BlXLmjaZq6pRHcPJIPgHousrdI6Q/0?wx_fmt=jpeg)

# 【安全圈】名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意软件

Aqua Security Nautilus 研究人员发现了一种名为 Hadoop 的新型 Linux 恶意软件，该恶意软件以 Weblogic 服务器为目标。这个名字来自于《街头霸王》系列中的攻击“浪涌拳头”。执行后，该恶意软件会放置 Tsunami 恶意软件并部署加密挖矿程序。

WebLogic Server 是由 Oracle 开发的企业级 Java EE 应用程序服务器，旨在构建、部署和管理大规模分布式应用程序。

在针对 Weblogic 蜜罐公司的攻击中，暴露了漏洞和弱密码，威胁行为者利用弱密码获得了对服务器的初始访问权限并实现了远程代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFB6I3NQxBv2PCC582nLGc3uJQJPK2plrk9RI3dJ6ky9F2py4YXXMYWow/640?wx_fmt=png&from=appmsg)

一旦入侵了 WebLogic 服务器，威胁行为者就会使用 shell 脚本和 Python 脚本（分别称为“c”和“y”）来下载和执行 Hadooken 恶意软件。这两个脚本都通过将其下载到临时文件夹来用于恶意软件部署。此 Python 代码尝试通过迭代多个路径然后删除文件来下载和运行 Hadooken 恶意软件。shell 脚本还以包含 SSH 数据的目录为目标，以允许在组织内横向移动并破坏其他服务器。然后，恶意代码会清除日志以隐藏活动。

*“Hadooken 恶意软件本身同时包含加密挖矿程序和 Tsunami 恶意软件。当 Hadooken 恶意软件被执行时，它会丢弃两个 elf 文件。第一个文件是一个打包的加密挖矿程序，以 3 个不同的名称分为 3 个路径：’/usr/bin/crondr’、’/usr/bin/bprofr’ 和 ‘/mnt/-java’。“Aqua Security 发布的报告写道。第二个文件是 Tsunami 恶意软件，生成随机名称后，它被丢弃到 ‘/tmp/<<random>>”。我们没有看到任何迹象表明攻击者在攻击期间使用了 Tsunami 恶意软件。不过，它可以在以后的攻击中使用。*

两个 IP 地址用于下载 Hadooken 恶意软件;第一个 89.185.85.102 仍然有效，并在德国注册为 Aeza International LTD，而第二个 185.174.136.204 为非活动状态，在俄罗斯注册为 AEZA GROUP Ltd。活动 IP 之前曾与 TeamTNT 和 Gang 8220 相关联，但研究人员表示，没有足够的证据将这次攻击归因于任何一个组织。

报告表明，使用 Hadooken 恶意软件的威胁行为者将 Windows 端点作为勒索软件攻击的目标，以及大型组织通常使用的 Linux 服务器来部署后门和加密挖矿程序。对 Hadooken 二进制文件的静态分析揭示了与 RHOMBUS 和 NoEscape 勒索软件的联系，尽管动态分析显示没有积极使用。

*“在 Shodan（用于查找互联网连接设备和系统的搜索引擎）中搜索表明，有超过 230K 互联网连接的 Weblogic 服务器。”该报告总结道，该报告还提供了妥协迹象 （IOC）。“进一步的分析表明，他们中的大多数都受到了保护，这非常好。我们看到了几百个连接互联网的 Weblogic 服务器管理控制台。这些可能会受到利用漏洞和错误配置的攻击。*

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjicbKBqZwLQOxpR2qCTWlaiaM5jCxqdicU8OIgjqQBficHFboNPXYSLA7LQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibj8Zw7CkjRgdkISTjGSylfpzEbSeU0MR1MyV4mNgsDVGYFpFRciaw820Q/640?wx_fmt=jpeg)[【安全圈】公然入侵国家机关系统篡改网络传输数据，法院判了！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064438&idx=2&sn=a3e598d8790286b671037a89c877b5b7&chksm=f36e66f6c419efe02eef7d5e55a96db27cbb4fbe484b306f55b675f49724e292d4579a810bf9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjUZHVxvj9xuwq2VUNY7LWzsU86Iq9WQVMCN792aE23UQIC6BtOzoNHA/640?wx_fmt=other)[【安全圈】57岁前员工怒删公司备份、搞瘫3000+台电脑，勒索532万元未遂被捕！网友：怀疑他是被裁的](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064438&idx=3&sn=437555202148f978ad5399834d57c798&chksm=f36e66f6c419efe00dd8ee70aca196a85b33e51b6e80c08228cc0809448d3628bdddffa8bdf1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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