---
title: 【安全圈】MuddyWater 黑客组织通过鱼叉式钓鱼向中东多部门传播 RustyWater 远程木马
url: https://mp.weixin.qq.com/s/UjC8UexQjVcZBdO-nai-Aw
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:29:45.684190
---

# 【安全圈】MuddyWater 黑客组织通过鱼叉式钓鱼向中东多部门传播 RustyWater 远程木马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jY4ia5HygPdPicEBrWJ5UbID0YNAvcWqMmBekiaUaTpqAo9RvoF9jC5tsicQ/0?wx_fmt=jpeg)

# 【安全圈】MuddyWater 黑客组织通过鱼叉式钓鱼向中东多部门传播 RustyWater 远程木马

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

被称为MuddyWater的伊朗黑客组织近日被指发动了一场针对中东地区外交、海事、金融及电信实体的鱼叉式钓鱼攻击，其使用的是一款**基于Rust语言、代号为RustyWater的植入程序**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jYibQsicic5KXNpd1FQGBIoBSWaicnVewiawe7MILJsNpvaprKicBzaVqpiaDAg/640?wx_fmt=png&from=appmsg)

CloudSEK的研究员Prajwal Awasthi在本周发布的报告中表示：“此次攻击活动利用图标伪装和恶意Word文档，投放基于Rust语言开发的植入程序。该植入程序具备异步命令与控制（C2）通信、反分析、通过注册表实现持久化以及模块化扩展等能力。”

这一最新进展表明MuddyWater的攻击手法持续演变。该组织已逐步但稳步减少对合法远程访问软件作为入侵后工具的依赖，转而采用多样化的定制恶意软件库，包括Phoenix、UDPGangster、BugSleep和MuddyViper等工具。

**该黑客组织被评估隶属于伊朗情报与安全部，其活动至少可追溯至2017年。**

传播RustyWater的攻击链较为直接：伪装成网络安全指南的鱼叉式钓鱼邮件附带一个Microsoft Word文档。当受害者打开文档时，会收到“启用内容”的提示，一旦执行，便会激活一个负责部署Rust植入程序的恶意VBA宏。

RustyWater会收集受害者计算机信息、检测已安装的安全软件、通过Windows注册表项建立持久化，并与命令与控制（C2）服务器（”nomercys.it[.]com”）建立联系，以执行文件操作和命令。

值得注意的是，Seqrite Labs在上月底曾报告RUSTRIC被用于针对以色列的信息技术（IT）公司、管理服务提供商（MSP）、人力资源及软件开发公司的攻击活动中。这家网络安全公司将该活动追踪命名为UNG0801和Operation IconCat。

CloudSEK指出：“从历史手法看，MuddyWater一直依赖PowerShell和VBS加载程序进行初始入侵和后续操作。此次引入基于Rust语言的植入程序，标志着其工具链向更结构化、模块化和低噪声的远程访问木马能力显著演进。”

***END***

阅读推荐

[【安全圈】BreachForums论坛数据库32.4万个账户泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=1&sn=47a2ea7b05c99c8d23e9b8e6fb8ab229&scene=21#wechat_redirect)

[【安全圈】Meta澄清Instagram“密码重置风暴”非发生数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=2&sn=23f8372e701cf483b7cf976c0b207268&scene=21#wechat_redirect)

[【安全圈】恶性 Chrome 扩展盗窃用户信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=3&sn=b285a1738ee7ba582e9647f76afac35a&scene=21#wechat_redirect)

[【安全圈】2025年中国十大宕机事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073647&idx=1&sn=16fab3921adf37bcd4042f3c44594ffc&scene=21#wechat_redirect)

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