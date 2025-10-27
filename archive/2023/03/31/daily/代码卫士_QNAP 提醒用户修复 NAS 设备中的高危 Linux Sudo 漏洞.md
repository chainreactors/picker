---
title: QNAP 提醒用户修复 NAS 设备中的高危 Linux Sudo 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516096&idx=3&sn=82f067c61adcd0aa4a98ca6165d9c9d3&chksm=ea948eaadde307bc40d0015e6feadf0f1264ab387fd2b2500439ce984d5722ddf2e79da15ca4&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-31
fetch_date: 2025-10-04T11:15:28.595439
---

# QNAP 提醒用户修复 NAS 设备中的高危 Linux Sudo 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ib6qXSjjA5qYCssZsP4NQqZLgfDkjMGwbCcF5Pn5mTWlEWveNKRGg1cQ/0?wx_fmt=jpeg)

# QNAP 提醒用户修复 NAS 设备中的高危 Linux Sudo 漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibRxuOIwscjgDA8rFZCIwVNoAbV3rqdRYbjqMLzkHicEudB8OeMTFMPbA/640?wx_fmt=gif)

**QNAP 公司提醒客户修复位于 NAS 设备中的一个高危 Sudo 提权漏洞 (CVE-2023-22809)。**

该漏洞是由 Synacktiv 安全研究员发现的，被描述为“sudo 用户在使用 sudoedit 时可绕过 Sudo 版本1.9.12p1中的策略”漏洞。如成功利用使用 Sudo 版本1.8.0至1.9.12p1 的未修复设备上的漏洞，可导致攻击者通过将任意条目附加在需处理的文件列表后编辑越权文件的方法，提升权限。

QNAP 在安全公告中指出，该漏洞还影响 QTS、QuTS hero、QuTScloud 和 QVP NAS 操作系统。虽然该漏洞已修复 QTS 和 QuTS hero 平台中，但仍在推出 QuTScloud 和 QVP 安全更新。

QNAP 提醒称，“请定期查看获取安全更新，将操作系统尽快升级到最新推荐版本。为保护您的设备安全，我们建议您定期将系统升级到已修复的最新版本。”

**如何保护 QNAP NAS 设备安全？**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

要更新 QTS、QuTS hero 或 QuTScloud，客户需以管理员用户身份登录后，在控制面板＞系统＞固件更新的“实时更新”下点击“查看更新”选项。或者可以在选择设备的产品类型和型号后，从QNAP公司的下载中心手动下载固件更新。

QNAP 公司并未在安全通告中将 CVE-2023-22809 漏洞标记为已遭在野活跃利用状态。然而，鉴于该漏洞的严重程度以及威胁行动者一直活跃利用 QNAP NAS 安全漏洞，建议客户尽快应用安全更新。

最近，DeadBolt 和 eCh0raix 勒索组织就滥用多个漏洞，加密在互联网设备上暴露的数据，攻击 QNAP NAS 设备。今天，QNAP公司宣布正在修复影响其产品的其它漏洞，位于 OpenSSL、Samba 和QNAP 自身的操作系统中，可被用于执行远程代码和泄漏信息。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[前安全主管指责推特隐藏重大缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513659&idx=3&sn=83c9171a4f8f66638bcb11e45ba2c290&chksm=ea948751dde30e472e7875c8b3204ff855b8f1b5ddc5cf453365da35cdbbd8a84d71764425cb&scene=21#wechat_redirect)

[黑客利用推特漏洞，暴露540万个账户的信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513431&idx=5&sn=0346caf7c1c41c8422d1e72b5f8f2269&chksm=ea94843ddde30d2b2f9c5f09450d3fb86026d32586332c600d220fd63d917484996b91614e7b&scene=21#wechat_redirect)

[加拿大第二大电信运营商的源代码和员工数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515762&idx=3&sn=26f5b087e791a7161bd89b0e3702a8db&chksm=ea948f18dde3060e5240089e18dc49989ea692e539dac35579e8b91baa81345d11dc2c394944&scene=21#wechat_redirect)

[俄罗斯版“谷歌”Yandex源代码遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515387&idx=3&sn=28fb6538b4b168c8a79d6bace6795343&chksm=ea948d91dde30487738e1f1b496baddad423bc371bc08e152dd0dc1ceba25187f0f0c81d9a38&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/qnap-warns-customers-to-patch-linux-sudo-flaw-in-nas-devices/

题图：Pexels License

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