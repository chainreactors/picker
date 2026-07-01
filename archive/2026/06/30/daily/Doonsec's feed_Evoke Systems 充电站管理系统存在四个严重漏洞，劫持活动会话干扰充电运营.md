---
title: Evoke Systems 充电站管理系统存在四个严重漏洞，劫持活动会话干扰充电运营
url: https://mp.weixin.qq.com/s/lzI98GqfRXjXh2_XDtiViw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:21.392304
---

# Evoke Systems 充电站管理系统存在四个严重漏洞，劫持活动会话干扰充电运营

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXHIJibH0jOe4NSTB9cXpxg9lFiaVx8YdSayGHPJoNcORR4rq7TvV8G3LBDoHZKg1KtTSTHZh9ziawF4fEc3Y7kzEGdM95ibJGvqOA/0?wx_fmt=jpeg)

# Evoke Systems 充电站管理系统存在四个严重漏洞，劫持活动会话干扰充电运营

Do Sun
Do Sun

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**EVoke Systems****充电站管理系统的所有版本当前均受四个严重安全漏洞影响。这些漏洞可使攻击者劫持活动会话，并扰乱日常充电运营。管理员必须立即实施现代身份验证配置，保护这些关键网络的安全。**

该管理软件控制着分布于美国多个地点的电动汽车充电关键基础设施。攻击者可对存在漏洞的充电站获取未经授权的管理控制权，进而通过定向拒绝服务攻击扰乱基础服务。这一威胁危及公共充电的可用性，并破坏电网稳定性。此外，恶意人员还可能从网络中窃取敏感的运营数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWKic4s6ib0rwORe4Xia0SAgm4NTEjTlJxLW6aufy70Bkssibs0mm5ZchI6Bh1nDeOY6aF3ibMHiawjRibSFIku9MNlHxTykrO0yWvHb0/640?wx_fmt=gif&from=appmsg)

**攻击方法**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfX8oQALDl1jeFTsTlYut8xQuico3ePFOs1YXEGAXz1ImjicWgn7oExP1LKGSicsuJhwTto19NNjfSU6sNsyt4BGX8LEeCFCaVrlJg/640?wx_fmt=gif&from=appmsg)

该平台的主要 WebSocket 端点完全缺乏适当的身份验证检查。具体而言，CVE-2026-40702 允许攻击者以极低代价冒充合法充电站。其次，CVE-2026-50176 反映了编程接口上严重缺乏速率限制。这一缺陷使得针对后台系统的自动化暴力破解攻击成为可能。

此外，CVE-2026-54479 在应用程序内生成了高度可预测的会话标识符，多个端点可能错误地使用完全相同的会话 ID 进行连接。最后，基于 Web 的映射平台公开暴露了充电站的身份验证标识符。攻击者综合利用这些问题，可完全绕过访问控制。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWJDia2USHqRrAG1Tsn3thawIEicu3H08ttI5xM0bnZyY6X0ibKBLKEBbkicRp7DuPE7qSiaHtYJOmSl1sYkticicXBqF7nVKhoEdqs2c/640?wx_fmt=gif&from=appmsg)

**利用状态**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXxjtAoTEOfASVmL46ywFR8PsicDMZZHG29GX63NGibz6ic5K3UZzicE5mTutPCwjJxsoviciapdichIwHYiaK26KUFJSUQwqiabwLMDCtk/640?wx_fmt=gif&from=appmsg)

安全研究人员尚未证实这些漏洞已遭在野利用。同样，目前也不存在公开的概念验证利用代码。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXMXzNrCuNZoGFtPAzqsk9aHiaagiaz4kXDh2ofShiaic7kpYXErs0GVc7zxSLN3XWSqjWdic8vE2Via3x5R2ibR37tCulp93ibCSjZgUU/640?wx_fmt=gif&from=appmsg)

**受影响版本**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWy8wIeQDC08YHVSB4DicFxzvkNG1HHIsKeiaSZ2GVvGfzGeaUkwodZs0hKMpF8kRN9hM3HlwuGAayhKyPf1fB7QIphzkxCVTbeg/640?wx_fmt=gif&from=appmsg)

这些严重漏洞影响所有已部署的 EVoke CSMS 软件版本。每个安装实例均需立即进行审查。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfW31R66PK43664Yw0g2yk2vRzT9SN3adiceT1Ym77trm54QGfMFTCNLxNh7P3fDp9xXg8ibnnPDeDgVyZibpNoefwkfc1nrFKVcB8/640?wx_fmt=gif&from=appmsg)

**补丁或缓解措施**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUZuhYfZku0zXdJaeGyiaia0pU5kgjIbEoTmeVxCEic1aTUmFcwh5Le0RImSM1uvl70d3AtXmGiaxub3pV0jsMyawFD031SuL2JwSQ/640?wx_fmt=gif&from=appmsg)

EVoke 强烈建议将所有充电桩升级至 OCPP 安全配置 2 或 3。这些更新的配置要求强制使用 TLS 加密和基本身份验证方法。然而，部分老旧充电桩无法支持这些现代安全标准。因此，EVoke 正在部署服务端防护措施，以拒绝未知的充电桩标识符。

此外，该平台现在将每个充电桩 ID 的活动连接限制为单个会话。后台将自动终止重复会话以防止欺骗攻击。EVoke 还将在网关层实施连接速率限制。同时，该平台正在为不受支持的老旧充电桩制定生命周期策略，包括风险分类以及与站点运营商的具体迁移规划。用户可访问 CISA 公告页面查阅官方公告。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[XCharge C6电动汽车充电桩存在多个严重漏洞，可导致任意代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526201&idx=2&sn=94f249f0b82ed4528faa20db71165ca7&scene=21#wechat_redirect)

[电动汽车充电网络告警：Everon OCCP 后端系统存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525349&idx=1&sn=352cbd47ed06c60804138658fa37fece&scene=21#wechat_redirect)

[施耐德EVlink 电动车充电站有新漏洞，可导致电动车遭劫持](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509886&idx=2&sn=416f5084c5202191f48db6446540334e&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/evoke-systems-vulnerabilities/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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