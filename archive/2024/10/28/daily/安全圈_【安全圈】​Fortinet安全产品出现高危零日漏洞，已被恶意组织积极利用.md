---
title: 【安全圈】​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065543&idx=3&sn=b8a04fa9094f1ff644a46c7e77e91aad&chksm=f36e6347c419ea5117820d0337cd4fc89a241b03666d801bebddaba03c52cb638805deea4261&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-28
fetch_date: 2025-10-06T18:49:56.493189
---

# 【安全圈】​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh9QudMgdXF2d7gM77gf3WgTsticKjhzLMzvJJ9j3AIR0bAVcM8jcoKPTb3ic7TZVPOd9lQEoojpiaTQ/0?wx_fmt=jpeg)

# 【安全圈】​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

网络安全公司 Fortinet 日前披露了自家软件产品 FortiManager 存在的一个关键零日漏洞，能够允许未经身份验证的远程攻击者通过特制请求执行任意代码或命令。目前该漏洞已在野外被积极利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh9QudMgdXF2d7gM77gf3Wgv8Lic3k0tE8Vycwtl1XvibYoPX3OGAPFGPENDsMBHtGGhic4j44ianoVuA/640?wx_fmt=jpeg&from=appmsg)

根据 Fortinet 10月23日发布的报告，该漏洞被追踪为CVE-2024-47575，CVSS v3 评分高达9.8，对多个版本的 FortiManager 以及 FortiManager Cloud 都有影响。该公司已经发布了一个补丁，并列出了用户可以采用的几种解决方法。

报告表明，该漏洞已被利用以自动从 FortiManager 中泄露敏感文件，包括 IP 地址、凭证和托管设备配置，但目前尚未收到在受感染的 FortiManager 系统上安装任何恶意软件或后门的低级系统报告。

参与此漏洞调查的Mandiant表示，一个新的威胁组织UNC5820早在 2024 年 6 月 27 日就利用了 FortiManager 漏洞，泄露并暂存了FortiManager 管理的 FortiGate 设备配置数据，其中包含受托管设备的详细配置信息以及用户的 FortiOS256 加密密码，这些数据可能被 UNC5820 用来进一步破坏 FortiManager，并在企业环境中横向移动。

目前Mandiant无法确定利用漏洞的攻击者身份及其最终目的，因此提醒任何 FortiManager 暴露在互联网上的组织都应立即进行取证调查。

## 受影响的版本和缓解措施

该漏洞影响 FortiManager 和 FortiManager Cloud 的多个版本：

* FortiManager：版本 7.6.0、7.4.0 到 7.4.4、7.2.0 到 7.2.7、7.0.0 到 7.0.12 以及 6.4.0 到 6.4.14。
* FortiManager Cloud：版本 7.4.1 到 7.4.4、7.2（所有版本）和 7.0（所有版本）。

Fortinet 已经发布了这些版本的补丁，并敦促用户立即升级到安全版本。此外，某些版本还提供了解决方法，包括阻止未知设备注册和使用自定义证书进行身份验证。

Fortinet 建议立即采取措施保护受影响的系统：

1. 升级：安装 FortiManager 的最新补丁，如果使用 FortiManager Cloud，请迁移到固定版本。
2. 查看配置：通过将配置与 IoC 检测之前获取的备份进行比较，确保配置未被篡改。
3. 更改凭证：更新所有托管设备的密码和用户敏感数据。
4. 隔离受感染的系统：将受感染的 FortiManager 系统与互联网隔离，并将其配置为离线模式，以便与新设置进行比较。

参考来源：Fortinet FortiManager RCE zero-day Flaw Exploited in-the-wild

***END***

阅读推荐

[【安全圈】香港政府禁用WhatsApp、微信、Gmail和Google Drive等](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065529&idx=1&sn=c36a7b5e69e4053fb0ed21e733df2fa7&chksm=f36e62b9c419ebafb71155e1e54ba6f677aaff35040815ad1866d7a978264104fbef5159a438&scene=21#wechat_redirect)

[【安全圈】数据库空口令造成数据泄露，郑州两公司被罚！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065529&idx=2&sn=c4a633763780f3e3c8da1b7bf671c583&chksm=f36e62b9c419ebaf6f1e03e75ee772b74e29b0f66af2aec7d6680a5c4480a21860e96dba2fb2&scene=21#wechat_redirect)

[【安全圈】苹果建议将SSL/TLS证书有效期从398天缩短到45天](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065529&idx=3&sn=cd192f18c226986b4880b3ea3590c13e&chksm=f36e62b9c419ebaf4cf852d9d0c9b42c739d2ca0eed9cb741da86ec633a35f6e276161833207&scene=21#wechat_redirect)

[【安全圈】处理用户个人数据违规，LinkedIn 领英被罚3.1 亿欧元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065529&idx=4&sn=fc2bd539a8d9c079a4349f54fa7e63c8&chksm=f36e62b9c419ebaf31b7798ea6609292008691b4cbac0279e8e0be887a43049145d72546a354&scene=21#wechat_redirect)

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