---
title: 紧急安全提醒：PVE 8 全系列已被攻破，请立即升级至 PVE 9
url: https://mp.weixin.qq.com/s/M8XsQWpBxq0S-D0_OViDkw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:50.106280
---

# 紧急安全提醒：PVE 8 全系列已被攻破，请立即升级至 PVE 9

# 紧急安全提醒：PVE 8 全系列已被攻破，请立即升级至 PVE 9

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

紧急安全提醒预计阅读 2 分钟 · 共 732 字

紧急安全提醒：PVE 8 全系列已被攻破，请立即升级至 PVE 9

PVE 8 全系列已被攻破，请立即升级至 PVE 9

#Proxmox VE#安全漏洞#身份验证绕过

各位运维朋友、PVE 用户们：最近我刚把 Proxmox VE 从 8.4 升级到了 9.2.11。升级过程中，一个严重的安全问题再次被证实：不止 PVE 7 受到影响，**PVE 8 全系列**（已知报告版本包括 8.0.3、8.2、8.4）均已被攻破，可绕过身份验证。

BREAKING

PVE 8 全系列存在身份验证绕过漏洞

攻击者可未授权访问管理界面或 API

#高危#已确认#多版本受影响

这意味着，攻击者可以在未授权的情况下直接访问你的 PVE 管理界面或 API，风险极高。  无论你是否已经把公网的 8006 端口堵住，都强烈建议尽快升级到 PVE 9。升级虽然只是堵住了这个已知漏洞，但能尽可能降低那些必须暴露在公网的 PVE 服务器所面临的威胁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxkbQez1uSjuv8xibF3uy3FGQJxkR6V0ZE5JdIAicXJ8AfxLh2niaSIg5j2UPnyCsvD5hrkHkbcJUp9MeV1qMIBdELJRsqqcnsNVI/640?wx_fmt=jpeg&from=appmsg)

## 操作建议（请立刻对照检查）

SECURITY HARDENING

六步安全加固清单

1

立即停止直接暴露

停止将任何 PVE WebUI、WebAPI（默认 8006 端口）以及 SSH 直接暴露在公网

2

必须暴露时增加二层防护

使用 VPN（如 Tailscale）、SD-WAN 或 Cloudflare Zero Trust 等方式为 PVE WebUI 增加额外防护层，最简单也可先加一层 Basic Auth；同时 sshd 配置中禁止密码登录，强制密钥认证

3

内网环境也不能掉以轻心

哪怕 PVE 只部署在内网，也请配置好 IP-ACL 规则，严格限制可访问的 IP 范围

4

PVE ≤ 8 已正式 EOL

无论当前是否受影响，都请尽快升级到 PVE 9，老版本已不再获得官方安全支持

5

PVE 9 同样建议落实以上措施

升级到最新版本后，仍建议继续执行上述安全加固，不要因为"已经是最新版"就放松警惕

6

持续关注补丁

近期运维过程中，请投入更多精力关注 PVE 相关的安全补丁和官方公告，及时跟进更新

安全无小事，虚拟化平台一旦被攻破，后果往往是灾难性的

建议大家尽快检查自己的环境，该升级的升级，该加固的加固。如果升级或加固过程中遇到问题，欢迎在评论区交流。也请把这篇文章转给身边同样在用 PVE 的朋友，一起提高安全水位。

**保持警惕，安全运维！**

感谢你的阅读与支持！

觉得有用就转给身边的 PVE 用户吧～ 🛡️

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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