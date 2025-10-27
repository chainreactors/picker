---
title: CISA提醒注意西门子、通用数字和康泰克工控系统中的漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515346&idx=2&sn=9c64d78059c7b3ee275ab9039c5b3544&chksm=ea948db8dde304aeca214fe6e90ce53733d06ee853e596d44400020349aeb9c8fd6ab433bba3&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-20
fetch_date: 2025-10-04T04:23:12.210206
---

# CISA提醒注意西门子、通用数字和康泰克工控系统中的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTemklgaj68k6nObQicJq7m7bptrL8VbOibUJrd5zEQAQ155bIliaLoibAlyfCtuXcyIDNMEQ6xCQvw5Q/0?wx_fmt=jpeg)

# CISA提醒注意西门子、通用数字和康泰克工控系统中的漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国网络安全和基础设施安全局 (CISA) 发布四份工控安全公告，说明了影响西门子、通用数字 (GE Digital) 和日本康泰克 (Contec) 多款产品的安全漏洞。**

其中最严重的漏洞是位于西门子SINEC INS 中的通过路径遍历漏洞导致远程代码执行的CVE-2022-45092（CVSS评分9.9）和命令执行漏洞CVE-2022-2068（CVSS评分9.8）。

西门子还修复了位于llhttp解析器中的一个认证绕过漏洞（CVE-2022-35256，CVSS 评分9.8）以及与OpenSSL 库中的一个界外写漏洞（CVE-2022-2274，CVSS评分9.8），后者可用于触发远程代码执行。

西门子在2022年12月发布Service Pack 2 Update 1软件缓解这些漏洞。

另外，CISA还提醒注意GE Digital Proficy Historian 解决方案中的一个严重漏洞CVE-2022-46732（CVSS评分9.8）。该漏洞可导致代码执行后果，无需任何认证状态。该漏洞影响 Proficy Historian 版本7.0及后续版本，已在Proficy Historian 2023中修复。

工业安全公司Claroty 表示，“攻击者可利用该事实，通过假冒本地服务绕过认证，从而导致攻击者登录到任何GE Proficy Historian 服务器并使其执行越权操作。”

CISA还更新了在上个月发布的一份ICS安全公告，说明了位于Contec CONPROSYS HMI SYSTEM中的一个命令注入漏洞（CVE-2022-44456，CVSS评分10），它可导致远程攻击者发送特殊构造的请求，执行任意命令。

虽然Contec 在版本3.4.5中修复了该漏洞，但该软件还被指易受其它四个漏洞影响，可导致信息泄露和越权访问后果。

CISA建议CONPROSYS HIMI System 用户更新至版本3.5.0或后续版本，并采取相关措施减少网络暴露以及将这类设备与业务网络隔离开来。

不到一周前，CISA发布12份相关安全公告，提醒用户注意Sewio、InHand Networks、Sauter Controls 和西门子软件中的严重漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA提醒注意日立能源产品中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=2&sn=df29998bb260f1c274b561d8d33c1ed7&chksm=ea948d0bdde3041d86dd780d173b82a65374d35b5fc063d67de6fb5a4dde1e81e6b3d7805a8c&scene=21#wechat_redirect)

[CISA称两个JasperReports老旧漏洞遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515167&idx=2&sn=20af92858a0c19feb709a6d9fe2b8626&chksm=ea948d75dde3046329314ec3cdf0d4402e72468464a1d691d7674006d19ac7af82207ad2f131&scene=21#wechat_redirect)

[CISA：注意这三个工控系统软件中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=3&sn=dd3d82b3a03b5b06090e5bc38014da44&chksm=ea948844dde301521b0cb907cb7dc3aadabd0e9a46e67d5b3855a850f580c0124798fa2504ec&scene=21#wechat_redirect)

[CISA：注意影响Advantech 和日立工业设备的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514269&idx=3&sn=42277be117ca4047c20dedbf1712beee&chksm=ea9489f7dde300e1a90950387af6f1655ca62e307fbb6644d0534ad880c3e4b3c475bed3e5fa&scene=21#wechat_redirect)

[CISA要求联邦机构定期追踪网络资产和漏洞情况](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514137&idx=2&sn=3d803ae8e1029afd224613643defdb11&chksm=ea948973dde3006536a10f203f81bedae2b006911e312c4e70bd28d1aded4a00ee678ac3c714&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/01/cisa-warns-of-flaws-in-siemens-ge.html

题图：Pixabay License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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