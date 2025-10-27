---
title: 思科修复已有 PoC 的根提权漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=1&sn=00f735c28afb0e6cc70f919cade9dc5c&chksm=ea94a0c1dde329d7537d32cf0cc038587d8e6da619b0dc82fb99bb8917e432ece7028a7dd65c&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-06
fetch_date: 2025-10-06T18:27:33.145246
---

# 思科修复已有 PoC 的根提权漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT6xjqHOeO1vcMPdOia7sO53KvQ4g54aO36mtuHXTtBFPYRibOXTG3NwMt4ONYhHCpRfia00icagzMP7g/0?wx_fmt=jpeg)

# 思科修复已有 PoC 的根提权漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科已修复 PoC 已公开的一个命令注入漏洞 (CVE-2024-20469)，它可导致攻击者在易受攻击系统上的权限提升至根。**

该漏洞位于思科的身份服务引擎 (ISE) 解决方案中。ISE 是基于身份的网络访问控制和策略执行软件，供用户在企业环境中进行网络设备管理和端点访问控制。

该OS命令注入漏洞是由对用户提供输入的验证不充分导致的。本地攻击者可通过在复杂度低的无需用户交互的攻击中提交恶意构造CLI命令的方式利用该漏洞。然而，正如思科解释的那样，威胁行动者只有在未修复系统上已经拥有管理员权限的前提下才能成功利用该漏洞。

思科在本周三发布的安全公告中提到，“思科ISE的特定CLI命令中存在一个漏洞，可导致认证的本地攻击者在底层操作系统上执行命令注入攻击并将权限提升至根。思科产品安全应急响应团队发现已存在针对公告中所提漏洞的 PoC 利用代码。”

| **Cisco ISE** **发布** | **首次修复的发布** |
| --- | --- |
| 3.1 及更早版本 | 不受影响 |
| 3.2 | 3.2P7（2024年9月） |
| 3.3 | 3.3P4（2024年10月） |
| 3.4 | 不受影响 |

截止到目前，思科并未发现该漏洞在野利用的证据。

思科在今天提醒客户称已删除Smart Licensing Utility （智能许可工具）Windows 软件中的一个后门账户，可被攻击者用于以管理员权限登录未修复系统。

4月份，思科发布 Integrated Management Controller（IMC，集成管理控制器）漏洞CVE-2024-20295的安全补丁。该漏洞的 PoC 已存在，可导致本地攻击者将权限提升至根。另外一个严重漏洞 (CVE-2024-20401) 可导致威胁行动者们添加恶意根用户并通过恶意邮件使安全邮件网关 (SEG) 设备崩溃，已在上个月修复。就在同一周，思科提醒用户注意，易受攻击的Cisco Smart Software Manager On-Prem（Cisco SSM On-Prem，思科本地智能软件管理器）许可服务器中存在一个满分漏洞，可导致攻击者修改任何用户密码，包括管理员密码在内。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[思科修复由NSA报送的两个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=1&sn=74a7817b3955a25dccb8da1009e1b185&chksm=ea94a05cdde3294ad5842ade4355f86f5346f7c319e2260c6999b9fc84577eeff1b3f257c0f3&scene=21#wechat_redirect)

[思科：注意这些已达生命周期IP电话中的RCE 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=2&sn=bad61fd4a7dd0064d773564100fa0d93&chksm=ea94a1fbdde328ed9792a7787f0942bd8375dfb3d8e89c5d0413c4d48ad449acff958b59a1b2&scene=21#wechat_redirect)

[思科严重漏洞可导致黑客在SEG设备上添加 root 用户](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520104&idx=2&sn=7a044b182ec50064eba8b67fb588a968&chksm=ea94be02dde33714a87ec047348cf4004a40a24f05ca079479dd287aec723a3790919198933e&scene=21#wechat_redirect)

[思科 SSM 本地漏洞可用于修改任意用户的密码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520092&idx=1&sn=2c708cd0c74c042942553df613872635&chksm=ea94be36dde33720d8a6f9c9e9a9916bd1d19d05920d0f2d2081b29cbced7d6cf15ffee76430&scene=21#wechat_redirect)

[德国政府会议信息遭泄露，思科修复 Webex 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519685&idx=3&sn=5ff2515ea003efe342365bfb3e9d8af7&chksm=ea94bcafdde335b9fed2634f43fe71bf14953a3fbc06a298ce9ac436a576ce39e6b2dfa25269&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisco-fixes-root-escalation-vulnerability-with-public-exploit-code/

题图：Pixabay License

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