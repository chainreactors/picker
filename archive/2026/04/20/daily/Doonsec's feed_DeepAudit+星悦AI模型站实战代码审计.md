---
title: DeepAudit+星悦AI模型站实战代码审计
url: https://mp.weixin.qq.com/s/YrASPZsy6o7SYVpB5LXuuQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:46:30.246992
---

# DeepAudit+星悦AI模型站实战代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/De3yb4u5JSorHMMoCgQ8fgmoAUEUdo1LtXzGld0yeg57wWX4yL6J3QWh4Dq3xXXsWg7U3r2ChiaKAOkoL1fBiaiaCUVDuiaJczc4vbrltk4xXVE/0?wx_fmt=jpeg)

# DeepAudit+星悦AI模型站实战代码审计

原创

XingYue404
XingYue404

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lSQtsngIibibSOeF8DNKNAC3a6kgvhmWqvoQdibCCk028HCpd5q1pEeFjIhicyia0IcY7f2G9fpqaUm6ATDQuZZ05yw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=1jvfty28&tp=webp#imgIndex=0)

点击上方蓝字关注我们 并设为星标

## 0x00 前言

**DeepAudit** 是一个基于 **Multi-Agent 协作架构**的下一代代码安全审计平台。它不仅仅是一个静态扫描工具，而是模拟安全专家的思维模式，通过多个智能体（**Orchestrator**, **Recon**, **Analysis**, **Verification**）的自主协作，实现对代码的深度理解、漏洞挖掘和 **自动化沙箱 PoC 验证**。

项目地址 : https://github.com/lintsinghua/DeepAudit

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSonibuPOSlWHEjC5FxuPQB6Oibcial50FHTJTiaT3YKq2nicLVh26tYYbQrcIyiaHce45C6oyxPddfE03iaa2uZq5O0mLkph4uq0JYVX0/640?wx_fmt=png&from=appmsg)

星悦AI模型站: 配置的 GPT/Claude 系列大模型的中转站，高效率使用Codex和Claude code，链接不中断，持续更新更强大的模型，Plus + Team号池，为你带来高效 Working.

星悦AI中转站地址 : https://xyusec.com/ (现在注册送10$，进群再送5$)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSorIbuGTDvfb1mzicmSjRGY2y2FfvPDj62u5HETgibRKt3OqMHIHFib5BlibHuDN0pZiauuwnNEpib8jTr0k1QQPmHFHWcvdFxoFrkHE/640?wx_fmt=png&from=appmsg)

目前模型列表 :

|  |  |
| --- | --- |
| OpenAi | Anthropic |
| GPT-5.4 | claude-opus-4-7 |
| GPT-5.3-codex | claude-opus-4-6 |
| GPT-5.4-mini | claude-sonnet-4-6 |
| GPT-5.2 | claude-haiku-4-5-20251001 |

## **0x01 DeepAudit 简介+实操**

**DeepAudit 控制台:**

![仪表盘.png](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSoeVA2LbyQB81SicqPUEwz4PNkNN2EOianzcCgH0MqITn78TJ3LUdIibhcxiboM01xAOicbrC4WH8DB4K1ZiaLQBicic809de4qYW5gAaI/640?wx_fmt=png&from=appmsg)

致力于解决传统 SAST 工具的三大痛点：

* **误报率高**

  — 缺乏语义理解，大量误报消耗人力
* **业务逻辑盲点**

  — 无法理解跨文件调用和复杂逻辑
* **缺乏验证手段**

  — 不知道漏洞是否真实可利用

用户只需导入项目，DeepAudit 便全自动开始工作：识别技术栈 → 分析潜在风险 → 生成脚本 → 沙箱验证 → 生成报告，最终输出一份专业审计报告。

> **核心理念**: 让 AI 像黑客一样攻击，像专家一样防御。

一.部署并运行DeepAudit

首先通过Docker compose进行直接部署，一条命令即可

```
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml | docker compose -f - up -d
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSoAaLBGBOG5HoZ3nW87lhHwgBm7iaRBBaAk2ZNXueaULMWuf6hrGfS1Plaqn13bFMyk6dscAHnDF1kCXmjq86V4eNPqxPib3o4TM/640?wx_fmt=png&from=appmsg)

如果一切顺利，那部署完成之后直接访问 ip:3000 即可看到DeepAudit，然后在这里注册一个账号，并登录.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSoeQzeDtUNTicdBJUBia7KjML345XibDYRJemGrQicfhW3fKhNaibiblQZmuDlv8wpYSdxRoQjExARlmm5z6OUIrSam1kFpOgbhUEsEc/640?wx_fmt=png&from=appmsg)

二.配置大模型 Token 令牌

访问 https://xyusec.com/register 注册一个账号，并登录，然后点击控制台-左边的令牌管理-添加令牌-直接点创建令牌

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSpVlTtZvfA6V64gDooKpQytuO6XiaWRSPC0SsqGoia3knNyWoQiasEvPOHndEmh3z8HTBDZYfvSjt534QARvbB1IYI446TF3AGvOc/640?wx_fmt=png&from=appmsg)

注册的邮箱白名单:

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSpk9AHBDXMWp8H3NqnbiaIfGpiaQEC9JmfBD9Qa2R05Iia85O5OicHhKoZdvuBjVmP0e86xukMwXF2FXLjnLFLX3AckBoChN5T76wM/640?wx_fmt=png&from=appmsg)

然后直接就能看到密钥，点击复制密钥，这个就是你需要的Token令牌

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSpNZKccsw08ToGXeIeXPwpFkKf2VmkTgn1d4q5ib12MrzYGSibFGVzFTFzNq8oOoregEAbvXV9qVveXEfII0GwCQ8CDljYmyheEI/640?wx_fmt=png&from=appmsg)

然后访问 https://xyusec.com/pricing 模型广场，选择你想用的模型

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSowRs88GtiaJVXv6hVktEs8RE9As9Z2n8GBLSrgOibD3J2SNjRlTC6wLT87nFBve3dticfFqKHRlAy9kl6g8tibib9v1bkUibS0XxhRY/640?wx_fmt=png&from=appmsg)

然后回到 DeepAudit 点击左边的系统管理，选择一下AI大模型的厂商，我这里用的是openai的GPT-5.4模型，然后填入中转站/官方地址 和 Token令牌(如果你要用GPT，那你API BASE URL 就填https://xyusec.com/v1)

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSomML4fNFIn1wic2JAbnHBNyPxXm5cxV2kpffGiaIiaN8yibAy1oWMKhibc1cibWibUeS5LbOBU978EHb3NpHyhCTxwvdP8ubLeAeOKR0/640?wx_fmt=png&from=appmsg)

然后测试联通即可 :

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSp4GRyvILjcST5mHnEelW6VHFnic8WQx6xib9iaO3SAdgMb7uVm4dleomxBVPLVOIm05Xg67icaroLxU7uAmnRNDzApYm66pMic4oDs/640?wx_fmt=png&from=appmsg)

三.添加项目并进行代码审计

访问项目管理-新建项目，然后上传你想要审计的源码项目

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSoSPcCzemFd1XG9TeFPVdJgfZu3KN71ZPkBGBia1U6Rv5hWzLRyEKnyrabAZyhicYdedOe4V55jZBdfYdK5qNqAROGib8prWicexXI/640?wx_fmt=png&from=appmsg)

这里也可以从 Git 获取项目源码，当然也可以直接上传，然后点执行创建

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSos29iaMRJIkwry1tuNu83VNfDqbEv7cbmlZhyt5jLlsB2HVakoiaCyELFwkf4p3NMpqDUib66zNC2blIZN64zecUYvmj03IFrWVw/640?wx_fmt=png&from=appmsg)

然后点进你的项目，点一下启动审计即可

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSry9kciajazcBf1yIvVGmMfAmxXrQoG7r2svulJguRtRIUusxrdibYW3rTKRiajIyc2ZLibNUkAwsibXlLiaFXNgVkCFXdGRLCurS9X0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSrPJlXfRpJjaRPofJo8dKWYU4XrCWrq8hicSibLsRZVp2gzUicaFH0dGicb1SIOOTwwSsI26onpQKaFHuYJnbN90Wdg577knISrox0/640?wx_fmt=png&from=appmsg)

我这边审计完一个小项目，大概只花了 1.6$ 的额度，目前注册送10$，使用GPT-5.4的话完全是够用的.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSquslk7egrXs4lZxOj8xAtUWBNNDgZTsgdhwxnAibf0hETC1K03dBaRlwgIK3rh8PXIallRV6dqLeHR24Bx74mqo1Xia50kYUZtM/640?wx_fmt=png&from=appmsg)

站点可用性观测 :

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSrq2hIxiblGK5eaXsibGqzwTHicfDDQmCicY8yXNIK6fvH4NLnEv4ic7ygUqP6E4lujopyViatW1QPD6juLeRVXNSIyQBElaxJicQiaPn0/640?wx_fmt=png&from=appmsg)

星悦AI站交流2群

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/De3yb4u5JSqJcNepvEQIx9YCofrtqGnxHKffbodIBma0ecO1YYxgazBlODxgnBcEUDJ5CMzIQOeyFWh63Sx2E2NYEBznsas0GOZph1cPGC8/640?wx_fmt=jpeg&from=appmsg)

## **0x02 20$兑换码获取**

****标签:代码审计，0day，渗透测试，系统，通用，0day，闲鱼，交易所****

******5个AI站 20$ 兑换码，发送 260420 获取(先到先得).******

******免责声明:****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由读者承担全部法律及连带责任，文章作者和本公众号不承担任何法律及连带责任，望周知！！!******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

星悦安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicic8KPZnD5dyHp8uiasNyNWQgSUlzVSibCfnv5HjhSB9o1zibZnicxGGalykSuiaux0iaMneticVbzcGFRxbLP5kaSg1A/0?wx_fmt=png)

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