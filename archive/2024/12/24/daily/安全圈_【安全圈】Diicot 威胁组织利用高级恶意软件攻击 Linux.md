---
title: 【安全圈】Diicot 威胁组织利用高级恶意软件攻击 Linux
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066835&idx=4&sn=66217b60f43298ef9b36aff4b47463a1&chksm=f36e7853c419f14555f33a9c74aa76bcabfa8baa2629f8401844f085086efd3efdaef0962e99&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-24
fetch_date: 2025-10-06T19:40:38.689632
---

# 【安全圈】Diicot 威胁组织利用高级恶意软件攻击 Linux

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9Q0BCDAruYIoibPkJyYYSWicicKFJUZ8CCCMXP3GnhiawSmSicgcK9MlXA1g/0?wx_fmt=jpeg)

# 【安全圈】Diicot 威胁组织利用高级恶意软件攻击 Linux

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

Wiz Threat Research 揭示了一个由讲罗马尼亚语的威胁组织 Diicot（又称 Mexals）策划的新恶意软件活动。该活动以 Linux 环境为目标，采用了先进的恶意软件技术，标志着其能力显著升级。该组织一直利用 Linux 系统进行加密劫持，使用 XMRig 等工具和复杂的自传播机制。

据 Wiz Research 称，与早期迭代版本相比，更新后的恶意软件显示出惊人的复杂程度，凸显了攻击者适应和完善其战术的能力。报告指出：“我们分析的恶意软件包括一些显著的改进，反映了更高的复杂程度。”主要的进步包括引入了新的指挥控制（C2）基础设施，从基于 Discord 的 C2 过渡到 HTTP，以及采用 Zephyr 协议和 Monero 挖矿。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9E4kx80bq8PXOVEOgByWW52OaaRlLKe7l4Dse6TpTrqcQ5f7INoxymg/640?wx_fmt=other&from=appmsg)Diicot 图表 | 来源：Wiz Research Wiz Research

该恶意软件还改进了混淆技术。例如，修改后的 UPX 标头现在包括损坏的校验和，使标准解包工具失效。这些变化表明，该恶意软件正在努力绕过现代安全措施，阻挠自动检测。

该活动的一个突出特点是它能够根据环境调整自己的行为。在云环境中，恶意软件会优先向其他主机传播，而在传统环境中，它会部署加密有效载荷。报告解释说，“云检测逻辑”“基于远程机器的 Linux 发行版和版本”，显示了该组织对目标的细致关注。

调查中发现的有效载荷包括：

* Brute-Spreader：在网络中传播并保持持久性的主要有效载荷。
* 反向外壳 (client.go)：允许攻击者完全远程控制被入侵的机器。
* SSH 标记扫描器：识别弱 SSH 凭据以获得初始访问权限。

该活动对运行 OpenSSH 的 Linux 系统构成重大风险。薄弱的凭证和错误配置的安全设置很容易成为这种高级恶意软件的入口点。Wiz 研究人员强调：“如果你的系统依赖 SSH 且没有适当的安全保护，它们很容易成为攻击目标。”

加密劫持仍然是 Diicot 行动的核心动机。攻击者从 Monero 挖矿中赚取了超过 16,000 美元，还从 Zephyr 协议中赚取了更多难以追踪的收入。除了经济损失，企业还面临数据外渗、系统受损和潜在运营中断的风险。

随着 Diicot 集团的不断发展，防御策略也必须与时俱进。Wiz Research 建议加强 SSH 配置，强制执行强密码，并部署能够识别混淆有效载荷的高级检测机制。

***END***

阅读推荐

[【安全圈】谷歌测试在Chrome中启用人工智能检测诈骗 当发现钓鱼网站时弹出警告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=1&sn=dddcab37c43e140a04d10fdf74ccf0e4&scene=21#wechat_redirect)

[【安全圈】FortiWLM 曝关键漏洞，攻击者可获得管理员权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=2&sn=d36a351bfabba8d719c29fa871c22b3c&scene=21#wechat_redirect)

[【安全圈】Mozilla再次发文称禁止谷歌搜索向浏览器分成将威胁火狐等独立浏览器的生存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=3&sn=5e35754a7884cd8ec8ef21319f9245ca&scene=21#wechat_redirect)

[【安全圈】罗马尼亚国民因 NetWalker 勒索软件攻击被判处 20 年监禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=4&sn=86f5fdfe10bdcdd67c657f5b8141121d&scene=21#wechat_redirect)

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