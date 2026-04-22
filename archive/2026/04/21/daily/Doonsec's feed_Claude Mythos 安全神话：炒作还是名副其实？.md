---
title: Claude Mythos 安全神话：炒作还是名副其实？
url: https://mp.weixin.qq.com/s/DX62GD6CtOw_oqcc3p_A_Q
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:57.211338
---

# Claude Mythos 安全神话：炒作还是名副其实？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3AvaqQ592MnTLuQrzsyVT6hicyBzjCm3Lw5eQmssn71dd1bQiayzuKIo8FRRvTXlCqBtSk7Pdy6tN5vtc5hAbgibOodUmaAobfpg/0?wx_fmt=jpeg)

# Claude Mythos 安全神话：炒作还是名副其实？

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1YeSia3kN5NI9O5YkUNULyYpIoBua2or4nb14vAjMPGXpEqiaJahrAJwzWzqEXxFabrF8YpJ5RMsRFibbUSDVxF6GnVlq3VibebgA/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****炒作遇冷：****

## ****VulnCheck分析质疑实际成效****

当OpenAI正计划推出专注于网络安全的AI模型展开竞争时，VulnCheck安全专家最新研究对Claude Mythos（即"Project Glasswing"）的实际影响提出了质疑。目前该模型仅由美国大型科技公司等精选机构参与测试。

VulnCheck研究员Patrick Garrity在博客中指出："Anthropic的Project Glasswing引发了广泛关注，但提供的具体数据却非常有限。"虽然Anthropic的研究活动确实有助于发现漏洞且整体前景看好，但该项目目前可验证的实际影响仍较为有限。

> Glasswing备受关注，我们通过分析验证其当前成效：https://t.co/UKmHYT3vaJ
>
> 75个CVE提及Anthropic
>
> 40个归功于其研究人员
>
> 1个明确关联Glasswing（截至目前）
>
> 预计今年将有更多进展，我们将持续追踪。
>
> — VulnCheck (@VulnCheckAI) 2026年4月15日

**Part02**

## ****CVE数据深度剖析****

VulnCheck团队对"Project Glasswing"相关的CVE记录进行了全面审查。Garrity表示："无论是Glasswing报告还是Anthropic发布的安全公告，都未提供完整的漏洞发现清单。因此我决定检索整个CVE数据库，筛选包含'anthropic'关键词的记录并逐一验证。"

研究共识别出75条相关CVE记录，其中仅40条明确归功于Anthropic研究人员。进一步分析显示，只有1个CVE（涉及FreeBSD远程代码执行漏洞）被明确标记为"Project Glasswing"自主发现并利用的成果。另有三个处于保密期的漏洞未被计入分析：

* OpenBSD中存在27年的安全漏洞
* FFmpeg长达16年的缺陷
* Linux内核权限提升攻击链

Garrity指出："只有待Anthropic全面公开Project Glasswing发现和修复的漏洞详情后，才能客观评估Claude Mythos的实际能力。"他预计相关报告将于2026年7月发布。

**Part03**

## ****专家观点交锋****

VulnCheck的发现为评估Claude Mythos能力提供了新视角——可归因CVE数量仅是衡量其影响的指标之一。

安全厂商Tanium高级总监、SANS技术研究所理事Melissa Bischoping持有不同观点："我们分析了Claude Mythos预览版的系统卡，该模型在漏洞利用方面取得了前所未有的成功率。对同类攻击目标，成功率从近乎零跃升至约72%，表明其已突破开发复杂漏洞利用的技术瓶颈。"

尽管Claude Mythos目前仅在Project Glasswing限定范围内测试，Bischoping认为它已展现未来潜力："前沿模型与开源模型的差距已从一年多缩短至数周。这种能力水平将快速扩散，而安全防护措施很可能无法同步跟进。"她特别担忧企业在模型公开前能否及时响应其发现的威胁："虽然自动化补丁工作流可对抗AI威胁，但企业策略和变更控制目前仍无法匹配AI的速度。"

**参考来源：**

Claude Mythos – ist der Hype gerechtfertigt?

https://www.csoonline.com/article/4160754/claude-mythos-ist-der-hype-gerechtfertigt.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

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