---
title: 思科物联网无线AP遭遇严重命令注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247531975&idx=1&sn=56c499e1153e0c4f6356185ac1ded5a1&chksm=c1440f7af633866c05c42df55d11bf04d3c958aa61ec6c19861393ad6e599687d4011abedd73&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-12-21
fetch_date: 2025-10-06T19:38:43.625634
---

# 思科物联网无线AP遭遇严重命令注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoO1SJCtkELUib5ggwXGfkW7cOWOXpSVkTqKr8ws7fsT2h2uJXmKE1yfupW3KVpVNquUSH90iaOx9dQ/0?wx_fmt=jpeg)

# 思科物联网无线AP遭遇严重命令注入漏洞

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqpElNdtFsCp3IrxRyPu1CF9rCVE3Ed2GrXp6SDsyafvPLFibfAdiaKCSLBeuMfRWfeeOjsXYX6mYbIQ/640?wx_fmt=png&from=appmsg)

思科公司的URWB硬件出现了一个难以忽视的漏洞，攻击者可利用伪造的 HTTP 请求劫持接入点的 Web 界面。

Cisco 称该问题CVE-2024-20418影响三种产品：Catalyst IW9165D 接入点、Catalyst IW9165E 接入点和无线客户端以及 Catalyst IW9167E 接入点。

不过，思科表示，接入点只有在 URWB 模式下运行易受攻击的软件时才会受到攻击。管理员可以使用 show mpls-config 命令确认 URWB 模式是否正在运行。如果禁用，则设备不受影响。不使用 URWB 的 Cisco 其他无线接入点产品不受影响。

**至于缺陷本身：**

"该漏洞是由于对基于 Web 的管理界面的输入验证不当造成的。攻击者可以通过向受影响系统的基于网络的管理界面发送伪造的 HTTP 请求来利用这个漏洞。

"成功的漏洞利用可使攻击者在受影响设备的底层操作系统上以root权限执行任意命令"。

换句话说，这将是一次彻底的入侵。这类漏洞在常见弱点枚举（CWE）数据库中被列为第 77 个，又称 "命令注入"。

**这一点意义重大，因为就在今年 7 月，****CISA 曾警告****此类漏洞的危险性。**

"CISA 写道："当制造商在构建要在底层操作系统上执行的命令时，未能对用户输入进行适当验证和审查，就会产生操作系统命令注入漏洞。

该组织请求制造商采用安全设计原则来避免这一问题。

**谁在使用 URWB 接入点？**

URWB 产品线是一个物联网接入点系列，适用于工业或户外环境。2020 年，思科收购了意大利公司 Fluidmesh Networks ，从而获得了 URWB 的基础技术。

URWB 模式允许接入点在通常难以保证的环境中支持高速、可靠、低延迟的无线连接。

在 2021 年一篇关于该技术的博客中，Fluidmesh Network 的联合创始人兼前首席执行官 Umberto Malesci 列举了几个使用该技术的例子，其中包括在法国的动车组上实现 1000 台设备的 IP 摄像头网络，在马耳他实现港口起重机的无线控制，以及作为支持米兰无人驾驶地铁列车的基础设施的一部分。

"想象一下远程监控火车、地铁、公共交通、矿井或港口上的移动资产的情景。如果在查看电子邮件时掉了几个数据包，没有人会注意到。相比之下，远程控制起重机或自动驾驶汽车时丢包会造成严重后果，"Malesci 写道。

这些使用案例的关键性凸显了优先修补该漏洞的重要性。不过，由于这类接入点通常被隔离在专用的物联网网段上，因此尚不清楚攻击者直接瞄准该漏洞有多容易。如果是这样的话，攻击者可能需要无线接近才能利用这个漏洞。

**修补建议**

由于该漏洞的 CVSS 得分最高为 10.0，而且没有可用的解决方法，因此修复该漏洞需要管理员通过思科的更新渠道应用软件补丁。思科表示，使用 17.14 及更早版本软件的企业应更新至修复版本，而使用 17.15 版本的企业应更新至 17.15.1 版本。

建议若组织购买的URWB 接入点渠道商没有技术支持能力，请联系 Cisco 技术中心。

截至目前，思科的产品安全事故响应小组（PSIRT）表示，它没有发现任何针对该漏洞的漏洞利用。

\* 本文为闫志坤编译，原文地址：https://www.networkworld.com/article/3600993/cisco-iot-wireless-access-points-hit-by-severe-command-injection-flaw.html
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqos5a6Z5B6UrU0VmoicIP7IvuJWmXe2HBJ3ZUZuPdpG4uUiaVrTFajxtY0AIjWcrWUDDeC0EFT2waicg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513339&idx=1&sn=759f859d0cf7dd748d3dd83ce49cf4cc&chksm=c144c646f6334f5017581206b0da2af90d539c921614514e3eb40f6c80d846bece0e6b521067&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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