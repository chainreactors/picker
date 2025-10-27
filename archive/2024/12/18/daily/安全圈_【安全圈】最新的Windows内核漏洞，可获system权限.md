---
title: 【安全圈】最新的Windows内核漏洞，可获system权限
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066655&idx=4&sn=c56864b01e3e298b37ea2863eea40424&chksm=f36e7f1fc419f609a1fbb13ab7b6034ae28df0252abc5dbb47ba057c00c636754fcd86e2efcc&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-18
fetch_date: 2025-10-06T19:42:52.639851
---

# 【安全圈】最新的Windows内核漏洞，可获system权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgUwVcfEaY3HHicoCR0WwUKicia2xEUcyEIQC5CJRzUY78aBJv5HcpVKIJCvib1N4mE7HKaVP9MQrlVTA/0?wx_fmt=jpeg)

# 【安全圈】最新的Windows内核漏洞，可获system权限

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

内核漏洞

网络安全和基础设施安全局（CISA）已将两个新的漏洞添加到其已知被利用漏洞目录中，其中一个是涉及 Windows 内核的漏洞，目前正被用于攻击。

该漏洞编号为CVE-2024-35250，具体是在 Windows 的 ks.sys 驱动中存在的 "不受信任的指针解引用" 。这个漏洞可以通过利用未受信任的指针，来进行任意内存读写，最终实现权限提升。这种问题可能导致系统崩溃或使攻击者能够执行任意代码，对安全专业人员来说是一个重要关注点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgUwVcfEaY3HHicoCR0WwUKic2ibl5VqxGgAz3uzSXrMzcOERTRh4ibpZb56H9qAztKGzAhhgwOofH72g/640?wx_fmt=jpeg&from=appmsg)

微软已在最近的12月星期二补丁中修复了该漏洞 ，并表示“成功利用这一漏洞的攻击者可能获得 system权限。”该公司在6月发布的安全公告中仅提供了有限的细节，不过发现该漏洞的 DEVCORE 研究团队通过趋势科技的零日计划（Zero Day Initiative）将其报告给微软，并确定受影响的系统组件为 Microsoft Kernel Streaming Service (MSKSSRV.SYS)。

影响版本：

* Windows 10 20H2 Build 19042
* Windows 11 22H2 Build 22621
* VMWare Workstation 17 Pro 环境下也可被利用

漏洞细节：

攻击者可以通过发送特制的 IOCTL 请求触发 ks.sys 驱动中的漏洞，利用不可信指针的解引用，最终对系统内存进行任意读写操作。

限制条件：

* 实测该漏洞无法在 Hyper-V 环境中成功利用；
* 攻击者需要拥有中等权限（Medium Integrity Level，通常为普通用户权限），才能触发漏洞进行提权。

当前大部分 XDR（扩展检测和响应）解决方案能够检测并阻止该漏洞的利用行为。

另外一个漏洞编号是CVE-2024-20767：此漏洞影响 Adobe ColdFusion，涉及不当的访问控制。攻击者可以利用此类漏洞来获取敏感信息或系统的未经授权访问，对网络安全构成重大威胁。对此，CISA 的操作指令（BOD）22-01，题为“减少已知被利用漏洞的重大风险”，要求联邦政府行政部门（FCEB）机构在指定的截止日期前修补这些漏洞，并表示“此类漏洞是一种常见的攻击途径，对联邦企业构成重大风险。”

虽然 BOD 22-01 明确针对 FCEB 机构，但CISA 依旧强烈建议所有组织采取积极措施，以减少其网络攻击的暴露面。

参考来源：https://cybersecuritynews.com/windows-kernal-vulnerability-actively-exploits-in-attacks/

***END***

阅读推荐

[【安全圈】赛博菩萨Cloudflare更新服务条款：禁止将其作为代理使用及优选IP](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=1&sn=eac9fa65e1d3c1f6c5688eacc6c39188&scene=21#wechat_redirect)

[【安全圈】密码将死？微软无密码时代取得重大进展](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=2&sn=f81de7c93b3005422e46cbec006e2f5d&scene=21#wechat_redirect)

[【安全圈】针对安全人员，攻击者窃取了39万个WordPress凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=3&sn=06b72f6bc788395990f167cdbed88121&scene=21#wechat_redirect)

[【安全圈】iOS和macOS系统曝关键漏洞，可破坏TCC框架](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=4&sn=34b67f730621eac29fece525a015ab35&scene=21#wechat_redirect)

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