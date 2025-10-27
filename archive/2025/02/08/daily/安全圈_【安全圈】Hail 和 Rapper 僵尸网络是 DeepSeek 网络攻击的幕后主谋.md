---
title: 【安全圈】Hail 和 Rapper 僵尸网络是 DeepSeek 网络攻击的幕后主谋
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067692&idx=1&sn=a6e07f45327351c84ccc70652f2e8f8e&chksm=f36e7b2cc419f23aa1fca971c8a6ca3064d84e4246102acab4c166e88b7dc75cb068d9b6806c&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-08
fetch_date: 2025-10-06T20:47:04.891240
---

# 【安全圈】Hail 和 Rapper 僵尸网络是 DeepSeek 网络攻击的幕后主谋

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WLEt5uJRnP64ZLplR0K2ySdrAM3RdPKsJMjxupb0regbWF976qFHySw/0?wx_fmt=jpeg)

# 【安全圈】Hail 和 Rapper 僵尸网络是 DeepSeek 网络攻击的幕后主谋

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

DeepSeek

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WuNncianhp7pkqGU3Js2KGgFWabIHMGGZPic7aQibI2NRJ5hiaCiad2fPJRg/640?wx_fmt=jpeg&from=appmsg)

DeepSeek推出不到一个月，就陷入了网络安全风暴的中心。

该公司于 2025 年 1 月 20 日推出了其首款 AI 模型 DeepSeek-R1，但一直在努力应对严重的网络攻击，这些攻击导致公司运营中断并延迟了新用户注册。

这些涉及僵尸网络 HailBot 和 RapperBot 的攻击引起了整个科技行业的警惕，他们意识到网络威胁日益复杂化。

## **DeepSeek 的迅速崛起**

DeepSeek成立于 2023 年底，随着 DeepSeek-R1 模型的发布，它迅速引起了全球关注。该模型实现了与 OpenAI 的 ChatGPT 相当的 AI 性能，但成本仅为后者的一小部分（不到 600 万美元）。

通过利用不太先进的芯片，DeepSeek 与竞争对手相比将运营成本降低了 50 倍。

此外，该公司决定将 AI 开源，这进一步提升了其受欢迎程度，导致其在推出后的几天内下载量达到数百万次。然而，这种快速的成功也使其成为网络犯罪分子的目标。

### **网络攻击时间表**

针对 DeepSeek 的攻击始于1 月初，并在月底大幅升级。以下是事件的详细时间表：

1 月 27 日：DeepSeek 宣布由于其基础设施遭受“大规模恶意攻击”，将暂停新用户注册。

1 月 28 日：网络安全公司 Wiz.io报告称，与 DeepSeek 相关的 ClickHouse 数据库被泄露。该数据库包含敏感用户数据，包括聊天记录和 API 密钥。不过，此次泄露被认为与正在进行的攻击无关。

1月29日：《环球时报》披露，DeepSeek自1月初开始频繁遭受DDoS攻击，这些攻击利用反射放大技术，并伴有HTTP代理攻击和来自美国IP地址的暴力破解尝试。

1 月 30 日：XLab 的一份报告披露，最新一波攻击的幕后黑手是两个 Mirai 僵尸网络变种HailBot和 RapperBot。这两个僵尸网络利用 16 个命令和控制(C2) 服务器和超过 100 个 C2 端口发起协同攻击。

## **攻击背后的僵尸网络**

据 ANY.RUN报道，破坏 DeepSeek 运营的两个僵尸网络是臭名昭著的 Mirai 僵尸网络的复杂变种：

### **冰雹机器人**

HailBot 擅长 DDoS 攻击，利用华为某些设备中的漏洞（例如CVE-2017-17215）。通过入侵各种设备，HailBot 可以发起大规模拒绝服务攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WpRsbmZwsBZMZtB3PrNqWodHKZcXoZFaSUQWoKx9FIf2BLSG935TdGQ/640?wx_fmt=jpeg&from=appmsg)

使用 ANY.RUN 的交互式沙箱进行分析 表明，HailBot 通过可检测的网络流量模式与其 C2 服务器建立连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WmOiatHjrSnwG7fia2RNOWMMe6TbStSKQ3t1LHVY6opYnVU5CuJG2JycA/640?wx_fmt=png&from=appmsg)

*ANY.RUN 检测到 HailBot 的网络连接*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WsDG9MhC0b6vvg1Uf0PTlWEjPB5haD4POx4drre3W5oxdhvMZATrAOA/640?wx_fmt=jpeg&from=appmsg)

*用于检测 HailBot 的 C2 活动的 Suricata 规则*

### **RapperBot**

RapperBot 通过SSH 暴‍力攻击进行传播，其标识为字符串“SSH-2.0-HELLOWORLD”。一旦它攻陷了设备，就会通过替换 SSH 密钥并创建名为“suhelper”的超级用户帐户来确保持续访问。

此外，RapperBot 还通过 XMRig Monero 矿工提供加密劫持功能，使其能够在受感染的设备上挖掘加密货币。

沙盒分析显示，RapperBot 在三分钟内产生了近 140,000 次网络连接尝试，这一惊人的数量凸显了其破坏性潜力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljaNLVWGwz8Zwiaic4bSicpe1WH44QpCRyM8iaFJKuue9VFvlT14VvGC9y2uLzYEaOSdiaBHD84rX4OTibA/640?wx_fmt=png&from=appmsg)

*RapperBot 在三分钟内尝试的连接数量达到 139,405*

DeepSeek 遭受的网络攻击清楚地提醒人们依赖数字基础设施的公司所面临的脆弱性。

有了 HailBot 和 RapperBot 等僵尸网络作为服务提供，即使是技术知识有限的攻击者也可以发动毁灭性的攻击。

对于 DeepSeek 这样的人工智能驱动型企业来说，此类中断可能会导致服务中断、数据泄露和客户信任度下降。

DeepSeek 的遭遇凸显了快速技术进步的前景和危险。虽然其创新的人工智能模型颠覆了整个行业，但它也吸引了复杂的网络威胁，这些威胁可能会破坏其成功。

随着网络安全专家进一步分析这些事件，全球各地的组织必须对不断演变的威胁保持警惕。

事实证明， ANY.RUN 的 Interactive Sandbox等工具在识别和分析 HailBot 和 RapperBot 等恶意软件方面具有巨大价值。通过利用此类技术，公司可以更好地保护其数字生态系统免受未来类似攻击。

来源：https://cybersecuritynews.com/hail-and-rapper-botnet-is-the-mastermind-behind-the-deepseek-cyberattack/#google\_vignette

***END***

阅读推荐

[【安全圈】PyPI 上的信息窃取恶意软件冒充了 DeepSeek AI 工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=1&sn=87a028f93da64d77ab88febfae2b2d56&scene=21#wechat_redirect)

[【安全圈】2024 年勒索软件支付额下降 35%，总额达 813,550,000 美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=2&sn=20f95ef580e0ec24f8d83012372886ab&scene=21#wechat_redirect)

[【安全圈】恶意 Go 软件包利用模块镜像缓存实现持久远程访问](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=3&sn=0a2ed43f7e7eb5e16bbf8a4cf07d0964&scene=21#wechat_redirect)

[【安全圈】研究人员发现新方法防御 AI 模型的通用越狱攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=4&sn=027c0126ec6f44288fe766c11d208124&scene=21#wechat_redirect)

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