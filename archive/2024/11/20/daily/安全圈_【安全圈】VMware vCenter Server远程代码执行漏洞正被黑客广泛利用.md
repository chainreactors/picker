---
title: 【安全圈】VMware vCenter Server远程代码执行漏洞正被黑客广泛利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066082&idx=4&sn=c7244d3c2cda936e8c968cf0a2ade6d0&chksm=f36e7d62c419f474201413fc6e1edcc5c024cfb6fa12a9adf16b49526e98689324bb9aa57fd0&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-20
fetch_date: 2025-10-06T19:19:12.273908
---

# 【安全圈】VMware vCenter Server远程代码执行漏洞正被黑客广泛利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliae9FZ00ZQA2uZc7wMoOZCG2ib7hjxxFtTMMWVRibfCATiaIjXbcMKmgZHKNMDebcoUNdgwc7uff9ibpw/0?wx_fmt=jpeg)

# 【安全圈】VMware vCenter Server远程代码执行漏洞正被黑客广泛利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据Cyber Security News消息，11月18日，博通发布了紧急警告，称 VMware vCenter Server 中的两个关键漏洞现在正被广泛利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliae9FZ00ZQA2uZc7wMoOZCGQHvhL1kXlm7erXgCUQVcgzUibvb2OOCaLicuodsBQNaBHze9cjd4fQzw/640?wx_fmt=jpeg&from=appmsg)

这两个漏洞包含一个CVSS评分达9.8分的远程代码执行 （RCE） 漏洞，被跟踪为 CVE-2024-38812。该漏洞源于 vCenter Server 实现 DCE/RPC 协议时的堆溢出问题，具有网络访问权限的攻击者可以通过发送特制数据包来触发此漏洞，从而可能导致远程代码执行和整个系统受损。

第二个漏洞被跟踪为CVE-2024-38813， CVSS 评分7.5，允许攻击者通过发送恶意构建的网络数据包将权限升级到根权限。

这两个漏洞最初是由 TZL 团队的研究人员 zbl 和 srs 在中国 2024 年矩阵杯黑客大赛期间发现并报告，受到影响的版本包括 VMware vCenter Server 7.0 和 8.0 版本以及 VMware Cloud Foundation 4.x 和 5.x 版本。

11月18日，博通发布了最新安全公告，指出 CVE-2024-38812 和 CVE-2024-38813 都已在野外被积极利用。鉴于这些漏洞的严重性和主动利用，博通强烈建议使用受影响的VMware 产品要立即应用最新的安全更新。

博通于 2024 年 9 月 17 日首次发布了针对这些漏洞的补丁，但值得注意的是，该公司在10月21日再度发布了补丁更新，指出先前的修复并不完整，强烈建议用户立刻更新最新的补丁。

目前最新的受影响产品修复版本包括：

VMware vCenter Server 8.0：需更新到 8.0 U3d 版本

VMware vCenter Server 7.0：需更新到 7.0 U3t 版本

VMware Cloud Foundation 5.x：将异步修补程序应用于 8.0 U3d版本

VMware Cloud Foundation 4.x：将异步修补程序应用于 7.0 U3t版本

这一事件凸显了及时应用安全更新的重要性，尤其是对于 VMware vCenter Server 等关键基础架构组件。因此建议企业组织审查自身的VMware 部署，应用必要的补丁，并监控是否有任何泄露迹象。鉴于存在远程代码执行和权限提升的可能性，任何可能已暴露的系统都应经过全面的安全评估。

参考来源：VMware vCenter Server RCE Vulnerability Actively Exploited in Attacks

##

***END***

阅读推荐

[【安全圈】QQ/TIM大面积崩溃 有人发恶意代码到群里 请清理群聊记录](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=1&sn=45e791fe7d52666b15728e9809e42f49&chksm=f36e7d4fc419f4591dd287f8fd86f01f3ac0d8e35a67d2a82292f8c331025ede15735774e9ae&scene=21#wechat_redirect)

[【安全圈】黑客在瑞士发放纸质钓鱼邮件来传播恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=2&sn=709c586c8880dc4f98a07670bd50e0d2&chksm=f36e7d4fc419f459a7322ae54c4ba8995f6d06a0a24418a8caabc119966ba2cb04ff8531ed79&scene=21#wechat_redirect)

[【安全圈】研究人员曝光利用 Microsoft Visio 文件的两步式网络钓鱼技术](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=3&sn=fd139cbc62a8b20cf6ae19f09c9b869f&chksm=f36e7d4fc419f459b22649e69eb0e69a8f7ce49a075b11ead7d774157b77dfd51ba8497355f6&scene=21#wechat_redirect)

[【安全圈】LodaRAT 再次袭击：新活动以更新的功能针对全球受害者](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066063&idx=4&sn=759487cd86deebbcd134eb38cc19b103&chksm=f36e7d4fc419f4594c9075760e8c7e7a3eb669cc40768e68d15c266778283a77244a1e06078d&scene=21#wechat_redirect)

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