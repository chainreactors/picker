---
title: 【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=2&sn=c856137ec845bc74a8a86abc23c1eb69&chksm=f36e7e35c419f723beffbdca1db705d69cd6c43e9da167f5a9d1b2905a34a6e32ae2740c3743&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-06
fetch_date: 2025-10-06T19:39:21.013252
---

# 【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylial99L55LA7ZOu76kVlReQ6GflhkF5AfAVFbhKkz4g5lOVz2Q3Nl1yEsc2QUEibJyb918vst3FJpWA/0?wx_fmt=jpeg)

# 【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

近日，微软被曝Windows AFD.sys漏洞（编号：CVE-2024-38193）正在被黑客组织利用。该漏洞被归类为自带易受攻击驱动程序（BYOVD）漏洞，可影响Windows套接字的注册I/O（RIO）扩展，并允许攻击者远程接管整个系统。

漏洞影响版本包括Windows 11（ARM64、x64，多个版本）、Windows 10（ARM64、x64、32位，多个版本）、Windows Server 2008、2012、2016、2019、2022（多个版本）。![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylial99L55LA7ZOu76kVlReQ61OT77M5wj1icnLxCibhmU4EjibRTvUGTy39yshp1ucXYLPEGUbLuabZLA/640?wx_fmt=jpeg&from=appmsg)

目前，已有迹象表明黑客组织正在利用该漏洞发起攻击，例如朝鲜黑客组织Lazarus就是其中之一，其安装名为FUDModule的根工具包（rootkit），可在目标系统上获得最高权限。2024年8月，微软发布安全更新已经修复该漏洞，强烈建议组织及时进行修复。

## 漏洞概述

### 漏洞成因

CVE-2024-38193漏洞存在于Windows辅助功能驱动程序（AFD.sys）中。AFD.sys是Winsock协议栈的关键组件之一，处理底层网络调用，并在内核模式下执行操作。漏洞的根本原因是AFD.sys在处理特定系统调用时缺乏适当的边界检查，导致攻击者可以构造恶意输入，触发内存溢出或其他未定义行为，从而绕过安全检查，提升权限。由于AFD.sys在所有Windows系统中广泛部署，这使得该漏洞特别危险。

### 漏洞利用过程

漏洞触发

攻击者首先通过恶意应用程序或远程代码执行方式，向AFD.sys驱动程序发送恶意构造的系统调用请求。通过精心构造的输入，攻击者可以让AFD.sys在内核模式下执行越权操作。
这种攻击方式利用了Windows内核的漏洞，能够在用户态和内核态之间绕过安全边界，执行未授权的操作。

权限提升

一旦漏洞触发，攻击者可以利用漏洞执行任意代码，并获得SYSTEM权限。通过这种方式，攻击者能够完全控制受影响的设备，部署恶意软件或修改系统配置。获得SYSTEM权限后，攻击者可以执行一系列高级操作，包括禁用安全软件、修改系统文件和执行其他恶意活动。

FUDModule根工具包的安装

获得SYSTEM权限后，攻击者会安装FUDModule根工具包。FUDModule是一种专门设计用于隐藏攻击痕迹、绕过安全监控的复杂恶意软件。通过关闭Windows的监控功能，FUDModule可以让攻击者在受害者系统中保持长期隐蔽。FUDModule的存在使得攻击者能够在不被发现的情况下持续控制目标系统，增加了防御的难度。

## 修复建议

微软已经发布了针对CVE-2024-38193的安全补丁，覆盖了多个Windows版本。建议所有用户和组织尽快应用补丁，避免系统遭到利用。及时应用补丁是防止漏洞利用的最有效手段之一，用户应确保系统和应用程序都安装了最新的安全更新。

参考来源：https://cybersecuritynews.com/windows-driver-use-after-free-vulnerability/

***END***

阅读推荐

[【安全圈】曾是全球最大暗网黑市的九头蛇市场头目被俄罗斯法院判处终身监禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=1&sn=2ee2071726cfb4ce3094d140ede4aec8&scene=21#wechat_redirect)

[【安全圈】因涉嫌实施侵入性的监控行为，苹果公司在加州被员工起诉](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=2&sn=e7bfb574035ddf65de6fd8b49b20379e&scene=21#wechat_redirect)

[【安全圈】思科安全设备ASA十年老漏洞正在被利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=3&sn=26ea707878614e9c3a2395f4334a3b4c&scene=21#wechat_redirect)

[【安全圈】只需几分钟，AWS密钥泄露即被利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066407&idx=4&sn=9cbfcbbf89fbee51aff80ed24c0d0684&scene=21#wechat_redirect)

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

阅读原文

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