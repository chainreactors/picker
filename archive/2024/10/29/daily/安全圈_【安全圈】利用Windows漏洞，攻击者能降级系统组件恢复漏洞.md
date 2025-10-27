---
title: 【安全圈】利用Windows漏洞，攻击者能降级系统组件恢复漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065566&idx=4&sn=2b801b48c3a2637022eda84b8ded4b9b&chksm=f36e635ec419ea48fb3673df944a0a01efd65ec51428521954973b7f681350f5cba836cf2779&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-29
fetch_date: 2025-10-06T18:55:30.677329
---

# 【安全圈】利用Windows漏洞，攻击者能降级系统组件恢复漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhMxJNJc2b6qIKuQgm0Jz5kPUpf80NjdxIOiaDmMrI2U33dPD3uCd2T6EUaG6yK6Ln5A2Qb9lUslaQ/0?wx_fmt=jpeg)

# 【安全圈】利用Windows漏洞，攻击者能降级系统组件恢复漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据Hackread消息，在最近的一项研究中，SafeBreach Labs 研究员揭露了一种新的攻击技术，能够操纵Windows 11系统在更新时降级关键系统组件，从而让一些漏洞修复补丁失效。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhMxJNJc2b6qIKuQgm0Jz5kTibKgMrQnibb566UPgyV1OnjIXqBibvUBDEBfv5dddQHkxDR30N1RNemA/640?wx_fmt=jpeg&from=appmsg)

该攻击原理最初于2024 年 8 月在Black Hat USA 2024上披露，而现在研究人员公布了更多细节，以加强公众对这次攻击的了解。

这种被称为 Windows Downdate 的技术利用的其中一个漏洞是“ItsNotASecurityBoundary”驱动程序签名强制 （DSE） 绕过，能允许攻击者加载未签名的内核驱动程序，将经过验证的安全目录替换为恶意版本，从而能够加载未签名的内核驱动程序。

比如，攻击者可以针对特定组件，例如解析安全目录所必需的“ci.dll”模块，并将它们降级到易受攻击的状态，从而能够利用此绕过并获得内核级权限。

"ItsNotASecurityBoundary "DSE 绕过是一类名为 "虚假文件不变性"（FFI）的新漏洞的一部分，利用了关于文件不可变性的错误假设 ，允许通过清除系统工作集来修改 "不可变 "文件。

研究人员概述了在具有不同级别虚拟化安全（VBS）保护的 Windows 系统中可利用漏洞的步骤，发现了多种禁用 VBS 关键功能的方法，包括凭证防护和受管理程序保护的代码完整性（HVCI）等功能，甚至首次使用了 UEFI 锁。

要利用没有 UEFI 锁的系统，攻击者必须通过修改注册表设置来禁用 VBS。一旦禁用，就可以将 ci.dll 模块降级到易受攻击的版本，并利用“ItsNotASecurityBoundary”漏洞。对带有 UEFI 锁和 "强制（Mandatory ）"标志的 VBS 是最安全的配置，即使锁被绕过，VBS 也不会被禁用。研究人员解释说，目前还没有已知的方法可以在没有物理访问的情况下利用具有这种保护级别的系统。

总体而言，这种 Windows 更新接管功能允许攻击者加载未签名的内核驱动程序、启用自定义 rootkit 以解除安全控制、隐藏进程并保持隐蔽性，从而对企业构成了重大威胁。攻击者可以对关键操作系统组件（包括 DLL、驱动程序甚至 NT 内核）进行自定义降级。通过对这些组件进行降级，攻击者可以暴露以前修补过的漏洞，使系统容易被利用。

为降低风险，企业应及时更新系统，打上最新的安全补丁，以解决漏洞问题，同时部署有效的端点检测和响应（EDR）解决方案，以检测和响应恶意活动，防止未经授权的访问和数据泄露。此外，使用 UEFI 锁定和 "强制 "标志启用 VBS 还能提供额外的保护。

参考来源：New Attack Lets Hackers Downgrade Windows to Exploit Patched Flaws

***END***

阅读推荐

[【安全圈】黑客组织宣称入侵被动元件大厂华新科 不付赎金10月31日公开机密](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065543&idx=1&sn=f13f0caedf978f0f25a9982941913117&chksm=f36e6347c419ea518b271725651d92832b6c3d49e44aaec947be4944df6245b6dd50554c5bb7&scene=21#wechat_redirect)

[【安全圈】因非法使用用户数据，这家社交巨头被罚23.8亿元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065543&idx=2&sn=4efe91e50571c82da0a634286b7b211f&chksm=f36e6347c419ea515299022efe3c6a4d5be1040a4fdf9e91c466b492cc1a057d677c13c4e01c&scene=21#wechat_redirect)

[【安全圈】Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065543&idx=3&sn=b8a04fa9094f1ff644a46c7e77e91aad&chksm=f36e6347c419ea5117820d0337cd4fc89a241b03666d801bebddaba03c52cb638805deea4261&scene=21#wechat_redirect)

[【安全圈】因持续技术问题未能解决 微软宣布暂时撤掉Windows 11所有开发虚拟机](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065543&idx=4&sn=0f91eb5837ad0719008c96a2ecf89334&chksm=f36e6347c419ea51727a60401161113b752587353cae0f5d7a29b5d8841ea5b109024e622296&scene=21#wechat_redirect)

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