---
title: 突发！俄罗斯科技巨头Yandex内部源代码全部泄露
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507640&idx=1&sn=e19d613e7c93ab4a896e5c32f8811076&chksm=ebfa9998dc8d108ea4f87bdb2846ca25eadabe4cf6be27b6bea7ad9cac8388a329e2cdb543d2&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-01-29
fetch_date: 2025-10-04T05:08:12.435675
---

# 突发！俄罗斯科技巨头Yandex内部源代码全部泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7upU3wxEsibzZicicWgU3ibWG7wJZpfZ1OhF21nZYTzYoEvPibN2puTO1cqD2h6JlFcCw5dXvaoB1tMe4g/0?wx_fmt=jpeg)

# 突发！俄罗斯科技巨头Yandex内部源代码全部泄露

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7upU3wxEsibzZicicWgU3ibWG7wibehbsHlq6nAg8JJzcY3Qy9BDwFgcd1JBhdFj8gp93iaVPSWyP45MicicA/640?wx_fmt=jpeg)

**这批据称为Yandex前员工2022年7月从公司窃取，总计44.7GB，包含了该公司除反垃圾邮件规则之外的全部源代码；**

****Yandex前技术主管分析，**此次数据泄露的动机与政治有关，窃取数据的这位恶意员工并未试图将代码出售给商业竞争对手；**

**泄露内容不包含任何客户数据，因此不会对用户隐私或安全构成直接风险，也不会导致专有技术外流，但增加了黑客暴露风险。**

前情回顾·**俄罗斯网络威胁态势**

* [乌克兰“网军”入侵俄罗斯央行，公布大量敏感数据](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247506718&idx=1&sn=8ce3ed8b25ddf2a100d4be4184a0c79c&chksm=ebfa9c3edc8d1528b9a5fb8bf623f887deeef7eac8f9dd14ba540b5415d9ada11ff6de8e4b41&scene=21#wechat_redirect)
* [恶意黑客“操纵”网约车订单，在俄罗斯首都制造交通拥塞](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247505804&idx=1&sn=d55dfca151a5b17cbb6ff61485c14d4f&chksm=ebfa90acdc8d19ba25f97e690282cd8e6f1ad7320725d8d32f2c0e4612ff07a5500ecb2983fc&scene=21#wechat_redirect)
* [俄最大银行遭到最严重DDoS攻击，普京称正经历“信息空间战争”](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247503110&idx=1&sn=92d0866b7f56e30c17673068fd8271b2&chksm=ebfa8a26dc8d03300c510d44e068d400c2a78298254fdc8beca0e9fb1ef3db1ea8306cab4129&scene=21#wechat_redirect)

安全内参1月28日消息，俄罗斯最大的IT科技公司之一Yandex的源代码仓库据传遭到前员工窃取，相关数据已在某个流行黑客论坛上以BT种子形式泄露。

1月25日，泄密者公开发布了一条磁力链接，宣称这是“**Yandex git sources**”，包含了2022年7月从Yandex公司窃取的**44.7 GB**文件。据称，**这批数据包含了该公司除反垃圾邮件规则之外的全部源代码**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7upU3wxEsibzZicicWgU3ibWG7wqhOtj2yOiaplI4rwianp7tSficNdEcF5WTEOpeEFpEYMWy594JYkB05rA/640?wx_fmt=png)

*图：泄露在黑客论坛上的Yandex代码仓库*

软件工程师Arseniy Shestakov分析了泄露的Yandex Git代码仓库，并表示其中包含关于以下产品的技术数据和代码：

* Yandex搜索引擎与索引机器人
* Yandex Maps
* Alice (AI助手)
* Yandex Taxi
* Yandex Direct (广告服务)
* Yandex Mail
* Yandex Disk (云存储服务)
* Yandex Market
* Yandex Travel (旅游预订平台)
* Yandex360 (办公服务)
* Yandex Cloud
* Yandex Pay (支付处理服务)
* Yandex Metrika (互联网分析)

Shestakov还在GitHub上共享了泄露文件的目录列表，感兴趣的读者可以具体查看有哪些源代码遭到窃取。
（http://gist.github.com/ArseniyShestakov/53a80e3214601aa20d1075872a1ea989）

“**其中至少包含部分API密钥，但它们可能仅用于测试部署**。”Shestakov在谈到泄露数据时说。

Yandex官方给外媒的声明中表示，**他们的系统并未遭受黑客入侵，泄露源代码仓库的是一名前雇员**。

> “Yandex并未遭受黑客入侵。我们的安全服务从公共域的内部仓库中发现了代码片段，但内容**与Yandex服务中的当前代码仓库版本不同**。
>
> 代码仓库是用于存储和使用代码的工具。大多数公司都通过这种内部仓库的方式使用代码。
>
> 代码仓库的作用在于处理代码，而非存储个人用户数据。我们正对源代码片段外泄的原因开展内部调查，但并未发现用户数据或平台性能面临任何威胁。”
>
> ——Yandex公司

**源代码泄露将内部架构暴露于黑客**

外媒BleepingComputer与Yandex公司前高级系统管理员、开发副主管兼技术传播总监Grigory Bakunov讨论了此次泄露事件。Bakunov对泄露的代码内容非常熟悉，曾在2002年至2019年期间在这家俄罗斯科技巨头工作。

Bakunov解释称，**此次数据泄露的动机与政治有关，窃取数据的这位恶意员工并未试图将代码出售给商业竞争对手**。

这位前高管补充道，**泄露内容不包含任何客户数据，因此不会对Yandex用户的隐私或安全构成直接风险，也不会导致专有技术外流**。

> Yandex使用了名为“Arcadia”的单一仓库结构，但也有一部分服务不使用该结构。此外，即使只是构建服务，也需要大量内部工具和专业知识，因为这个并不适用标准构建程序。
>
> 泄露的代码仓库仅包含代码内容，另一重要部分数据并不在其中。神经网络的模型权重等关键信息也都没有，所以几乎无法实际使用。
>
> 尽管如此，仍有许多有趣的文件，比如“blacklist.txt”文件可能会暴露正在运行的服务。

但Bakunov在采访中证实，**黑客确实有可能通过泄露代码发现安全漏洞，并实施有针对性的漏洞利用行为**。Bakunov认为这类状况的发生将只是时间问题。

这位前高管也评论了Yandex的官方回应，称泄露代码虽然可能跟当前工作服务中的代码版本不尽相同，但相似度也许高达90%。

因此，对泄露代码开展全面检查之后，恶意黑客很可能会从Yandex系统中发现可供利用的缺口。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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