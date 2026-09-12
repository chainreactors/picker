---
title: 【已复现】漏洞通告 | JumpServer Access Key 越权泄露漏洞
url: https://mp.weixin.qq.com/s/Fb8EEGUbipH2Y66hBdKn8A
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:42:09.495825
---

# 【已复现】漏洞通告 | JumpServer Access Key 越权泄露漏洞

# 【已复现】漏洞通告 | JumpServer Access Key 越权泄露漏洞

安全实验室
安全实验室

中成信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6QEqrJF4JnQOGkr3oahUUZeljHItNu0Jlv4XmRBM5vibEPSfsM0o02hF9lNSTnOItNvzqETpOOVbiag/640?wx_fmt=png&from=appmsg)

**1**

**漏洞描述**

JumpServer Access Key 越权泄露漏洞是JumpServer开源堡垒机软件中的高危漏洞（CVSS 3.1评分8.8），允许普通用户通过API请求越权获取所有用户的Access Key明文。该漏洞利用两个查询参数（action=create和\_rel=not）组合触发，导致权限过滤失效，攻击者可接管管理员账户并访问敏感数据。

2

**影响范围**

v3.7.0 <= JumpServer V3 < v3.10.23 LTS

v4.0.0 <= JumpServer V4 < v4.10.19 LTS

3

**漏洞详情**

|  |  |  |  |
| --- | --- | --- | --- |
| 漏洞详情 | | | |
| 漏洞名称 | JumpServer Access Key 越权泄露漏洞 | | |
| 评级 | 高危 | CVSS 3.1分数 | 8.8 |
| 威胁类型 | 权限提升、越权访问 | 利用情况 | 更可能被利用 |
| 公开状态 | POC已公开 | 在野利用 | 已发现 |
| 危害描述：攻击者可利用该漏洞越权读取所有用户的Access Key明文，进而接管管理员账户并访问敏感数据。 | | | |
| 参考链接:  https://github.com/jumpserver/jumpserver/security/advisories/GHSA-6rp5-ff2m-qfrm | | | |

4

**漏洞复现**

中成信息安全实验室已复现JumpServer Access Key 越权泄露漏洞，验证如下。

![](https://mmbiz.qpic.cn/mmbiz_png/IOnTlXyEl27Oibgz8lm5ZO5libjThLJo5U1fVCwRbMyMV1c5ibQ5gB7735ncDYy3ZI03aYc22rCUibyAkfiazo8WsC8V2rkaLIO2rlahIXufDYlw/640?wx_fmt=png&from=appmsg)

5

**修复建议**

官方已发布安全补丁，请及时更新至最新版本：

JumpServer V3 >= v3.10.23 LTS

JumpServer V4 >= v4.10.19 LTS

补丁下载地址：

https://github.com/jumpserver/jumpserver/pull/17295

临时缓解措施：

在 Nginx 或反向代理层拦截包含 \_rel 参数的请求，使用正则表达式匹配明文和 URL 编码形式（如 %5frel），返回 400 状态码。同时，限制 API 访问权限，仅允许可信 IP 或网络段访问，并轮换所有用户的 Access Key。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SUlNQ5ia1qWP6CdmAnkTDWcgGM21xo6kqGqMicl0NPpncTGJZWwzicoO5A/640?wx_fmt=png&from=appmsg)

关于我们

漳州中成信息科技有限公司是一家专注于网络安全实战防护的创新型服务提供商。我们深刻理解网络安全的核心在于攻防对抗的持续较量，并以此独特视角为基石，致力于为客户构建动态、主动、智能化的纵深防御体系。区别于传统的被动防御，我们坚信“未知攻，焉知防”。公司汇聚了顶尖的渗透测试专家（红队）、应急处置精英（蓝队）及经验丰富的安全服务工程师，形成了一支具备完整攻防对抗能力的专业团队。我们的渗透测试团队模拟真实攻击者的思维与手段，深入挖掘系统、应用及网络中的深层次漏洞与风险点；应急处置团队则能在安全事件发生时快速响应、精准定位、有效遏制损失并溯源根因；安服工程师团队则致力于将攻防对抗中获得的宝贵经验转化为常态化的安全策略、加固措施与运营流程。

---

**点击名片**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4Siau2HicdH2XxjSEtMnzvqz4cTYibemFyA3TvGH4ZLYABel0MzmHoL8wJQ/640?wx_fmt=png&from=appmsg)

**关注我们**

**扫描官网二维码**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SWlEyv47fvIgYlBYvBPY4Siau2HicdH2XxjSEtMnzvqz4cTYibemFyA3TvGH4ZLYABel0MzmHoL8wJQ/640?wx_fmt=png&from=appmsg)

**了解更多**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IOnTlXyEl26GI78T6YncCwKHUKyaGaPfNrv9UJ9HO2UzCY5bafOpicHYkAQ0GM2nN2ib7D75utBpNud4pfcYSb2zojicstr6bVn2jOrIw6ick5s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SXmokj8yGgrQAoBPcFlOgWdWUcj8e5rUKUQVVTQ0ibsppahzAstALX6w/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4ShmKJlD9Q30YqOaiamGgmfOA3libRTCd5cNA1qM7z8RUsAr56ibrAocibiag/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/iboUMajImW6SWlEyv47fvIgYlBYvBPY4SsibXafic39wibiaEqD6KgYYCSR6Fn5PgAclH1kkky6SglBKoSOTDo4A8wA/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iboUMajImW6SQoSNk9tODofTCnyfyYcxxotNAKCWTxN1PYUvaZ1cFx99I4iayaiaNzGUl1KmibAgvvVWnCkvAF1w5Q/0?wx_fmt=png)

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