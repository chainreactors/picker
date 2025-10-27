---
title: 【安全圈】研究人员入侵苹果新 USB-C 控制器
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067321&idx=3&sn=0baa019796225a8a1f3681f24e502952&chksm=f36e79b9c419f0afe0189b75ee69031de31213c10e55e69f5d89c92abcaabad3e78d2661af5f&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-14
fetch_date: 2025-10-06T20:11:12.410686
---

# 【安全圈】研究人员入侵苹果新 USB-C 控制器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljiazuFMNGnUe5Ms2UhJ2sTxib7ksXmnOWC78pic8jKc1aV7ia8ibq64cCia8ibDprPicUq2pvdm5vjYQ6r5A/0?wx_fmt=jpeg)

# 【安全圈】研究人员入侵苹果新 USB-C 控制器

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljiazuFMNGnUe5Ms2UhJ2sTxL75q6t9iakNU6NdeklCk4ZphiaAntZdAVYINrokuAhVicGFOvQ9GknZcA/640?wx_fmt=jpeg&from=appmsg)

安全研究人员成功破解了 Apple 专有的 ACE3 USB-C 控制器。这款随 iPhone 15 和 iPhone 15 Pro 推出的芯片代表了 USB-C 技术的重大飞跃，可处理电力传输并充当可访问关键内部系统的复杂微控制器。

尽管苹果加强了安全措施，但研究人员仍采用先进的技术绕过其防御措施，这引发了人们对设备安全性和潜在漏洞的担忧。

德州仪器为苹果制造的 ACE3 控制器远不止是一个标准的 USB-C 芯片。它运行完整的 USB 堆栈并连接到内部设备总线，例如 JTAG 应用处理器和 SPMI 总线。

这些功能使其成为 Apple 生态系统不可或缺的一部分，同时也是安全研究人员的有吸引力的目标。

与其前身 ACE2 不同，ACE3 具有个性化的固件更新、禁用的调试接口和经过加密验证的外部闪存，而 ACE2 更容易利用软件漏洞和调试接口进行攻击。

### **破解苹果的新款 USB-C 控制器**

###

研究人员首先分析了 ACE2，以了解其架构和漏洞。他们利用 MacBook 上的硬件漏洞和自定义 macOS 内核模块，成功对 ACE2 进行了持续的后门攻击。

然而，由于 ACE3 强大的安全增强功能，它带来了更严峻的挑战。

为了克服这些障碍，该团队采用了逆向工程、射频侧信道分析和电磁故障注入相结合的方法。

这些技术使他们能够在 ACE3 芯片上执行代码。通过仔细测量芯片启动过程中的电磁信号，他们确定了固件验证发生的精确时刻。

在这个关键时刻，他们使用电磁故障注入，成功绕过验证检查，并将修改后的固件补丁启动到芯片的 CPU 中。

这项突破对设备安全具有重大意义。ACE3 与内部系统的集成意味着，如果对其进行破坏，可能会导致不受限制的越狱或持久固件植入，从而破坏主操作系统。

恶意行为者可以利用此类漏洞来未经授权访问敏感数据或控制设备。

这项研究还强调了硬件黑客技术日益复杂化。随着苹果等公司实施更严格的安全措施，传统的基于软件的攻击变得越来越无效。

旁道分析和故障注入等高级物理攻击表明，坚定的攻击者仍然可以找到方法来利用高度安全的系统。

虽然这次黑客攻击凸显了苹果硬件设计中的潜在漏洞，但它也为进一步研究保护 ACE3 等定制芯片的安全开辟了途径。

苹果可能需要探索针对物理攻击的额外对策，例如改进屏蔽或更强大的故障检测机制。

目前，这一发展提醒我们，没有哪个系统能够完全免受攻击。随着技术的进步，我们的安全方法也必须随之进步——无论是防御机制还是围绕漏洞披露的道德考虑。

来源：https://cybersecuritynews.com/apples-new-usb-c-controller-hacked/

***END***

阅读推荐

[【安全圈】腾讯协助警方破获木马盗窃游戏账号案，涉案金额超 3000 万](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=1&sn=e99889dcbf4e15a2ad7a2217e3f850a3&scene=21#wechat_redirect)

[【安全圈】勒索木马 Banshee 针对苹果 macOS 下手，冒充安全组件躲避检测](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=2&sn=72944b1de7bb9205840492e28ba936b4&scene=21#wechat_redirect)

[【安全圈】卡西欧遭勒索软件攻击？8500人数据被窃取！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067304&idx=3&sn=1f094579cd41cb8e1f1583f6eb592503&scene=21#wechat_redirect)

[【安全圈】江苏一男子利用小程序Bug逃匿28万加油费，法院判了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067274&idx=1&sn=5bef640b5980a10e736f5e8b28bb6773&scene=21#wechat_redirect)

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