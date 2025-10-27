---
title: 【安全圈】全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031161&idx=2&sn=0ad92a203111c8447ed691505935b62c&chksm=f36fe4f9c4186defc5d33e654a6423b20d0f2a7a1af08acc134eed13bdb277df0b9c6defeff2&scene=58&subscene=0#rd
source: 安全圈
date: 2023-03-09
fetch_date: 2025-10-04T09:02:03.539254
---

# 【安全圈】全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZSaoviaStSw60AvWsP61Y033ygDthErEjibQyqkPb5fTYGZHBFGMBmIJbQ/0?wx_fmt=jpeg)

# 【安全圈】全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZS1w62vR7Ct5mFkemLicTl7ATLicmpwXCzHEDtYEukoAyib4h24CZcFGAaA/640?wx_fmt=jpeg)

Emotet恶意软件在沉寂了三个月后，从本周二上午开始再次发送恶意电子邮件，并感染世界各地的设备。

Emotet是一种臭名昭著的恶意软件，通过含有病毒的Word和Excel的电子邮件传播。当用户打开这些文档并启用时，Emotet DLL将被下载并加载到内存中。一旦Emotet被加载，该恶意软件将潜伏等待来自远程命令和控制服务器的指示。

最终，该恶意软件将窃取受害者的电子邮件和联系人，用于后续的Emotet活动或下载额外的有效载荷，例如Cobalt Strike或其他的恶意软件。

虽然Emotet在过去被认为是分布最广的恶意软件，但它已经逐渐放缓，其最后一次恶意邮件活动还是在2022年11月，而且垃圾邮件也仅仅持续了两个星期。

## Emotet在2023年回归

3月7日，网络安全公司Cofense和Emotet追踪小组Cryptolaemus警告说，Emotet僵尸网络再次开始发送恶意电子邮件。

Cofense表示，"我们看到的第一封邮件是在美国东部时间早上7点左右。由于他们需要重建和收集新的证书，目前的恶意邮件的数量还比较低。

攻击者没有像以前的活动那样使用回复链电子邮件，而是利用冒充是发票的电子邮件，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZS41Ud7S9vQW6gcjPfGIfjsdrhNkRR4mpL3icaKFZ8tauOdxtMVYgiaahA/640?wx_fmt=jpeg)

Emotet 钓鱼邮件

这些电子邮件的附件是ZIP压缩包，其中包含Word文档，大小超过500MB。它们被填充了未使用的数据，以使文件更大，这让查杀软件更难扫描和检测到它们是否是包含病毒的。

这些Word文档使用Emotet的'红色黎明'文档模板，提示用户启用文档上的内容才能正确看到它。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZSk1u99kb4CDnvM9NLwN1C7bS7kek1mpcDyiajdHsQFbibnyxcic8kRm9Bw/640?wx_fmt=jpeg)

使用 "红色黎明 "模板的恶意微软Word文档

这些文档包含了乱七八糟的宏，会从被攻击的网站上下载Emotet加载器作为DLL，其中很多是被黑的WordPress博客。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZS2Qic6zfqeaaMsclCykwpFm5nibnrmH0OsD6bjiblmWfCemgiaHngqmB6aA/640?wx_fmt=jpeg)

Emotet Word文档中混乱的恶意宏程序

下载后，Emotet会被保存到%LocalAppData%下的一个随机命名的文件夹，并使用regsvr32.exe启动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZSG6FKibCD8G6mRdVRQRoV09z5XZgxeK9c6L3YSKb6NuzEIzMR5ljTodg/640?wx_fmt=jpeg)

由Regsvr32.exe启动的Emotet加载器

与Word文档一样，Emotet DLL也被填充为526MB，以阻碍杀毒软件对恶意软件的检测能力。

这种规避技术目前来看是成功的，正如VirusTotal扫描显示的那样，在64个引擎中，该恶意软件只被一个安全厂商检测到，该厂商只将其检测为 "Malware.SwollenFile"。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhfmNyl6NiaKr6agNP1TxiaZSxGSfeXlsxYXXopbO70E2mp3ztTsqIw9QcBxOt4AoibibHqKnbibtOsoBw/640?wx_fmt=jpeg)

大型Emotet DLL以逃避检测

一旦运行，恶意软件将在后台运行，等待命令，这可能会在设备上安装更多的有效载荷。这些有效载荷允许其他攻击者远程访问该设备，然后在被攻击的网络中进一步传播。这些攻击通常会导致数据被盗。

Cofense表示，他们现在还没有看到任何额外的有效载荷被安装，该恶意软件目前还只是在为垃圾邮件活动收集数据。

## 微软的调整

虽然Emotet正在重建其网络，但随着微软在最近的调整后，目前的方法可能不会有太大成功。

2022年7月，微软终于在从互联网下载的微软Office文档中默认禁用了宏。

由于这一变化，打开Emotet文件的用户将收到一条信息，说明由于文件的来源不受信任，宏程序被禁用。

ANALYGENCE高级漏洞分析师Will Dormann表示，这一变化也影响电子邮件中保存的附件。对于大多数收到Emotet电子邮件的用户来说，这项功能可以有效的保护他们，除非他们执意要打开附件。

由于微软的这一调整导致其他攻击者不再使用Word和Excel文档，而是滥用其他文件格式，如微软OneNote、ISO图像和JS文件。

这一调整也打乱了Emotet的计划，目前Emotet也开始转向不同的附件类型。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vhJibjlNfV6zncicMyLxptJCIJGcyelX4AsHI4q176nwBUAe6tWT2yCr0A/640?wx_fmt=jpeg)[【安全圈】研究机构披露某购物平台利用漏洞，非法获取竞对信息，阻止用户卸载 APP](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031129&idx=1&sn=0ef375ee19fbac8349168c2a3eeac4b8&chksm=f36fe4d9c4186dcfb046175851735080259d5b44643c7d9f0c8f32d7d1741cc6bc81387ce7c4&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vh3wnhXjU6ehQvr0RPYZFLPJLZiaC5ZHA12LWPkxuibMdHTicsthjkrdvSQ/640?wx_fmt=png)[【安全圈】最新在线版ChatGPT，调用GPT3.5接口，快如闪电！附中文调教指南](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031129&idx=2&sn=b6ded67a78944baf0212577bcd175ca4&chksm=f36fe4d9c4186dcf03356df2636e62c5a6ead4c8c0830ff19f022196e0040457682360c2e867&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vhpiaibMuadwsK2yOJCibiaP25swVXExmrNuw0Jl3DHdJOlYDVKCO1aOGUKQ/640?wx_fmt=jpeg)[【安全圈】西班牙医院遭遇勒索攻击，大量手术和预约检查被迫取消！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031129&idx=3&sn=1ee8d27a5d24cba3d062d11217dcd9dc&chksm=f36fe4d9c4186dcf93b42f2639c72ec94966b80d7a7a48623ecd53221ff18f32c52b3ed5e4eb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgaNMK1XicS1iacM9XWuW90vh0t62bgyQibTcRjdunic4DENtEdkUU8sSCkbBiacsBupBK3jrafVFemJicQ/640?wx_fmt=jpeg)[【安全圈】DoppelPaymer勒索软件组织被欧洲警方查获](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652031129&idx=4&sn=f71acb60308c567533a5ae6c006d7c8c&chksm=f36fe4d9c4186dcfbd8a5427fe218b5de9663780ed7f757e18e51fe1ef3e5ef265504ec32b18&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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