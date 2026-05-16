---
title: 在 Pwn2Own Berlin 2026 大会上，Microsoft Edge、Windows 11 和 LiteLLM 遭到攻击
url: https://mp.weixin.qq.com/s/XBz6ha4me9Q-jlo27Vl2Cg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:59.522960
---

# 在 Pwn2Own Berlin 2026 大会上，Microsoft Edge、Windows 11 和 LiteLLM 遭到攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MjmIk9BhyqpaJZApSqfh22UE3a7SksI1cjh8EZacjnichYGC5LmqVIQUm1QI6m8dBNf7iabysrsxhfq1RYIvEscvxNVUdm16Fu8/0?wx_fmt=jpeg)

# 在 Pwn2Own Berlin 2026 大会上，Microsoft Edge、Windows 11 和 LiteLLM 遭到攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在 Pwn2Own Berlin 2026 开幕当天，世界顶级道德黑客迅速攻破了现代软件和人工智能系统，暴露了 Microsoft Edge、Windows 11、LiteLLM 和 NVIDIA 平台中的关键零日漏洞。

据趋势科技零日漏洞计划 (ZDI) 称， 5 月 14 日，研究人员展示了 24 个独特的零日漏洞利用程序，共获得 52.3 万美元的奖励。此次竞赛凸显了人工智能工具、浏览器和操作系统中日益增长的安全风险。

DEVCORE 在发动了当天最具影响力的攻击之一后，迅速在“Pwn 大师”排行榜上占据领先地位。

## **微软 Edge 沙盒逃逸**

来自 DEVCORE 的安全研究员 Orange Tsai 利用四个逻辑漏洞成功突破了 Microsoft Edge 浏览器的沙盒机制，这是该浏览器的核心安全保护措施之一。

该攻击允许在受限环境之外执行代码，从而可能导致系统完全被攻陷。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7P2XHsiaibrYV6N6Shl5QwITuicvEgEAoBMDG4ibY2kxnYbfdGupLBWNibYicDlAfBAFNQPCd4C2Y9lglrQKhxVskr8ByGL3OiaNY5GyA/640?wx_fmt=png&from=appmsg)

该漏洞利用程序获利 17.5 万美元，成为首日最高收益。沙盒逃逸尤其危险，因为它们绕过了浏览器旨在阻止恶意网络内容的隔离机制。

## **Windows 11 权限提升**

微软Windows 11也成为了攻击目标。多名研究人员成功提升了权限，获得了更高的系统访问权限：

* DEVCORE利用不当的访问控制漏洞提升了权限。
* Marcin Wiązowski 利用了基于堆的缓冲区溢出漏洞。
* Kentaro Kawane 利用两次释放后使用漏洞，成功发动了第三次攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NzKAQ3piasdECnnTb8SkKd7IUTYBIo1CRcEDNLPAIziaS6l0GdmMezibK8T7qHcaIFwHmmVmwLQzBWGQhKxO3RU9Grh6K8UtLstM/640?wx_fmt=png&from=appmsg)

这些漏洞可能使攻击者能够从有限的用户访问权限扩展到完全的管理控制，这是现实世界攻击中常见的目标。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7O5yYZ8h3VXagrGIGia2tuPvM9sKK46B7jiaVR3zmZGPSu9JO1jicGyqj6iaxOgYsqYgXnAYrhbEV8nOJyXibuxibRlrfJmw8rnahR00/640?wx_fmt=png&from=appmsg)

## **LiteLLM 和 AI 系统遭受攻击**

在这次事件中，人工智能基础设施成为了主要的攻击面。

研究人员 k3vg3n 利用包括服务器端请求伪造 (SSRF)和代码注入在内的三个漏洞，成功攻破了用于管理大型语言模型 API 的工具 LiteLLM。此次攻击展示了人工智能平台如何被滥用以执行未经授权的命令或访问内部系统。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OicaCoudaXcEWN2Gib57Ppv0jd0lIWceQ5uAMO7Kkznrb3EFj7MBKztiagUJibGtwvCNPylibEChLqibyKoy6KibLfaB01pBSuxoybt0/640?wx_fmt=png&from=appmsg)

来自 STARLabs SG 的另一个团队通过串联五个漏洞利用了 LM Studio，这表明复杂的 AI 工作流程可能会引入多个弱点。

甚至连 OpenAI Codex 也被 Compass Security 通过 CWE-150 漏洞成功利用，这凸显了 AI 编码助手带来的风险。

## **NVIDIA 和 Linux 漏洞利用**

NVIDIA产品也遭遇了多次成功的攻击：

* NV Container Toolkit 利用单个漏洞遭到入侵。
* NVIDIA Megatron Bridge 因访问控制过于宽松和路径遍历漏洞而被利用。

此外，IBM X-Force 还演示了利用竞争条件漏洞提升 Red Hat Enterprise Linux 系统权限。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MFgkYJPdbibNIZu9z0peiaftGBaa0pEJFX3j4axTy9clpwJYIAR6DzQQW0mr5QrYp7suf7Cia5DIua8uibTAGyJfMxYebKQsjUVSo/640?wx_fmt=png&from=appmsg)

并非所有尝试都成功了。针对 OpenAI Codex和 Oracle Autonomous AI Database 的攻击在执行过程中失败。部分攻击被标记为“冲突”，表明这些漏洞已被供应商知晓，从而降低了其影响。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7O35RbMibgtRyhXU3V567tfVljM3RT8kt81cZgDic1ia3B4SUSJWpnbNBJSzTAMInyNdn93sMdo10bBIMTkCtbBD2eppwTD7uDpQw/640?wx_fmt=png&from=appmsg)

今年的 Pwn2Own 大赛明显转向以人工智能为重点的目标。人工智能数据库、编码代理和本地推理系统等类别吸引了研究人员的广泛关注。

结果表明，虽然人工智能工具发展迅速，但其安全成熟度仍有待提高。

随着竞争的继续，预计会有更多漏洞浮出水面，从而为了解攻击者如何在现实场景中针对下一代技术提供关键见解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7PShGVV2ePswsewHW2njxt6AUq55LxMx85CDHREYwpj8cVEUNAhLcHQfLeMzq7MDpHoFLuCSdejxjiarwLMJ1G52shtzNvYt8Ag/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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