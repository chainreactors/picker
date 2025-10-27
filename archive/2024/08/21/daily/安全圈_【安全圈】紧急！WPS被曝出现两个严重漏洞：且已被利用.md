---
title: 【安全圈】紧急！WPS被曝出现两个严重漏洞：且已被利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063733&idx=1&sn=04dd13bf3a0e027fb707f063fa89ffbf&chksm=f36e6bb5c419e2a399b928d676f3db243488855358d520c5a9617dc0e258679995acfe13a05d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-08-21
fetch_date: 2025-10-06T18:04:54.825208
---

# 【安全圈】紧急！WPS被曝出现两个严重漏洞：且已被利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliax3htCKf6qvK3OibcOTibqNTZ32Jab0kia9VSDhRDegbLBtMSXWcagfCIOSAibjuWAZjeoAh9TCXAXtA/0?wx_fmt=jpeg)

# 【安全圈】紧急！WPS被曝出现两个严重漏洞：且已被利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliax3htCKf6qvK3OibcOTibqNTUzn8XeNB95FhFuOVgfcNdOr9eDWPqCN9JHnwTXS3qB3733AvrqHdxw/640?wx_fmt=jpeg&from=appmsg)

2024年8月20号最新消息，广泛使用的办公软件套件WPS Office被曝出存在两个严重的安全漏洞，可能导致用户遭受远程代码执行攻击。根据安全研究人员的报告，这些漏洞已被标识为CVE-2024-7262和CVE-2024-7263，且其CVSS评分高达9.3，表明其严重性和被利用的可能性非常高。WPS Office用户群体庞大，超过2亿用户可能受到影响。

这两个漏洞均出现在WPS Office的promecefpluginhost.exe组件中，影响版本包括：

CVE-2024-7262：影响版本为12.2.0.13110至12.2.0.13489。

CVE-2024-7263：影响版本为12.2.0.13110至12.2.0.17153。

这两个漏洞都源于不正确的路径验证，允许攻击者加载和执行任意Windows库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliax3htCKf6qvK3OibcOTibqNTPsIDlII2aaib6XD3bu1y8y83VYv0noLbLmAnkD8Xha2glztEs9obKMA/640?wx_fmt=png&from=appmsg)

CVE-2024-7262：该漏洞涉及promecefpluginhost.exe进程的文件路径验证机制不足，攻击者可以通过诱骗用户打开特制的电子表格文档，加载恶意Windows库。这一“单击式”漏洞可能允许攻击者在受害者的计算机上执行任意代码，从而导致数据盗窃、勒索软件攻击或进一步的系统入侵。

CVE-2024-7263：为了解决CVE-2024-7262，WPS Office发布了版本12.2.0.16909的补丁。然而，研究人员发现，这个补丁并不充分。CVE-2024-7263漏洞影响到最高版本12.2.0.17153（不包括），攻击者利用了原始修复中忽略的其他未审查参数，从而绕过了WPS Office实施的安全措施，再次加载任意Windows库。

特别令人担忧的是，CVE-2024-7262漏洞已经被武器化。ESET的安全研究人员发现，攻击者正在积极利用该漏洞，通过分发特制的电子表格文档来触发漏洞利用。这种武器化攻击表明，恶意行为者已经开始利用这一漏洞进行实际攻击，用户面临着迫在眉睫的安全威胁。

### 风险缓解措施：鉴于这些漏洞的严重性以及CVE-2024-7262已被积极利用，建议所有WPS Office用户尽快将其软件更新至最新版本（12.2.0.17153或更高版本）。这一更新是用户保护自己免受远程代码执行攻击的关键措施。

WPS Office用户应密切关注软件发布的更新，并及时应用补丁，以降低被攻击的风险。企业用户尤其应警惕这些漏洞的利用，确保所有员工的WPS Office版本均为最新，防止因安全漏洞而导致的潜在损失。除了更新软件版本外，用户近期最好不打开来源不明的文件，尤其是可能含有恶意代码的电子表格和文档。

此外还有未经证实的消息表示，可能只有WPS国际版受到影响，国内版本或不受影响，但出于安全考虑，还是建议升级到最新版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliax3htCKf6qvK3OibcOTibqNT5ae1vE0fWSd7wo6pC0iczsy7pOJp40YZOsphsFJfxn5k1P3WxX2nLdQ/640?wx_fmt=jpeg)

***END***

阅读推荐

 [【安全圈】网易云音乐大规模崩溃，用户反映：“上班全靠网易云吊着一口气，现在最后一口气也没了”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063716&idx=4&sn=c1f2a6f5f8aa95370ef0b47078e77dbe&chksm=f36e6ba4c419e2b2b1ee20b9d248d89d647b49dac395b06e7e313df3b9e4928bed8cc4449d8c&scene=21#wechat_redirect)

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