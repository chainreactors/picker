---
title: 深信服运维安全管理系统 get_all_application_release 敏感信息泄露
url: https://mp.weixin.qq.com/s/peVdns4WP25CCLs-4-q0oQ
source: Doonsec's feed
date: 2026-09-07
fetch_date: 2026-09-08T06:40:12.276623
---

# 深信服运维安全管理系统 get_all_application_release 敏感信息泄露

# 深信服运维安全管理系统 get\_all\_application\_release 敏感信息泄露

Superhero
Superhero

Nday Poc

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkYN4sZibCVo6EFo0N9b7Kib4I4N6j6Y10tynLOdgov9ibUmaNwW5yeoCbQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=8n1b48rw&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCkhic5lbbPcpxTLtLccZ04WhwDotW7g2b3zBgZeS5uvFH4dxf0tj0Rutw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=vx7xykg3&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Melo944GVOJECe5vg2C5YWgpyo1D5bCk524CiapZejYicic1Hf8LPt8qR893A3IP38J3NMmskDZjyqNkShewpibEfA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=x3261qcu&tp=webp#imgIndex=2)

内容仅用于学习交流自查使用，由于传播、利用本公众号所提供的POC信息及POC对应脚本而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号Nday Poc及作者不为此承担任何责任，一旦造成后果请自行承担！

**01**

**漏洞概述**

深信服运维安全管理系统 get\_all\_application\_release 存在信息泄露漏洞，未授权攻击者可利用该漏洞获取系统用户信息，可能导致进一步的攻击。

**02**

****搜索引擎****

fofa:

```
body="/fort/login" && header="FORTSESSIONID"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8o9dnzNIF1g3fX3MCAo8c1FgCow7dulJF1UnnZ1wLeSqZNJxJnWSs0CUsasushgFP5EibWz0zBUNNuffB1W3CTz3Htkuf9uatupZaOYL8ibjI/640?wx_fmt=png&from=appmsg)

**03**

**漏洞复现**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8o9dnzNIF1hrcxztNpRQbCAIic6ozcdg9IkJBtHKsEb0zyToicTfAZnCQlOBohibyEu14XVjicibYxG8dn4TYuHEgdyhbmeibtofeVlia2T9NiaicEv4/640?wx_fmt=png&from=appmsg)

**04**

**自查工具**

nuclei

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8o9dnzNIF1gaUx8MTsN40uriaeZYickX2quHhxH9U6N74nlREvFThCIZTAtacXTe82CK6cEdoGgqfRZtTcsHDK9ibzNpBlictN2Dv1PF1hEgzss/640?wx_fmt=png&from=appmsg)

afrog

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8o9dnzNIF1iauwdCdMqgMcvicPLicPFiaoH1u5lnWTCvv40sia4WEDjfCENph27DRxqO7nLIlibCkB4DCdWq8sxU8TK78AsyVNPPfeLSPQWLVhIIM/640?wx_fmt=png&from=appmsg)

**05**

**修复建议**

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

**06**

**内部圈子介绍**

### **【Nday漏洞实战圈】🛠️**

专注公开1day/Nday漏洞复现 · 工具链适配支持
✧━━━━━━━━━━━━━━━━✧

🔍 **资源内容**
▫️ 整合全网公开1day/Nday漏洞POC详情
▫️ 适配Afrog/Nuclei检测脚本
▫️ 支持内置与自定义POC目录混合扫描

🔄 **更新计划**
▫️ 每周新增7-10个实用POC（来源公开平台）
▫️ 所有脚本经过基础测试，降低调试成本

🎯 **适用场景**
▫️ 企业漏洞自查 ▫️ 渗透测试 ▫️ 红蓝对抗 ▫️ 安全运维

✧━━━━━━━━━━━━━━━━✧
⚠️ **重要声明**

▫️仅限合法授权测试，严禁违规使用

**▫️虚拟资源服务，购买后不接受任何形式退款**

▫️付款前请评估需求，慎重考虑

![图片](https://mmbiz.qpic.cn/mmbiz_png/8o9dnzNIF1jOz2NQAkjcESOiaso1KwSGRjJyf82vOumm32c28ReqUyJ6paoTcaMyicfjl4iaE1GYiabIeEbAgLM1o74Z2YhROxyqibuVqqLCLN9M/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/8o9dnzNIF1iarsazJCVPyYXnZHR84oCBjUtOOhrAh9mysxXYot1ia7GmzWv0CUdraS6abia1kia3qpicCxxniasNBmAZJB7LJ6lN8sKvmdagKunaQ/0?wx_fmt=png)

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