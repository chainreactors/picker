---
title: FortiGate防火墙遭自动化攻击，攻击者窃取配置数据
url: https://mp.weixin.qq.com/s/zcEhHRGryf4Uv8Ej-QVbBg
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:27:28.784071
---

# FortiGate防火墙遭自动化攻击，攻击者窃取配置数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJZpTxpYYQtLW9fPVic9DLR2IEgZnBZMqGlAsiaDa8aXtH3rEicysZpkkfUHkuibLYYa8YLj5MVAs1yA/0?wx_fmt=jpeg)

# FortiGate防火墙遭自动化攻击，攻击者窃取配置数据

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJZpTxpYYQtLW9fPVic9DLRZ6pRz7QJ2mYX4uXfYGKLibWu1ecugKPbdx3x5wSbvKhRZicNsPmKXBlQ/640?wx_fmt=jpeg&from=appmsg)

网络安全研究人员发现针对FortiGate防火墙设备的新型自动化恶意活动集群。自2026年1月15日起，威胁行为者被观察到执行未经授权的配置更改、通过通用账户建立持久性访问权限，并窃取敏感防火墙配置数据。

此次攻击活动与2025年12月的事件相呼应，当时Fortinet披露关键漏洞（CVE-2025-59718）和（CVE-2025-59719）后不久，就发生了恶意单点登录（SSO）事件。

Arctic Wolf指出，初始访问方式尚未确认，但攻击手法与此前的SSO滥用相似。检测系统已激活，可向客户发出可疑活动警报。Fortinet尚未确认现有补丁是否能完全防御这波攻击。

2025年12月初，Fortinet发布安全公告FG-IR-25-647，详细说明了两项关键的身份验证绕过漏洞。当启用FortiCloud SSO时，攻击者可构造恶意SAML消息绕过SSO登录。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icJZpTxpYYQtLW9fPVic9DLRPO8x4jLepG0EHaU6nkwRo2IzBf32cuaI9GHIz6bQM8byRsE1nLfeGQ/640?wx_fmt=png&from=appmsg)

漏洞披露后，Arctic Wolf观察到管理员账户的SSO登录活动，随后出现配置转储和持久化行为。目前尚不清楚1月的攻击是否利用了相同漏洞或已修补的变体。

**Part01**

## ****攻击链分析****

Arctic Wolf的遥测数据显示，这些攻击高度自动化，杀伤链的多个阶段在几秒内相继完成。

* 初始访问：恶意SSO登录从特定托管服务提供商IP地址发起。入侵使用的主要账户为cloud-init@mail.io。
* 数据外泄：登录后，攻击者立即通过GUI界面将系统配置文件下载至同一源IP。
* 持久化：为维持访问权限，攻击者创建次级管理员账户。常见观察到的用户名包括secadmin、itadmin和remoteadmin。

日志显示，登录、配置导出和账户创建之间的时间差可以忽略不计，证实使用了自动化脚本。

**Part02**

## ****入侵指标（IOC）****

监控以下入侵指标以发现潜在威胁：

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icJZpTxpYYQtLW9fPVic9DLR9znicQoyicMbIwibhbAjanFy8Fe2yG96rFh3dQ9dltTmYFtHXZtKUjckA/640?wx_fmt=png&from=appmsg)

**Part03**

## ****缓解措施****

Fortinet用户应监控官方安全公告并及时应用补丁（升级指南）。若发现匹配活动，应立即重置所有凭证——哈希凭证可能被离线破解。

将管理接口限制在可信内部网络是防御大规模扫描的最佳实践。作为临时解决方案，可禁用FortiCloud SSO：

```
textconfig system globalset admin-forticloud-sso-login disableend
```

企业应立即搜索这些入侵指标并审查FortiGate日志。

**参考来源：**

FortiGate Firewalls Hacked in Automated Attacks to Steal Configuration Data

https://cybersecuritynews.com/fortigate-firewalls-hacked/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibofXkkXsibM0gxKLeZpLUxE5N5yynHrkPcsZaNiadWaTSImfSkk4VOXvR94ll4rG2VEPGMur17m97A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

###

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