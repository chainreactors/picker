---
title: “我没黑进去，智能体自己干的” - Meta安全工程师Aditya Om @2026白帽世界大会
url: https://mp.weixin.qq.com/s/S1Qnyn1x5RWStkdDMHWhMw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:30:11.817518
---

# “我没黑进去，智能体自己干的” - Meta安全工程师Aditya Om @2026白帽世界大会

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1Bic5ozpR7u0DmJ2eOxdXN5ERbrdicQGibplOjdxsS6PkSKAu90UheEBPOibB6zPkqRK1MdyC2jAPnlENAV8evKKICLXTHJoyvMgU/0?wx_fmt=jpeg)

# “我没黑进去，智能体自己干的” - Meta安全工程师Aditya Om @2026白帽世界大会

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![图片](https://mmecoa.qpic.cn/mmecoa_png/4tc6mDlGcQS11Xz3CrfqeMG8dH3O6WNClx9kDxMrF7Tz2u80Z5lqvjCw77GLzYbwk6JZZw8APXyzdnPm6eCQsM1Eh5vNrqZJcttIOStC0p8/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=0)

**Topic   Preview**

**议题关键词**

随着企业从单一AI模型向多智能体系统演进，

数据开始在多个智能体之间逐级流转，

并频繁跨越不同的信任边界。

然而，当前的安全防护仍主要依赖

传统的输入验证与隔离机制，

忽视了智能体间通信所形成的隐式信任通道，

由此引发了**新型的横向移动风险**。

**🎤 重磅分享**

Meta 工程师 Aditya Om

亲临 HPW2026

拆解**多智能体隔离绕过、**

**上下文污染、Agent 通信攻防**

从理论到实战，

一次性讲透 AI 安全新变局。

![图片](https://mmbiz.qpic.cn/mmbiz_png/oaWBaYhbvR1YSBRY25K7Ef5cC3RGFTB0nibyExlqS7e8GylHIGPriaQziaMgYsXMazJZSY88Iib53t5flV4cHFemGw/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=1)

![图片](https://mmecoa.qpic.cn/mmecoa_gif/Lz7kwtXbxCGWBEGFgs7DMLQ9RjVLAcT6mUFvRYKWmIWVuvRBs55iamvjP9pMXAlVZ96JlCUiaqIFObzFagFQhPjA/640?wx_fmt=gif&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=2)

**Topic Summary/ 议题梗概**

本次演讲将针对智能体通信形成隐式信任通道带来的新型横向移动风险，**提出****策略合规性伤害攻击**：攻击者从外部注入恶意意图，经多智能体传导，由高权限隔离节点执行。攻击全程表面合规、日志正常，风险隐匿于工作流组合中。我们将展示级联攻击路径：污染数据被接入并规范化为 “合规上下文”，由可信智能体凭自身权限执行，无需漏洞与恶意代码，仅利用系统结构即可得手。**演讲将提示注入重新定义为智能体横向移动，指出传统零信任在非人类身份场景的局限，并提出可验证通信、上下文溯源、执行隔离等防护思路。**

In this talk, I talk about a new class of attacks: Policy-Compliant Harm—where malicious intent is introduced outside the perimeter, propagated across agents, and executed by a high-privilege, air-gapped node.

Every step is expected and every log is clean. The harm only exists in the composition of the workflow.I frame this as a **cascading swarm compromise.**

![图片](https://mmecoa.qpic.cn/mmecoa_gif/Lz7kwtXbxCGWBEGFgs7DMLQ9RjVLAcT6mUFvRYKWmIWVuvRBs55iamvjP9pMXAlVZ96JlCUiaqIFObzFagFQhPjA/640?wx_fmt=gif&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=3)

**Speaker Profile/ 议题嘉宾**

**Aditya Om**

Meta 软件工程师，长期专注于 AI 基础设施与系统架构设计，深度参与**MTIA（Meta Training and Inference Accelerator）**软件架构的设计与优化工作，致力于推动 Superintelligence（超级智能）时代的算力演进与推理效率提升。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/4tc6mDlGcQSwNQjvu3ZA4LtibM8hxa1X8h8zlVM520fXdYt3PEq3HHBsWaqoSC8MbyabaZmS1jewxk0iafXZuNoVrpTknTayrJLtZjycklWak/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=4)

HACKPROVE WORLD

2026/05/16

![图片](https://mmbiz.qpic.cn/mmbiz_png/IH4hGrDAYVN9WlBYAaDzeF2Hcf3XQwBrEwyXibTI9IuoxcEQrJZ095wHwqgriaSJibNcJpiaXic9Y3OYwzZSMhBIgcw/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/oaWBaYhbvR1YSBRY25K7Ef5cC3RGFTB0nibyExlqS7e8GylHIGPriaQziaMgYsXMazJZSY88Iib53t5flV4cHFemGw/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=6)

**大会报名**

**时间：**2026年5月16日
**地点：**澳门美高梅 2楼百宝箱厅

**官网链接：**https://www.hackprove.com/hpw2026

![图片](https://mmecoa.qpic.cn/mmecoa_png/4tc6mDlGcQRAbvzGpbcUdNQemLicVk5HWthTIzvpH7mauZO3FJT4lYDickLaD9xX5ykwNTr2OVI6icwdb1wnxvPCicrdciaSsuFI74UZfoJE8gIg/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=7)

扫描上方二维码

即刻报名

我们澳门见！

![图片](https://mmecoa.qpic.cn/mmecoa_png/4tc6mDlGcQQq70SV69ibxpshv78DPl9icKb13TLHPehUCMIOkjyiblfYibFqQty1ialcH0Ja9WsPVveoyAwiajlibsNmxM5O3LwiarndKbzYXnUTEics/640?wx_fmt=png&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=8)

— END —

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

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