---
title: 挖矿加DDoS：奇安信X实验室发现 “8220”挖矿团伙推出新型攻击工具
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247510966&idx=2&sn=36f3bc58809983007325b91babd97069&chksm=ea665cc1dd11d5d7352c9d47d94da4b2e88bf389cace03ee9c9bf7e3187224e16eb5c874398e&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-07-06
fetch_date: 2025-10-06T17:43:41.836525
---

# 挖矿加DDoS：奇安信X实验室发现 “8220”挖矿团伙推出新型攻击工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9vNZej1YXXqZgblp1wFib1r625PdxkC1qXOiabhvT45u0Je84HoI5kicxbwuOQ6308xkLZHepqu084w/0?wx_fmt=jpeg)

# 挖矿加DDoS：奇安信X实验室发现 “8220”挖矿团伙推出新型攻击工具

奇安信威胁情报中心

![](https://mmbiz.qpic.cn/mmbiz_png/jrGLLBlMflC5HbKmF9clLBtYn5YKDfX4vo0nXKH54rFJovibEkO0mH0z5tDKjibPIoxMSHmeVPDbQrqAeP2KrJgw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other)

服务器中招后既要挖矿，又要被拖入僵尸网络发动DDos攻击，彻底沦为黑客的赚钱机器。**近日，奇安信X实验室揭露了一款名为"k4spreader"的新型恶意软件。**这是臭名昭著的"8220"挖矿团伙最新开发的攻击工具，它不仅能够轻松躲避主流杀毒软件的火眼金睛，还具备强大的隐蔽性和多功能攻击能力。"k4spreader"近三个月非常活跃，仅研究人员监测到的数据，访问量已有80多万。

![](https://mmbiz.qpic.cn/mmbiz_png/OwOE73ibiaPBqxne79c69HWOyJiclZ6h72OJRdVKXksR2iaIsibUvQbxnCzTbp3ptia8bNfevZicAl5o5Tq5BoIUjHiaxQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other)

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjaqlF0iblOXZwDJfRwECibEfqOFA6dVicw8ibicecIsMX0H1ibWntkFbn5lgMEYAQRxbtUIQBiahc0SnS33EA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

安全研究人员介绍，"k4spreader"的出现标志着网络攻击手段又向前迈进了一大步。这款恶意软件采用了多层加密和变形技术，能够在受害者的计算机上悄无声息地建立持久控制。更令人担忧的是，它充当了一个"跳板"，随后下载僵尸网络程序、挖矿程序等对主机进行控制和恶意利用。

深入分析后发现，"k4spreader"主要用于部署两种恶意软件：一是名为"Tsunami"的僵尸网络程序，二是被称为"PwnRig"的加密货币挖矿工具。"Tsunami"能够将被感染的计算机变成"僵尸"，组建成一个庞大的网络，随时可能发动分布式拒绝服务（DDoS）攻击，对互联网基础设施造成严重威胁。而"PwnRig"则会在受害者不知情的情况下，偷偷利用计算机资源进行加密货币挖矿。

"k4spreader"的强大之处不仅在于其攻击能力，更在于其精心设计的生存策略。研究人员发现，这款恶意软件具有多种反检测机制，并能够清除系统中其他的恶意程序，确保自己独占"地盘"。它还能通过修改系统配置文件、创建系统服务等方式实现持久化，即使在系统重启后仍能继续运行。这种"寄生"能力让"k4spreader"成为一个难缠的"数字蛀虫"。

更值得警惕的是，"k4spreader"还在不断开发和进化中。目前已经出现三个不同的版本，每个版本在迭代后都在功能和隐蔽性上有所提升。这表明"8220"团伙正在积极开发和完善这个工具，未来可能会出现更加难以检测和清除的变种。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSTev7u7LEMcSo3ve1RC29WohATAeES1mKkCgNMklkRvxpofgQOmKDJBufGAtNPBvicTdlOdTlstJPoCBIX0wQg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

"8220"挖矿团伙并非默默无闻之辈。该黑客组织自2017年开始活跃。该团伙最初以利用服务器漏洞进行非法加密货币挖矿而闻名，近年来，随着加密货币市场的起伏，"8220"团伙的活动范围也在不断扩大。从最初的单纯挖矿，到现在涉足DDoS攻击网络的构建,该团伙的野心也在不断扩大。"k4spreader"的出现，不仅标志着"8220"团伙技术实力的提升，也反映出当前网络安全形势的严峻性。随着数字化进程的不断推进，网络攻击的手段也在不断升级，攻击者们正在开发越来越复杂、越来越难以检测的恶意软件。这对网络安全防御提出了更高的要求。

![](https://mmbiz.qpic.cn/mmbiz_png/62Chicia6tFmkMyeqf143PxnGcgLNuRicL12IHTWAC5jGebXXj4EzOTzrNHkfOUf67StS2XyHaO7Y3cNicZ99icbrlQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other)

☞相关推荐：[《8220挖矿团伙的新玩具：k4spreader》](http://mp.weixin.qq.com/s?__biz=MzkxMDYzODQxNA==&mid=2247483741&idx=1&sn=b19938db22e5663517843c0cf500eebb&chksm=c1292d7cf65ea46a030579627f40c0632557333053ffec85ad2c3bf6f48cd849213aedfe2421&scene=21#wechat_redirect)

☞更多技术细节可点击阅读原文查看

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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