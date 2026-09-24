---
title: Check Point 紧急修复已遭利用的 Management Server 0day
url: https://mp.weixin.qq.com/s/GUrhp3P5_EAbjyRMXbtcPA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:06:10.336044
---

# Check Point 紧急修复已遭利用的 Management Server 0day

# Check Point 紧急修复已遭利用的 Management Server 0day

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**Check Point****软件公司发布紧急热修复程序，修复了一个严重的安全管理服务器漏洞****(CVE-2026-93616)****，可导致攻击者运行任意脚本。**

安全管理服务器是一个中央存储库，用于存储和管理安全策略、处理管理员更改，并收集企业网络中的系统日志。该路径遍历漏洞可导致未经身份验证的威胁行动者在易受攻击的 Check Point 管理服务器上上传任意脚本，并在低复杂度攻击中执行这些脚本。

自 2024 年 5 月以来，美国网络安全和基础设施安全局 (CISA) 和联邦调查局 (FBI) 就一直敦促软件公司在发布产品前消除路径遍历弱点，称此类安全问题“至少自 2007 年以来就被称为‘不可原谅’”。

Check Point 公司已在 R82.20 安全热修复方案中修复该漏洞，并表示受影响产品的完整列表包括安全管理服务器、多域安全管理服务器、日志服务器、多域日志服务器和 SmartEvent。

该公司在安全公告中提到，“该漏洞正遭在野利用，Check Point 已知有少数客户遭到攻击。”该公司同时建议安全团队使用安全公告中共享的入侵指标检查网络，寻找成功利用的证据。

Check Point 还为无法立即在易受攻击系统上部署热修复程序的客户提供临时缓解措施，包括将易受攻击系统置于防火墙之后，并在 SmartConsole 仪表板的“管理 & 设置 > 权限 & 管理员 > 受信任客户端”中限制只有受信任 IP 地址可以访问，从而加固这些系统以抵御攻击。

近几个月，Check Point 还提醒客户注意正遭在野活跃利用的漏洞。两年前，CISA 将 Check Point Quantum 安全网关中的一个漏洞 (CVE-2024-24919) 标记为已被勒索软件团伙积极利用，并证实了 Orange Cyberdefense CERT将这些攻击与 NailaoLocker 勒索软件关联起来的一份报告。

Qilin 勒索软件附属组织自 6 月以来还利用了身份验证绕过漏洞 (CVE-2026-50751) 0day漏洞，而第二个身份验证绕过 0day 漏洞 (CVE-2026-16232)至少自 7 月以来一直被利用，以管理员权限对 SmartConsole 管理面板进行身份验证。

两周前，荷兰国家网络安全中心 (NCSC-NL) 也提醒各组织机构紧急修复两个严重的 Check Point VPN 漏洞（CVE-2026-85102 和 CVE-2026-85103），因为该中心“预计利用尝试很快就会发生”。

上周五，Check Point 公司发布安全更新，修复安全管理服务器和安全网关登录过程中的另一个严重身份验证绕过漏洞 (CVE-2026-16232)，它可导致攻击者在管理系统上以 root 权限执行代码。

虽然该公司尚未将 CVE-2026-16232 标记为正在遭活跃利用，但认为安全团队可以通过在审计和管理员登录日志中查找“Administrator failed to log in: Username too long（管理员登录失败：用户名太长）”警报来识别攻击。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[Check Point 紧急修复严重漏洞，可使远程未认证攻击者获得 root 权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247527165&idx=1&sn=065c0d69dff53c546fce09eee69ae140&scene=21#wechat_redirect)

[Check Point 提醒注意两个严重的未认证 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247527106&idx=1&sn=bbf5299ba4eef963c2c55d28c8620961&scene=21#wechat_redirect)

[攻击者利用 Check Point VPN 访问企业网络](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519614&idx=2&sn=61729da3c7c16514ae5bdae557f4e001&scene=21#wechat_redirect)

[思科：ISE 认证绕过满分 0day 已遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247527173&idx=1&sn=1ae52540af18bbb2b176b85380e718cc&scene=21#wechat_redirect)

[GeoServer 0day 已遭利用，可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526875&idx=1&sn=a17a7b733568d42551bc0237a295999e&scene=21#wechat_redirect)

**原文链接**

**https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/**

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞”

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