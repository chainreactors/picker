---
title: Synology 修复严重的VPN路由器漏洞，CVSS评分10分
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515192&idx=1&sn=e87e601569d5822582e1538bb28323b7&chksm=ea948d52dde30444d574600b79a6c202142ec2bf9b6ce53a72934ada80a5c93a9670132bbf3f&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-05
fetch_date: 2025-10-04T03:04:41.138873
---

# Synology 修复严重的VPN路由器漏洞，CVSS评分10分

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSfgiamuOvibLI4GvAxMV0iaOSX2iaeadlEF2zjia2QtyuUGhoQbIazLZSospJLMpbvsTo0ne6tOtYIgjw/0?wx_fmt=jpeg)

# Synology 修复严重的VPN路由器漏洞，CVSS评分10分

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSfgiamuOvibLI4GvAxMV0iaOSZFDPEATO5HUCkhA6zVrzYQbvT1EMHb3icWnMvH96hOUmGOY6Mx3gicnA/640?wx_fmt=gif)

**台湾NAS厂商Synology 修复了一个CVSS评分为10分的严重漏洞，影响配置为VPN服务器运行的路由器。**

VPN Plus Server 是一款虚拟的私有网络服务器，可使管理员将Synology路由器设置为VPN服务器，从而远程访问路由器背后的资源。该漏洞可用于低复杂度的攻击活动中，无需目标路由器的权限或用户交互。

Synology 公司在周五发布的安全公告中指出，“漏洞可使远程攻击者通过Synology VPN Plus Server的可疑版本执行任意命令。Synology VPN Plus Server 1.4.3.-0534和1.4.4-0635之前版本的远程桌面功能中存在一个界外写漏洞，可使远程攻击者通过未指定向量执行任意命令。”

界外写漏洞可造成严重影响，如数据损坏、系统崩溃和内存损坏后的漏洞执行等。Synology 已发布安全更新修复该漏洞，并建议客户将VPN Plus Server for SRM（Synology 路由器管理器）升级至最新可用版本。VPN Plus Server for SRM 1.3应升级至1.4.4-0635或后续版本；VPN Plus Server for SRM 1.2 应升级至1.4.3-0534或后续版本。

上个月，Synology 公司发布另外一份被评级为严重漏洞的安全公告，并表示已修复位于Synology 路由器管理器中的多个漏洞。

该公司指出，“多个漏洞可导致远程攻击者执行任意命令，展开拒绝服务攻击或通过可疑的SRM版本读取任意文件。”

虽然Synology 并未列出这些漏洞的CVE编号，但多名安全研究员和多个安全团队因此而致谢，其中至少两名研究员或团队成功在2022年Pwn2Own多伦多黑客大赛上演示了针对Synology RT6600ax路由器的0day利用。

Gaurav Baruah 因在Synology RT6600ax的WAN接口上成功执行命令注入攻击，而获得2万美元的奖励。Computest 也在该公司的十二月份关键安全公告中获得致谢，他在同款Synology路由器的LAN接口上成功演示了命令注入 root shell 利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[开源组件 Netatalk 存在多个严重漏洞，Synology 多款产品受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511627&idx=2&sn=2ad8e314dfc9a7c5a8bcb5668e49b4f2&chksm=ea949f21dde31637c2b8855f093f9389f7a47187b7d4f00ed7e189132c1f0629ad5d60a8b7b1&scene=21#wechat_redirect)

[思科决定不修复已达生命周期路由器中的认证绕过0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513869&idx=2&sn=7199bcc2306ffa52728d244b3157c9c6&chksm=ea948667dde30f7126092d37c3a6b6ec03c1517c0a95065187739d5cfc9e2b810e54fa40d8b9&scene=21#wechat_redirect)

[NetModule 路由器中存在多个严重漏洞，客户或不知情](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513524&idx=2&sn=75b9e2e0489fcac4d6edb58489284cc4&chksm=ea9484dedde30dc8ba8bbcfc4446f5957f084754fa9b9aafeb01ce658eea44dcdbfd12d7e633&scene=21#wechat_redirect)

[思科路由器高危漏洞可导致攻击者完全访问小企业网络](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513524&idx=1&sn=a5cf54dfa1670abff17d695dbab1a5ce&chksm=ea9484dedde30dc86a0d6e81f89bbfb8ae2ce49a7c6c2d4d32a5fd6f3a9eac0ab53ba53a8092&scene=21#wechat_redirect)

[29款DrayTek 路由器受严重RCE漏洞影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513397&idx=3&sn=566426539ddd8e6e9a9982797a9e151e&chksm=ea94845fdde30d4922d1104ebea514228ae1f71f8fc57e62da41edf49b71fff71d691325cc0f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/synology-fixes-maximum-severity-vulnerability-in-vpn-routers/

题图：Pexels License‍

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