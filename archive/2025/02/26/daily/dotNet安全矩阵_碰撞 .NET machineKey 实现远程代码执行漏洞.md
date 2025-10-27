---
title: 碰撞 .NET machineKey 实现远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247499005&idx=2&sn=9c47da3e24414169e02a6c2294740935&chksm=fa595210cd2edb06d588fc0bb09c1c0b69c020b0c666f089bf17f53a28b8e2c719690e980d27&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2025-02-26
fetch_date: 2025-10-06T20:37:35.264356
---

# 碰撞 .NET machineKey 实现远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQvicj6lCHbe1vM5FMPfQyAjLYm2XZCYJRW3MBbqTemgxUf0OFnHHia3SA/0?wx_fmt=jpeg)

# 碰撞 .NET machineKey 实现远程代码执行漏洞

专攻.NET安全的

dotNet安全矩阵

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NO8Q9ApS1YibJO9SDRBvE01T4A1oYJXlTBTMvb7KbAf7z9hY3VQUeayWI61XqQ0ricUQ8G1FykKHBNwCqpV792qg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

近期，Microsoft Threat Intelligence监测到一起由未知威胁行动者发起的攻击事件。该行动者利用从公开资源中获取的 .NET 机器密钥，成功注入了恶意代码，并部署了Godzilla，尽管其活动范围有限。经调查，发现问题的根源在于部分开发人员错误地从可公开访问的代码文档和存储库中整合了已公开的 .NET 机器密钥，为威胁行动者提供了可乘之机。

**01. ViewState攻击**

ViewState是 .NET Web窗体用于在回发之间保存页面和控件状态的一种机制。ViewState数据被存储在页面上的隐藏字段中，并使用Base64编码。

为保护ViewState免受篡改和信息泄露，.NET页面框架使用机器密钥：ValidationKey和DecryptionKey。这些密钥可自动生成并存储在注册表中，也可在配置文件中手动指定。

若这些密钥被盗或泄露给威胁者，他们可利用这些密钥制作恶意ViewState，并通过POST请求发送至网站。当目标服务器上的.NET运行时处理该请求时，由于使用了正确的密钥，ViewState将被解密并验证通过。随后，恶意代码将被加载到工作进程内存中并执行，使威胁者能够在目标IIS Web服务器上获得远程代码执行能力。

为了直观展现此类攻击的危害，并在我们的dot.Net安全代码审计课程中深入讲解，我们设计了视频教程和demo代码案例。通过这些材料，可以亲自挖掘漏洞，并观察实际操作触发漏洞的过程。以下图示展示了相关的内容和演示效果。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQI2asQYMLrSkz8ZyrFcsGUD21AFBpPGJRuZOGWsblNQicreJ5psRw2OQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQr45eeDHOrlTTvXUicKNPGr3G46EtZLXUibfu9sG9Hl9ILao5gVVxkib0A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQCIwkXqY2IoiaVpQibicwtHJp8xEIoKmsia72UB8oIrzfxl4RuaRHIb9DIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQIoHrFAbAUxvov3eQFh1OfUAgwQVKdVpMkW7ibXZk1xJGWv8RrhYN3Cg/640?wx_fmt=png&from=appmsg)

**02. Godzilla内存马**

在近期的攻击事件中，一位攻击者利用公开的机器密钥成功实施了ViewState代码注入攻击。他们通过恶意ViewState负载反射性地加载了名为assembly.dll的Godzilla工具，其中 SHA-256哈希值为19d87910d1a7ad9632161fd9dd6a54c8a059a64fc5f5a41cf5055cd37ec0499d及其插件模块。Godzilla的功能包括执行恶意命令、将shellcode注入进程等，攻击过程如下图所示。

![图表显示了威胁行为者用来发起 ViewState 代码注入攻击的公开机器密钥。](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9OR8iapNWk1qj3sy365WdpQCicBxF0pNpeg8v4WiaPkHzBQ5DC61zLibowyZC6BKbTqHqXNO8lEjBaKQ/640?wx_fmt=other&from=appmsg)

**03. NET代码审计学习**

微软的.NET技术广泛应用于全球企业级产品，包括其知名的**Exchange**、**SharePoint**等，国内如**某友的Cloud**、**某通的T系列**、**某蝶的云产品**等也广泛采用。各行业核心业务均依赖于此技术。这些基于.NET的系统频繁遭攻击，问题涵盖任意文件上传、反序列化漏洞、SQL注入、文件下载漏洞、命令执行漏洞等。

截至目前，星球已推出近**100节内容** (还在持续增加)，包括**70个视频+30份PDF文档**。我们已将内容细致划分为15个分类，并随新漏洞类型的出现持续扩展。在这里您将学到包括但不限于以下漏洞类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwdR00lAaNpUuDDlI6Gk1uEEPZxUMlb4FkDvOBLYq92InlzpwmzWeibjQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

详细的内容与结构，请参考下方的星球大纲版块，包括但不限于OWASP十大漏洞类型，涉及SQL注入漏洞、文件上传下载漏洞、任意文件操作漏洞、XML外部实体注入漏洞、跨站脚本攻击漏洞、反序列化漏洞、命令执行漏洞、未授权和越权漏洞、第三方组件漏洞等等。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwMahhN19jbtUiax5UWVU0R3n4eick9XQEHyf3lhjE3wvCic9ZFD3h9tWsQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 专属福利

1. 学习模式: 代码审计知识星球**在线录播视频** +后续漏洞挖掘直播、内部专属交流社区答疑解惑；

2. 优享福利：加入.NET代码审计星球后**赠送永久**dot.Net安全基础入门星球。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANI9DCxS2KHkqiaXBk22ZevuRm08onmEibIUvdEy5zJGCoHg4HAsrgQ22w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

欢迎对.NET代码审计关注和关心的同学加入我们 [dot.Net安全代码审计] ，目前已有近 100+ 位朋友抢先预定。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

星球门票后期价格随着内容和质量的不断沉淀会适当提高，**越早加入越划算！** 现在加入星球可享受星球早鸟价，并可**领取100元优惠券**，期待在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事，**可扫描下方老师二维码了解更多详情。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANBJ4t8XC4ibbWjhzj0447zAJcWgwV9wcDhcibNiax3P7iagSYwn31GEkTBw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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