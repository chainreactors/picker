---
title: 针对DeepSeek的网络攻击再升级：僵尸网络进场 攻击指令激增上百倍​
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513623&idx=1&sn=d0d49c0d4b6e85b4dd8aacd8623ca272&chksm=ebfaf137dc8d782175c2209f64fe50b91bf2c7ff519b1be99b56d7f5f4f3171fe8cb575f539a&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-31
fetch_date: 2025-10-06T20:10:36.891363
---

# 针对DeepSeek的网络攻击再升级：僵尸网络进场 攻击指令激增上百倍​

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uFbTwibqDggwYpCiaMPaPibjTRsHWvhGhN5SibsAU1UjRtWJDBqgia4bIelBHKbeEiaVLjRZibTjj2iby3oA/0?wx_fmt=jpeg)

# 针对DeepSeek的网络攻击再升级：僵尸网络进场 攻击指令激增上百倍​

安全内参

**关注我们**

**带你读懂网络安全**

**奇安信安全专家：针对DeepSeek的网络攻击再升级，攻击指令激增上百倍。**

1月30日凌晨，即农历大年初二，奇安信XLab实验室监测发现，针对DeepSeek（深度求索）线上服务的攻击烈度突然升级，其攻击指令较1月28日暴增上百倍。XLab实验室观察到至少有2个僵尸网络参与攻击，共发起了两波次攻击。

“最开始是SSDP、NTP反射放大攻击，1月28日增加了大量HTTP代理攻击，今天凌晨开始僵尸网络（botnet）进场了，针对DeepSeek的网络攻击一直在层层加码，攻击手段越来越多，防范难度越来越大，使得DeepSeek面临的安全考验愈发严峻。”奇安信XLab实验室安全专家表示。

# 01

两个变种僵尸网络加入攻击，

指令激增100多倍

XLab实验室通过对DeepSeek持续近1个月的监测发现：攻击模式从最初的易被清洗的放大攻击，升级至1月28日的HTTP代理攻击（应用层攻击，防御难度提升），现阶段已演变为以僵尸网络为主。攻击者使用多种攻击技术和手段，持续攻击DeepSeek。

1月30日凌晨，XLab观察到2个Mirai变种僵尸网络参与攻击，分别为HailBot和RapperBot。此次攻击共涉及16个C2服务器的118个C2端口，分为2个波次，分别为凌晨1点和凌晨2点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiafMs5L7TJx8Utqq8nlH1IiawkrNHvtvccGKW4WmSNZy1Z9wXP4aBkfWQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：部分攻击指令详情

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiaKnyd1AuTFnroic6E6Eq12QtGvscTbz91vBW1plVval4CzLGROicpp2sw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：攻击指令趋势

“僵尸网络的加入，标志着职业打手已经开始下场，这说明DeepSeek面对的攻击方式一直在持续进化和复杂化，防御难度不断增加，网络安全形势愈发复杂严峻。”XLab表示。

# 02

两个僵尸网络的身世揭秘

僵尸网络是由攻击者通过恶意软件感染并控制的设备网络，这些设备被称为“僵尸”或“机器人”。攻击者通过命令与控制（C&C）服务器向这些设备发送指令，执行各种任务，例如向目标服务器同时发起DDoS攻击，持续增加攻击规模和强度，耗尽目标服务器的网络带宽和系统资源，使其无法响应正常业务，最终瘫痪或服务中断。

本次采用的两个僵尸网络分别是HailBot和RapperBot，这两个Botnet常年活跃，攻击目标遍布全球，专业为他人提供DDoS服务。

其中，RapperBot平均每天攻击上百个目标，高峰时期指令上千条，攻击目标分布在巴西、白俄罗斯、俄罗斯、中国、瑞典等地区。具体攻击指令趋势和攻击目标地区分布如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkia5UgFCPL3V0UyiaItvvJUwOd2nm2pKZb1GzKwjCbWwyZltC9nYbIjUfw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

HailBot的攻击比RapperBot更加稳定。平均每天攻击指令上千条、攻击上百个目标。攻击目标分布在中国、美国、英国、中国香港、德国等地区。具体攻击指令趋势和攻击目标地区分布如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/G3LNmiaOGjarhL2ibX0a0yOXlWNLBV4dkiaypmc5K4EHlJyoaau5WuGH0KGsZubhZToDIfL5ZYLMZRHVEE8wtib6Ug/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从两张图不难发现，这两个僵尸网络“接单”频繁，符合典型的“职业打手”特征。XLab安全专家认为，僵尸网络攻击虽然是一种很古老的攻击方式，但依然屡试不爽。“很显然，今天凌晨这一波儿，黑客采购的是专业的网络攻击僵尸网络服务”。

# 03

树大招风？

中国明星企业易被攻击者“眷顾”

DeepSeek推出R1模型后不久，就凭借其性价比、开源及推理能力的提升等方面获得了广泛关注。除夕当天，DeepSeek还推出了新模型，其中Janus-Pro-7B在基准测试中击败了OpenAI。在外网被不少人称为“神秘的东方力量”。

DeepSeek的成功不仅引发了硅谷的震动，更让华尔街陷入了恐慌。就在1月28日，美国芯片巨头英伟达一夜市值蒸发5900亿美元，合4.3万亿人民币，纳斯达克综合指数跌3.07%，台积电、博通公司、超微半导体等科技股也遭遇集体暴跌。美国总统特朗普表示， DeepSeek的崛起应当为美国企业敲响“警钟”，美国公司“需要专注于竞争以赢得胜利”。

每次中国优秀的明星产品或企业崛起之时，总会遭到一些境外不法势力的暗中阻击。上一次是黑神话悟空全球上线后，就遭遇了海外60个僵尸网络大规模攻击，而这次DeepSeek上线以来，也遭遇了包括僵尸网络在内的多轮攻击，攻击方式一直在进化和复杂化。从他们所遭遇的攻击可以看出，随着我国在科技领域的不断崛起，国外黑客的恶意攻击也日益增多。这些攻击不仅可能导致服务中断、数据泄露等严重后果，还可能对我国的科技形象和国际竞争力造成负面影响。因此对于所有企业而言，第一要务就是要加强网络安全防护。

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