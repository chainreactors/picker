---
title: 两个漏洞可用于攻陷谷歌 Looker 实例
url: https://mp.weixin.qq.com/s/h0sTAppUiTNsQRzcKgz7Pw
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:04:28.757818
---

# 两个漏洞可用于攻陷谷歌 Looker 实例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfU445mK24oFosxfTVAfba5DsSWGiaWfqOUGjDvqeW4eH0OMq8B57WjGFJJ875hxKoWTlX6ct8xw4DeON1FLibZQ4oDoz9ypSAnCI/0?wx_fmt=jpeg)

# 两个漏洞可用于攻陷谷歌 Looker 实例

Eduard Kovacs
Eduard Kovacs

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全公司 Tenable 的研究人员发现了两个漏洞，可用于完全攻陷谷歌 Looker 商业情报平台的实例。**

谷歌 Looker 使组织机构能将分散的数据集整合到统一数据层，以创建实时可视化图表、交互式仪表盘和数据驱动型应用。企业可选择由谷歌云完全托管实例的SaaS版本，也可将平台部署在自有基础设施上。

研究人员发现该平台存在两个漏洞，若被利用可能导致远程代码执行及敏感信息泄露。这些漏洞被统称为“LookOut”，可遭拥有目标Looker实例开发者权限的攻击者利用。

研究人员指出，远程代码执行漏洞可使攻击者获得底层基础设施的完全管理权限。攻击者能够窃取机密信息、篡改数据，或进一步渗透内部网络。Tenable公司进一步说明指出，在云端部署的实例中，该漏洞可能引发跨租户访问风险。第二个漏洞为"授权绕过漏洞"，攻击者可利用该漏洞接入Looker内部数据库连接，并通过基于错误的SQL注入技术窃取完整的内部MySQL数据库。

谷歌已于2025年9月下旬修复了这些漏洞。虽然该公司已为云端托管实例部署补丁，但自托管实例的用户需确保其运行的是已修复漏Looker版本。谷歌表示目前未发现漏洞遭在野利用的证据。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[谷歌 Gemini 提示注入漏洞可用于暴露私有日历数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524925&idx=2&sn=f89ae14d71d858aa5b0a3b1ba66faf9d&scene=21#wechat_redirect)

[谷歌紧急修复 Chrome 中的两个高危内存损坏漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524683&idx=3&sn=ccf1081df758629e4af0ca28f97b0972&scene=21#wechat_redirect)

[谷歌Gemini Enterprise存在漏洞，可导致企业数据遭暴露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524630&idx=2&sn=be82a743b4b79c2cc101a8757cb82cc4&scene=21#wechat_redirect)

[谷歌修复107个安卓漏洞，其中2个已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524571&idx=1&sn=877a0981b4dec19068dff6f479fce3b9&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vulnerabilities-allowed-full-compromise-of-google-looker-instances/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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