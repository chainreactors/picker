---
title: 思科：注意已遭利用的满分 SD-WAN 新 0day
url: https://mp.weixin.qq.com/s/QtIoNRdUW6t4dQfpzr6OCA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:14:07.480310
---

# 思科：注意已遭利用的满分 SD-WAN 新 0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfVNicdema5yJRNXxThbVquMVsLXgibvJnJN451zv5ic02a2RWVUyublbvXGtaydr6h7CDTm2hnvicsupK5WuDU6uEnGbpUvwujC8lI/0?wx_fmt=jpeg)

# 思科：注意已遭利用的满分 SD-WAN 新 0day

Lawrence Abrams
Lawrence Abrams

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科提醒注意严重的 Catalyst SD-WAN Controller 认证绕过漏洞CVE-2026-20182（CVSS评分满分10分）已遭 0day 攻击利用，可导致攻击者在受陷设备上获得管理员访问权限。**

该漏洞影响本地版和 SD-WAN 云部署下的思科 Catalyst SD-WAN 控制器和 Catalyst SD-WAN 管理器。思科在今天发布的一份安全公告中提到，该漏洞源自一个“无法正常运作”的对等认证机制，“攻击者可向受影响系统发送构造的请求，利用该漏洞。成功利用该漏洞可导致攻击者以内部人员、高权限的非 root 用户账号身份登录到受影响的思科 Catalyst SD-WAN 控制器。攻击者可借该账号访问 NETCONF，之后导致攻击者操纵 SD-WAN 整个架构的网络配置。”

思科 Catalyst SD-WAN 是通过中心管理系统连接办事处分支、数据中心和云环境的基于云的软件网络平台，使用一款控制器通过加密连接安全地路由网站之间的流量。

思科表示在5月份检测到威胁行动者们在利用该漏洞，但并未分享关于如何利用的详情。不过从分享的入侵指标 (IOC) 提醒管理员检查 SD-WAN 控制器日志中未授权对等事件可看出，威胁行动者在 SD-WAN 架构中注册恶意设备。攻击者可通过增加一台恶意对等体的方式，将看似合法的恶意设备插入 SD-WAN 环境中，之后该设备在攻击者的控制下设立加密连接和广告网络，从而可能移动到组织机构网络的更深处。

该漏洞是 Rapid7 团队在分析另外一个 SD-WAN 控制器漏洞CVE-2026-20127时发现的，后者也在2023年遭 0day 攻击利用。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUq3VsriaiaLtfnQZIg7wI1FCsIaPI3TgfLv8icdD19IAysxszFHEYlPQrp07HJH0HPrWIjVh6loKCpdIZBvPAwc7sOSnD3dwlcD0/640?wx_fmt=gif&from=appmsg)

**修复方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXQHWuUXkpSyvXibfClqNibo15kXPpZlVB2ic0rWRpZekTVEJqvHH3Tia7gQr2wM4sYJ4CgAtjb4YiceicCkjpWwX6iacTfWLQHDNHKn0/640?wx_fmt=gif&from=appmsg)

思科已发布安全更新修复该漏洞，并表示不存在能够完全缓解该问题的应变措施。该公司还建议仅限受信任的内部网络或授权的IP地址访问 SD-WAN 管理和控制面板接口，并审查认证日志中的可疑登录活动。

CISA 已将该漏洞纳入“已知遭利用漏洞 (KEV)” 目录，要求联邦机构在2026年5月17日之前修复该漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXmibTjIVfKW2UvdIudXedia75vTLookicPm68lUmN6RBNJ2xsmoL4f6DhAElDOANyUJGntPKw9N07ZhnALWpKcfaCdXNZTedUKZc/640?wx_fmt=gif&from=appmsg)

**入侵指标**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVXV6jDQfzUvRD8okOOjic2B2amlLuJ3Uia4MgvOu9V6PzTJeX2dDiartRQVq8VwyLElQOn44XA96bVuiaPrTpxCiaMbvqwy9Rtfialw/640?wx_fmt=gif&from=appmsg)

思科督促组织机构从任何暴露到互联网的 Catalyst SD-WAN Controller 系统中查看日志，找到可能表明未授权访问事件或对等连接事件。

思科表示，管理员应该查看 /var/log/auth.log 文件中是否来自未知IP地址、显示“Accepted publickey for vmanage-admin”内容的条目：

2026-02-10T22:51:36+00:00 vm sshd[804]: Accepted publickey for vmanage-admin from port [REDACTED PORT] ssh2: RSA SHA256:[REDACTED KEY]

管理员应该对比日志中的IP地址与WebUI＞Devices＞System IP思科 Catalyst SD-WAN 管理器 web UI 中所列的配置系统 IP。如发现未知 IP 地址成功验证，则管理员应该将设备视为已受陷并设立一个 Cisco TAC 开设案例。思科还建议查看 SD-WAN 控制器日志中的未授权对等体活动，因为攻击者可能会尝试在 SD-WAN 架构中注册恶意设备。示例如下：

Jul 26 22:03:33 vSmart-01 VDAEMON\_0[2571]: %Viptela-vSmart-VDAEMON\_0-5-NTCE-1000001: control-connection-state-change new-state:up peer-type:vmanagepeer-system-ip:1.1.1.10 public-ip:192.168.3.20 public-port:12345 domain-id:1 site-id:1005

思科强烈建议更新至已修复软件版本，这是完全修复该漏洞的唯一方法。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[思科紧急修复高危 ISE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525791&idx=1&sn=8e8b1cc8aa09816bba96ee685aa24394&scene=21#wechat_redirect)

[思科 IMC 中存在严重的认证绕过漏洞，可用于获取管理员权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525643&idx=1&sn=123aa4e38d29ce29d7107d5e7378e00f&scene=21#wechat_redirect)

[思科修复多个高危 IOS XR 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525403&idx=1&sn=a7ca207e2fb245b56f2a17c2cf9d5f80&scene=21#wechat_redirect)

[思科：注意已遭利用的两个 Catalyst SD-WAN 管理器 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525349&idx=2&sn=d24d6683fb3bc04d5b47bb36bf521194&scene=21#wechat_redirect)

[思科提醒注意满分 Secure FMC 漏洞可用于获取 root 权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525317&idx=1&sn=400b0183f75f78413cb8fd0ab335e576&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-critical-sd-wan-flaw-exploited-in-zero-day-attacks/

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