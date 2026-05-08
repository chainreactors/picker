---
title: Palo Alto防火墙高危漏洞遭野外利用，攻击者可一键获取root权限
url: https://mp.weixin.qq.com/s/dS-IuF5aVdZPoO2z9kzfdQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:55.069614
---

# Palo Alto防火墙高危漏洞遭野外利用，攻击者可一键获取root权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1LY1eNh1EB12Vq3YozIx21fbe90INe2tGlCKvkDujCMVL06Oic6lyYZx8ibIrqTpz8Qk21Sv8JvdZRU5KfvG40hOnKjhKDQwOuM/0?wx_fmt=jpeg)

# Palo Alto防火墙高危漏洞遭野外利用，攻击者可一键获取root权限

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0vIsplZtXsUUOCiayttMKG8OSqfIK7XxDKRPu2K6VH4OkeicZIHflrvz3W1iaWXgic5KlRQG0yLT1HXicUMU4qP4mT0NLCvJ8y7dA8/640?wx_fmt=png&from=appmsg)

##

Palo Alto Networks披露了PAN-OS软件中存在的一个关键缓冲区溢出漏洞（CVE-2026-0300），该漏洞目前已在野外遭到主动利用。该漏洞的CVSS 4.0评分为9.3（严重级别），允许未经身份验证的攻击者在受影响的PA系列和VM系列防火墙上以完整root权限执行任意代码，且无需凭证、无需用户交互、也无需任何特殊条件。

##

**Part01**

## ****漏洞技术细节****

该漏洞存在于PAN-OS的User-ID™认证门户（又称Captive Portal）服务中。未经认证的远程攻击者可发送特制数据包，触发越界写入（CWE-787），导致缓冲区溢出，最终在目标防火墙上实现root级代码执行。该漏洞具有网络攻击向量、零攻击复杂度且无需任何权限，完全具备自动化利用的条件，是规模化攻击活动的理想目标。

漏洞的利用成熟度已被归类为“已遭攻击”，Palo Alto Networks确认已观测到针对暴露在非受信IP地址和公共互联网上的认证门户的有限攻击活动。

**Part02**

## ****受影响产品范围****

该漏洞影响PA系列和VM系列防火墙的多个PAN-OS版本，具体包括：

* PAN-OS 10.2 — 低于以下版本的版本：10.2.7-h34、10.2.10-h36、10.2.13-h21、10.2.16-h7 和 10.2.18-h6
* PAN-OS 11.1 — 低于以下版本的版本：11.1.4-h33、11.1.6-h32、11.1.7-h6、11.1.10-h25、11.1.13-h5 和 11.1.15
* PAN-OS 11.2 — 低于以下版本的版本：11.2.4-h17、11.2.7-h13、11.2.10-h6 和 11.2.12
* PAN-OS 12.1 — 低于以下版本的版本：12.1.4-h5 和 12.1.7

值得注意的是，Prisma Access、Cloud NGFW 和 Panorama 设备不受影响。该漏洞仅影响明确启用了 User-ID™ 认证门户且可从非受信网络访问的防火墙。当认证门户暴露在互联网上时，CVSS评分达到最高威胁等级9.3；即使在相邻网络场景下，评分仍高达8.7，属于严重级别。

**Part03**

## ****潜在危害与缓解措施****

成功利用该漏洞将对产品层面的机密性、完整性和可用性造成严重影响，实质上使威胁行为者获得对目标防火墙的完全控制权。考虑到企业防火墙作为关键网络节点的高价值密度，其风险状况尤为严峻。入侵边界防火墙可促进横向移动、流量拦截、凭证窃取和完全网络接管。

Palo Alto Networks确认，补丁将在2026年5月13日至28日之间陆续发布，具体时间取决于PAN-OS分支版本。在应用补丁之前，管理员应立即采取以下措施之一：

* 按照Palo Alto最佳实践指南，将认证门户的访问权限限制为仅允许受信内部IP地址
* 如果业务上不需要，则完全禁用 User-ID™ 认证门户

2026年5月5日，已为 PAN-OS 11.1 及以上版本提供了威胁防护签名，为已授权威胁防护的组织增加了额外的检测和拦截能力。安全团队应立即通过导航至“设备 > 用户识别 > 认证门户设置”来审核其PAN-OS配置，以确定是否存在暴露风险。鉴于 CVE-2026-0300 已确认存在野外利用，任何可从互联网或非受信区域访问的门户都应作为紧急修复的优先事项。

**参考来源：**

Critical Palo Alto Firewalls Vulnerability Exploited in the Wild to Gain Root Access

https://cybersecuritynews.com/palo-alto-firewalls-vulnerability-exploited/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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