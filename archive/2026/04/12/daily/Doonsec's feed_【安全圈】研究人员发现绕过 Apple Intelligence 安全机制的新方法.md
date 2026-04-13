---
title: 【安全圈】研究人员发现绕过 Apple Intelligence 安全机制的新方法
url: https://mp.weixin.qq.com/s/LwYrbocojsSEOaI0sNeMgg
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:54:48.932495
---

# 【安全圈】研究人员发现绕过 Apple Intelligence 安全机制的新方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFvj7JUYWhHunBEia4KkWiaK0gsakHG0ib0D5CzWLgFSy81uw5VxicZqWrpnPGb484dq6ruEvGOpnfaWe80eMrZN1tFGDrh45CyTDA/0?wx_fmt=jpeg)

# 【安全圈】研究人员发现绕过 Apple Intelligence 安全机制的新方法

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyG1WzNTW3uYzGAEJhUfgicmQUX556MpwxugLpibSI6fnxzaEzDy5KqgvP1mLkkClicIPP4ZEzdGYe6IFjvcuwpmRWT7EQWxrbBpL8/640?wx_fmt=png&from=appmsg)

RSAC研究人员发现一种高成功率绕过苹果Apple Intelligence AI安全协议的方法。

Apple Intelligence是深度集成于iOS、iPadOS和macOS的个人智能系统，结合生成式AI与个人上下文。它主要通过紧凑的端侧大语言模型在苹果芯片上直接处理任务，利用用户独特上下文（消息、照片和日程）为系统级写作工具和Siri等功能提供支持。对于更复杂的推理，它通过私有云计算将请求卸载至苹果专用云基础设施上的更大基础模型。

RSAC研究团队对Apple Intelligence进行了安全审查，试图绕过端侧大语言模型的输入输出过滤器（用于阻止恶意输入和防止不良输出）及内部防护栏以影响其行为。

为此，他们结合两种对抗技术。**第一种是Neural Execs——一种已知的提示注入攻击，使用”乱码”输入欺骗AI执行攻击者定义的任意任务，这些输入作为通用触发器无需针对不同载荷重新制作。**

**第二种方法是Unicode操纵。**研究人员通过将恶意输出文本反向书写并使用Unicode从右至左覆盖功能，成功绕过内容限制。”本质上，我们将恶意/冒犯性英文输出文本反向编码，使用Unicode技巧强制大语言模型正确渲染，”研究人员解释。

结合两种方法可使攻击者强制端侧Apple Intelligence大语言模型生成冒犯性内容，或更关键地，操纵与Apple Intelligence集成的第三方应用中的私有数据和功能，如健康数据或个人媒体。

该攻击经100个随机提示测试，成功率达76%。研究人员估计，10万至100万用户已安装可能易受此类攻击的应用。

“RSAC估计，截至2025年12月，消费者手中已有至少2亿台支持Apple Intelligence的设备，苹果应用商店已出现使用Apple Intelligence的应用——因此它已成为高价值目标，”研究人员指出。

苹果于2025年10月接到通知，据RSAC研究，防护措施已在近期iOS 26.4和macOS 26.4中推出。研究人员尚未发现恶意利用的证据。

***END***

阅读推荐

[【安全圈】久病成黑客？男子自学编程，与妻子合作“代抢”医院号源，涉案金额超57万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=1&sn=9a045324f1ff78774756b8efb57efde4&scene=21#wechat_redirect)

[【安全圈】加密货币 ATM 巨头 Bitcoin Depot 遭黑客入侵，损失 366 万美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=2&sn=8876814d45a7894a0eec1623c4593149&scene=21#wechat_redirect)

[【安全圈】欧洲铁路公司 Eurail 数据泄露，30 万人受影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=3&sn=d3863852a3157fbc5b9a5430b0b66768&scene=21#wechat_redirect)

[【安全圈】老板倒卖26万条客户信息获利600万](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075510&idx=1&sn=b41c183cb3e61e1068a583217c6e8b2d&scene=21#wechat_redirect)

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