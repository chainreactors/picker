---
title: 【安全圈】小心 Python 开发人员： 恶意 “fabrice ”软件包从 37,000 多次下载中窃取 AWS 凭据
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065786&idx=3&sn=5c8b175a427cc9df9cbe8c4e6ec87014&chksm=f36e63bac419eaac5b60dc0af753e58e6470a4924f26ccb84aeb2b93cb1b7e5a71d52f8510b7&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-09
fetch_date: 2025-10-06T19:19:12.590680
---

# 【安全圈】小心 Python 开发人员： 恶意 “fabrice ”软件包从 37,000 多次下载中窃取 AWS 凭据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR9cr2805dLK44jWic9EibRN2T1dKAI3WbEeSrq1DwOj6icDoJtgYb9XkdVQ/0?wx_fmt=jpeg)

# 【安全圈】小心 Python 开发人员： 恶意 “fabrice ”软件包从 37,000 多次下载中窃取 AWS 凭据

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg5ZQcZEq3ZdBoKh2Wq7BR99AZ8UDZHdGQ2PBaQMsLUA1LH21hlj4XhKnzZOMgkia28Jlxv0eKteibQ/640?wx_fmt=other&from=appmsg)

对于 Python 开发人员和云管理员来说，一个令人担忧的进展是，Socket 研究团队发现了一个名为 fabrice 的恶意软件包，它伪装成合法且广泛使用的 Fabric SSH 自动化库。自 2021 年在 PyPI 上发布以来，fabrice 已悄无声息地外泄了敏感的 AWS 凭据，影响了那些在不知情的情况下安装了该排印错误软件包的用户。fabrice 软件包的下载量已超过 37000 次，凸显了恶意软件在开源软件源中带来的持续风险。

恶意 fabrice 软件包采用了多种技术来交付其有效载荷，并针对 Linux 和 Windows 环境定制了不同的恶意操作：

1. 在 Linux 系统上： 该软件包使用一个名为 linuxThread() 的函数从外部服务器下载并执行隐藏脚本。研究发现，“linuxThread()函数会创建一个隐藏目录（~/.local/bin/vscode）来存储下载的有效载荷”，从而使检测变得困难。此外，该软件包会连接到一个 IP 地址为 89.44.9.227 的 VPN 服务器来下载这些恶意脚本，并使用混淆技术来躲避检测。
2. 在 Windows 系统上： Windows 版本使用 winThread() 函数，依赖于存储在变量 vv 和 zz 中的 base64 编码有效载荷。研究解释说，“vv 变量解码为 VBScript (p.vbs)，运行隐藏的 Python 脚本 (d.py)”，然后下载更多恶意可执行文件。zz 脚本通过调度任务重新执行恶意代码来建立持久性，即使在系统重启后也能保持攻击的存在。

fabrice 的主要目的似乎是窃取 AWS 凭据。通过利用 boto3 库，该软件包可以从被入侵的环境中提取 AWS 访问和密钥。一旦捕获，这些凭据就会被传输到 VPN 端点，从而使受害者难以追踪外泄数据。正如报告所强调的，“通过收集 AWS 密钥，攻击者获得了对潜在敏感云资源的访问权限”，有可能将重要数据和云资源暴露给未经授权的访问。

该恶意软件的设计与平台无关，其 test() 函数可检查操作系统并执行相应的恶意线程。这一功能使恶意软件能够同时针对 Linux 和 Windows 用户，扩大了其影响范围。“报告指出：”这种与平台无关的触发器确保攻击不受操作系统的影响，从而扩大了其潜在影响。

Typosquatting 攻击，即恶意软件包的命名与可信库相似，仍然是开源软件库中一个日益增长的风险。由 bitprophet 创建的合法 Fabric 库拥有超过 2.01 亿次下载，受到开发者的广泛信任。fabrice 背后的攻击者利用了这种信任，在毫无戒备的系统中大肆窃取凭据并安装后门。

***END***

阅读推荐

[【安全圈】Windows 10 将于明年 10 月停止支持 对你我有何影响](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=1&sn=20737c81521c2b60c2ae6e68bd85cf08&chksm=f36e63a6c419eab0559b56523c0815b5e760666eb51eaa8a0579237fda5bd619c529c56f24fe&scene=21#wechat_redirect)

[【安全圈】谷歌云将在2025年底强制实施多因素身份验证](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=2&sn=60b2502195278b934474b1c4a7fc49bd&chksm=f36e63a6c419eab08fb88d51ccdbf0cb4bfe5081e8ccfe502ee69577918cb1ada38f8721c993&scene=21#wechat_redirect)

[【安全圈】黑客可以随意访问EA公司7亿用户账号](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=3&sn=bcdf6497f31db93acd068fb24f76e293&chksm=f36e63a6c419eab04b707515e3ec637038e1f931dd74f1640728e7904bece00c01cfe82fde69&scene=21#wechat_redirect)

[【安全圈】Schneider Electric 在报告黑客索赔后调查安全“事件”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065766&idx=4&sn=792c2e0aa0defbba125b9aeffcfd1210&chksm=f36e63a6c419eab0a561defb5b66ec4b27a9cf4821a910f2d64455a2cb15fdd063a65f35cf94&scene=21#wechat_redirect)

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