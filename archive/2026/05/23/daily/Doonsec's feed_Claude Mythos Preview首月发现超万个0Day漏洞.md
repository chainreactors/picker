---
title: Claude Mythos Preview首月发现超万个0Day漏洞
url: https://mp.weixin.qq.com/s/2vlzln_L0sEBs-sH66rzSw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:42.328092
---

# Claude Mythos Preview首月发现超万个0Day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1nQwdPU8B4C0JgbMFKP6s5ZiaPyR88H8YwudMe64ic7JWOJuiaiaUP4SY6qtpwf1J0CKm7fibHMksP75cyYR3icUlDaL6xiaBsnU1KxM/0?wx_fmt=jpeg)

# Claude Mythos Preview首月发现超万个0Day漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2ssm2YXQB7ZxEBG5LxfsFurlDqISktMfVCSx9Rsqp042PCGiapiaOyXVzJ8l8iaOlXmTgjJzzCngoeknQNbMF7bFxXibL5JomQcgM/640?wx_fmt=jpeg&from=appmsg)

Anthropic公布了Project Glasswing项目的惊人初期成果，这项协作式网络安全计划旨在利用先进AI技术，在恶意攻击者利用之前保护关键基础设施安全。在项目启动的首月，团队借助尚未发布的Claude Mythos Preview模型，在全球最关键软件系统中自主发现了超过1万个高危和严重级别的0Day漏洞。

**Part01**

## 突破性漏洞发现能力

Anthropic与微软、苹果、谷歌和Cloudflare等50余家大型科技企业合作，将Claude Mythos Preview部署到高度定向的代码库中。该模型不仅展现出识别漏洞的非凡能力，还能自主构建功能性漏洞利用程序。Cloudflare报告发现了2000个漏洞，其中400个属于高危或严重级别，并指出该模型的误报率优于人类安全测试人员。

独立评估在多环境中验证了这些能力。英国AI全研究所观察到，Mythos Preview是首个完全解决其多步骤网络攻击模拟的模型；而Mozilla利用该模型在Firefox 150中发现并修复了271个漏洞，发现数量是此前使用 Claude Opus 4.6测试的十倍。

**Part02**

## 开源项目关键漏洞曝光

鉴于这些自主漏洞利用能力存在严重的双重用途风险，Anthropic暂未向公众发布Mythos，仅限防御联盟成员使用。除专有企业系统外，Anthropic还指导Claude Mythos Preview扫描了1000多个广泛使用的开源项目，其中最引人注目的是wolfSSL加密库中的高危漏洞（CVE-2026-5194）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3liaKwsdA7bg76Pef6TO0oxL3pvJ523awmzukLiaNErcCPznicrzH1iaxqlwUzEQTszLjX0ms0xPibCGCBkLqGKClVT5XQcvqeib2Hk/640?wx_fmt=jpeg&from=appmsg)

Mythos Preview成功构建了针对该漏洞的利用程序，可实现安全证书伪造，这种攻击向量能让攻击者悄无声息地仿冒银行或电子邮件域名。

**Part03**

## 漏洞修复能力面临挑战

庞大的漏洞发现量暴露出软件行业的关键结构性缺陷：人类在漏洞分类、报告和修复方面的能力无法跟上AI驱动的发现速度。初始扫描阶段产生了23019个候选发现，当外部安全公司审查其中1900个发现时，确认1726个（90.8%）为真实有效漏洞。

尽管Anthropic直接向维护者报告了总计1596个经过验证的发现，但迄今为止上游仅修复了97个漏洞，仅发布了88份安全公告。这种巨大的落差凸显了志愿开源维护者面临的严重能力限制，他们现在被高质量的AI漏洞披露压得喘不过气。

**Part04**

## 行业防御策略转型

## Mythos级模型将0Day发现的成本和时间几乎降为零，从发现到广泛部署补丁之间的时间差为威胁行为者提供了极其危险的漏洞利用窗口。 业界建议组织不应仅依赖补丁，而应通过强制执行严格的默认配置、强制多因素认证以及利用高级行为分析来调整网络防御策略，从而缩短入侵后活动的平均检测时间（MTTD）。 为在Mythos受限期间支持更广泛的生态系统，Anthropic面向企业客户公开发布了Claude Security测试版。该工具采用Opus 4.7模型，已协助修复了2100多个企业漏洞。此外，Anthropic还为其网络安全验证计划合作伙伴提供专用skills、代码库映射工具和自动化威胁模型构建器，以简化分类流程。 根据初步结果报告，Anthropic正考虑未来发布Mythos级模型。思科等联盟合作伙伴已开源Foundry Security Spec等资源，帮助全球防御者构建强大的AI辅助评估系统，以应对即将到来的漏洞数据浪潮。

|
|  |

**参考来源：**

Anthropic’s Claude Mythos Preview Uncovers 10,000+ 0-Days in Project Glasswing

https://cybersecuritynews.com/anthropics-claude-mythos-preview-0-days/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

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