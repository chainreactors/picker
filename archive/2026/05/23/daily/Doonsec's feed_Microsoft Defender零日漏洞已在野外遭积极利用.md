---
title: Microsoft Defender零日漏洞已在野外遭积极利用
url: https://mp.weixin.qq.com/s/mzawD-_crDMa0Awmk-i8eQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:26.668021
---

# Microsoft Defender零日漏洞已在野外遭积极利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJntZ7GuFfhNSbO4X3eGBkzicuuJmcMEPMTqJ36ZHg5gRiaKRbPljnjNQQ3rGxdKAzEk6MHviaYPcqZOYU1libraMmjrL53dz5xsk6XY/0?wx_fmt=jpeg)

# Microsoft Defender零日漏洞已在野外遭积极利用

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnspPJHc2HoiawcVf7dUcdMpNjiaLVicTmEKiaSPD5oayb5cnGibuYOk2ja0SwSG6pWUvRZzq1picl1Qtx7ScLh6Kicsc3VUM7dJ1EI6Mc/640?wx_fmt=png&from=appmsg)

Microsoft已披露Microsoft Defender中两个正在野外被积极利用的新型零日漏洞，引发安全从业者及企业用户的广泛担忧。

这两个漏洞的编号分别为CVE-2026-41091和CVE-2026-45498，微软安全公告确认其于2026年5月19日正式公开，且均存在实际攻击活动。

其中更关键的CVE-2026-41091是一个权限提升漏洞，CVSS评分为7.8。该问题源于文件访问前的链接解析不当，归类于CWE-59（符号链接跟随）。

此漏洞允许低权限攻击者在无需用户交互的情况下提升目标系统的访问权限。

据微软说明，该漏洞可通过本地方式以低攻击复杂度被利用，对于攻击者已获得初始访问权限的环境尤为危险。

一旦被利用，攻击者将获取高级权限，从而危及受影响系统的机密性、完整性和可用性。

微软已确认该漏洞遭公开披露且正在被积极利用。

漏洞可利用性评估显示"已检测到利用行为"，凸显组织需立即应用补丁的紧迫性。尽管当前漏洞利用代码成熟度标记为"未经验证"，但实际攻击已被观测到。

第二个漏洞CVE-2026-45498是严重性评级为4.0的拒绝服务（DoS）问题。

Microsoft Defender Zero-Day Vulnerabilities
尽管影响较低，该漏洞同样正在野外被积极利用。攻击者无需特权或用户交互即可破坏系统可用性。

此DoS漏洞可通过本地低复杂度方式触发，可能导致运行Microsoft Defender的系统无响应或运行不稳定。

虽然不影响机密性与完整性，但安全服务的中断可能为后续攻击创造机会，或阻碍事件响应工作。

两个漏洞均具备加剧风险的关键特征：无需用户交互、攻击复杂度低，且已确认存在活跃攻击。

这些特性使其成为威胁行为者实施漏洞链利用或在受 compromise 环境中维持持久性的理想目标。

安全研究人员警告，权限提升漏洞可能在事后利用场景中被滥用。

例如，攻击者通过钓鱼攻击或其他漏洞获得初始访问权限后，可利用CVE-2026-41091提升权限并完全控制系统。

此类攻击链在高级持续性威胁（APT）行动和勒索软件攻击中极为常见。

微软已为两个漏洞发布官方修复程序，强烈建议用户立即应用最新安全更新。

组织还应审查系统日志，监控可能表明利用尝试的可疑活动。

除打补丁外，安全团队应实施纵深防御策略，包括端点检测与响应（EDR）、最小权限访问控制及持续监控。

这些措施有助于减轻漏洞利用影响，并提升应对新兴威胁的整体韧性。

此次漏洞披露凸显了广泛部署的安全工具自身成为攻击面的持续风险。

随着威胁行为者技术不断演进，及时修补与主动威胁狩猎仍是现代网络安全防御的关键环节。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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