---
title: 每天扫描全网 IPv4！VirusTotal新能力上线，入局网络空间资产测绘
url: https://mp.weixin.qq.com/s/6PRTxT07-u7hzIwDwio1tA
source: Doonsec's feed
date: 2026-10-11
fetch_date: 2026-10-12T08:12:58.279582
---

# 每天扫描全网 IPv4！VirusTotal新能力上线，入局网络空间资产测绘

# 每天扫描全网 IPv4！VirusTotal新能力上线，入局网络空间资产测绘

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

过去在 VirusTotal 搜索一个 IP ，你能看到的东西其实很有限：谁托管的、有哪些域名解析到过它、有没有恶意文件跟它通信、检测引擎给了多少分。

这些信息有个共同点：全是别人对它的记录。

过去VirusTotal只能告诉你一台服务器**名声好不好**。

至于这台机器本身在跑什么，页面上都没有。

现在，VirusTotal 开始每天扫描整个公网 IPv4 空间，把每个 IP 的开放端口、关闭端口、服务、Banner、指纹全部存下来，并且做成可搜索字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtibQA8OrrgkPu8FSm2s0oSkzOmBssp9L3AibG8nQnm5naR1BiaFyYlibx8t1ZWWlmibww2vX80WBorOreTUkCqqXAcQt9iczJ4b5AJ2A/640?wx_fmt=png&from=appmsg)

这不是小功能更新，这是VirusTotal 威胁情报生产逻辑的一次改写。

以前你只能问：这个 IP是不是恶意的？

现在你可以问：**这台机器长什么样？哪些机器和他是同一批的？**

让人眼前一亮的是，**关闭的端口**也被保留了。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt9KLrufzyriavA0Mz2ibgTKFcFJ755ZiaHPqRu0icInRyocK6nNrF1icq7vt5pGItWtqHGYAvnJe552Be0meNU8xcic2zq1lWT9cW5DE/640?wx_fmt=png&from=appmsg)

端口不是开了就永远开着。

以前端口一关这些信息就没了，现在 VirusTotal 会把状态翻成 closed，同时记下最后一次看到它开放的日期。

> 这个 C2 是什么时候下线的?

做过应急的人都知道这句话的含金量，有些攻击者的基础设施的寿命往往只有几天到几周，等你拿到线索，它早就没了。

能回头看"它什么时候存在过"，就很有必要了。

指纹的价值，比想象中更大。

SSH Host Key 在服务器安装时生成，几乎等于机器的 DNA。

两个 IP 如果共享同一个密钥，要么是同一台机器搬家了，要么是同一镜像批量克隆出来的。

无论哪种，背后往往是同一拨人。

VT的博客里给了一个例子：从一个已经被标记为 APT28 / Havoc 相关的匈牙利 IP 出发，用 SSH 指纹一搜，直接挖出另一个**完全干净**的冰岛 IP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt80LzibniaCNEPLGop9qicQzBSiacKfNOMjWFOl2KFlCMEMQwYk5GsXepcckO2LBJapyRZLwicSXCo57N2pvRh7MxQXt96MQdYTFRII/640?wx_fmt=png&from=appmsg)

声誉分数是 0，没有检测，没有集合，按以前的逻辑根本不会有人多看一眼。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtick3sic9J8pI9p4ZrzvMqhnicLSFSjJ28egDDM0qF5R6CrfZYxJGcyk97hZCjAmyzzhRxCWlJYhrfam4ibGkhNjrgB5dEibDaB4uzo/640?wx_fmt=png&from=appmsg)

但 Ports 数据告诉你：同一密钥、同一 OpenSSH 版本、同一 nginx、一样奇怪的证书。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFticUAB99zZicXibibqE01pMmIqkKTiccoiaWKhicpo346zd3Hrq7bFuGqMVcD2CGS45xnsia1rG1ft9gpRtNz9g6Yo0mQku94m6fjy5cuk/640?wx_fmt=png&from=appmsg)

再往下挖，第三个已经关掉端口的 IP 也现身了。

时间线对得上——旧节点下线，新节点几天内拉起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9be2xD0ibg002LUV2JcarFg59Po24ic36rAsGdhgYFkZficZY2xRN7ZqjCJ1TbKle14Hmia0zxmbaXlh1WJzDaBA83gibxtGdFHxsc/640?wx_fmt=png&from=appmsg)

这就是以前声誉分数回答不了的问题：
**看起来干净的IP，是不是其实是同一拨人的备用节点？**

当然，指纹也不是万能的。共享密钥只有在「稀有」时才有意义。

VPS 模板可能让一千多个 IP 撞同一把钥匙，家用路由固件也能批量中招。

两三个命中是线索，上千个只是厂商默认值。

另一个例子更直观。

有人用 URL 搜索挖到一个挂在裸 IP + 非标准端口上的登录页，截图一看，是 `NOX Stealer` 的操作面板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt8K6q0gvOtt4RAoyZ6YibdMOdqFAoUmtO5cpCs0hCYAW5iaicBOMrba1hLwxcMhTaF5kb3Opg8uLMEtql71qYABqSJORe52BP4H4A/640?wx_fmt=png&from=appmsg)

域名藏在 Cloudflare 后面，源站不好追。

但点进对应 IP 的 Ports 标签页，整台机器的画像：Windows Server 2022、SMB 和 RDP 全开、nginx + PHP 跑在 8443。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt82wYf2uEO1nr3Ur3ENRqYNEkwAHBOOKxBNAlEnELKrXzfDhtbSeoMrIreia6LlS2moXsqDBb5pDVDNGqUZuficJg5XgPlaWcb2U/640?wx_fmt=png&from=appmsg)

单独搜开放 8443 的 IP 有四百多万。加上服务栈和操作系统条件后，只剩 10 个。

更有意思的是，写博客期间这个面板被重新扫描，运营者把名字从 `NOX` 改成了 `BOMBAY`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtibjL9XmNSG5B027JJZ0mSE5fqiayN90SbM603YQl1ickqYr4GgFib2GnBu9ezhNhesTzGGSwaiasJ9HiasuH5rxIK7nxgR96yr8XiaG8/640?wx_fmt=png&from=appmsg)

页面文案换了，静态响应压成了 193 字节的小 stub。

但主机指纹没动——服务、版本、操作系统全没变。

最后，VirusTotal新增的端口与服务扫描能力，明显直接与Shodan、Censys形成竞争

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFticj01HoFBribtrsrhEHEgsR5OjJ6192b4tJrs3kJ2Z6hHS4ibMY16kgQic3jiaNl2WAq3Ijx9YF3rGcuEH3J6M4VaR76vblic7Intb0/640?wx_fmt=png&from=appmsg)

一个日语用户直接称其为“Shodanもどき”（Shodan 仿品）

Shodan、Censys之前就基于端口测绘，推出了用于威胁狩猎的功能/产品。也经常发布技术文章，探讨如何基于互联网资产测绘做恶意基础设施发现（国内一般叫资产拓线）。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFticaDu3nuecK5Frv0xdrTG16DO9G7ficoSvshciavXdacT0PXu1JvBFy17uxD0LVMHPpaSSHstxicRSW7aROFw3XcGfTf7YA1GzjicU/640?wx_fmt=png&from=appmsg)

Censys 的Adversary Investigation模块

现在 VT覆盖互联网扫描、服务指纹检索和恶意基础设施发现，意图明显是把原本需要跨平台切换到 shodan/censys完成的威胁调查，尽量留在VT/GTI体系内。

谁能看见更多、更及时的线索，谁能让用户少切换几个工具、更快完成证据关联，谁就更有机会成为用户日常调查的首选入口。

参考资料：https://blog.virustotal.com/2026/10/internet-scanning-in-vt.html#

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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