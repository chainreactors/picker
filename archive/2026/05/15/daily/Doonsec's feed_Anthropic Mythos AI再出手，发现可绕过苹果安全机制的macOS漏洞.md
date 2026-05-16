---
title: Anthropic Mythos AI再出手，发现可绕过苹果安全机制的macOS漏洞
url: https://mp.weixin.qq.com/s/8_gNFJoziWjWjkhD_KGESQ
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:21.568484
---

# Anthropic Mythos AI再出手，发现可绕过苹果安全机制的macOS漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3UdT1icibquj8Bzba728JD6N3F3BicCsJSoGHxp6mHKqrloZ6hQzH6eIFgdyuFn0f3xC5SbzZVhY3MjxNTVYssGGOSveNrBrX4f0/0?wx_fmt=jpeg)

# Anthropic Mythos AI再出手，发现可绕过苹果安全机制的macOS漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3iaKiamoeEo1z0dI7icBpa6tMicsuXM5Mic3XCdeicyDAolvox53IF59kUIaU7SDZnZAOGmZ9rCaPo1KODJxUicTZibX6CsibNNqT5iaMDc/640?wx_fmt=png&from=appmsg)

位于帕洛阿尔托的网络安全公司Calif的研究人员，运用了源自Anthropic秘密研发的Mythos AI早期版本的技术，发现了macOS系统中两个此前未记录的漏洞。这两个漏洞被串联成一条权限提升攻击链，能够绕过苹果最先进的内存完整性保护机制，访问本应完全禁用的系统内存区域。

苹果公司正在审核Calif提交的55页技术报告，预计验证后将发布补丁。

**Part01**

## ****漏洞攻击链技术细节****

该漏洞组合于四月份的测试中发现，通过结合两个macOS漏洞与多项高级技术，破坏Mac内存，最终突破普通进程无法触及的受限制系统区域。据《华尔街日报》报道，若将此权限提升漏洞与其他攻击手段相结合，攻击者可完全控制目标Mac设备。

Calif研究人员编写了定制化软件，将两个漏洞串联，形成了macOS系统前所未见的新型攻击向量。值得注意的是，这并非可远程传播的蠕虫病毒。攻击仍需在Mythos生成内容的基础上，叠加大量人工专业知识。Calif首席执行官Thai Dong坦言：“仅靠Mythos无法完成攻击，还需借助Calif安全专家的人工研判能力。”

**Part02**

## ****Mythos AI的特殊定位****

因其识别软件漏洞的卓越能力可能带来潜在风险，Anthropic的Mythos（前称Claude Mythos Preview）被刻意限制公开。该模型是Anthropic“玻璃之翼”项目的组成部分，目前仅向苹果、谷歌、微软等约40家选定机构开放，用于防御性安全研究。Anthropic已承诺投入1亿美元使用额度，以支持该合作计划。

在发现macOS漏洞之前，Mythos曾成功找出OpenBSD中潜伏27年的漏洞，并识别出可劫持Linux设备的漏洞。Anthropic工程师明确警告，该模型挖掘安全缺陷的能力过于强大，必须设置严格防护措施才能使用。

**Part03**

## ****漏洞披露流程****

Calif研究人员对此次发现极具信心，专程前往苹果库比蒂诺总部当面提交技术报告。苹果发言人向《华尔街日报》表示：“安全是我们的首要任务，我们非常重视潜在漏洞报告。”虽然苹果尚未确认是否已开始修复漏洞，但Calif首席执行官预计“漏洞可能会很快得到修复”。在苹果解决根本问题之前，Calif不会公开完整技术细节。

**参考来源：**

Anthropic’s Mythos AI Reportedly Found macOS Vulnerabilities that Could Bypass Apple Security

https://cybersecuritynews.com/anthropics-mythos-macos-vulnerabilities/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOichlYJst28QicxZVpXP1ibeVdB4iawibWIFgqV6Ry4LzdhyQbspxEr3NAqQviatF6AoAYMl0qboYWSzKwjM7zPSKtD3ncv5joxpM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337950&idx=1&sn=12d64571335d50c1b93389447dfb8ef1&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibzbO8hNu1jchaRibLfz5ZHmRibzmT7nmjUqZSAswml2TEozpdNFMZw8N1ShpFef0a2bibN2crXGM5BZhMQjgAbAOY0DN1yjl1Cc/640?wx_fmt=png&from=appmsg)

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