---
title: 钓鱼警报：通过 Evernote 的 AI 驱动“氛围编码”钓鱼攻击
url: https://mp.weixin.qq.com/s/_cQ829g1bGkeaEet4vH-Ow
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:07:49.357703
---

# 钓鱼警报：通过 Evernote 的 AI 驱动“氛围编码”钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J7CSmJcRR8lXICibKwgRgKYVcAtmajd7KFibFiblgYFmCy9cvq3WS1U4r4UGxVtrDdcGzBmYLW0AfJ4Rfks2Tia3VDoYMEZlc5zjENj08vNaark/0?wx_fmt=jpeg)

# 钓鱼警报：通过 Evernote 的 AI 驱动“氛围编码”钓鱼攻击

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

KnowBe4 ThreatLabs 正在跟踪一个活跃的活动，该活动利用 Evernote 的合法基础设施来分发高保真 Microsoft 凭据收集器。此次攻击突显了一个不断变化的格局：威胁行为者现在利用 Base44，一个 AI“氛围编码”平台，来构建复杂的钓鱼页面，而无需编写一行代码。

攻击流程

诱饵：用户收到一封“与您共享的笔记”电子邮件，其中包含高压力的财务诱饵——付款批准、合同或财务报告。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8lREkjBYWmDnB51chdwbq9RzwP3eiclymDrlyvpIMTLG4vwQc6okMYRFuZvfibGGicgYpdvRXgK6FlEhbacwLjIIzhUzwRXNmWEkA/640?wx_fmt=png&from=appmsg)

绕过：这些电子邮件从 no-reply[@]mail[.]evernote[.]com 发送，通过 SPF/DKIM/DMARC 认证畅通无阻。

桥梁：链接指向真实的 share.evernote[.]com 笔记，其中包含“查看文档”行动号召。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8kIPpeIf6TckyVVianETWITOFFqJrPTibicxo5D9Libia1HmxFvWPzaghyBXbxopHZO9l1Sz7NdHEgSmT6WcuW4DjGcHUtFsspvCvico/640?wx_fmt=png&from=appmsg)

AI 转折：该行动号召指向一个使用 Base44 AI（一个 AI“氛围编码”平台）构建的钓鱼页面。这些页面受 Cloudflare 机器人检查保护，以规避沙箱检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8nDE7zhvhtBGva7swTTaibCcqhaOicj1MCetoamEib0vSibWVCq2hEWSKGibiczvbhs34ASwcoAM5uVCWDnNhNicETibUJtovX5xuY45FE/640?wx_fmt=png&from=appmsg)

致命一击：一个像素级完美的 M365 登录屏幕，旨在实时收集凭据。

为什么有效：

✓ 声誉劫持：发件人和初始主机是合法的 Evernote 域名。

✓ AI 速度：Base44 允许攻击者即时创建独特、专业级别的页面。

✓ 沙箱规避：多阶段重定向隐藏最终负载，避开自动化扫描器。

入侵指标 (IOCs)

```
ashrafreda[.]comatomicurl[.]comvoice0356[.]ustechformulagrayfellowshipinvestments[.]tvwpotalsources[.]vueasywaytech[.]co[.]keenthusiastic-secure-link-go[.]base44[.]appfreight-sync-link[.]base44[.]applogin[.]yum[.]homesoffice[.]cotiviti[.]tophticybernetics[.]com[.]sharepoint[.]com/s/finance/Eba1berenzweiglaw[.]com[.]sharepoint[.]com/:f:/s/finance/Eba1serviceamericanreprographicscompany[.]golkppdmansachs[.]vu/
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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