---
title: Sub2Api 网关平台存在0计费bug漏洞
url: https://mp.weixin.qq.com/s/waGLYUcPMMttlPZsVDq09w
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:59:16.319534
---

# Sub2Api 网关平台存在0计费bug漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/De3yb4u5JSpRwf3llReGfIqA8T2XIu7YgVz6OwIWticlWefBxDNC0tEjx332aBUrMTzQ7dgau1JhGSA8ficdeO4AZflR5BgyVgjayI3TGAWnE/0?wx_fmt=jpeg)

# Sub2Api 网关平台存在0计费bug漏洞

原创

Mstir
Mstir

星悦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lSQtsngIibibSOeF8DNKNAC3a6kgvhmWqvoQdibCCk028HCpd5q1pEeFjIhicyia0IcY7f2G9fpqaUm6ATDQuZZ05yw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=1jvfty28&tp=webp#imgIndex=0)

点击上方蓝字关注我们 并设为星标

## 0x00 前言

Sub2API 是一个 AI API 网关平台，用于分发和管理 AI 产品订阅的 API 配额。用户通过平台生成的 API Key 调用上游 AI 服务，平台负责鉴权、计费、负载均衡和请求转发，一般人是用来搭建中转站的，就跟下图一样.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/De3yb4u5JSq9cKggP2F6xu2jJOjlBwJkiaFqvwS8Z8ddyeRQmhORLQg9RTtLdx7JLf8Vjfr8XyONH4eOkr3AjWBl8fy4wEPUliaJEzfbIQ4Ho/640?wx_fmt=png&from=appmsg)

## **0x01 0计费bug漏洞**

Sub2API 可以把gpt-5.5改成gpt5.5就能0扣费无限使用，原因不明，而且只有gpt可以，Sub2API有效，通过更改 Codex 的Config.toml文件的 model 即可实现.

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSrBOeA1ecNa8hqay6AUia9YvVtluFaHmQwy7uYVYbeqVS2gibLJIYlP23Cnvn6CF8twrGdLCrSiamT5Ih4OjNKQYmf1nhrPCUDm1E/640?wx_fmt=png&from=appmsg)

Codex实测:

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSr8NEuUBjAljRBZYTX0ZByHqLwIribwjiax71odL3rIUQoWrvOxwdSmsqLMwicPN39dIaB4ib6kTibd4XwPPFIWgEVcNzLU2I4AH1Zc/640?wx_fmt=png&from=appmsg)

跑完一个任务之后，后台日志中无计费，不扣费，可无限使用

![](https://mmbiz.qpic.cn/mmbiz_png/De3yb4u5JSq0v81UuSicG5Gn5iaQGzL5EibEkO2Xtk49F4tSFibicYEqUAZtIf4wxxmxZL2JcSgdzxXz8ebTLrLibH6P2qA5Du0LzTT1Gs5WjCu00/640?wx_fmt=png&from=appmsg)

## **0x02 关注公众号**

****标签:代码审计，0day，渗透测试，系统，通用，0day，闲鱼，交易所****

******关注公众号，时刻更新信息安全知识******

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