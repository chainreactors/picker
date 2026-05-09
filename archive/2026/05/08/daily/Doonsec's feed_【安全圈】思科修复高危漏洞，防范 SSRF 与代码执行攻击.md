---
title: 【安全圈】思科修复高危漏洞，防范 SSRF 与代码执行攻击
url: https://mp.weixin.qq.com/s/NhDh5d8A4GWYKv-l8JEFrg
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:05:42.692391
---

# 【安全圈】思科修复高危漏洞，防范 SSRF 与代码执行攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEvxBMQ8oKxlIRzot6tIpCBXZ7Mvy37c79ussiaibR1Mz3795aVUiafVFBic0UXndxsDjy2kicD3b7W0V7ibOckB0mqbMOic87S7z6EDc/0?wx_fmt=jpeg)

# 【安全圈】思科修复高危漏洞，防范 SSRF 与代码执行攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

思科已修复其企业产品中的多个高危漏洞，其中包括 Unity Connection 中的服务器端请求伪造（SSRF）漏洞，这些漏洞可能导致代码执行或服务中断。

思科针对影响其企业产品的多个高危漏洞发布了补丁。若这些漏洞被成功利用，可能导致代码执行、服务器端请求伪造（SSRF）或拒绝服务攻击。**两个值得关注的漏洞，CVE - 2026 - 20034 和 CVE - 2026 - 20035，影响到思科 Unity Connection。攻击者可利用这些漏洞发动 SSRF 攻击。**

思科发布的公告称：“思科 Unity Connection 中的多个漏洞，可能使远程攻击者通过受影响设备执行任意代码，或进行服务器端请求伪造（SSRF）攻击。”

CVE - 2026 - 20034 是思科 Unity Connection 中的一个漏洞，允许经过身份验证的远程攻击者在设备上运行任意根级别代码。该问题源于对用户输入的验证不当，攻击者可发送精心构造的 API 请求，从而完全攻陷系统。思科已发布修复程序，目前没有可用的变通方法。

公告指出：“此漏洞是由于对用户提供的输入验证不足导致。攻击者可通过提交精心构造的 API 请求来利用此漏洞。成功利用该漏洞可使攻击者以根用户身份执行任意代码，这可能导致目标设备被完全攻陷。要利用此漏洞，攻击者必须拥有受影响设备上的有效用户凭据。”

CVE - 2026 - 20035 是思科 Unity Connection Web Inbox 用户界面（UI）中的漏洞，允许未经身份验证的远程攻击者执行 SSRF 攻击。该问题源于对某些 HTTP 请求的验证不当。攻击者通过发送精心构造的请求，可使设备代表他们发送任意网络流量，有可能访问内部服务。

公告称：“思科 Unity Connection Web Inbox 的 Web 用户界面中存在一个漏洞，可能使未经身份验证的远程攻击者通过受影响设备进行 SSRF 攻击。”

“此漏洞是由于对特定 HTTP 请求的输入验证不当导致。攻击者可通过向受影响设备发送精心构造的 HTTP 请求来利用此漏洞。成功利用该漏洞可使攻击者发送源自受影响设备的任意网络请求。”

以下是受影响的版本及修复版本：

|  |  |
| --- | --- |
| 思科Unity Connection 版本 | 修复版本 |
| 12.5 及更早版本 | 迁移至修复版本 |
| 14.0 | 14SU5 |
| 15.0 | 15SU4 或应用补丁文件：1 ciscocm.cuc.V15\_CSCwq36774 - CSCwq36834\_C0277 - 1.zip |

***END***

阅读推荐

[【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=1&sn=38a3aaf6dc9ce8f8a4c69044d68a8236&scene=21#wechat_redirect)

[【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=2&sn=1777c0b96b34a5c5c86af01090010f49&scene=21#wechat_redirect)

[【安全圈】基于 Mirai 的 xlabs\_v1 僵尸网络利用 ADB 劫持物联网设备发动 DDoS 攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=3&sn=0fb288079b71e898e51fe38b9fec7073&scene=21#wechat_redirect)

[【安全圈】安卓高危0Day漏洞可远程获取Shell访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=1&sn=f04ddcae84cf9ff13b2696de01ec65eb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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