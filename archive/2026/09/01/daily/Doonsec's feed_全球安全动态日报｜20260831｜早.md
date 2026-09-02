---
title: 全球安全动态日报｜20260831｜早
url: https://mp.weixin.qq.com/s/z2lOJU6fnfdpQqo65Mgj3w
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:36:29.891760
---

# 全球安全动态日报｜20260831｜早

# 全球安全动态日报｜20260831｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260831｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年8月30日共收录2条安全动态，内容涵盖WordPress 组件漏洞与伪造 CAPTCHA 部署反向隧道后门。

The Hacker News **2**  ·  HackerOne **0**

## The Hacker News

### 01 五个严重的 WordPress 插件和主题漏洞可导致网站接管或远程代码执行 (RCE)

**公开时间：**2026年08月30日 00:25

AI 解读

文章披露了5个WordPress插件或主题的严重漏洞，均可被未认证攻击者利用，影响包括认证绕过、管理员账户接管、权限提升、任意文件写入及远程代码执行。WPMU DEV Dashboard在启用特定SSO配置时可导致站点接管；Avada与Fusion Builder组合可写入并执行PHP文件；TranslatePress可泄露管理员密码重置信息；Pods可提升为管理员或覆盖任意账户密码；GiveWP则因不安全反序列化、攻击者可控捐赠数据及现成利用链，可能实现服务器任意命令执行。

原文：https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html

### 02 TerminalFix 利用虚假 Cloudflare CAPTCHA 部署反向隧道后门

**公开时间：**2026年08月30日 00:00

AI 解读

微软披露了一种名为TerminalFix的新型ClickFix变体，攻击者利用被入侵网站投放伪造Cloudflare验证码，诱导用户在Windows Terminal或PowerShell中复制执行恶意命令。命令下载包含合法程序与恶意DLL的压缩包，通过DLL侧加载、从PNG图片隐写提取载荷，并以注册表启动项和计划任务实现持久化；随后收集系统及Active Directory信息、探测内部网络，并部署基于Python的反向隧道后门，通过加密WebSocket转发TCP流量，使攻击者能够访问受害网络中的其他主机。该入侵还包含持续监控文件并执行新命令的PowerShell循环，可能进一步被用于权限提升、关闭安全控制、窃取数据及部署勒索软件。

原文：https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)![]()

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoPgcybP7CdwQuthRKXPkpYnwaQcOnXgEZT4r1rNWBU8D1I9HAMGWEWricXrOJ2UZNjo3YghpiaevyQ/0?wx_fmt=png)

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