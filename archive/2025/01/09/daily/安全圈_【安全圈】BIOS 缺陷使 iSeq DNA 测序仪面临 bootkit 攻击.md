---
title: 【安全圈】BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=4&sn=02eb8fe14f312d38658f3ad26fcd4cb9&chksm=f36e79d4c419f0c2216df5b24b6ad49ac52f726425dbd75b1907b487f7830768fba82e47f2de&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-09
fetch_date: 2025-10-06T20:11:34.915803
---

# 【安全圈】BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaGZya5Fue1ZicCVlowwoypOtnULGpeBxXmZic4966HuyEH0XJ4j46kP9kDPzBsrqxUI8lHA7IYwn2w/0?wx_fmt=jpeg)

# 【安全圈】BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

BIOS

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaGZya5Fue1ZicCVlowwoypOLhmMG0v6SKXuMv4ibJredZfD9C5kk1lGuic24ouyleicECBmI9xpyomyA/640?wx_fmt=other&from=appmsg)

美国生物技术公司Illumina的iSeq 100 DNA测序仪存在BIOS/UEFI漏洞，可能让攻击者破坏用于检测疾病和开发疫苗的设备。

Illumina iSeq 100 被宣传为一种 DNA 测序系统，医疗和研究实验室可利用它进行 “快速、经济的基因分析”。

固件安全公司Eclypsium对Illumina设备的BIOS固件进行了分析，发现它在启动时没有标准的写入保护措施，因而容易被覆盖，导致系统 “变砖 ”或植入长期存在的植入物。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaGZya5Fue1ZicCVlowwoypOk4B7ZWNuSDIa2QPv3XNFoLSBjeB5pQXkYdBKFznHeTLkPCtSefQXNQ/640?wx_fmt=other&from=appmsg)

研究人员发现，iSeq 100 运行的是过时版本的 BIOS 固件，该固件在兼容支持模式（CSM）下运行，以支持旧设备，而且没有安全启动技术的保护。Eclypsium 的分析发现了五个主要问题，这些问题允许利用九个高、中严重程度的漏洞，其中一个漏洞早在 2017 年就存在了。除了缺少 BIOS 写保护外，iSeq 100 设备还容易受到 LogoFAIL、Spectre 2 和微架构数据采样 (MDS) 攻击。虽然在 CSM 模式下启动允许支持传统设备，但不建议敏感设备使用，尤其是新一代设备。

研究人员发现，iSeq 100 上存在漏洞的 BIOS（B480AM12 – 04/12/2018）没有启用固件保护，这就允许修改启动设备的代码。再加上缺乏安全启动（Secure Boot）功能（可检查启动代码的有效性和完整性），任何恶意更改都不会被发现。Eclypsium 在今天的报告中强调，他们的分析 “仅限于 iSeq 100 测序仪设备”，其他医疗或工业设备也可能存在类似问题。

研究人员解释说，医疗设备制造商使用外部供应商提供系统的计算能力。就 iSeq 100 而言，该设备依赖于 IEI Integration 公司的 OEM 主板。

由于 IEI Integration Corp 开发了多种工业计算机产品，并且是医疗设备的原始设计制造商（ODM），Eclypsium 表示，“这些问题或类似问题极有可能出现在使用 IEI 主板的其他医疗或工业设备中”。

研究人员还解释说，已经入侵设备的攻击者可以利用这些漏洞修改固件，使系统崩溃。掌握必要知识的威胁者还可以篡改测试结果。“如果数据被这些设备中的植入/后门篡改，那么威胁者就可能篡改一系列结果，包括伪造存在或不存在遗传病、篡改医学治疗或新疫苗、伪造祖先DNA研究等。” – Eclypsium

Eclypsium 向 Illumina 通报了 iSeq 100 设备的 BIOS 问题，该生物技术公司通知他们已向受影响的客户发布了补丁。

BleepingComputer 联系了Illumina公司，要求其就修复程序的交付方式和应收到修复程序的iSeq 100系统数量发表评论。

该公司发言人表示，Illumina 正在遵循其 “标准流程，如果需要采取任何缓解措施，将通知受影响的客户”。“我们的初步评估表明，这些问题的风险并不高，”Illumina 的一位代表告诉 BleepingComputer。“Illumina致力于我们产品的安全和基因组数据的隐私，我们已经建立了监督和问责流程，包括我们产品开发和部署的安全最佳实践。“作为这一承诺的一部分，我们一直在努力改进为现场仪器提供安全更新的方式。”Eclypsium 的研究人员在报告中警告说，威胁者如果能覆盖 iSeq 100 的固件，就能 “轻易地使设备瘫痪”。

通过破坏高价值系统来扰乱业务正是勒索软件攻击者的目的，因为他们的目标是通过尽可能增加恢复难度来迫使受害者支付赎金。

除了出于经济动机的攻击者，Eclypsium 表示，国家行为者也可能发现 DNA 测序系统很有吸引力，因为它们 “对于检测遗传疾病、癌症、识别耐药细菌和生产疫苗至关重要”。

2023年，美国网络安全基础设施安全局（CISA）和食品药品管理局（FDA）发布了一份紧急公告，指出Illumina公司的通用复制服务（UCS）存在两个漏洞。其中一个问题（CVE-2023-1968）获得了最高严重性评分，而另一个问题（CVE-2023-1966）则获得了高严重性评分。当时，Illumina 做出了反应，提供了有关如何缓解安全问题的更新和说明。

***END***

阅读推荐

[【安全圈】突发！美国国防部将华为、腾讯、长鑫、商汤等134家中国企业列入黑名单，6家被移出](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067202&idx=1&sn=97ab8cecb79ef8ef7f1b0f9e1f763a05&scene=21#wechat_redirect)

[【安全圈】12306崩了？官方客服：现在已陆续恢复](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=1&sn=43161803d494ae048c39293a76429c49&scene=21#wechat_redirect)

[【安全圈】Kimi崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=2&sn=37f830d2b9baded62b6af05e5a623f76&scene=21#wechat_redirect)

[【安全圈】Nikki-Universal 网络攻击 – 黑客声称窃取了 761.8 GB 的数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067195&idx=3&sn=146eb72a2193578816de50a7988608bc&scene=21#wechat_redirect)

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