---
title: 首日狂揽 52.3 万刀！Pwn2Own 柏林拿下 Edge/Win11/LiteLLM
url: https://mp.weixin.qq.com/s/biQV_1QEgFtHaAshFUr72w
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:11.199046
---

# 首日狂揽 52.3 万刀！Pwn2Own 柏林拿下 Edge/Win11/LiteLLM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3b2h2jziabAicnC4p9e6eYRKTZDibXSZYMyzllnmkiaNAhlSKjrLMibbRqCQjPWtq6Qbsiaia1oSTQs4ibiaamtcHwZVakYhJF8I965glo/0?wx_fmt=jpeg)

# 首日狂揽 52.3 万刀！Pwn2Own 柏林拿下 Edge/Win11/LiteLLM

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2qmPNoaojuV7Ff45Sr79ySHVCZ5KX8ojBJQGqeU3A7ugwV1QDaCiciaSPMsoQiaw0icweoyDvR8TAK92JYTRE0pvRQZW4ia2iaHwluQ/640?wx_fmt=jpeg)

Pwn2Own柏林2026赛事首日即掀起针对现代浏览器、操作系统和新兴AI平台的0Day漏洞利用浪潮。安全研究人员在首日就成功攻破微软Edge、Windows 11和LiteLLM，通过24个独特漏洞总计斩获52.3万美元奖金。这一结果凸显出AI生态系统与企业核心技术正面临日益复杂的链式攻击威胁。

**Part01**

## ****Edge沙箱逃逸技术****

DEVCORE研究团队成员Orange Tsai展示了最具影响力的攻击演示——针对微软Edge的精密沙箱逃逸技术。该漏洞利用串联了四个独立逻辑漏洞，将细微缺陷转化为完整的系统入侵。

![微软Edge遭攻破（来源：Zero Day Initiative）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3ITrO9G40n5IakneSJFZ6cgrmuLaSUFvfO0iaXicjBa6ibwPgicwibtxicibzXRYicVkyVBx0w4oACOSDibC6mBIkia3RgicaTW7En6JDbibY/640?wx_fmt=jpeg&from=appmsg)

这项高级技术为DEVCORE赢得7.5万美元奖金和17.5个"破解大师"积分，使其暂居赛事榜首。该攻击表明，当多个安全弱点被策略性组合时，现代浏览器防护仍可被突破。

**Part02**

## ****Windows 11权限提升漏洞****

微软Windows 11成为另一主要攻击目标，当日出现多起成功的权限提升攻击案例。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3QsKm55oOXkwqAz8W49FyicUiahg5iaykMyJKQvrElqdReicyNQUogpRp4HguY91UjpaT7smicbdGcLWG3qkLZTPnBoGWpQqOhRoIM/640?wx_fmt=jpeg&from=appmsg)

后续研究人员演示了基于堆的缓冲区溢出和释放后重用漏洞攻击。DEVCORE团队成员Angelboy与TwinkleStar03则利用访问控制缺陷获取系统高级权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1ElFZA905YhNIh9dIy0MAEEgUCaA3pGYicabiaVpjKP238kICqg1OGoiaDQ9q9bNNIJpNTlE7upTzTqZHuNX5KCuu9lDRyxoVf18/640?wx_fmt=jpeg&from=appmsg)

这些连环入侵事件表明，即使成熟操作系统仍难以规避内存破坏和访问控制问题。

**Part03**

## ****LiteLLM框架沦陷****

##

AI基础设施面临严峻考验，研究员k3vg3n通过全链漏洞利用攻破LiteLLM。该攻击结合服务端请求伪造（SSRF）和代码注入等三个漏洞，最终实现系统完全控制。

![LiteLLM遭攻破（来源：Zero Day Initiative）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2ZMjVvQbibWZ7gcENSgicSwaBiabmMfbcuQZJdSATehoiclT1icnMpHlXoWFaMfic2X1MWdh3KQZDVgpbng9Ric7fu5MltjKt6Fjn9W8/640?wx_fmt=jpeg&from=appmsg)

该漏洞利用获得4万美元奖金，暴露出AI框架（特别是处理外部输入和API的框架）若未充分加固将产生重大安全缺口。

**Part03**

## ****AI与开发工具安全危机****

##

其他AI相关目标同样遭遇攻击：Compass Security团队利用CWE-150漏洞攻破OpenAI Codex；NVIDIA Megatron Bridge因过度宽松的许可列表和路径遍历漏洞被多次入侵。

![NVIDIA遭攻破（来源：Zero Day Initiative）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3XlEpoUSXzSTm2KT0ZzLWOJ3iblYGujoC0bXCictbaXRwDhgO0qeckgyxBDwwXQuqW6tGWvFibHOD3MTsY8clibweVjlxXhVBnflU/640?wx_fmt=jpeg&from=appmsg)

IBM X-Force研究人员则通过NV Container Toolkit的单一漏洞实现入侵。这些案例印证了AI与开发工具生态系统在安全设计和威胁抵御方面仍不成熟。

并非所有攻击尝试都取得成功，部分研究人员未能在时限内攻破OpenAI Codex和Oracle Autonomous AI Database等目标。赛事还记录多起"碰撞"案例——攻击者利用的竟是已知未修复漏洞。

![Linux遭攻破（来源：Zero Day Initiative）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX39KfbtYyewotCfU4efj1wUz7YJPhRzicomoEl53boR3U1IV38Pp8oFgnrubiaJTHS1dQNQom8KBndY0g6kicPCEOicgOF38L2NbdM/640?wx_fmt=jpeg&from=appmsg)

Zero Day Initiative指出，Pwn2Own柏林2026首日战果揭示了威胁格局的重大转变：攻击者不再局限于传统软件，开始积极瞄准AI平台、推理引擎和开发工具。随着DEVCORE领跑赛事，更多高价值目标等待攻破，预计未来几天将暴露更深刻的安全漏洞，为厂商和企业敲响警钟。

**参考来源：**

Microsoft Edge, Windows 11 and LiteLLM Hacked in Pwn2Own Berlin 2026

https://cybersecuritynews.com/pwn2own-berlin-2026/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOichlYJst28QicxZVpXP1ibeVdB4iawibWIFgqV6Ry4LzdhyQbspxEr3NAqQviatF6AoAYMl0qboYWSzKwjM7zPSKtD3ncv5joxpM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337950&idx=1&sn=12d64571335d50c1b93389447dfb8ef1&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibzbO8hNu1jchaRibLfz5ZHmRibzmT7nmjUqZSAswml2TEozpdNFMZw8N1ShpFef0a2bibN2crXGM5BZhMQjgAbAOY0DN1yjl1Cc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

内容含AI生成图片

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