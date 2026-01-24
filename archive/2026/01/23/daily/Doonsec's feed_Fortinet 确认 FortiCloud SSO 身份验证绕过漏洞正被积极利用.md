---
title: Fortinet 确认 FortiCloud SSO 身份验证绕过漏洞正被积极利用
url: https://mp.weixin.qq.com/s/vngnc3t2mZfVMflpOhYaYw
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:17.161259
---

# Fortinet 确认 FortiCloud SSO 身份验证绕过漏洞正被积极利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKItuIXQIIytjmVe0qR1ZFqqJghNMYT4NfMYBIibNuOcBvjpRnrvxe0fPvibe6ibFCOKEicHvbRZhVC22Q/0?wx_fmt=jpeg)

# Fortinet 确认 FortiCloud SSO 身份验证绕过漏洞正被积极利用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Fortinet 证实 FortiCloud SSO 身份验证绕过漏洞正被积极利用，一项新的自动化攻击活动甚至针对已完全修补的 FortiGate 设备。

网络安全公司 Arctic Wolf 于 2026 年 1 月 15 日首次观察到此类攻击，攻击涉及通过通用管理员账户快速窃取配置信息并实现持久化。

2025 年 12 月，Fortinet 披露了两个严重漏洞，CVE-2025-59718和CVE-2025-59719 (FG-IR-25-647)，使得未经身份验证的攻击者能够在启用 FortiCloud SSO 时使用精心构造的 SAML 消息绕过 SSO 身份验证。

这些漏洞会影响 FortiOS、FortiWeb、FortiProxy 和 FortiSwitchManager，允许管理员无需凭据即可访问。虽然已发布补丁，但最近在 7.4.10 等更新固件上发生的事件表明，所有SAML 单点登录实现都存在持续性或变体问题。

## **受影响版本**

Fortinet 的 PSIRT 安全公告详细介绍了存在漏洞的版本和修复方案。

| 产品 | 受影响版本 | 解决方案 |
| --- | --- | --- |
| FortiOS 7.6 | 7.6.0 至 7.6.3 | 7.6.4 或更高版本 |
| FortiOS 7.4 | 7.4.0 至 7.4.8 | 7.4.9 或更高版本 |
| FortiOS 7.2 | 7.2.0 至 7.2.11 | 7.2.12 或更高版本 |
| FortiProxy 7.2 | 7.2.0 至 7.2.14 | 7.2.15 或更高版本 |
| FortiSwitchManager 7.2 | 7.2.0 至 7.2.6 | 7.2.7 或更高版本 |

报告证实7.4.9、7.4.10 和 7.6.x 版本存在漏洞，修复程序计划在后续版本中发布。

## **攻击行动详情**

Arctic Wolf 的遥测数据显示，高度自动化的攻击与 2025 年 12 月的活动如出一辙。攻击者使用恶意SSO 登录（例如 cloud-init@mail.io），通过 GUI 窃取配置信息以进行离线凭据破解，然后创建持久账户以授予 VPN 访问权限。

攻击事件间隔数秒，目标是暴露于互联网的设备；根据之前的扫描结果，超过25000台设备启用了单点登录（SSO）。Field Effect指出，尽管已发布补丁，但最新的FortiOS系统仍然存在安全漏洞。

IOC

| 类型 | 国际奥委会 | 用处 |
| --- | --- | --- |
| 用户帐户 | cloud-noc@mail[.]io | 单点登录 |
| 用户帐户 | cloud-init@mail[.]io | SSO登录，配置泄露 |
| IP地址 | 104.28.244[.]115 | Cloudflare IP |
| IP地址 | 104.28.212[.]114 | 入侵 |
| IP地址 | 37.1.209[.]19 | 第三方观察 |
| IP地址 | 217.119.139[.]50 | 入侵 |

## **立即采取的缓解措施**

Fortinet敦促禁用 FortiCloud 单点登录：

```
textconfig system global
set admin-forticloud-sso-login disable
end
```

实施本地策略以限制管理员访问权限：

```
```
text config firewall local-in-policy
edit 1
set intf "port1"
set srcaddr "10.10.10.0"  # Trusted subnet
set dstaddr "all"
set service "HTTPS"
set schedule "always"
next
end
```
```

将已遭入侵的设备视为完全拥有：升级到最新固件（例如 7.6.x），恢复干净的配置，轮换所有凭据（包括 LDAP/AD），并审核 VPN 设置。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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