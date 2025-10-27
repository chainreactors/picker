---
title: 【安全圈】VMware vCenter Server 漏洞让攻击者能够执行远程代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064505&idx=2&sn=4f43301ff2f7aea69701f9caee393e63&chksm=f36e66b9c419efaf8abe64f74ac1deebb763a2ad3298be33ecad40d79f7d7eb8c50ee69e6649&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-19
fetch_date: 2025-10-06T18:26:17.504530
---

# 【安全圈】VMware vCenter Server 漏洞让攻击者能够执行远程代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHdQOUTOTj9WxbSmhlc2KdYAd0qwWwZcOWibRKClPURhfpEvQIAYFboeg/0?wx_fmt=jpeg)

# 【安全圈】VMware vCenter Server 漏洞让攻击者能够执行远程代码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

据Cyber Security News消息，VMware 披露了两个影响其 vCenter Server 和 Cloud Foundation 产品的关键安全漏洞，这些漏洞可能允许攻击者执行远程代码并提升权限。该公司敦促客户立即修补受影响的系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHtjbFLiahibic0tYD0K2XEo41KeRFgxtWDliaWApAJGjOG9o7p1mPlxiaXmQ/640?wx_fmt=jpeg&from=appmsg)

其中一个漏洞被追踪为 CVE-2024-38812，是在 vCenter Server 中实施 DCERPC 协议时存在的堆溢出漏洞，CVSS 评分高达 9.8。根据 VMware 的公告，具有网络访问权限的攻击者对易受攻击的 vCenter Server可以通过发送特制网络数据包来触发此漏洞，从而导致远程代码执行。

另一个漏洞被追踪为CVE-2024-38813，属 vCenter Server 中的权限提升缺陷，CVSS 评分7.5，可能允许攻击者通过发送恶意网络数据包将权限升级到 root。

这两个漏洞都会影响 VMware vCenter Server 7.0 和 8.0 版本，以及 VMware Cloud Foundation 4.x 和 5.x 版本。

VMware 已发布修补程序来解决这些缺陷，并强烈建议客户尽快应用这些更新。对于 vCenter Server，用户应尽快升级到8.0 U3b 或 7.0 U3s 版本，Cloud Foundation 客户应应用 KB88287 中引用的异步修补程序。

该公司表示，到目前为止还没有发现任何对这些漏洞的野外利用。但是，鉴于 vCenter Server 在管理虚拟化环境方面的关键性质，这些缺陷可能成为攻击者的诱人目标。

据悉，这两个漏洞由参加中国2024“矩阵杯”网络安全大赛的TZL研究人员发现，并在事后向 VMware 进行了报告。

今年6月，VMware 曾修复了一个类似的 vCenter Server 远程代码执行漏洞 （CVE-2024-37079），该漏洞可通过特制数据包进行攻击。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHTo2hby0p445o089tcsRZb2SHbqicZ80PZzS2mUGB3gBiaPtgEU9qhBHA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHKZNq9KmYMzEBwlcl93l9ibJcObLACoDwvoImY3I74PUhibuPDVYENfnA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHvlZpkwGia9sic96uQotplBa5I1H8rMIqE0Vc9aXrydq2ykhbeLpibrZnQ/640?wx_fmt=jpeg)[【安全圈】表弟遭“表哥”诈骗 1.5 万元，宁夏一起 AI 换脸诈骗案细节曝光](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064483&idx=3&sn=135f9b6a7a9e8fb0dfe2a3f1d997aa90&chksm=f36e66a3c419efb5838d0801b682c02b1319d05e1166218972645e68208c83e9685c315f3473&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylguXyao8qLTDpAhrpWyrGdHArXcdT6ricDHWJ29rrxJP1NJJzf6ANVfb7vo55397oG7OkX458NHwPA/640?wx_fmt=jpeg)[【安全圈】虚拟货币交易发生纠纷，买家起诉后，法院判了](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064483&idx=4&sn=96ffc8a524be62a883fdd3ab09b6382f&chksm=f36e66a3c419efb520c2fdde5d78508f9eb005217d3ace1bc6da8491afc697fa78643d05dc94&scene=21#wechat_redirect)

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