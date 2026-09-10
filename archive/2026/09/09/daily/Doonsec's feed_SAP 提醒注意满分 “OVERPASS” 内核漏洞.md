---
title: SAP 提醒注意满分 “OVERPASS” 内核漏洞
url: https://mp.weixin.qq.com/s/XMloH8KZLXuf0gD56mVapg
source: Doonsec's feed
date: 2026-09-09
fetch_date: 2026-09-10T06:46:52.039285
---

# SAP 提醒注意满分 “OVERPASS” 内核漏洞

# SAP 提醒注意满分 “OVERPASS” 内核漏洞

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**SAP****在****9****月的安全更新中修复了多个产品中的总计****20****个漏洞，其中包括一个****SAP Kernel****代码中的满分内存损坏漏洞****(CVE-2026-44756)****。**

报送该漏洞的Onapsis公司的安全研究人员将其称为OVERPASS，其根源在于扩展护照协议 (EPP) 处理库中存在常见的缓冲区溢出弱点。成功利用该漏洞可使未授权威胁攻击者以管理员权限在易受攻击的SAP主机上运行任意命令，从而导致底层SAP进程和业务数据被完全攻陷。

该漏洞可通过SAP Internet通信管理器 (ICM) 进行利用。ICM是SAP应用服务器的网络组件，负责通过HTTP、HTTPS和SMTP将SAP系统（SAP NetWeaver应用服务器）连接到互联网。

根据Onapsis公司的估计，超过10000个面向互联网的SAP系统使用了该易受攻击的组件，可能面临利用CVE-2026-44756漏洞的攻击风险。Onapsis公司的首席技术官JP Perez-Etchegoyen周二表示：“使用高保真指纹进行定向搜索，识别出超过10000个唯一的面向互联网的IP地址，这些地址展示了可从公共互联网访问的SAP Web界面，而且这个数字还是保守估计。它只统计了可通过HTTP访问的系统，并且实质上少计算了SAP Web Dispatcher，因为后者代理其后端，且在其根路径上不返回可区分的SAP横幅，这使得互联网范围的扫描器在归因上存在结构性困难。”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWuEP4vcZBqm8B1TYWs0yeY0GbZ9jBsVJUTno7GLhYbBzZ1NCo75gWAtkuN5vreaic3DcdA4YMfVWvLDicRFPKcFwsibk4ibavMZuM/640?wx_fmt=gif&from=appmsg)

**S4GET，SAP NetWeaver消息服务器中的逻辑漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUj4EHcFMQyCMTy5Y7qaHYUZ9hBXcnK2HnzC5UOsua2hX4xfS3axLpotN6nVxUlQ4cWYvZkbZA3CCEJttyeX5kyUEX92b1ctM4/640?wx_fmt=gif&from=appmsg)

今天，SAP还修复了位于SAP NetWeaver消息服务器中的一个严重身份验证缺失漏洞 (CVE-2026-58240)，被Onapsis研究实验室命名为“S4GET”。成功利用该漏洞可导致未认证攻击者访问整个SAP系统集群，并在网络中远程执行恶意负载和任意命令。Onapsis公司的安全研究员Pablo Artuso解释称：“该漏洞通过每个SAP GUI客户端都连接的同一公共端口触发，因此无法在不破坏最终用户登录的情况下通过防火墙隔离。利用该漏洞无需凭据、无需证书，也无需预先存在的错误配置。攻击一旦成功，可在集群中的每个应用服务器上以<sid>adm（运行SAP的操作系统级用户）身份实现完全远程代码执行。”

上个月，SAP修复了基于云的电子商务平台Commerce Cloud中的另一个满分的严重漏洞 (CVE-2026-58231)，威胁情报公司Defused在该漏洞被修补后数天内就标记其已被活跃利用。

自2021年11月以来，美国网络安全和基础设施安全局 (CISA) 已将14个SAP安全漏洞添加到其已被积极利用的漏洞列表中，其中包括三个被勒索软件团伙滥用的漏洞。SAP是一家德国跨国软件公司，报告称2025财年总收入超过360亿欧元，为全球最大的100家公司中的99家提供服务。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[SAP 官方 npm 包受陷，被用于供应链攻击窃取凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525926&idx=3&sn=f176577fa7fbeba25d5c024f432e1ade&scene=21#wechat_redirect)

[SAP NetWeaver 出现新漏洞 无需登录即可接管服务器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524187&idx=1&sn=7c8c5d4d69007d76c87484476c80addd&scene=21#wechat_redirect)

[SAP S/4HANA 中严重漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523967&idx=1&sn=4fb0beaa6d1cf5b33d3224c1e6783d9f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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