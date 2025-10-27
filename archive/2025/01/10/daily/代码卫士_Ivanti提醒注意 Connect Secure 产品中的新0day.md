---
title: Ivanti提醒注意 Connect Secure 产品中的新0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522025&idx=2&sn=f67e98879ae334210339981b77e939e9&chksm=ea94a783dde32e95cdc7f507b228d2e8c85822c8950419c515b096009972bdf7a059d31d6dfc&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-10
fetch_date: 2025-10-06T20:09:03.718871
---

# Ivanti提醒注意 Connect Secure 产品中的新0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQ8fh197ibfsdMWeicqHI7zHib00jwX4NgXhCh2p98pwmjia5cm5QDIz5SxkxM1vFRE3tXsvFx8nic2XIg/0?wx_fmt=jpeg)

# Ivanti提醒注意 Connect Secure 产品中的新0day

Ryan Naraine

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周三，Ivanti 公司提醒注意面向企业的产品中的远程可利用漏洞，并表示其中一个漏洞已遭在野利用。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ8fh197ibfsdMWeicqHI7zHibBAib0KqYKM4b2ic0xSAaHj4KscgW4kGic4BMibtkj5IhTzhYaxCPH85Ppw/640?wx_fmt=gif&from=appmsg)

这两个高危漏洞为CVE-2025-0282和CVE-2025-0283，可导致未认证的远程攻击者发动代码执行和提权攻击。

Ivanti 公司在一份安全公告中提到，“披露时我们注意到数量有限的客户的 Ivanti Connect Secure 设备遭CVE-2025-0282利用。我们并未发现这些漏洞在Ivanti Policy Secure 或 ZTA 网关中遭利用。”该公司并未分享妥协指标 (IoC) 或其它遥测数据帮助防御人员寻求妥协指标。

Ivanti 公司在安全通告中提到：

CVE-2025-0282：CVSS评分为9.0，是严重的栈缓冲区溢出漏洞，可导致未认证的远程攻击者执行任意代码。遭利用的版本包括 Ivanti Connect Secure 22.7R2.5 之前版本、Ivanti Policy Secure 22.7R1.2 之前版本以及适用于 ZTA Gateways的 Ivanti Neurons 22.7R2.3之前版本。

CVE-2025-0283：CVSS评分为7.0，是一个高危漏洞，可导致本地认证攻击者通过栈缓冲溢出漏洞提升权限，影响产品版本与上一个漏洞一样。Ivanti 公司提到，“我们并未在披露时发现CVE-2025-0283遭利用的证据。”

Ivanti 公司提到，可通过其ICT工具检测CVE-2025-0282是否遭利用，并督促客户密切监控内部和外部的ICT，确保整个网络基础设施的完整性和安全性。该公司建议客户立即升级至 Ivanti Connect Secure 22.7R2.5并继续通过其它安全工具密切监控内部和外部ICT。建议在将 22.7R2.5投入生产之前通过已通过绿色ICT扫描的设备上执行恢复出厂设置。

值得一提的是，Ivanti 公司提到，并未打算将Ivanti Policy Secure 产品面向互联网，从而大大降低利用风险。Ivanti Policy Secure的修复方案将于2025年1月21日发布。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Ivanti：注意这个CVSS 满分的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521758&idx=1&sn=d87a2de8e47def08cf6aca1b91b6e064&scene=21#wechat_redirect)

[Ivanti 中的3个0day已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521006&idx=2&sn=9a5993bb8ee14a8ab3071f40bb56c909&scene=21#wechat_redirect)

[CISA：这个严重的 Ivanti vTM 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520913&idx=2&sn=2148647cf20c87cf57d601cf283f4805&scene=21#wechat_redirect)

[CISA 和 Ivanti：Cloud Services Appliance 高危漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520811&idx=1&sn=890fffef04e0244ca4a0fe359dfb3886&scene=21#wechat_redirect)

[Ivanti 修复Endpoint Management 软件中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520759&idx=2&sn=1fc5e0f7a15b2f6ee85191294e7148e0&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/ivanti-warns-of-new-zero-day-attacks-hitting-connect-secure-product/

题图：Pexels License

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